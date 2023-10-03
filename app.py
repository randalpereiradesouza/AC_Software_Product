from flask import Flask, render_template, request, jsonify, redirect
import mysql.connector
app = Flask(__name__)

# Configuração do banco de dados MySQL
db = mysql.connector.connect(
    host='localhost',
    user='developer',
    password='',
    database='bd_teste'
)


# Rota para a página principal
@app.route('/')
def principal():
    return render_template('principal.html')


# Rota para verificar CPF
@app.route('/verificar_cpf', methods=['POST'])
def verificar_cpf():
    try:
        cursor = db.cursor()
        cpf = request.form['cpf']

        # Verifique se o cliente já existe no banco de dados com base no CPF
        query = "SELECT * FROM tb_cadastro WHERE cpf = %s"
        cursor.execute(query, (cpf,))
        existing_customer = cursor.fetchone()

        if existing_customer:
            # Se o cliente existir, redirecione para a rota de cadastro de chamado
            return redirect('/cadastrar_chamado')
        else:
            # Se o cliente não existir, redirecione para a rota de cadastro de cliente
            return redirect('/cadastro')
    except Exception as e:
        return jsonify({'mensagem': f'Erro ao verificar CPF: {str(e)}'})


# Rota para cadastro
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


# Rota para a página de chamado
@app.route('/cadastrar_chamado')
def chamado():
    return render_template('chamado.html')


@app.route('/cadastrar_chamado', methods=['POST'])
def cadastrar_chamado():
    try:
        cursor = db.cursor()

        modelo = request.json['modelo']
        defeito = request.json['defeito']
        cpf = request.json['cpf']

        insert_query = "INSERT INTO tb_chamado (modelo, defeito, cpf) VALUES (%s, %s, %s)"
        insert_values = (modelo, defeito, cpf)
        cursor.execute(insert_query, insert_values)
       
        db.commit()
        cursor.close()
        return jsonify({'mensagemchamado': 'Chamado cadastrado com Sucesso!'})

    except Exception as e:
        return jsonify({'mensagemchamado': f'Erro ao cadastrar chamado: {str(e)}'})


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
            insert_values = (nome, cpf, email, endereco, contrato)
            cursor.execute(insert_query, insert_values)

        db.commit()
        cursor.close()
        return jsonify({'mensagem': 'Cliente cadastrado/atualizado com sucesso!'})

    except Exception as e:
        return jsonify({'mensagem': f'Erro ao cadastrar/atualizar cliente: {str(e)}'})


if __name__ == '__main__':
    app.run(debug=True)
