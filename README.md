# PosTech-FIAP-Entrega-04


## Apresentação 
https://prezi.com/view/EeNrffgyfjCEKJ0Mr2LX/


## Link Video para Download
https://drive.google.com/file/d/1B5PbZdUDi-r7Ac7BK3a3WdNppfQqM_Ne/view?usp=drive_link

# Antes de iniciar o codigo precisamos seguir os passos abaixo;

## Instalação das bibliotecas
pip install opencv-python
pip install face-recognition
pip install deepface
pip install mediapipe
pip install matplotlib
pip install tqdm

## Para facilitar execute o comando abaixo com todas as libs juntas;

pip install opencv-python face-recognition deepface mediapipe matplotlib tqdm

## Caso tenha MAC pode ter um possivel problema com face-recognition então instale o brew:
brew install cmake
brew install libomp

## Caso rodar no Linux
sudo apt-get install build-essential cmake
sudo apt-get install libopenblas-dev liblapack-dev
sudo apt-get install libx11-dev libgtk-3-dev

## Caso rodar no Windows
Pode ser necessário instalar o Visual Studio Build Tools se der erro ao instalar o face-recognition:
	•	Baixe em: https://visualstudio.microsoft.com/visual-cpp-build-tools/



## Altera o caminho de origem do video baixado
video_path = '/caminho origem XXXXXXX /Unlocking Facial Recognition_ Diverse Activities Analysis.mp4'

## Alterar o caminho de destino do relatorio gerado.
relatorio_path = "/caminho origem XXXXXXX/relatorio_video.txt"

## Caso for rodar o codigo via cli chamando o arquivo;
python nome_do_arquivo.py
