from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Hello World!</h1>'


@app.route('/usuario')
def usuario():
    usuario = {
        "nome": "Gustavo",
        "idade": 17,
        "telefono": "(19)-997922681"
    }

    return usuario


@app.route('/produto', methods=['POST'])
def cadastrar_produto():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    print(f'Novo produto: {dados}')

    return jsonify({
        "mensagem": "Produto salvo com sucesso",
        "produto cadastrado": dados
    }), 201


@app.route('/produto', methods=['PUT'])
def atualizar_produto():
    produto = {
        "id": 1,
        "nome": "Caneta azul",
        "preco": 5.00,
        "descricao": "Caneta esferográfica",
        "marca": "Bic"
    }

    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    if dados.get('id') == produto['id']:
        produto = dados

        print(f'Produto atualizado com sucesso: {produto}')

        return jsonify({
            "mensagem": "Produto atualizado com sucesso",
            "produto": produto
        }), 200

    return jsonify({
        "erro": "Produto não encontrado"
    }), 404

    if dados.get('id') != produto['id']:
        produto = dados
        print(f'Produto atualizado com sucesso: {produto}')
        return jsonify({"mensagem": "Produto atualizado com sucesso"}), 200
    else:
        return jsonify({"mensage": "Produto não encontrado"}), 404


if __name__ == '__main__':
    app.run(debug=True)