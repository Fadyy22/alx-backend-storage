-- SQL script that creates a stored procedure AddBonus that adds a new correction for a student
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus (user_id INT, project_name VARCHAR(255), score INT)
BEGIN
    -- Declare variable to store in it wether the project exists or not
    DECLARE project_exists INT DEFAULT 0;

    -- Check if the project exists
    SELECT COUNT(id)
    INTO project_exists
    FROM projects
    WHERE name = project_name;

    -- If the project doesn't exist then create it
    IF project_exists = 0 THEN
        INSERT INTO projects (name)
        VALUES (project_name);
    END IF;

    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END $$
DELIMITER ;
