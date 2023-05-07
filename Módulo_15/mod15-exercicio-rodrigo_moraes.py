import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import wikipedia
import requests
import time

from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


st.set_page_config(
    page_title="EBAC | Módulo 15 | Streamlit I | Exercício",
    # page_icon="https://ebaconline.com.br/favicon.ico",
    page_icon="https://raw.githubusercontent.com/RodzMoraes/curso-ebac/main/Media/favicon.ico",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown('''
<img src="https://raw.githubusercontent.com/RodzMoraes/curso-ebac/main/Media/ebac_logo_black.png" alt="ebac-logo">

---

# **Profissão: Cientista de Dados**
### **Módulo 15** | Streamlit I | Exercício

Aluno [Rodrigo Moraes](https://www.linkedin.com/in/moraes-rodrigo/)<br>
Data: 7 de maio de 2023.

---
            ''', unsafe_allow_html=True)


st.markdown("# Main page 🖥️")
st.sidebar.markdown("# Siebar 💻")

# 01 / 02 -------------------------------------------------------------------------------------------------------------------------
st.sidebar.title('Layout')

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)
# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

# 03 ------------------------------------------------------------------------------------------------------------------------------
st.title('Contador de Caracteres')

def contar_caracteres(texto):
    return len(texto)

def main1():
    texto = st.text_area("Insira um texto")
    if st.button("Contar"):
        num_caracteres = contar_caracteres(texto)
        st.write("O texto inserido possui", num_caracteres, "caracteres.")

if __name__ == "__main__":
    main1()

'---'

# 04 ------------------------------------------------------------------------------------------------------------------------------
st.title('Gerador de Gráfico')

def plot_grafico(dados):
    df = pd.DataFrame(dados, columns=["Categoria", "Valor"])
    fig, ax = plt.subplots()
    ax.bar(df["Categoria"], df["Valor"])
    ax.set_xlabel("Categoria")
    ax.set_ylabel("Valor")
    ax.set_title("Gráfico de Barras")
    st.pyplot(fig)

def main2():
    st.write("Insira os dados para o gráfico:")
    num_dados = st.number_input("Número de dados", min_value=1, step=1, value=1)
    dados = []
    for i in range(num_dados):
        categoria = st.text_input(f"Categoria {i+1}")
        valor = st.number_input(f"Valor {i+1}", value=0.0)
        dados.append((categoria, valor))
    
    if st.button("Gerar Gráfico"):
        plot_grafico(dados)

if __name__ == "__main__":
    main2()

'---'

# 05 ------------------------------------------------------------------------------------------------------------------------------
st.title('Conversor de Temperatura')

def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main3():
    celsius = st.number_input("Insira a temperatura em Celsius")
    if st.button("Converter"):
        fahrenheit = celsius_para_fahrenheit(celsius)
        st.write(f"A temperatura em Fahrenheit é: {fahrenheit:.2f} °F")

if __name__ == "__main__":
    main3()

'---'

# 06 ------------------------------------------------------------------------------------------------------------------------------
st.title('Calcular o Quadrado')

def calcular_quadrado(numero):
    quadrado = numero ** 2
    return quadrado

def main4():
    numero = st.number_input("Insira um número")
    if st.button("Calcular"):
        resultado = calcular_quadrado(numero)
        st.write(f"O quadrado de {numero} é: {resultado}")

if __name__ == "__main__":
    main4()


'---'

# 07 ------------------------------------------------------------------------------------------------------------------------------
st.title('Informações Nutricionais')

def obter_informacoes_fruta(fruta):
    informacoes = {
        "Maçã": "A maçã é uma fruta deliciosa e saudável.",
        "Laranja": "A laranja é rica em vitamina C e possui um sabor cítrico.",
        "Banana": "A banana é uma fruta energética e fonte de potássio.",
    }
    return informacoes.get(fruta, "Selecione uma fruta.")

def main5():
    fruta_selecionada = st.selectbox("Selecione uma fruta", ["Maçã", "Laranja", "Banana"])
    informacoes = obter_informacoes_fruta(fruta_selecionada)
    st.write(informacoes)

if __name__ == "__main__":
    main5()

'---'

# 08 ------------------------------------------------------------------------------------------------------------------------------
st.title('Previsão de Classificação de Flores')

def carregar_dataset():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    return X, y

def treinar_modelo(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

def fazer_previsao(model, entrada):
    previsao = model.predict(entrada)
    return previsao

def main6():
    X, y = carregar_dataset()
    model = treinar_modelo(X, y)

    sepal_length = st.slider("Comprimento da Sépala", 0.0, 10.0)
    sepal_width = st.slider("Largura da Sépala", 0.0, 10.0)
    petal_length = st.slider("Comprimento da Pétala", 0.0, 10.0)
    petal_width = st.slider("Largura da Pétala", 0.0, 10.0)

    entrada = [[sepal_length, sepal_width, petal_length, petal_width]]

    if st.button("Fazer Previsão"):
        previsao = fazer_previsao(model, entrada)
        especies = ["Setosa", "Versicolor", "Virginica"]
        st.write(f"A espécie prevista é: {especies[previsao[0]]}")

if __name__ == "__main__":
    main6()

'---'

# 09 ------------------------------------------------------------------------------------------------------------------------------
st.title("Previsão de Vendas")

def realizar_previsao(df, meses):
    X = df['Mes'].values.reshape(-1, 1)
    y = df['Vendas'].values

    modelo = LinearRegression()
    modelo.fit(X, y)

    proximos_meses = df['Mes'].max() + pd.date_range(start='1/1/2023', periods=meses, freq='M')
    previsao_vendas = modelo.predict(proximos_meses.values.reshape(-1, 1))

    previsao_df = pd.DataFrame({
        'Mês': proximos_meses,
        'Previsão de Vendas': previsao_vendas
    })

    return previsao_df

def mai7():

    df = pd.read_csv('dados.csv')
    st.write(df)

    meses = st.slider("Selecione o número de meses para a previsão", min_value=1, max_value=24, value=12)
    
    if st.button("Realizar Previsão"):
        previsao_df = realizar_previsao(df, meses)
        st.write(previsao_df)

if __name__ == "__main__":
    main7()

'---'

# 10 ------------------------------------------------------------------------------------------------------------------------------
st.title('Calcular IMC')

def calcular_imc(peso, altura):
    altura_metros = altura / 100
    imc = peso / (altura_metros ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc >= 18.5 and imc < 25:
        return "Peso normal"
    elif imc >= 25 and imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main8():
    peso = st.number_input("Insira seu peso (em kg)")
    altura = st.number_input("Insira sua altura (em cm)")
    if st.button("Calcular"):
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        st.write(f"Seu IMC é: {imc:.2f}")
        st.write(f"Classificação: {classificacao}")

if __name__ == "__main__":
    main8()

'---'

# 11 ------------------------------------------------------------------------------------------------------------------------------
st.title('Lista de Tarefas')

def adicionar_tarefa(tarefa, lista_tarefas):
    lista_tarefas.append(tarefa)
    return lista_tarefas

def remover_tarefa(tarefa, lista_tarefas):
    if tarefa in lista_tarefas:
        lista_tarefas.remove(tarefa)
    return lista_tarefas

def exibir_tarefas(lista_tarefas):
    st.write("Lista de Tarefas:")
    for i, tarefa in enumerate(lista_tarefas, start=1):
        st.write(f"{i}. {tarefa}")

def main9():
    lista_tarefas = []

    tarefa = st.text_input("Digite uma tarefa")
    if st.button("Adicionar"):
        lista_tarefas = adicionar_tarefa(tarefa, lista_tarefas)
        tarefa = ""

    exibir_tarefas(lista_tarefas)

    tarefa_remover = st.text_input("Digite a tarefa a ser removida")
    if st.button("Remover"):
        lista_tarefas = remover_tarefa(tarefa_remover, lista_tarefas)

    exibir_tarefas(lista_tarefas)

if __name__ == "__main__":
    main9()

'---'

# 12 ------------------------------------------------------------------------------------------------------------------------------
st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    def lowercase(x): return str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)

'---'

# 13 ------------------------------------------------------------------------------------------------------------------------------
st.title('Draw a line chart')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

'---'

# 14 ------------------------------------------------------------------------------------------------------------------------------
st.title("Gráfico de Linhas Interativo")

def gerar_dados():
    # Gera dados aleatórios para o exemplo
    df = pd.DataFrame({
        'x': np.arange(1, 11),
        'y': np.random.randn(10)
    })
    return df

def gerar_grafico(df):
    plt.plot(df['x'], df['y'])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Gráfico de Linhas')
    st.pyplot()

def main10():

    df = gerar_dados()
    st.write(df)

    gerar_grafico(df)

if __name__ == "__main__":
    main10()

'---'

# 15 ------------------------------------------------------------------------------------------------------------------------------
st.title('Plot a map')

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

'---'

# 16 ------------------------------------------------------------------------------------------------------------------------------
st.title('Use a selectbox for options')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
option = st.selectbox(
    'Which number do you like best?',
    df['first column'])
'You selected: ', option

'---'

# 17 ------------------------------------------------------------------------------------------------------------------------------
st.title('Widgets')

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name

'---'

# 18 ------------------------------------------------------------------------------------------------------------------------------
st.title('Layout')

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Escolha o seu temperamento',
        ("Colérico", "Sanguíneo", "Melancólico", "Fleumático"))
    st.write(f"Você escolheu o tempermanto: {chosen}. Parabéns!")

'---'
# 19 ------------------------------------------------------------------------------------------------------------------------------
st.title('Use checkboxes to show/hide data')

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    chart_data

'---'

# 20 ------------------------------------------------------------------------------------------------------------------------------
st.title('Show progress')

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'...and now we\'re done!'

'---'