#SQL > Python > csv files

import pandas as pd
import pyodbc as odbc
from datetime import datetime

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

DF.to_csv('BD_TON'+datetime.now().strftime("%Y%m%d")+'.csv',index=False,encoding='utf-8') 