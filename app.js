// =========================================================================
// PORTFOLIO LOGIC - SQL ENGINE & CHARTING (SMILLA GUSTAFSSON)
// =========================================================================

// --- DEL 1: INTERAKTIVT DIAGRAM (Chart.js) ---
const ctx = document.getElementById('performanceChart').getContext('2d');
new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Investor', 'Volvo', 'Saab', 'SEB', 'AstraZeneca', 'SBB', 'Evolution', 'Sandvik'],
        datasets: [{
            label: 'Aktieutveckling på Stockholmsbörsen (%)',
            data: [1.79, -2.59, 4.76, 2.46, 2.41, -13.33, 3.13, -1.40], 
            backgroundColor: [
                '#00ff88', '#ff4d4d', '#00ff88', '#00ff88', '#00ff88', '#ff4d4d', '#00ff88', '#ff4d4d'
            ],
            borderWidth: 1
        }]

    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: false,
                grid: { color: '#334155' },
                ticks: { color: '#f8fafc' }
            },
            x: {
                grid: { display: false },
                ticks: { color: '#f8fafc' }
            }
        },
        plugins: {
            legend: { labels: { color: '#f8fafc' } }
        }
    }
});

// --- DEL 2: IN-BROWSER SQL-DATABAS (SQL.js WASM) ---
let db;

// Initiera SQL-databasen i webbläsaren
initSqlJs({ locateFile: file => `https://cloudflare.com{file}` }).then(SQL => {
    db = new SQL.Database();
    
    // Skapa dina tabeller
    db.run(`
        CREATE TABLE Companies (
            CompanyID INT, CompanyName TEXT, Ticker TEXT, Sector TEXT, DividendYield_Percent REAL
        );
        CREATE TABLE StockPrices (
            PriceID INT, CompanyID INT, TradingDate TEXT, ClosingPrice REAL, Volume INT
        );
    `);

    // Skjut in din aktiedata
    db.run("INSERT INTO Companies VALUES (1, 'Investor', 'INVE-B', 'Investment', 2.10);");
    db.run("INSERT INTO Companies VALUES (2, 'Volvo', 'VOLV-B', 'Industri', 5.50);");
    db.run("INSERT INTO Companies VALUES (3, 'Saab', 'SAAB-B', 'Försvar', 1.20);");
    
    db.run("INSERT INTO StockPrices VALUES (101, 1, '2026-09-04', 285.00, 1200000);");
    db.run("INSERT INTO StockPrices VALUES (102, 2, '2026-09-04', 272.50, 2500000);");
    db.run("INSERT INTO StockPrices VALUES (103, 3, '2026-09-04', 252.00, 800000);");

    document.getElementById('sqlStatus').innerText = "✓ Databasen är laddad med aktiedata! Tryck på kör för att testa.";
    document.getElementById('sqlStatus').style.color = "#00ff88";
    
    // Kör startfrågan automatiskt
    runQuery();
}).catch(err => {
    document.getElementById('sqlStatus').innerText = "Kunde inte ladda SQL-motorn: " + err.message;
});

// Funktion för att exekvera SQL-frågan från textrutan
function runQuery() {
    const query = document.getElementById('sqlQuery').value;
    const table = document.getElementById('sqlResultTable');
    table.innerHTML = ""; // Rensa gamla resultat

    try {
        const results = db.exec(query);
        if (results.length === 0) {
            table.innerHTML = "<tr><td>Frågan kördes utan resultat (eller tom tabell).</td></tr>";
            return;
        }

        const columns = results[0].columns;
        const values = results[0].values;

        // Bygg tabellhuvud (Headers)
        let headerRow = "<tr>";
        columns.forEach(col => { headerRow += `<th>${col}</th>`; });
        headerRow += "</tr>";
        table.innerHTML += headerRow;

        // Bygg rader (Data)
        values.forEach(row => {
            let rowHtml = "<tr>";
            row.forEach(val => { rowHtml += `<td>${val !== null ? val : 'NULL'}</td>`; });
            rowHtml += "</tr>";
            table.innerHTML += rowHtml;
        });
    } catch (error) {
        table.innerHTML = `<tr><td style="color: #ff4d4d; font-weight: bold;">SQL Fel: ${error.message}</td></tr>`;
    }
}

// Koppla händelser till knappen
document.getElementById('runSqlBtn').addEventListener('click', runQuery);
