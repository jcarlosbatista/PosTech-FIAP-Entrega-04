from pyspark.sql import SparkSession
import cv2
import face_recognition
from deepface import DeepFace
import mediapipe as mp
from tqdm import tqdm
import matplotlib.pyplot as plt
import os

spark = SparkSession.builder.appName("VideoAnalysisApp").getOrCreate()

# Configurações para detecção de atividades
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Carregar o vídeo

#ATENÇÃO ALTERAR O CAMINHO DE ORIGEM DO ARQUIVO DE VIDEO
video_path = '/caminho origem XXXXXXX /Unlocking Facial Recognition_ Diverse Activities Analysis.mp4'
cap = cv2.VideoCapture(video_path)
relatorio_path = "relatorio_video.txt"


frame_count = 0
anomaly_count = 0
emotions_detected = []
activities_detected = []

# Obter total de frames do vídeo
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Barra de progresso
progress_bar = tqdm(total=total_frames, desc="Processando Vídeo")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
# Detectar
    # Reconhecimento facial e análise emocional
    for top, right, bottom, left in face_locations:
        face = frame[top:bottom, left:right]
        try:
            analysis = DeepFace.analyze(face, actions=['emotion'], enforce_detection=False)
            emotion = analysis[0]['dominant_emotion']
            emotions_detected.append(emotion)
        except:
            pass

    # Detecção de atividades com pose estimation
    results = pose.process(rgb_frame)
    if results.pose_landmarks:
        activities_detected.append('movimento')
    else:
        activities_detected.append('parado')

    # Detecção de anomalias simples (gestos bruscos como exemplo)
    if len(face_locations) > 2:  # Exemplo simplificado
        anomaly_count += 1

    # Atualizar barra de progresso
    progress_bar.update(1)

cap.release()
progress_bar.close()

# Geração de resumo
summary_text = f"Relatório de Análise de Vídeo\n"
summary_text += f"-----------------------------------\n"
summary_text += f"Total de frames analisados: {frame_count}\n"
summary_text += f"Número de anomalias detectadas: {anomaly_count}\n"
summary_text += f"Emoções detectadas (quantidade):\n"
for emotion in set(emotions_detected):
    summary_text += f"  - {emotion}: {emotions_detected.count(emotion)} vezes\n"
summary_text += f"\nAtividades detectadas (quantidade):\n"
summary_text += f"  - Movimento: {activities_detected.count('movimento')} frames\n"
summary_text += f"  - Parado: {activities_detected.count('parado')} frames\n"
summary_text += f"\nResumo Geral:\n"
summary_text += f"  - Emoções predominantes: {set(emotions_detected)}\n"
summary_text += f"  - Atividades predominantes: {set(activities_detected)}\n"
summary_text += f"  - Detecção de anomalias em {anomaly_count} frames\n"
summary_text += f"-----------------------------------\n"

# Exibindo o resumo no notebook
print(summary_text)

# Salvando o relatório
# ATENÇÃO ALTERAR O CAMINHO DE DESTINO DE GRAVAÇÃO DO RELATÓRIO
relatorio_path = "/caminho origem XXXXXXX/relatorio_video.txt"

with open(relatorio_path, 'w') as f:
    f.write(summary_text)

print(f"Relatório salvo em: {relatorio_path}")

# Gráficos
emotions_categories = ["surprise", "sad", "neutral", "disgust", "happy", "fear", "angry"]
emotions_count = [emotions_detected.count(e) for e in emotions_categories]

plt.figure(figsize=(12, 8))

# Gráfico de Pizza
plt.subplot(1, 3, 1)
if sum(emotions_count) == 0:
    plt.text(0.5, 0.5, 'Nenhuma emoção detectada', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
    plt.axis('off')
else:
    plt.pie(emotions_count, labels=emotions_categories, autopct='%1.1f%%', startangle=140)

plt.title("Distribuição das Emoções Detectadas")

# Gráfico de Barra
plt.subplot(1, 3, 2)
plt.bar(['Movimento', 'Parado'], [activities_detected.count('movimento'), activities_detected.count('parado')])
plt.title("Distribuição das Atividades Detectadas")

# Gráfico Padrão (Resumo Geral)
plt.subplot(1, 3, 3)
plt.bar(['Emoções Predominantes', 'Atividades Predominantes', 'Anomalias'], [len(set(emotions_detected)), len(set(activities_detected)), anomaly_count])
plt.title("Resumo Geral")

plt.tight_layout()
plt.show()
