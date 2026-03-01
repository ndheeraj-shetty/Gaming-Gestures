import cv2
import mediapipe as mp
from gesture_logic import GestureLogic
from camera import Camera
from controller import Controller

# Initialize MediaPipe Hands correctly
mp_hands = mp.solutions.hands
hand_tracker = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Initialize webcam, gesture logic, controller
camera = Camera()
controller = Controller()
gesture = GestureLogic()
prev_x, prev_y = 0, 0

while True:
    frame = camera.get_frame()
    if frame is None:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hand_tracker.process(rgb)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

            h, w, _ = frame.shape
            # Palm center using stable landmarks
            palm_ids = [0, 5, 9, 13, 17]

            xs = [hand.landmark[i].x for i in palm_ids]
            ys = [hand.landmark[i].y for i in palm_ids]

            current_x = int((sum(xs) / len(xs)) * w)
            current_y = int((sum(ys) / len(ys)) * h)

            dx = current_x - prev_x
            dy = current_y - prev_y

            g = gesture.detect_gesture(dx, dy, current_y)
            if g:
                print("GESTURE:", g)
                controller.execute_gesture(g)

            prev_x, prev_y = current_x, current_y

    cv2.imshow("Gesture Control", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

camera.release()
cv2.destroyAllWindows()