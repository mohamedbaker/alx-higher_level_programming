-- Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

CREATE TABLE IF NOT EXISTS second_table (id INT AUTO_INCREMENT, name VARCHAR(256), score INT);
INSERT INTO second_table VALUES(1, Jhon, 10);
INSERT INTO second_table VALUES(Alex, 3);
INSERT INTO second_table VALUES(Bob, 14);
INSERT INTO second_table VALUES(George, 8);
