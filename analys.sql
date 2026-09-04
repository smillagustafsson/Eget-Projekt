-- =========================================================================
-- JUNIOR DATA ANALYST - NASDAQ STOCKHOLM RELATIONAL MODEL
-- Syfte: Strukturera data för hela den svenska aktiemarknaden.
-- =========================================================================

-- 1. Dimensionstabell för noterade bolag på Stockholmsbörsen
CREATE TABLE StockholmExchange (
    CompanyID INT PRIMARY KEY,
    Ticker VARCHAR(10) NOT NULL,
    CompanyName VARCHAR(100) NOT NULL,
    Sector VARCHAR(50),
    Segment VARCHAR(20),             -- Large Cap, Mid Cap, Small Cap
    Is_OMXS30 BOOLEAN DEFAULT FALSE   -- Om aktien ingår i storbolagsindexet
);

-- 2. Faktatabell för finansiella nyckeltal och marknadsdata
CREATE TABLE MarketMetrics (
    MetricID INT PRIMARY KEY,
    CompanyID INT,
    PE_Ratio DECIMAL(5,2),            -- P/E-tal (Värdering)
    DividendYield_Percent DECIMAL(4,2),-- Direktavkastning
    MarketCap_MSEK INT,               -- Börsvärde i miljoner kronor
    FOREIGN KEY (CompanyID) REFERENCES StockholmExchange(CompanyID)
);

-- 3. Lägg till data för marknaden
INSERT INTO StockholmExchange VALUES (1, 'INVE-B', 'Investor', 'Investment', 'Large Cap', TRUE);
INSERT INTO StockholmExchange VALUES (2, 'VOLV-B', 'Volvo', 'Industri', 'Large Cap', TRUE);
INSERT INTO StockholmExchange VALUES (3, 'SAAB-B', 'Saab', 'Försvar', 'Large Cap', TRUE);
INSERT INTO StockholmExchange VALUES (4, 'SEBA', 'SEB', 'Bank', 'Large Cap', TRUE);
INSERT INTO StockholmExchange VALUES (5, 'SBB-B', 'SBB', 'Fastighet', 'Mid Cap', FALSE);

INSERT INTO MarketMetrics VALUES (501, 1, 14.20, 2.10, 850000);
INSERT INTO MarketMetrics VALUES (502, 2, 11.50, 5.50, 560000);
INSERT INTO MarketMetrics VALUES (503, 3, 28.40, 1.20, 130000);
INSERT INTO MarketMetrics VALUES (504, 4, 9.80, 6.20, 310000);
INSERT INTO MarketMetrics VALUES (505, 5, NULL, 0.00, 15000);

-- 4. BI ADVANCED QUERY: Hämta genomsnittlig värdering (P/E) och direktavkastning 
-- per segment för storbolag (Visar djup förståelse för datastrukturer)
SELECT 
    e.Segment,
    COUNT(e.CompanyID) as Total_Companies,
    AVG(m.PE_Ratio) as Avg_PE,
    AVG(m.DividendYield_Percent) as Avg_Yield
FROM 
    StockholmExchange e
JOIN 
    MarketMetrics m ON e.CompanyID = m.CompanyID
GROUP BY 
    e.Segment;
