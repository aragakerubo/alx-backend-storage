-- Write a SQL script that creates a trigger that resets
-- the attribute valid_email only when the email has been changed.

-- Context: Nothing related to MySQL, but perfect for
-- user email validation - distribute the logic to the database itself!

CREATE TRIGGER valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  IF NEW.email NOT REGEXP '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' THEN
    SET NEW.valid_email = 0;
  END IF;
END;
