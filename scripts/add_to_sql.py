import mysql.connector as mysql
import pandas as pd
from pathlib import Path
import os, logging

def DBConnect(dbName=None):
    """connect to SQL database"""
    conn = mysql.connect(host='localhost', user='root', password='password', database=dbName, buffered=True)
    cur = conn.cursor()
    return conn, cur

def createDB(dbName: str) -> None:
    """
    create database
    Parameter: database name : string
    """
    conn, cur = DBConnect()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbName};")
    conn.commit()
    cur.close()

def createTable(dbName, sqlFilePath) -> None:
    """
    create table
    Parameters: database name : string
                schema file path : string
    """
    conn, cur = DBConnect(dbName)
    sqlFile = sqlFilePath
    fd = open(sqlFile, 'r')
    readSqlFile = fd.read()
    fd.close()

    sqlCommands = readSqlFile.split(';')

    for command in sqlCommands:
        try:
            cur.execute(command)
        except Exception as ex:
            logging.error("Command skipped: ", command)
            logging.error(ex)
    conn.commit()
    cur.close()
    return

def read_from_file(filename: str) -> pd.DataFrame:
    """
    access data from dvc using repository url and mode of opening file
    Parameters: filename - must include extension; must be csv file
    """
    dataframe = pd.read_csv(filename)
    return dataframe


def insert_to_table(dbName: str, df: pd.DataFrame, table_name: str) -> None:
    """
    add records to table using SQL 'insert' command
    Parameters: database name
                dataframe from CSV file
                table name
    """
    conn, cur = DBConnect(dbName)
    for _, row in df.iterrows():
        sqlQuery = None
        data = None
        if table_name.__eq__("completed_orders"):

            sqlQuery = f"""INSERT INTO {table_name} (Trip_ID, Trip_Origin,Trip_Destination,Trip_Start_Time,Trip_End_Time) VALUES(%s, %s, %s, %s, %s);"""

            data = (row[0], row[1],row[2], row[3], (row[4]))

        elif table_name.__eq__("driver_location"):
            sqlQuery = f"""INSERT INTO {table_name} (id, order_id,driver_id,driver_action,latitude,longitude,created_at,updated_at) VALUES(%s, %s, %s, %s, %s, %s, %s, %s);"""

            data= (row[0], row[1],row[2],row[3],row[4], row[5], row[6],row[7])
        if (sqlQuery is not None) and (data is not None):
            try:
                # Execute the SQL command
                cur.execute(sqlQuery, data)
                conn.commit()
            except Exception as e:
                conn.rollback()
                logging.error("Error while inserting data", e)

if __name__ == "__main__":

    database_name = 'gokada_db'
    scripts_path = str(Path(os.getcwd()))+'/scripts'
    data_path =  str(Path(os.getcwd()))+'/data'

    # creating database
    createDB(dbName=database_name)

    # creating tables for each dataset
    createTable(dbName=database_name, sqlFilePath= scripts_path+'/nb_schema.sql')
    createTable(dbName=database_name, sqlFilePath= scripts_path+'/dloc_schema.sql')
    
    # read data from csv files in local storage
    dataframe_nb = read_from_file(data_path+'/nb.csv')
    dataframe_dloc = read_from_file(data_path+'/driver_locations_during_request.csv')
   
    # add data to the database tables
    insert_to_table(dbName=database_name, df=dataframe_nb, table_name='completed_orders')
    insert_to_table(dbName=database_name, df=dataframe_dloc, table_name='driver_location')