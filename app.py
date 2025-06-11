from flask import Flask, request, jsonify, render_template
from collections import deque
import json
import os

app = Flask(__name__)

# Cada veículo terá uma fila (deque) de até 5 posições
veiculos = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/cadastrar-pontos")
def cadastrar_pontos():
    return render_template("cadastrar_pontos.html")

DATA_FILE = 'dados_locais.json'

@app.route('/salvar-local', methods=['POST'])
def salvar_local():
    dados = request.get_json()

    if not dados:
        return jsonify({'error': 'Nenhum dado recebido'}), 400

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            locais = json.load(f)
    else:
        locais = []

    locais.append(dados)

    # Salva de volta
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(locais, f, ensure_ascii=False, indent=2)

    return jsonify({'message': 'Local salvo com sucesso!'}), 200

@app.route('/locais')
def listar_locais():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            locais = json.load(f)
    else:
        locais = []

    return jsonify(locais)

@app.route('/api/locais/origem')
def locais_origem():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            locais = json.load(f)
    else:
        locais = []

    origens = [loc for loc in locais if loc.get('tipoLocal') == 'origem']
    return jsonify(origens)

@app.route('/api/locais/destino')
def locais_destino():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            locais = json.load(f)
    else:
        locais = []

    destinos = [loc for loc in locais if loc.get('tipoLocal') == 'destino']
    return jsonify(destinos)

@app.route('/api/veiculos', methods=['GET', 'POST'])
def api_veiculos():
    if request.method == 'POST':
        dados = request.get_json()

        id_veiculo = str(dados['id'])
        lat = dados['lat']
        lon = dados['lon']

        # Cria a fila do veículo se ainda não existir
        if id_veiculo not in veiculos:
            veiculos[id_veiculo] = deque(maxlen=5)

        # Adiciona nova posição (mantendo só as últimas 5)
        veiculos[id_veiculo].append({
            "lat": lat,
            "lon": lon
        })

        return jsonify({"status": "ok"}), 200

    # Método GET: retorna todas as posições de todos os veículos
    resposta = []
    for id_veiculo, posicoes in veiculos.items():
        resposta.append({
            "id": id_veiculo,
            "historico": list(posicoes)
        })

    return jsonify(resposta)

if __name__ == '__main__':
    app.run(debug=True)
