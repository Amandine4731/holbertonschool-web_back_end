-- Crée une table "users" si elle n'existe pas déjà
CREATE TABLE IF NOT EXISTS users (
    -- Colonne "id" de type INT, se remplissant automatiquement et servant de clé primaire
    id INT AUTO_INCREMENT PRIMARY KEY,
    -- Colonne "email" de type VARCHAR, ne pouvant pas être vide (NOT NULL) et devant être unique
    email VARCHAR(255) NOT NULL UNIQUE,
    -- Colonne "name" de type VARCHAR, pouvant contenir le nom de l'utilisateur
    name VARCHAR(255)
);
