-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$ 
CREATE PROCEDURE ComputeAverageScoreForUser (user_id INT)
BEGIN
    DECLARE AVG_SCORE FLOAT DEFAULT 0;

    SELECT AVG(score)
    INTO AVG_SCORE
    FROM corrections
    WHERE corrections.user_id = user_id;

    UPDATE users
    SET average_score = AVG_SCORE
    WHERE id = user_id;
END $$
DELIMITER ;
