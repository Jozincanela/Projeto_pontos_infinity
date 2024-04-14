import pandas as pd
import streamlit as st


def saber_numero_mes(mes:str) -> int:
        match mes.lower():
            case "janeiro":
                return 1
            case "fevereiro":
                return 2
            case "marco":
                return 3
            case "abril":
                return 4
            case "maio":
                return 5
            case "junho":
                return 6
            case "julho":
                return 7
            case "agosto":
                return 8
            case "setembro":
                return 9
            case "outubro":
                return 10
            case "novembro":
                return 11
            case "dezembro":
                return 12
              
def ler_arquivo_excel(caminho_arquivo: str, Nome: str = None, Mes: str = None):
    
    
    """
    Lê um arquivo Excel e retorna todas as linhas ou linhas filtradas com base na especificação.

    Args:
        caminho_arquivo (str): Caminho para o arquivo Excel.
        Nome (str, optional): Valor específico para filtrar as linhas por nome. Padrão é None.
        Mes (str, optional): Valor específico para filtrar as linhas por mês. Padrão é None.
        Dia (int, optional): Valor específico para filtrar as linhas por dia. Padrão é None.

    Returns:
        pandas.DataFrame: DataFrame com as linhas lidas ou linhas filtradas.
    """
    df = pd.read_excel(caminho_arquivo)
    


    # Convertendo a coluna 'DateTime' para datetime
    df['DateTime'] = pd.to_datetime(df['DateTime'], format='%Y/%m/%d %H:%M')
    df['Date'] = df['DateTime'].dt.date
    df['Time'] = df['DateTime'].dt.time


    if Nome is not None :
        if  Mes == None:
            linhas_filtradas = df[df['Name'] == Nome]
            return linhas_filtradas
        elif Mes != None:
            num_mes = saber_numero_mes(Mes) 
            linhas_filtradas = df[(df['DateTime'].dt.month == num_mes) & (df["Name"] == Nome)]
            return linhas_filtradas
    elif Mes is not None:
        num_mes = saber_numero_mes(Mes) 
        linhas_filtradas = df[df['DateTime'].dt.month == num_mes]
        return linhas_filtradas
    else:
        return df
    
def ler_coluna_excel(caminho_arquivo: str, Coluna: str):
    """
    Lê todas as linhas de uma coluna específica de um arquivo Excel e retorna uma lista com valores únicos.

    Args:
        caminho_arquivo (str): Caminho para o arquivo Excel.
        Coluna (str): Nome da coluna a ser lida.

    Returns:
        list: Lista com valores únicos da coluna.
    """
    try:
        df = pd.read_excel(caminho_arquivo)
        valores_coluna = df[Coluna].tolist()
        valores_unicos = list(set(valores_coluna))
        return valores_unicos
    except FileNotFoundError:
        st.write(f"Arquivo '{caminho_arquivo}' não encontrado.")
        return []

