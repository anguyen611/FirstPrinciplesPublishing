-- Users Setup
CREATE TABLE users (
	id INT GENERATED ALWAYS AS IDENTITY,
	username VARCHAR(255),
	displayname VARCHAR(255),
	password VARCHAR(255),
	PRIMARY KEY(id)
);

INSERT INTO users (username, displayname, password)
VALUES
	('user', 'User', 'pass'),
	('Sample', 'Blank', 'password'),
	('Test', 'Test Person', '12345');

-- Users record deletion
TRUNCATE users RESTART IDENTITY;

-- Users Identity reset
ALTER TABLE users
ALTER COLUMN id RESTART WITH 4;

-- Posts setup
CREATE TABLE posts (
	id INT GENERATED ALWAYS AS IDENTITY,
	title VARCHAR(255),
	body VARCHAR(255),
	userid INT,
	edited BOOLEAN DEFAULT False,
	PRIMARY KEY(id)
);

INSERT INTO posts (title, body, userid)
VALUES
	('Title', 'Body', 1),
	('Second', 'Post', 1),
	('Testing', 'Test Testing', 2);

-- Posts record deletion
TRUNCATE posts RESTART IDENTITY;

-- Posts Identity reset
ALTER TABLE users
ALTER COLUMN id RESTART WITH 4;