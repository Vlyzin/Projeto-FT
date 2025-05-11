// Código existente para o mapa
var map = L.map('map').setView([-23.5505, -46.6333], 12);

// Mapa base
L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="https://carto.com/attributions">CartoDB</a>',
    maxZoom: 19
}).addTo(map);

// Ícone do caminhão
function criarIcone() {
    return L.icon({
        iconUrl: '/static/img/truck.png',
        iconSize: [40, 40],
        iconAnchor: [20, 40],
        popupAnchor: [0, -40]
    });
}

// Guardar marcadores, linhas e pontos do rastro
let marcadores = {};
let linhas = {};
let rastros = {};

function atualizarVeiculos() {
    $.get('/api/veiculos', function (data) {
        // Limpa círculos antigos do rastro
        for (const id in rastros) {
            rastros[id].forEach(circulo => map.removeLayer(circulo));
        }
        rastros = {};

        data.forEach(function (veiculo) {
            const id = veiculo.id;
            const historico = veiculo.historico;

            if (historico.length === 0) return;

            const ultima = historico[historico.length - 1];
            const latlng = [ultima.lat, ultima.lon];

            // Remove marcador antigo
            if (marcadores[id]) {
                map.removeLayer(marcadores[id]);
            }

            // Novo marcador do caminhão
            const marker = L.marker(latlng, { icon: criarIcone() })
                .bindPopup(`Veículo ${id}`)
                .addTo(map);
            marcadores[id] = marker;

            if (linhas[id]) {
                map.removeLayer(linhas[id]);
            }

            const pontos = historico.map(p => [p.lat, p.lon]);
            const polyline = L.polyline(pontos, {
                color: '#ff0000',  // Linha vermelha
                weight: 3,
                opacity: 0.7
            }).addTo(map);
            linhas[id] = polyline;

            // Bolinhas brancas nos pontos
            rastros[id] = [];
            historico.forEach(p => {
                const circulo = L.circleMarker([p.lat, p.lon], {
                    radius: 4.5,  // raio da bolinha
                    color: '#d3d3d3',  // borda cinza claro
                    fillColor: '#ffffff',  // Bolinha branca
                    fillOpacity: 1,
                })
                .bindPopup(`Lat: ${p.lat.toFixed(5)}<br>Lon: ${p.lon.toFixed(5)}`)
                .addTo(map);

                rastros[id].push(circulo);
            });
        });
    });
}

// Atualização contínua
setInterval(atualizarVeiculos, 5000);
atualizarVeiculos();

// Lógica para abrir e fechar o painel lateral
$(document).ready(function() {
    $(".change-btn").click(function() {
        // Alternar o painel lateral
        $("#sidebar").toggleClass("open");
        $(".overlay").toggleClass("visible");

        // Mostrar/Esconder o ícone
        $(".button-container").toggleClass("hidden");
    });

    // Fechar o painel lateral ao clicar fora dele
    $(".overlay").click(function() {
        $("#sidebar").removeClass("open");
        $(".overlay").removeClass("visible");

        // Mostrar o ícone quando o painel for fechado
        $(".button-container").removeClass("hidden");
    });
});
