from flask import Flask, request, jsonify, render_template
from collections import deque

app = Flask(__name__)

# Cada veículo terá uma fila (deque) de até 5 posições
veiculos = {}

@app.route('/')
def index():
    return render_template('index.html')

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
