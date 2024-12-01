import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import requests
import pandas as pd

# Configurações do Streamlit
st.title("Valores de fechamento de ações")

# Entrada do usuário
opcoes = ['AAPL', 'NVDA', 'TSLA']
ticker = st.selectbox("Escolha uma opção:", opcoes)

# Obtenção dos dados
try:
    acao = yf.Ticker(ticker)
    hist = acao.history(period="3mo")

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

        #Chamada da API do modelo
        try:
            request = {}
            request['ticker'] = ticker
            request['closing_prices'] = hist['Close'].tail(30).values.tolist()

            url = "http://127.0.0.1:8000/"
            response = requests.post(url, json=request, timeout=5)
            response.raise_for_status()
            resultado = response.json()
            preco_estimado = resultado.get("prediction", "Chave não encontrada")
            st.write(f"**Próximo preço de fechamento estimado:** {round(preco_estimado, 2)} USD")


            # Gráfico com Matplotlib
            st.subheader("Histórico de preços")
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.plot(hist.index, hist['Close'], label='Fechamento', marker='o', linestyle='-', color='red')

            proxima_data = hist.index[-1] + pd.Timedelta(days=1)
            ax.plot([hist.index[-1], proxima_data], [ultimo_fechamento, preco_estimado],
                    label='Predição', marker='o', linestyle='-', color='blue')

            ax.set_title(f"Histórico de Preços - {nome_empresa}")
            ax.set_xlabel("Data")
            ax.set_ylabel("Preço (USD)")
            ax.legend()
            ax.grid(True)
            plt.xticks(rotation=45)
            st.pyplot(fig)

        except requests.exceptions.Timeout:
            st.error("A requisição demorou demais e excedeu o tempo limite.")
        except requests.exceptions.RequestException as e:
            st.error(f"Erro ao enviar dados: {e}")

    else:
        st.write("**Nenhum dado histórico encontrado para o ticker informado.**")

except Exception as e:
    st.error(f"Ocorreu um erro ao processar os dados: {e}")

