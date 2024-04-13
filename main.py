import pandas as pd
import streamlit as st
import funcoes
@st.cache_data
#decorator --> linha de codigo que adiciona uma funcionalidade para funcao que vem logo em baixo , vantagens ---> quando aplicamos ele, ele armazena no cache do usuario as informações que ele esta carreagando aqui , primeira vez geralmente demora mas depois ele flui melhor 

def o():...

CAMINHO_ARQUIVO = "pontoagoravai.xlsx"
lista_meses =  [None,"Janeiro","Fevereiro","Marco","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro" ]

lista_todos_nomes = funcoes.ler_coluna_excel(CAMINHO_ARQUIVO, 'Name')
lista_todos_nomes.sort()
lista_todos_nomes.insert(0, None)

st.set_page_config(page_title="Projeto Controle de Ponto Infinity Bh")
with st.container():
    st.title("Controle de ponto Infinity BH")
    st.subheader("Registros de Controle de Ponto")


selecao_pessoa = st.sidebar.selectbox('Selecione Um Funcionario', lista_todos_nomes)
selecao_mes =  st.sidebar.selectbox('Selecione um mes', lista_meses)
tabela = funcoes.ler_arquivo_excel(CAMINHO_ARQUIVO, selecao_pessoa, selecao_mes)

with st.container():
    st.write("---")
    ponto_por_pessoa = tabela[['Name','DateTime']]
    try:
        st.bar_chart(ponto_por_pessoa,x="DateTime",y="Name")
    except:
        st.write("Erro! por favor tente novamente mais tarde")
        






