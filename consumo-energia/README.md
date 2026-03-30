# ⚡ Calculadora de Consumo de Energia

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/status-concluído-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Energia](https://img.shields.io/badge/tema-energia-yellow)

---

## 📌 Sobre o projeto
Este projeto é uma **Calculadora de Consumo de Energia Elétrica**, desenvolvida para estimar o consumo mensal de aparelhos eletrônicos.  

O sistema permite que o usuário informe:
- Nome do aparelho  
- Potência (em watts)  
- Tempo médio de uso diário (em horas)  

Com base nesses dados, o programa calcula o consumo mensal em **kWh** e também estima o custo da energia.

---

## 🎯 Objetivo
Ajudar usuários a entenderem melhor o consumo de energia dos seus aparelhos e promover o uso consciente da eletricidade 💡

---

## 🖥️ Linguagem utilizada
- 🐍 Python

---

## 🧮 Fórmula utilizada
O cálculo do consumo mensal é feito com a seguinte fórmula:

consumoMensal = (potencia * horasDia * 30) / 1000

E o custo estimado:

custo = consumoMensal * 0.75

Exemplo de uso:
Digite o nome do eletrodoméstico: Geladeira
Digite a potência do aparelho em watts (W): 150
Qual o tempo médio de uso diário (em horas)? 10

--- Resultado ---
Aparelho: Geladeira
Consumo estimado: 45.00 kWh/mês
Custo estimado: R$ 33.75

## ▶️ Como executar o programa

### 🌐 1. Executando online (sem instalar nada)

Você pode rodar o código diretamente no navegador utilizando plataformas como:

Replit
Google Colab

Basta colar o código e executar.

💻 2. Executando pelo terminal (recomendado)

Abra o terminal (Prompt de Comando ou PowerShell)
Navegue até a pasta onde está o arquivo:
<pre> ```bash cd caminho/da/pasta``` </pre>


🖥️ 3. Executando pelo Visual Studio Code
Abra o VS Code
Clique em File > Open Folder e selecione a pasta do projeto
Abra o arquivo .py
Clique em Run ▶️ ou pressione Ctrl + F5

🐍 3. Executando pelo IDLE (Python padrão)
Abra o IDLE
Clique em File > Open
Selecione o arquivo do programa
Pressione F5 para executar
