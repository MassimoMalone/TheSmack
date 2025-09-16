


CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(15) UNIQUE NOT NULL,
    users_email UNIQUE,
    users_password TEXT NOT NULL
);

CREATE TABLE feelings (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE smacks(
    id SERIAL PRIMARY KEY,
    smack_username VARCHAR(15) REFERENCES users(username),
    feeling_id INT REFERENCES feelings(id),
    feeling VARCHAR(20) REFERENCES feelings(name),
    blurb VARCHAR(250),
    posted_at TIMESTAMP,
    likes INT DEFAULT 0,
    edited_at TIMESTAMP,
    is_deleted BOOLEAN DEFAULT FALSE
);


INSERT INTO feelings (name) VALUES
('happy'),
('sad'),
('angry'),
('excited'),
('bored'),
('tired'),
('lonely'),
('chill'),
('stressed'),
('confident');