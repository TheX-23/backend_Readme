-- SQL Server (T-SQL) compatible schema converted from the project's SQLite schema.
-- This file is intended for use with Microsoft SQL Server / Azure SQL.

-- Note: SQLite uses `CREATE TABLE IF NOT EXISTS`, `AUTOINCREMENT`, and `TEXT`.
-- In SQL Server we use IF NOT EXISTS checks, IDENTITY for auto-increment, and appropriate data types.

-- Tables
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'dbo.chats') AND type in (N'U'))
BEGIN
  CREATE TABLE dbo.chats (
    id INT IDENTITY(1,1) PRIMARY KEY,
    question NVARCHAR(MAX) NOT NULL,
    answer NVARCHAR(MAX) NOT NULL,
    language NVARCHAR(50) NOT NULL,
    timestamp DATETIME2 NOT NULL
  );
END

IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'dbo.forms') AND type in (N'U'))
BEGIN
  CREATE TABLE dbo.forms (
    id INT IDENTITY(1,1) PRIMARY KEY,
    form_type NVARCHAR(100) NOT NULL,
    form_text NVARCHAR(MAX) NOT NULL,
    responses_json NVARCHAR(MAX) NOT NULL,
    timestamp DATETIME2 NOT NULL
  );
END

IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'dbo.users') AND type in (N'U'))
BEGIN
  CREATE TABLE dbo.users (
    id INT IDENTITY(1,1) PRIMARY KEY,
    email NVARCHAR(320) NOT NULL UNIQUE,
    password_hash NVARCHAR(200) NOT NULL,
    is_verified BIT NOT NULL CONSTRAINT DF_users_is_verified DEFAULT(0),
    verification_token NVARCHAR(200) NULL,
    created_at DATETIME2 NOT NULL,
    verified_at DATETIME2 NULL
  );
END

-- Indexes
IF NOT EXISTS (SELECT name FROM sys.indexes WHERE name = N'idx_chats_timestamp')
BEGIN
  CREATE INDEX idx_chats_timestamp ON dbo.chats (timestamp DESC);
END

IF NOT EXISTS (SELECT name FROM sys.indexes WHERE name = N'idx_forms_timestamp')
BEGIN
  CREATE INDEX idx_forms_timestamp ON dbo.forms (timestamp DESC);
END

IF NOT EXISTS (SELECT name FROM sys.indexes WHERE name = N'idx_chats_language')
BEGIN
  CREATE INDEX idx_chats_language ON dbo.chats (language);
END

IF NOT EXISTS (SELECT name FROM sys.indexes WHERE name = N'idx_forms_form_type')
BEGIN
  CREATE INDEX idx_forms_form_type ON dbo.forms (form_type);
END

IF NOT EXISTS (SELECT name FROM sys.indexes WHERE name = N'idx_users_email')
BEGIN
  CREATE UNIQUE INDEX idx_users_email ON dbo.users (email);
END

IF NOT EXISTS (SELECT name FROM sys.indexes WHERE name = N'idx_users_verified')
BEGIN
  CREATE INDEX idx_users_verified ON dbo.users (is_verified);
END

-- Sample queries (T-SQL compatible)
SELECT id, question, answer, language, timestamp
FROM dbo.chats
ORDER BY timestamp DESC, id DESC;

SELECT id, form_type, form_text, responses_json, timestamp
FROM dbo.forms
ORDER BY timestamp DESC, id DESC;

SELECT language, COUNT(*) AS total
FROM dbo.chats
GROUP BY language
ORDER BY total DESC;

SELECT form_type, COUNT(*) AS total
FROM dbo.forms
GROUP BY form_type
ORDER BY total DESC;

SELECT COUNT(*) AS total_users FROM dbo.users;
SELECT COUNT(*) AS verified_users FROM dbo.users WHERE is_verified = 1;
