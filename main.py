import cv2
from mediapipe import solutions
from gesture_logic import GestureLogic
from camera import Camera
from controller import Controller

# Initialize hands
hands_module = solutions.hands
hand_tracker = hands_module.Hands(max_num_hands=1)
mp_draw = solutions.drawing_utils

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
            mp_draw.draw_landmarks(frame, hand, hands_module.HAND_CONNECTIONS)

            h, w, _ = frame.shape
            x = int(hand.landmark[8].x * w)
            y = int(hand.landmark[8].y * h)

            dx = x - prev_x
            dy = y - prev_y

            g = gesture.detect_gesture(dx, dy)
            if g:
                print("GESTURE:", g)
                controller.execute_gesture(g)

            prev_x, prev_y = x, y

    cv2.imshow("Gesture Control", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

camera.release()