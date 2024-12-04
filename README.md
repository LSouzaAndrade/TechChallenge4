# Tech Challenge - Fase 4 - Grupo 12 - 1MLET

## 🚀 Sobre o projeto 

### Objetivos da Fase 4
- **Desenvolvimento do Modelo LSTM**: Os códigos utilizados para coleta de dados e também para construção, treinamento, avaliação, salvamento e exportação dos modelos desenvolvidos podem ser acessados em [notebook.ipynb](notebook.ipynb);

- **Deploy do Modelo**: Foi criada API RESTful utilizando FastAPI e Docker para servir o modelo, os códigos utilizados podem ser acessados em [api.py](api.py) e [Dockerfile](Dockerfile);

- **Monitoramento**: Para monitoramento do tempo de resposta e utilização dos recursos por parte dos modelos foi utilizada a ferramenta Prometheus, cuja configuração pode ser acessada em [prometheus.yaml](prometheus.yaml);

- **Apresentação**: O uso do sistema de monitoramento, assim como os demais tópicos, podem ser melhor compreendidos conforme demonstrado na apresentação no seguinte [link](https://youtu.be/-3BDeu-7X5c)

## 📝 Arquitetura do Projeto

A estrutura de pastas e arquivos do projeto se encontra disposta da seguinte maneira:

```bash
├── Models                              # Diretório de modelos e derivados
    ├── model_AAPL.keras                # Modelo LSTM para ações da Apple
    ├── model_NVDA.keras                # Modelo LSTM para ações da NVidia
    ├── model_TSLA.keras                # Modelo LSTM para ações da Tesla
    ├── scaler_AAPL.pkl                 # Scaler serializado para modelo LSTM (Apple)
    ├── scaler_NVDA.pkl                 # Scaler serializado para modelo LSTM (NVidia)
    └── scaler_TSLA.pkl                 # Scaler serializado para modelo LSTM (Tesla)
├── api.py                              # API para requests aos modelos treinados
├── app.py                              # Aplicação Streamlit
├── LICENSE.txt                         # Licença MIT vigente sob este repositório
├── notebook.ipynb                      # Notebook utilizado para treinamento dos modelos
├── README.md                           # Documentação do projeto
└── requirements.txt                    # Dependências externas utilizadas
```

## 📋 Pré-requisitos
Para utilização da API para os modelos gerados neste projeto, se fazem necessárias as seguintes dependências:
- FastAPI;
- Joblib;
- Numpy;
- Prometheus_client;
- Psutil;
- Scikit-learn;
- Tensorflow;
- Uvicorn.

## 🔧 Instalação
Todas dependências necessárias para reprodução do projeto contido neste repositório foram testadas com a versão 3.12.7 do Python. \
É recomendado que sejam utilizadas as versões de dependências incluídas no arquivo [requirements.txt](requirements.txt), a fim de evitar erros originados por incompatibilidade de versões.\
Para isso, navegue até o diretório do projeto, e no terminal execute a seguinte sequência de comandos:

```bash
# Crie um ambiente virtual para instalar as dependências:
python3 -m venv .venv

# Para ativar o ambiente virtual, caso esteja usando Linux ou macOS, execute:
source .venv/bin/activate

# Para ativar o ambiente virtual, caso esteja usando Windows, execute:
.venv\Scripts\activate

# Instale as dependências do projeto:
pip install -r requirements.txt
```

Ou em caso de uso de Docker:
```bash
# Crie a imagem do Docker:
docker build -t nome-imagem:1.0 .

# Inicie o container com a imagem Docker criada:
docker run -d -p 8000:8000 --name nome-container nome-imagem:1.0
```

## ⚙️ Execução
Com o ambiente virtual ativo, e dependências necessárias instaladas, é necessario que sejam abertos em terminais distintos os servidores para a API do modelo, e para a aplicação.

### Uvicorn
```bash
# Inicie o servidor Uvicorn para execução do FastAPI:
# (Por padrão, o Uvicorn irá rodar na porta 8000)
uvicorn api:app
```
### Docker
```bash
# Inicie o container com a imagem Docker criada:
docker run -d -p 8000:8000 --name nome-container nome-imagem:1.0
```

Após o servidor da API estar em execução, é possível realizar requisições para API dos modelos. \
Sendo necessária a seguinte estrutura de payload para realizar a request à API:
```bash
{
    "ticker": str,                        #AAPL, NVDA ou TSLA
    "closing_prices": array[float](30)
}
 
```

## ✒️ Autores

Isabelli Andrade de Souza - https://github.com/Isabellitankian
<br>
Lucas Souza Andrade dos Santos - https://github.com/LSouzaAndrade
<br>
Michel de Lima Maia - https://github.com/Michel-Maia
<br>
Valquiria Rodrigues de Oliveira Pires - https://github.com/KyraPires