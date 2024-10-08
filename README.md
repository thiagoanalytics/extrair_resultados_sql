# Exportar consulta SQL Server para .csv
![SQL](https://img.shields.io/badge/SQL-blue)

![Python](https://img.shields.io/badge/Python-green)

Neste projeto, desenvolvi um script que transforma o resultado de uma consulta SQL Server em um arquivo CSV. O objetivo principal é fornecer uma maneira eficiente de exportar dados de um banco de dados SQL Server para um formato amplamente utilizado e fácil de manipular, como o CSV (Comma-Separated Values).

## 📃Descrição do Processo:
### 1 - Execução da Consulta SQL:

O script começa executando uma consulta SQL no banco de dados SQL Server. Esta consulta pode ser uma simples SELECT ou uma consulta mais complexa, dependendo das necessidades do usuário. O resultado da consulta é armazenado em um conjunto de dados que contém as informações que precisam ser exportadas.

### 2 - Criação do Arquivo CSV:

Após a execução da consulta, o script converte os dados retornados em um formato CSV. O CSV é um formato de texto onde cada linha representa um registro e os valores são separados por vírgulas. Este formato é amplamente utilizado para a troca de dados entre sistemas e pode ser facilmente aberto e editado em ferramentas como Microsoft Excel e Google Sheets.
### 3 - Exportação dos Dados:

O script escreve os dados no arquivo CSV, garantindo que cada coluna da tabela SQL seja corretamente representada como uma coluna no arquivo CSV. O nome das colunas é incluído na primeira linha do arquivo CSV, proporcionando uma estrutura clara e compreensível.
### 4 - Salvamento e Disponibilidade:

O arquivo CSV é salvo em um local especificado pelo usuário ou em um diretório padrão. Após a criação, o arquivo pode ser acessado e compartilhado conforme necessário.
## 💰Benefícios:
- Facilidade de Manipulação: Arquivos CSV são fáceis de importar e manipular em diversos softwares, como planilhas e ferramentas de análise de dados.
- Portabilidade: CSV é um formato leve e amplamente aceito, facilitando a transferência de dados entre diferentes sistemas e plataformas.
- Simples Integração: O script pode ser facilmente integrado em processos de ETL (Extração, Transformação e Carga) para automatizar a exportação de dados.


## 🔎Descrição da Versão

Nesta versão a configuração é feita na pasta **\config\config.json** onde você edita as seguintes informações:
```
{
    "connection_string": {
        "server": "nome_do_servidor",
        "database": "nome_do_banco"
    },
    "output_path": "pasta_de_destino",
    "file_prefix": "nome_do_arquivo"
}
```

E a query é configurada no arquivo **query.ini** localizado na pasta "Disco:/extrair_resultados_sql/query:
```
# Arquivo .ini
[SQL]
query = 
    select * 
    from [banco].[schema].[tabela]
        
``` 
Realizei o teste com queries simples como:
```
select * from [banco].[schema].[tabela]
```
E com queries com **joins** e **order by**:
```
SELECT TOP (200) a.[coluna_id]
      ,cast([coluna_data] as date) as 'Data'
      ,a.[coluna_status]
      ,[coluna_tipo]
      ,[coluna_responsavel]
      ,a.[coluna_email]
      ,a.[coluna_proprietario_email]
      ,[coluna_empresa]
	  ,b.[coluna_id]
	  ,c.[coluna_time]
	  ,d.[coluna_valor]
FROM [banco].[schema].[tabela] as a
left join [banco].[schema].[tabela2] as b on [b.coluna_id] = a.[coluna_id]
left join [banco].[schema].[tabela3] as c on [b.coluna_id] = c.[coluna_id] 
left join [banco].[schema].[tabela4] as d on d.[coluna_id] = a.[coluna_id]

order by c.[team_name],d.[novo_valor]
```  
## 🚀Como executar
Você deve passar como parâmetro o local onde está o arquivo **.json** com as configurações e o local onde se encontra o arquivo **.ini**.
``` 
python main.py "Disco:/extrair_resultados_sql/config/config.json" "Disco:/extrair_resultados_sql/query/query.ini"
``` 


## Conecte-se comigo

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/thiago-romualdo-732204244/)