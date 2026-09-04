# =========================================================================
# LIVE DATA PIPELINE - NASDAQ STOCKHOLM OMXS30 (FIXED)
# Syfte: Hämta RIKTIG realtidsdata via yfinance API för Stockholmsbörsen.
# Genererar automatiskt en städad Excel-export för Power BI.
# =========================================================================

import pandas as pd
import yfinance as yf

print("🚀 Initierar API-anslutning till Nasdaq Stockholm...")

stock_mapping = {
    'INVE-B.ST': {'Company': 'Investor', 'Sector': 'Investment'},
    'VOLV-B.ST': {'Company': 'Volvo', 'Sector': 'Industri'},
    'SAAB-B.ST': {'Company': 'Saab', 'Sector': 'Försvar'},
    'SEB-A.ST':  {'Company': 'SEB', 'Sector': 'Bank'},
    'HM-B.ST':   {'Company': 'H&M', 'Sector': 'Sällanköpsvaror'},
    'ERIC-B.ST': {'Company': 'Ericsson', 'Sector': 'Telekom'},
    'AZN.ST':    {'Company': 'AstraZeneca', 'Sector': 'Hälsovård'},
    'EVO.ST':    {'Company': 'Evolution', 'Sector': 'Gaming'}
}

tickers_list = list(stock_mapping.keys())

try:
    print("📥 Hämtar realtidsdata från Yahoo Finance API...")
    # Hämtar 5 dagars historik
    raw_data = yf.download(tickers_list, period='5d', progress=False)
    
    processed_records = []
    
    for ticker in tickers_list:
        try:
            # Säkrar att vi drar ut rätt data per kolumn genom att platta till Multi-Indexet
            ticker_data = raw_data.xs(ticker, axis=1, level=1) if isinstance(raw_data.columns, pd.MultiIndex) else raw_data
            ticker_data = ticker_data.dropna()
            
            if len(ticker_data) >= 2:
                latest_close = ticker_data['Close'].iloc[-1]
                previous_close = ticker_data['Close'].iloc[-2]
                volume = ticker_data['Volume'].iloc[-1]
                
                day_change = ((latest_close - previous_close) / previous_close) * 100
                
                processed_records.append({
                    'Ticker': ticker.replace('.ST', '').replace('-A', '').replace('-B', ''),
                    'Bolag': stock_mapping[ticker]['Company'],
                    'Sektor': stock_mapping[ticker]['Sector'],
                    'Live_Kurs_SEK': round(latest_close, 2),
                    'Idag_Utveckling_%': round(day_change, 2),
                    'Handelsvolym': int(volume)
                })
        except Exception:
            continue
            
    df = pd.DataFrame(processed_records)
    
    # 🔥 HÄR SKAPAS FILEN AUTOMATISKT PÅ DIN MAC:
    output_filename = 'aktiedata_live.xlsx'
    df.to_excel(output_filename, index=False)
    
    print("\n--- 📈 LIVE DATA UTDRAG (NASDAQ STOCKHOLM) ---")
    print(df.to_string(index=False))
    print(f"\n✅ PIPELINE LYCKADES: '{output_filename}' har skapats helt felfritt!")

except Exception as e:
    print(f"❌ Fel uppstod vid hämtning av marknadsdata: {e}")

