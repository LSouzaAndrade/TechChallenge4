import yfinance as yf
import matplotlib.pyplot as plt

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

# Gráfico com as séries (Máximo, Mínimo, Abertura, Fechamento)
plt.figure(figsize=(12, 6))
plt.plot(hist.index, hist['Open'], label='Abertura', marker='o', linestyle='-', color='blue')
plt.plot(hist.index, hist['High'], label='Máximo', marker='o', linestyle='-', color='green')
plt.plot(hist.index, hist['Low'], label='Mínimo', marker='o', linestyle='-', color='red')
plt.plot(hist.index, hist['Close'], label='Fechamento', marker='o', linestyle='-', color='purple')
plt.title(f"Histórico de Preços - {info['longName']} (Último Mês)")
plt.xlabel("Data")
plt.ylabel("Preço (USD)")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
