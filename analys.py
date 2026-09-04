# =========================================================================
# JUNIOR DATA ANALYST - FINANCIAL ANALYTICS (PYTHON)
# Syfte: Hämta aktiedata, beräkna procentuell utveckling och hitta köpsignaler.
# =========================================================================

import pandas as pd

# 1. Simulerar historisk aktiedata för en portfölj (Stängningskurser över 3 dagar)
stock_data = {
    'Ticker': ['INVE-B', 'VOLV-B', 'SAAB-B', 'INVE-B', 'VOLV-B', 'SAAB-B'],
    'Company': ['Investor', 'Volvo', 'Saab', 'Investor', 'Volvo', 'Saab'],
    'Sector': ['Investment', 'Industri', 'Försvar', 'Investment', 'Industri', 'Försvar'],
    'Price_Day1': [280, 270, 245, 286, 275, 248],
    'Price_Day2': [285, 272, 250, 284, 265, 252]
}

df = pd.DataFrame(stock_data)

# 2. Beräkna prisförändring i procent mellan dag 1 och dag 2
df['Performance_%'] = ((df['Price_Day2'] - df['Price_Day1']) / df['Price_Day1']) * 100

print("--- Finansiell dataanalys med Python (Rensad och beräknad) ---")
print(df[['Company', 'Sector', 'Performance_%']])

# 3. Filtrera fram aktier som har gått upp mer än 2% (Potentiella köpsignaler)
print("\n--- Aktier med stark positiv trend (> 2% utveckling) ---")
bullish_stocks = df[df['Performance_%'] > 2.0]
print(bullish_stocks[['Company', 'Performance_%']])