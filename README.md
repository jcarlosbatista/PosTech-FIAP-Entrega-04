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
```

### Caso tenha MacOS e ocorra erro ao instalar face-recognition:
```
brew install cmake libomp
```

### Caso esteja em Linux:
```
sudo apt-get install build-essential cmake
sudo apt-get install libopenblas-dev liblapack-dev
sudo apt-get install libx11-dev libgtk-3-dev
```

### Caso esteja em Windows e tenha erro ao instalar face-recognition:

- Baixe e instale [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

📂 Como Executar o Projeto

 1.	Faça o download do vídeo de exemplo: [click Aqui](https://drive.google.com/file/d/1B5PfzZdUDi-7Ac7BK3a3WdNppfQgM_Ne/view?usp=drive_link)
 2.	Ajuste os caminhos no código para o vídeo e o relatório:
     ```
    video_path = "/caminho/para/Unlocking Facial Recognition_ Diverse Activities Analysis.mp4"
    relatorio_path = "/caminho/para/relatorio_video.txt"
    ```
 3.	Execute o script:
    ```
    python nome_do_arquivo.py
    ```
    
🧪 Exemplo de Saída Esperada

Exemplo do Relatório Gerado:
```
Total de frames analisados: 2400
Número de anomalias detectadas: 12

Emoções detectadas:
- Happy: 120 vezes
- Neutral: 300 vezes
- Sad: 45 vezes

Atividades detectadas:
- Movimento: 1500 frames
- Parado: 900 frames
```

📊 Visualização Gráfica

Após a execução, serão exibidos os seguintes gráficos:

	•	Gráfico de Pizza: Distribuição das Emoções.
	•	Gráfico de Barras: Atividades (Movimento e Parado).
	•	Resumo Geral: Emoções predominantes, atividades predominantes e anomalias detectadas.


 🧑‍💻 Tecnologias Utilizadas
 
	•	Python 3.11
	•	OpenCV – Processamento de imagens e vídeos.
	•	Face Recognition – Detecção e reconhecimento facial.
	•	DeepFace – Análise de emoções faciais.
	•	MediaPipe – Detecção de posturas e movimentos corporais.
	•	Matplotlib – Visualização de gráficos.
	•	TQDM – Barra de progresso para monitorar o processamento.



    

    
























