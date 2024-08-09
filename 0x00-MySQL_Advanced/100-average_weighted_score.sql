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
  UPDATE users
  SET average_weighted_score = (
    SELECT AVG(weighted_score)
    FROM scores
    WHERE user_id = user_id
  )
  WHERE id = user_id;
END$$
DELIMITER ;
