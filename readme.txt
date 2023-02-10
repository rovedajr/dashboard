1) criar uma pasta e colocar os arquivos app.py e requirements.txt dentro dela
2) executar: python3 -m venv nome_do_ambiente_virtual
3) executar: source nome_do_ambiente_virtual/bin/activate  – a partir daqui, tudo é instalado no ambiente virtual e não mais global
4) pip3 install -r requirements.txt
5) depois da instalação de todas as dependências, executar: streamlit run app.py