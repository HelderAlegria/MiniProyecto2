import cv2
import mediapipe as mp
import serial
import time

arduino = serial.Serial('COM3', 9600)
time.sleep(2)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
anterior = -1

while True:
    ret, frame = cap.read()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    dedos = 0
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            lm = hand_landmarks.landmark

            if lm[4].x < lm[3].x:
                dedos += 1
            for id in [8, 12, 16, 20]:
                if lm[id].y < lm[id - 2].y:
                    dedos += 1

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.putText(frame, f'Dedos: {dedos}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    if dedos != anterior:
        arduino.write(str(dedos).encode())
        anterior = dedos

    cv2.imshow("Detección de dedos", frame)
    if cv2.waitKey(1) & 0xFF == 27:  
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
