-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    ALTER TABLE users ADD total_projects_weigth INT NOT NULL;
    ALTER TABLE users ADD total_score_weigth INT NOT NULL;

    UPDATE users
    SET total_projects_weigth = (
        SELECT SUM(weight)
        FROM projects
        JOIN corrections
            ON projects.id = corrections.project_id
        WHERE corrections.user_id = users.id
    );

    UPDATE users
    SET total_score_weigth = (
        SELECT SUM(projects.weight * corrections.score)
        FROM projects
        JOIN corrections
            ON projects.id = corrections.project_id
        WHERE corrections.user_id = users.id
    );

    UPDATE users
    SET average_score = users.total_score_weigth / total_projects_weigth;

    ALTER TABLE users DROP COLUMN total_projects_weigth;
    ALTER TABLE users DROP COLUMN total_score_weigth;
END $$
DELIMITER ;
