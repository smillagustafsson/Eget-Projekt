# =========================================================================
# JUNIOR DATA ANALYST - STOCKHOLM STOCK EXCHANGE (PYTHON DATA PIPELINE)
# Syfte: Analysera marknadsutveckling, index (OMXS30) och fördela sektorer.
# =========================================================================

import pandas as pd

# 1. Simulerar ett större dataset över Stockholmsbörsen (Nasdaq Stockholm)
market_data = {
    'Ticker': ['INVE-B', 'VOLV-B', 'SAAB-B', 'SEBA', 'AZN', 'SBB-B', 'EVO', 'SAND'],
    'Company': ['Investor', 'Volvo', 'Saab', 'SEB', 'AstraZeneca', 'SBB', 'Evolution', 'Sandvik'],
    'Segment': ['Large Cap', 'Large Cap', 'Large Cap', 'Large Cap', 'Large Cap', 'Mid Cap', 'Large Cap', 'Large Cap'],
    'Sector': ['Investment', 'Industri', 'Försvar', 'Bank', 'Hälsovård', 'Fastighet', 'Gaming', 'Industri'],
    'Price_Day1': [280.00, 279.75, 240.50, 142.00, 1450.00, 4.50, 1120.00, 215.00],
    'Price_Day2': [285.00, 272.50, 252.00, 145.50, 1485.00, 3.90, 1155.00, 212.00]
}

df = pd.DataFrame(market_data)

# 2. Beräkna procentuell utveckling per aktie
df['Performance_%'] = ((df['Price_Day2'] - df['Price_Day1']) / df['Price_Day1']) * 100

print("--- 📈 MARKNADSANALYS: NASDAQ STOCKHOLM ---")
# 3. Beräkna genomsnittlig utveckling per sektor (Verksamhetsnära BI-insikt)
sector_performance = df.groupby('Sector')['Performance_%'].mean().reset_index()
print("\nGenomsnittlig utveckling per sektor:")
print(sector_performance.round(2))

# 4. Beräkna totalt index-estimat (Simulerat OMXS30-drag)
omx_performance = df['Performance_%'].mean()
print(f"\nTotal marknadsutveckling (OMXS30-index): {omx_performance:.2f}%")
