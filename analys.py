# =========================================================================
# JUNIOR DATA ANALYST - FINANCIAL ANALYTICS (PYTHON)
# Syfte: Hämta aktiedata, beräkna procentuell utveckling och hitta köpsignaler.
# =========================================================================

import pandas as pd

# 1. Historisk aktiedata för din portfölj (Stängningskurser)
stock_data = {
    'Ticker': ['INVE-B', 'VOLV-B', 'SAAB-B'],
    'Company': ['Investor', 'Volvo', 'Saab'],
    'Sector': ['Investment', 'Industri', 'Försvar'],
    'Price_Day1': [280.00, 279.75, 240.50],
    'Price_Day2': [285.00, 272.50, 252.00]
}

df = pd.DataFrame(stock_data)

# 2. Beräkna prisförändring i procent mellan dag 1 och dag 2
df['Performance_%'] = ((df['Price_Day2'] - df['Price_Day1']) / df['Price_Day1']) * 100

print("--- Finansiell dataanalys med Python (Rensad och beräknad) ---")
print(df[['Company', 'Sector', 'Performance_%']])