import pyodbc

server = 'laptop-hardik'
database = 'user_demo'
username = ''
password = ''
connection_string = (
    'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

conn = pyodbc.connect(connection_string, autocommit=True, Pooling=True)

cursor = conn.cursor()
