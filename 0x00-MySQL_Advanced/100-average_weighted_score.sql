-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
BEGIN
    DECLARE weight_sum INT DEFAULT 0;
    DECLARE student_weighted_sum INT DEFAULT 0;

    SELECT SUM(weight)
    INTO weight_sum
    FROM projects
    JOIN corrections
        ON projects.id = corrections.project_id
    WHERE corrections.user_id = user_id;

    SELECT SUM(projects.weight * corrections.score)
    INTO student_weighted_sum
    FROM projects
    JOIN corrections
        ON projects.id = corrections.project_id
    WHERE corrections.user_id = user_id;

    UPDATE users
    SET average_score = student_weighted_sum / weight_sum
    WHERE id = user_id;
END $$
DELIMITER ;
