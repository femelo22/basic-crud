import mysql.connector

con = mysql.connector.connect(
    host='localhost',
    user='mysql',
    password='root',
    database='crud'
)

#Vai executar os comandos da execucao do banco, vai criar nossa conexão
cursor = con.cursor()

# CREATE

nome_produto = "Arroz"
nome_produto_2 = "Feijao"
valor = 20
valor_2 = 15
comando = f'INSERT INTO Vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor}), ("{nome_produto_2}", {valor_2})'
cursor.execute(comando)
con.commit() #Precisamos dar o commit sempre que tem modificacao no banco (create, update ou delete)


# READ

comando_read = "SELECT * FROM Vendas"
cursor.execute(comando_read)
result = cursor.fetchall()
print(result)

#UPDATE

nome_produto = "Arroz"
valor = 30
comando = f'UPDATE Vendas SET valor = {valor} WHERE nome_produto= "{nome_produto}"'
cursor.execute(comando)
con.commit()

#DELETE

nome_produto = "Feijao"
comando = f'DELETE FROM Vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
con.commit()
cursor.close()
con.close()


