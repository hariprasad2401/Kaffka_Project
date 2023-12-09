import os
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host=os.getenv('host')
user=os.getenv('user')
password=os.getenv('password')
db=os.getenv('db')







def read_sql_data():
   
    mydb=pymysql.connect(
        host=host,
        user=user,
        password=password,
        db=db
    )

    df=pd.read_sql_query("Select * From Students",mydb)
    print(df.head())

    return df