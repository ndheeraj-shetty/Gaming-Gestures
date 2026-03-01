import time


class GestureLogic:
    def __init__(self,
                 horizontal_threshold=60,
                 slide_threshold=70,
                 jump_velocity_threshold=-25,
                 cooldown=0.8):

        self.h_threshold = horizontal_threshold
        self.slide_threshold = slide_threshold
        self.jump_velocity_threshold = jump_velocity_threshold
        self.cooldown = cooldown

        self.last_trigger_time = 0
        self.prev_y = None

    def detect_gesture(self, dx, dy, current_y):
        current_time = time.time()

        # Cooldown
        if current_time - self.last_trigger_time < self.cooldown:
            self.prev_y = current_y
            return None

        # Ignore small noise
        if abs(dx) < 20 and abs(dy) < 20:
            self.prev_y = current_y
            return None

        gesture = None

        # --------------------
        # HORIZONTAL
        # --------------------
        if abs(dx) > abs(dy):
            if dx > self.h_threshold:
                gesture = "RIGHT"
            elif dx < -self.h_threshold:
                gesture = "LEFT"

        # --------------------
        # VERTICAL
        # --------------------
        else:
            if self.prev_y is not None:
                velocity_y = current_y - self.prev_y

                # FAST UPWARD MOVEMENT → JUMP
                if velocity_y < self.jump_velocity_threshold:
                    gesture = "JUMP"

            # DOWN MOVEMENT → SLIDE
            if dy > self.slide_threshold:
                gesture = "SLIDE"

        self.prev_y = current_y

        if gesture:
            self.last_trigger_time = current_time

        return gesture