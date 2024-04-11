import pandas as pd
import streamlit as st
CAMINHO_ARQUIVO = "pontoagoravai.xlsx"
@st.cache_data#decorator --> linha de codigo que adiciona uma funcionalidade para funcao que vem logo em baixo , vantagens ---> quando aplicamos ele, ele armazena no cache do usuario as informações que ele esta carreagando aqui , primeira vez geralmente demora mas depois ele flui melhor 
def ler_arquivo_exel(caminho_arquivo:str):
    ler = pd.read_excel(caminho_arquivo)
    pd.set_option('display.max_rows',None)# Mostra todas as linhas, sem abreviar nenhuma
    return ler


st.set_page_config(page_title="Projeto Controle de Ponto Infinity Bh")
with st.container():
    st.title("Controle de ponto Infinity BH")
    st.subheader("Registros de Controle de Ponto")

#menu para seleção de uma pessoa especifico
selecao_pessoa = st.sidebar.selectbox('Selecione Um Funcionario',['ALEX','ANA PIO','ANDRE F','ARTHUR','Barbara','Bruna A','CARLOS NOVAI','CECILIA LIZ','DERECK','Daniele','GABI','GABRIEL','GIANELL','HENRIQUE MUN','ISRAEL','Italo','JEAN B','LUCAS','MAIRA v','MARIA E','MARIANA','PEDRO LOYOLA','PEDROB','RAPHAEL','ROBERTO','ROCK','WASHINGTON LU','arthurd','joao V','livia'])


#Tela principal
with st.container():
    st.write("---")
    tabela = ler_arquivo_exel(CAMINHO_ARQUIVO)
    
    ponto_por_pessoa = tabela[['Name','DateTime']]
    #relacionando as datas com pessoas
    try:
        st.bar_chart(ponto_por_pessoa,x="DateTime",y="Name")
    except:
        st.write("Erro! por favor tente novamente mais tarde")
        






