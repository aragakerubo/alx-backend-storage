-- Write a SQL script that creates a stored
-- procedure ComputeAverageWeightedScoreForUsers that computes
-- and store the average weighted score for all students.

-- Requirements:

-- Procedure ComputeAverageWeightedScoreForUsers is not taking any input.
-- Tips:

-- Calculate-Weighted-Average

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  UPDATE users
  SET average_weighted_score = (
    SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
    FROM corrections, projects 
    WHERE corrections.project_id=projects.id
    AND corrections.user_id=users.id
  );
END$$
DELIMITER ;
