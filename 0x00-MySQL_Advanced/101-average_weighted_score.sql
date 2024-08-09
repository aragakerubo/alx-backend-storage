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
    SELECT AVG(weighted_score)
    FROM (
      SELECT
        user_id,
        SUM(score * weight) / SUM(weight) AS weighted_score
      FROM
        scores
      GROUP BY
        user_id
    ) AS weighted_scores
    WHERE
      users.id = weighted_scores.user_id
  );
END$$
DELIMITER ;
