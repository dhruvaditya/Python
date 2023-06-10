import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(1)
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False, max_num_hands=2)
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

