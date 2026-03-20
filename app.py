import streamlit as st
import cv2
from deepface import DeepFace
import pandas as pd

st.title("AI Emotion Analytics Dashboard")

cap = cv2.VideoCapture(0)

frame_placeholder = st.empty()
chart_placeholder = st.empty()

while True:
    ret, frame = cap.read()

    result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

    emotion = result[0]['dominant_emotion']
    emotions = result[0]['emotion']

    df = pd.DataFrame(emotions.items(), columns=['Emotion', 'Score'])

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frame_placeholder.image(frame)
    chart_placeholder.bar_chart(df.set_index('Emotion'))
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
#for emotion detection
from deepface import DeepFace

result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

emotion = result[0]['dominant_emotion']
print(emotion)
#Draw face box+emotions
face = result[0]['region']
x, y, w, h = face['x'], face['y'], face['w'], face['h']

cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
cv2.putText(frame, emotion, (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
#sowing emotion scores
import pandas as pd

emotions = result[0]['emotion']
df = pd.DataFrame(emotions.items(), columns=['Emotion', 'Score'])
print(df)
#run as :streamlit run app.py