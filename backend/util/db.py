from dotenv import load_dotenv
import cx_Oracle
import os


load_dotenv()
path = os.getenv("path")
address = os.getenv("address")
port = os.getenv("port")
service = os.getenv("service")
user = os.getenv("user")
password = os.getenv("password")


cx_Oracle.init_oracle_client(lib_dir=path)
dns = cx_Oracle.makedsn(address, port, service_name=service)
connection = cx_Oracle.connect(user=user, password=password, dsn=dns)
db = connection.cursor()


def select_all(table_name: str):
    db.execute("SELECT * FROM " + table_name)
    return db.fetchall()


def select_id(table_name: str, id_name: str, id_val):
    db.execute("SELECT * FROM " + table_name + " WHERE " + id_name + " LIKE '" + str(id_val) + "'")
    return db.fetchone()


def insert(table_name: str, column_names: str, column_vals: str):
    db.execute("INSERT INTO " + table_name + "(" + column_names + ") " + " VALUES(" + column_vals + ")")
    connection.commit()

def delete(table_name: str, id_val: str, id_name:str):
    db.execute("DELETE FROM " + table_name + " WHERE " + id_name + " = '" + str(id_val) + "'")
    connection.commit()


def custom_statement(statement: str):
    db.execute(statement)
    connection.commit()
    return db.fetchall()
