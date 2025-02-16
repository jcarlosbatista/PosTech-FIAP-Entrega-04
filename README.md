# 🚀 PosTech-FIAP-Entrega-04 – Análise de Vídeo com Reconhecimento Facial, Emoções e Detecção de Atividades

Este projeto tem como objetivo a criação de uma aplicação que realiza a **análise automática de vídeos** utilizando técnicas de:
- Reconhecimento Facial 🧑‍💻
- Análise de Emoções 😃😢😠
- Detecção de Atividades 🏃‍♂️🧍
- Geração de Relatórios e Gráficos 📊

## 🎥 Demonstração e Material de Apoio
- [Apresentação Interativa (Prezi)](https://prezi.com/view/EeNrfgyfjCEKJ0MzLX/)
- [Download do Vídeo de Exemplo](https://drive.google.com/file/d/1B5PfzZdUDi-7Ac7BK3a3WdNppfQgM_Ne/view?usp=drive_link)

---

## ⚙️ Funcionalidades
- Detecta rostos e analisa emoções (Feliz, Triste, Neutro, Bravo, Surpreso, Medo, Nojo).
- Identifica atividades como **Movimento** e **Parado**.
- Detecta anomalias (exemplo: presença de muitas pessoas no frame).
- Gera gráficos interativos:
  - **Gráfico de Pizza** – Distribuição de Emoções.
  - **Gráfico de Barras** – Atividades detectadas.
  - **Resumo Geral** – Emoções, atividades e anomalias.
- Produz relatório em texto com as estatísticas.

---

## 🛠️ Instalação das Dependências

### Instalar bibliotecas no ambiente Python:
```bash
pip install opencv-python face-recognition deepface mediapipe matplotlib tqdm
