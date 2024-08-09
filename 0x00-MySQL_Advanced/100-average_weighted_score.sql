-- Write a SQL script that creates a stored
-- procedure ComputeAverageWeightedScoreForUser that computes
-- and store the average weighted score for a student.

-- Requirements:

-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value
-- (you can assume user_id is linked to an existing users)

-- Tips:

-- Calculate-Weighted-Average

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
  DECLARE total_score DECIMAL(4, 2);
  DECLARE total_weight DECIMAL(4, 2);
  DECLARE average DECIMAL(4, 2);
  
  SELECT SUM(score * weight) INTO total_score
  FROM corrections
  JOIN projects
  ON corrections.project_id = projects.id
  WHERE user_id = user_id;
  
  SELECT SUM(weight) INTO total_weight
  FROM corrections
  JOIN projects
  ON corrections.project_id = projects.id
  WHERE user_id = user_id;
  
  IF total_weight IS NULL THEN
    SET average = 0;
  ELSE
    SET average = total_score / total_weight;
  END IF;
  
  INSERT INTO average_weighted_scores (user_id, average)
  VALUES (user_id, average)
  ON DUPLICATE KEY UPDATE average = average;
END$$
DELIMITER ;
