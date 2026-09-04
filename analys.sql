-- =========================================================================
-- BUSINESS ANALYSIS & DATA MODELING CASE
-- Syfte: Dokumentera och strukturera systemkrav direkt i datadatabasen 
-- för att visa spårbarhet mellan verksamhetsbehov och IT-leverans.
-- =========================================================================

-- 1. Skapa tabell för att hålla reda på intressenter (Stakeholders)
CREATE TABLE Stakeholders (
    StakeholderID INT PRIMARY KEY,
    Name VARCHAR(100),
    Department VARCHAR(50),
    InfluenceLevel VARCHAR(10) -- High, Medium, Low
);

-- 2. Skapa tabell för kravhantering (Requirements Traceability Matrix)
CREATE TABLE SystemRequirements (
    RequirementID VARCHAR(10) PRIMARY KEY,
    Description TEXT,
    RequirementType VARCHAR(30), -- Functional, Non-Functional, Regulatory
    Priority VARCHAR(10),        -- Must, Should, Could, Won't
    Status VARCHAR(20),          -- Approved, In Progress, Deferred
    OwnerID INT,
    FOREIGN KEY (OwnerID) REFERENCES Stakeholders(StakeholderID)
);

-- 3. Lägg till data som speglar Saabs efterfrågade profil
INSERT INTO Stakeholders (StakeholderID, Name, Department, InfluenceLevel) VALUES
(1, 'Finanschef', 'Verksamhet', 'High'),
(2, 'IT-Säkerhetschef', 'IT', 'High'),
(3, 'BI Developer', 'IT', 'Medium');

INSERT INTO SystemRequirements (RequirementID, Description, RequirementType, Priority, Status, OwnerID) VALUES
('FR-001', 'Systemet ska automatiskt uppdatera dashboards i molnet var 6:e timme.', 'Functional', 'Must', 'Approved', 1),
('NFR-001', 'Rapportgenerering i beslutsstödet får ta max 3 sekunder under hög belastning.', 'Non-Functional', 'Should', 'Approved', 3),
('RR-001', 'All lagrad data måste krypteras enligt rådande säkerhetsskyddsbestämmelser.', 'Regulatory', 'Must', 'Approved', 2);

-- 4. Analysfråga: Hämta alla kritiska krav inför nästa Agila Sprint/Workshop
-- Visar att BA kan köra SQL för att kontrollera scope
SELECT 
    RequirementID,
    RequirementType,
    Priority,
    Description
FROM 
    SystemRequirements
WHERE 
    Priority = 'Must' 
    AND Status = 'Approved'
ORDER BY 
    RequirementType DESC;