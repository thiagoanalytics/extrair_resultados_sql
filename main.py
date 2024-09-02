import pandas as pd
import pyodbc as odbc
import json
import os
from datetime import datetime
import sys

enable_venv = os.path.join(os.path.dirname(os.path.abspath(__file__)), r'.venv\Scripts\activate_this.py')
exec(open(enable_venv).read(), {'__file__': enable_venv})

def load_config(json_path):
    """Carrega as configurações do arquivo JSON."""
    with open(json_path, 'r') as file:
        config = json.load(file)
    return config

def get_connection_string(config):
    """Constrói a string de conexão a partir das configurações."""
    try:
        conn_str = (
            f"Driver={{ {config['driver']} }};"
            f"Server={config['server']};"
            f"Database={config['database']};"
            f"Trusted_Connection={config['trusted_connection']};"
        )
        return conn_str
    except KeyError as e:
        print(f"Erro na configuração da string de conexão: falta a chave {e}")
        sys.exit(1)

def main(json_path):
    """Função principal para execução do script."""
    try:
        # Carrega a configuração
        config = load_config(json_path)
        
        # Obtém as configurações
        conn_config = config['connection_string']
        output_path = config['output_path']
        file_prefix = config['file_prefix']
        
        # Constrói a string de conexão
        connection_string = get_connection_string(conn_config)
        
        # Conecta ao banco de dados
        ConnectionString = odbc.connect(connection_string)
        
        # Consulta SQL
        Query = pd.read_sql_query(
            '''
            select * from [dbStone].[Auxiliar].[StoneCampanhaCliente]
            ''', ConnectionString
        )
        
        # Cria DataFrame
        DF = pd.DataFrame(Query)
        
        # Define o caminho completo do arquivo CSV
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        caminho_completo = os.path.join(output_path, file_prefix + datetime.now().strftime("%Y%m%d") + '.csv')
        
        # Salva o DataFrame como CSV
        DF.to_csv(caminho_completo, index=False, encoding='utf8')
        print(f'Arquivo CSV salvo em: {caminho_completo}')
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Verifica o número de argumentos
    if len(sys.argv) != 2:
        print("Uso: python script.py <caminho_para_config.json>")
        sys.exit(1)
    else:
        json_path = sys.argv[1]
        main(json_path)
