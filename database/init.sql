-- Initialisation de la base de données PostgreSQL pour Mini SOC Intelligent

CREATE TABLE IF NOT EXISTS incidents (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    attack_type VARCHAR(100) NOT NULL,
    confidence FLOAT NOT NULL,
    confidence_level VARCHAR(50) NOT NULL,
    flow_features TEXT,
    status VARCHAR(50) DEFAULT 'Nouveau'
);

CREATE TABLE IF NOT EXISTS tickets (
    id SERIAL PRIMARY KEY,
    incident_id INT REFERENCES incidents(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    priority VARCHAR(50) DEFAULT 'Haute',
    status VARCHAR(50) DEFAULT 'Ouvert',
    assigned_to VARCHAR(100) DEFAULT 'SOC Analyst',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Index pour accélérer les requêtes du Dashboard SOC
CREATE INDEX IF NOT EXISTS idx_incidents_timestamp ON incidents(timestamp);
CREATE INDEX IF NOT EXISTS idx_incidents_status ON incidents(status);
CREATE INDEX IF NOT EXISTS idx_tickets_incident_id ON tickets(incident_id);
