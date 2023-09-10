import mysql.connector
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from mysql.connector import Error

app = Flask(__name__)
#config conexao banco
try:
    con = mysql.connector.connect(host='localhost',database='bd_teste',user='developer',password='')
    if con.is_connected():
    # Rota para adicionar um novo cliente
        @app.route('/adicionar_cliente',methods=['POST'])
        def adicionar_cliente():
            if request.method == 'POST':
                dados_cliente = request.get_json()
                nome = dados_cliente['nome']
                cpf = dados_cliente['cpf']
                email = dados_cliente['email']
                endereco = dados_cliente['endereco']

            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO cadastro_clientes(nome,cpf,email,endereco)VALUES(%s, %s, %s,%s)", (nome, cpf, email, endereco))
            mysql.connection.commit()
            return jsonify({'message': 'Cliente cadastrado com sucesso!'})
except Error as e:
    print("Erro ao acessar tabela MySQL", e)
finally:
    if (con.is_connected()):
        con.close()
        print("Conexão ao MySQL encerrada")
                      
if __name__ == '__main__':
    app.run(debug=True)

'''
if __name__ == '__main__':
    app.run(debug=True)

    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ",linha)
if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão ao MySQL foi encerrada")


# Rota para adicionar um novo cliente
@app.route('/adicionar_cliente', methods=['POST'])
def adicionar_cliente():
    if request.method == 'POST':
        dados_cliente = request.get_json()
        nome = dados_cliente['nome']
        cpf = dados_cliente['cpf']
        email = dados_cliente['email']
        endereco = dados_cliente['endereco']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO cadastro_clientes (nome, cpf, email, endereco) VALUES (%s, %s, %s,%s)", (nome, cpf, email, endereco))
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': 'Cliente cadastrado com sucesso!'})


if __name__ == '__main__':
    app.run(debug=True)
    '''