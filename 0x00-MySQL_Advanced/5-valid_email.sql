-- only when the email has been changed.
-- Creates a trigger that resets the attribute valid_email
-- @author husamrio <https://github.com/husamrio>

DELIMITER $$
CREATE TRIGGER new_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
	SET NEW.valid_email = 0;
    END IF;
END$$
DELIMITER ;$$
