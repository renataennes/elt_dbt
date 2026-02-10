import requests
import pandas as pd
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL
from dotenv import load_dotenv
import os

load_dotenv()

class JobicyAPI:
#definindo os atributos da classe
    def __init__(self, base_url:str, industry: str, count: int):
        self.base_url = base_url
        self.industry = industry
        self.count = count
        self.data = None

#requisitar os dados da API e salvar numa tributo da classe
    def fetch_data(self):
        url = f"{self.base_url}?count={self.count}&industry={self.industry}"
# Adicione este dicionário de headers
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json"
        }
        
        # Passe os headers dentro da função get
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            self.data = response.json()
            print("Dados extraídos com sucesso!")
        else:
            print(f"Falha na requisição. Status: {response.status_code}")
            response.raise_for_status()

#carregar dados do self.data em um dataframe
    def get_jobs_data(self):
        if self.data and 'jobs' in self.data:
            return pd.DataFrame(self.data['jobs'])
        else:
            return pd.DataFrame()
        

#classe para conectar e salvar os dados no snowflake
class Snowflake:
    def __init__(self, account: str, user: str, password: str, database: str, schema: str, warehouse: str):
        self.engine = create_engine(URL(
        account=account,
        user=user,
        password=password,
        database=database,
        schema=schema,
        warehouse=warehouse
    ))

    #salvar dados no snowflake a partir de um dataframe:
    def save_to_snowflake(self, df:pd.DataFrame, table_name:str):
        df.to_sql(table_name, self.engine, if_exists='replace', index=False)
    
def main():
    api = JobicyAPI(
        base_url="https://jobicy.com/api/v2/remote-jobs",
        industry="data-science",
        count=10
    )
    api.fetch_data()

    jobs_df = api.get_jobs_data()
    if not jobs_df.empty:#verificar se o dataframe não está vazio

    
        saver=Snowflake(
            account=os.getenv("ACCOUNT"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE"),
            schema=os.getenv("SCHEMA"),
            warehouse=os.getenv("WAREHOUSE")  
        )

        saver.save_to_snowflake(jobs_df, table_name="trabalhos_remotos")
        print("Dados salvo com sucesso no Snowflake!")

    else:
        print("Não existem dados a serem salvos no Snowflake!")


if __name__=='__main__':
    main()
    