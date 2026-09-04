-- =========================================================================
-- JUNIOR DATA ANALYST - SQL & AZURE DATABASE MODELING
-- Syfte: Strukturera finansiell data för en aktieportfölj.
-- Anpassad för migrering till Azure SQL Database och visualisering i Power BI.
-- =========================================================================

-- 1. Skapa tabell för bolagsinformation (Dimensionstabell)
CREATE TABLE Companies (
    CompanyID INT PRIMARY KEY,
    Ticker VARCHAR(10) NOT NULL,
    CompanyName VARCHAR(100) NOT NULL,
    Sector VARCHAR(50),
    DividendYield_Percent DECIMAL(4,2) -- Direktavkastning
);

-- 2. Skapa tabell för dagliga aktiekurser (Faktatabell för BI-analys)
CREATE TABLE StockPrices (
    PriceID INT PRIMARY KEY,
    CompanyID INT,
    TradingDate DATE,
    ClosingPrice DECIMAL(10,2),
    Volume INT,
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID)
);

-- 3. Lägg till data för analys (Svenska folkaktier)
INSERT INTO Companies VALUES (1, 'INVE-B', 'Investor', 'Investment', 2.10);
INSERT INTO Companies VALUES (2, 'VOLV-B', 'Volvo', 'Industri', 5.50);
INSERT INTO Companies VALUES (3, 'SAAB-B', 'Saab', 'Försvar', 1.20);

INSERT INTO StockPrices VALUES (101, 1, '2026-09-04', 285.00, 1200000);
INSERT INTO StockPrices VALUES (102, 2, '2026-09-04', 272.50, 2500000);
INSERT INTO StockPrices VALUES (103, 3, '2026-09-04', 252.00, 800000);

-- 4. BI-Fråga: Hämta bolag med hög direktavkastning (High Yield) till Power BI
-- Visar att du kan filtrera fram strategisk data med SQL
SELECT 
    CompanyName, 
    Ticker, 
    Sector, 
    DividendYield_Percent
FROM 
    Companies
WHERE 
    DividendYield_Percent > 2.0
ORDER BY 
    DividendYield_Percent DESC;
