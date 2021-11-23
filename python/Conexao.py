from mysql.connector import connect
from credenciais import user,password,host,banco

conn = connect(host=host,user=user,password=password,database=banco)


