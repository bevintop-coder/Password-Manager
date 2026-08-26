PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS passwords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    website TEXT NOT NULL,
    encrypted_password TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO passwords (
    website,
    encrypted_password
)
VALUES (
    'example.com',
    'sdvvzrug123'
);

SELECT
    id,
    website,
    encrypted_password,
    created_at
FROM passwords;

SELECT
    website,
    encrypted_password
FROM passwords
WHERE website = 'example.com';

UPDATE passwords
SET encrypted_password = 'qhzsdvvzrug'
WHERE website = 'example.com';

DELETE FROM passwords
WHERE website = 'example.com';

SELECT COUNT(*) AS total_passwords
FROM passwords;
