
# 🚚 Monitoramento de Frota

Sistema web para visualização em tempo real da localização e trajetória de veículos, com painel lateral de opções e visual moderno.

## ✨ Funcionalidades

- 📍 Exibe a posição atual dos veículos no mapa.
- 🛣️ Mostra o rastro das últimas 5 localizações de cada veículo.
- 🗺️ Interface interativa com mapa estilizado usando Leaflet.
- 📂 Painel lateral com opções como:
  - Cadastrar Origem
  - Extrair Relatórios
- 🎨 Design com gradientes, responsivo e intuitivo.

## 🧰 Tecnologias Utilizadas

- **Python + Flask** (backend)
- **HTML, CSS e JavaScript** (frontend)
- **Leaflet.js** (mapa interativo)
- **jQuery** (requisições AJAX)
- **Git + GitHub** (controle de versão)

## ▶️ Como rodar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/Vlyzin/Projeto-FT.git
cd Projeto-FT
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Rode o servidor:

```bash
python app.py
```

5. Acesse no navegador:

```
http://localhost:5000
```

## 📁 Estrutura do Projeto

```
Projeto-FT/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── img/
│       ├── truck.png
│       └── change.png
├── templates/
│   └── index.html
├── app.py
└── README.md
```

## 📌 Observações

- Os dados de veículos são carregados via endpoint `/api/veiculos`.
- O mapa atualiza automaticamente a cada 5 segundos.
- O painel lateral fecha ao clicar fora dele, criando uma experiência fluida.

---

Desenvolvido por [Vlyzin](https://github.com/Vlyzin)
