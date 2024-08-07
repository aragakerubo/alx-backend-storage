CREATE TRIGGER valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  IF NEW.email NOT REGEXP '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' THEN
    SET NEW.valid_email = 0;
  END IF;
END;
