DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score DECIMAL(4, 2))
BEGIN
  DECLARE project_id INT;
  DECLARE user_project_id INT;

  SELECT id INTO project_id
  FROM projects
  WHERE name = project_name;

  IF project_id IS NULL THEN
    INSERT INTO projects (name)
    VALUES (project_name);
    SET project_id = LAST_INSERT_ID();
  END IF;

  SELECT id INTO user_project_id
  FROM corrections
  WHERE user_id = user_id AND project_id = project_id;

  IF user_project_id IS NULL THEN
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, project_id, score);
  ELSE
    UPDATE corrections
    SET score = score
    WHERE id = user_project_id;
  END IF;
END$$
DELIMITER ;