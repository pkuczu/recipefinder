CREATE DATABASE recipes;

-- Use the 'recipes' database
USE recipes;

-- Create a table to store recipe titles
CREATE TABLE IF NOT EXISTS RecipeTitles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    ingredients TEXT,
    instructions TEXT
    -- prep_time FLOAT,
);
