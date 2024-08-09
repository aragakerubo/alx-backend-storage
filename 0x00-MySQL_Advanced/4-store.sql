-- Write a SQL script that creates a trigger that decreases
-- the quantity of an item after adding a new order.

-- Quantity in the table items can be negative.

-- Context: Updating multiple tables for one action from your application
-- can generate issue: network disconnection, crash, etc… to keep your data
-- in a good shape, let MySQL do it for you!

CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  UPDATE items
  SET quantity = quantity - 1
  WHERE id = NEW.item_id;
END;
