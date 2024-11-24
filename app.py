import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Configurações do Streamlit
st.title("Visualização de Ações com Yahoo Finance")

# Entrada do usuário
opcoes = ['TSLA', 'AAPL', 'NVDA']
ticker = st.selectbox("Escolha uma opção:", opcoes)

# Obtenção dos dados
try:
    acao = yf.Ticker(ticker)
    hist = acao.history(period="1mo")

    # Informações da empresa
    info = acao.info
    nome_empresa = info.get('longName', 'Nome não disponível')
    setor = info.get('sector', 'Setor não disponível')
    preco_atual = info.get('currentPrice', 'Preço não disponível')

    st.subheader(f"Informações da Empresa: {nome_empresa}")
    st.write(f"**Setor:** {setor}")
    st.write(f"**Preço Atual:** {preco_atual} USD")

    # Último preço de fechamento
    if not hist.empty:
        ultimo_fechamento = hist['Close'].iloc[-1]
        st.write(f"**Último preço de fechamento:** {ultimo_fechamento:.2f} USD")

        # Gráfico com Matplotlib
        st.subheader("Gráfico de Preços (Último Mês)")
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(hist.index, hist['Open'], label='Abertura', marker='o', linestyle='-', color='blue')
        ax.plot(hist.index, hist['High'], label='Máximo', marker='o', linestyle='-', color='green')
        ax.plot(hist.index, hist['Low'], label='Mínimo', marker='o', linestyle='-', color='red')
        ax.plot(hist.index, hist['Close'], label='Fechamento', marker='o', linestyle='-', color='purple')
        ax.set_title(f"Histórico de Preços - {nome_empresa} (Último Mês)")
        ax.set_xlabel("Data")
        ax.set_ylabel("Preço (USD)")
        ax.legend()
        ax.grid(True)
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.write("**Nenhum dado histórico encontrado para o ticker informado.**")

except Exception as e:
    st.error(f"Ocorreu um erro ao processar os dados: {e}")
