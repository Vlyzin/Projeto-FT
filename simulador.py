import time
import requests
import random

API_URL = "http://localhost:5000/api/veiculos"

# Caminhões com IDs como strings: "1" e "2"
caminhoes = {
    "1": [-23.5505, -46.6333],
    "2": [-23.5605, -46.6433]
}

def mover_posicao(lat, lon):
    """Aplica variação aleatória nas coordenadas para simular movimento."""
    nova_lat = lat + random.uniform(-0.005, 0.005)
    nova_lon = lon + random.uniform(-0.005, 0.005)
    return nova_lat, nova_lon

while True:
    for id_veiculo, (lat, lon) in caminhoes.items():
        nova_lat, nova_lon = mover_posicao(lat, lon)
        caminhoes[id_veiculo] = [nova_lat, nova_lon]

        payload = {
            "id": id_veiculo,
            "lat": nova_lat,
            "lon": nova_lon
        }

        try:
            response = requests.post(API_URL, json=payload)
            print(f"[{id_veiculo}] Enviado: {payload} | Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar dados de {id_veiculo}: {e}")

    time.sleep(5)
