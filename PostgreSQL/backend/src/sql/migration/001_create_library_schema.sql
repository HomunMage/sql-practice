-- src/sql/migration/001_create_library_schema.sql

-- Migration: Create Library Management Schema
-- Run automatically by src/model/migration.py

-- Create Authors table
CREATE TABLE IF NOT EXISTS authors (
    author_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    birth_date DATE
);

-- Create Books table
CREATE TABLE IF NOT EXISTS books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    publisher VARCHAR(255),
    publication_year INT,
    isbn VARCHAR(20) UNIQUE,
    author_id INT REFERENCES authors(author_id) ON DELETE SET NULL
);

-- Create Members table
CREATE TABLE IF NOT EXISTS members (
    member_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    membership_date DATE,
    email VARCHAR(255) UNIQUE
);

-- Create BorrowingHistory table
CREATE TABLE IF NOT EXISTS borrowing_history (
    borrow_id SERIAL PRIMARY KEY,
    book_id INT REFERENCES books(book_id) ON DELETE CASCADE,
    member_id INT REFERENCES members(member_id) ON DELETE CASCADE,
    borrow_date DATE,
    return_date DATE
);
