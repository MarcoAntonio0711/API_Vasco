from flask import Flask, jsonify, request
from DBvasco import JOGADORES
vasco = Flask(__name__)

vasco.config['JSON_AS_ASCII'] = False


@vasco.route('/jogadores/<int:camisa>', methods=['DELETE'])
def deletar_jogadores(camisa):
    for c in JOGADORES:
        if c['numero'] == camisa:
            JOGADORES.remove(c)
            return jsonify(mensagem=f'Jogador {camisa} removido com sucesso.'), 200
    return jsonify(mensagem=f'Jogador {camisa} não consta no elenco.'), 404


@vasco.route('/jogadores', methods=['POST'])
def adicionar_jogadores():
    jogador = request.json
    JOGADORES.append(jogador)
    return jsonify(mensagem='Jogador adicionado com sucesso.'), 201


@vasco.route('/jogadores', methods=['GET'])
def listar_jogadores():
    return jsonify(mensagem='LISTA DE ATLETAS VASCAINOS: ',
            lista=JOGADORES), 200


vasco.run(debug=True)
