@echo off

set AMBIENTE_VIRTUAL=env
python -m venv %AMBIENTE_VIRTUAL%
echo Ambiente virtual criado com sucesso.
call .\%AMBIENTE_VIRTUAL%\Scripts\activate
pip install pandas
pip install streamlit
pip install openpyxl
echo Libs instaladas
echo Ambiente virtual foi configurado!
echo Inicializando o projeto
call streamlit run main.py

