#SQL > Python > csv files

import pandas as pd
import pyodbc as odbc
import json
import os
from datetime import datetime



path = "D:/Thiago/TP - Home Office/BI/Python/extrair_resultados_sql/resultado"
os.makedirs(path, exist_ok=True)
caminho_completo = os.path.join(path, "BD_TON")

ConnectionString = odbc.connect(
    'Driver={SQL Server Native Client 11.0};'
    'Server=ListBiMis;'
    'Database=dbStone;'
    'Trusted_Connection=yes;'
)

Query = pd.read_sql_query(
    '''
    select * from [dbStone].[Auxiliar].[StoneCampanhaCliente]
    ''', ConnectionString
)

DF = pd.DataFrame(Query)

DF.to_csv(caminho_completo + datetime.now().strftime("%Y%m%d")+'.csv',index=False,encoding='utf8') 