import pandas as pd
import sqlalchemy as sa
import json
import os
from datetime import datetime
import sys
import configparser  # Para leitura do arquivo .ini

enable_venv = os.path.join(os.path.dirname(os.path.abspath(__file__)), r'.venv\Scripts\activate_this.py')
exec(open(enable_venv).read(), {'__file__': enable_venv})

# Definir um novo timeout de 10 minutos 60 segundos * 10
timeout = 60 * 10  # configuração padrão da TP

def load_config(json_path):
    """Carrega as configurações do arquivo JSON."""
    with open(json_path, 'r') as file: 
        config = json.load(file)
    return config

def get_connection_string(config):
    """Constrói a string de conexão SQLAlchemy a partir das configurações."""
    try:
        conn_str = (
            f"mssql+pyodbc://{config['server']}/{config['database']}"
            "?driver=SQL+Server+Native+Client+11.0"
            "&trusted_connection=yes"
            'Integrated Security=SSPI;'  # configuração padrão da TP
            'Persist Security Info=True;'  # configuração padrão da TP
            'APP=Dynamic Copy Table/1.0.0, Python, BI CORP;'  # configuração padrão da TP
            'QueryTimeout=' + str(timeout) + ';'  # configuração padrão da TP
        )
        return conn_str
    except KeyError as e:
        print(f"Erro na configuração da string de conexão: falta a chave {e}")
        sys.exit(1)

def load_query(ini_path):
    """Carrega a consulta SQL a partir de um arquivo .ini."""
    config = configparser.ConfigParser()
    config.read(ini_path)
    try:
        query = config.get('SQL', 'query')
        return query
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        print(f"Erro ao ler a consulta SQL do arquivo .ini: {e}")
        sys.exit(1)

def main(json_path, ini_path):
    """Função principal para execução do script."""
    try:
        # Carrega a configuração
        config = load_config(json_path)
        
        # Obtém as configurações
        conn_config = config['connection_string']
        output_path = config['output_path']
        file_prefix = config['file_prefix']
        
        # Constrói a string de conexão usando SQLAlchemy
        connection_string = get_connection_string(conn_config)
        
        # Conecta ao banco de dados
        engine = sa.create_engine(connection_string)
        
        # Carrega a consulta SQL do arquivo .ini
        query = load_query(ini_path)
        
        # Executa a consulta SQL
        df = pd.read_sql_query(query, engine)
        
        # Define o caminho completo do arquivo CSV
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        caminho_completo = os.path.join(output_path, file_prefix + datetime.now().strftime("%Y%m%d") + '.csv')
        
        # Salva o DataFrame como CSV
        df.to_csv(caminho_completo, index=False, encoding='utf-8-sig')
        print(f'Arquivo CSV salvo em: {caminho_completo}')
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Verifica o número de argumentos
    if len(sys.argv) != 3:
        print("Uso: python script.py <caminho_para_config.json> <caminho_para_query.ini>")
        sys.exit(1)
    else:
        json_path = sys.argv[1]
        ini_path = sys.argv[2]
        main(json_path, ini_path)
