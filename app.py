from flask import Flask, render_template, request, jsonify
import mysql.connector
app = Flask(__name__)

# Configuração do banco de dados MySQL
db = mysql.connector.connect(
    host='localhost',
    user='developer',
    password='',
    database='bd_teste'
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastrar_cliente', methods=['POST'])
def cadastrar_cliente():
    try:
        cursor = db.cursor()

        nome = request.json['nome']
        cpf = request.json['cpf']
        email = request.json['email']
        endereco = request.json['endereco']
        contrato = request.json['contrato']

        # Verifique se o cliente já existe no banco de dados com base no CPF
        query = "SELECT * FROM tb_cadastro WHERE cpf = %s"
        cursor.execute(query, (cpf,))
        existing_customer = cursor.fetchone()

        if existing_customer:
            # Cliente já existe, então atualize os dados
            update_query = "UPDATE tb_cadastro SET nome = %s, email = %s, endereco = %s, contrato = %s WHERE cpf = %s"
            update_values = (nome, email, endereco, contrato, cpf)
            cursor.execute(update_query, update_values)
        else:
            # Cliente não existe, insira um novo registro
            insert_query = "INSERT INTO tb_cadastro (nome, cpf, email, endereco, contrato) VALUES (%s, %s, %s, %s, %s)"
            insert_values = (nome, cpf, email, contrato, endereco)
            cursor.execute(insert_query, insert_values)

        db.commit()
        cursor.close()
        return jsonify({'mensagem': 'Cliente cadastrado/atualizado com sucesso!'})

    except Exception as e:
        return jsonify({'mensagem': f'Erro ao cadastrar/atualizar cliente: {str(e)}'})


if __name__ == '__main__':
    app.run(debug=True)
