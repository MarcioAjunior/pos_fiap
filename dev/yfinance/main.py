def get_data_from_yfinance():
    """Função que pega os tickers da api yfinance e salva em csv o ultimos 5 pregões"""
      
    ROOT = "C:\\Users\\marci\\OneDrive\\Desktop\\FIAP\\dev\\yfinance"
    
    str_date = date.today().strftime("%Y/%m/%d").replace('/','')
    
    today_path = os.path.join(ROOT, str_date)
    
    if not os.path.exists(today_path):
        os.mkdir(today_path)
    
    
    tickers = yf.Tickers('msft aapl goog')
    
    try:
        for key in tickers.tickers:
            df = tickers.tickers[key].history(period = '5d')

            df = df[['Open','High','Low','Close','Volume']]
            df['Amplitude_de_preco'] = abs(df['High'] - df['Low'])
            df['Volume'] = np.float64(df['Volume'])
            df['Total_RS_negociado'] = df['Volume'] * df['Close']
            
            df.to_csv(today_path + f'\\{key}.csv', header= False)
            
    except Exception as e:
        raise Exception(e)
        
            

if __name__ == '__main__':
    import yfinance as yf
    from datetime import date
    import numpy as np
    import os
    get_data_from_yfinance()