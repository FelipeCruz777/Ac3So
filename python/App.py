from Conexao import conn

cursor = conn.cursor()

# for i in range(0,3):
#     nome = input("Insira seu nome: \n ")
#     idade = int(input("Insira sua idade: \n"))
#     cursor.execute(f"Insert into pessoa values(null,'{nome}',{idade})")
#     conn.commit()

# cursor.close()
cursor2 = conn.cursor()

id = input("Insira o id do usuario que você quer saber a idade:\n")
cursor2.execute(f"select * from pessoa where idPessoa = '{id}'")
pessoa = cursor2.fetchone()

print(f"\nNome:{pessoa[1]} \nIdade:{pessoa[2]}\n1")
cursor2.close()
conn.close()

