import MySQLdb

db = MySQLdb.connect(user="root", passwd="@Seila00", db="Cadastro", host="localhost", port=3306, autocommit=False)
cursor = db.cursor()
cursor.execute("SELECT * from cliente")
print(cursor.fetchall())
print("conexão realizada com sucesso")


                                    #Criando novos usuários
try:
    db.begin()
    cursor.execute("INSERT INTO cliente (Nome,Login,Senha) VALUES ('Mayara','Mayra01',051401)")
    cursor.execute("INSERT INTO cliente (Nome,Login,Senha) VALUES ('Cleyson','Cleyson01',069710)")
    db.commit()

#except:
    #db.rollback()
#cursor.execute("SELECT * FROM cliente")
                                    #Verificando último ID utilizado.
#print(cursor.lastrowid)

                                    # Atualizando usuários
#cursor.execute("UPDATE cliente SET Nome='João',Login='joao01',Senha=789123  WHERE idcliente=1")
#cursor.execute("SELECT * from cliente")
#print(cursor.fetchall())


                                    # Delete usuários
#cursor.execute("DELETE FROM cliente WHERE idcliente=4")
#cursor.execute("SELECT * from cliente")
#print(cursor.fetchall())

#db.close()