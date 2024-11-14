import yfinance as yf

ticker = "AAPL" # Ticker da Apple
acao = yf.Ticker(ticker)

hist = acao.history(period="1mo")
print(hist) # Histórico da ação

info = acao.info
print(info['longName']) # Nome da empresa
print(info['sector']) # Setor de atuação
print(info['currentPrice']) # Preço atual da ação

ultimo_fechamento = acao.history(period="1d")['Close'].iloc[0] 
print(f"{ultimo_fechamento:.2f}") # Último preço de fechamento da ação
