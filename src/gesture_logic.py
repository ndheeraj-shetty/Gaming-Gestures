import time


class GestureLogic:
    def __init__(self, threshold=40, cooldown=0.5):
        """
        threshold : minimum movement required to trigger gesture
        cooldown  : time gap between two gesture triggers (seconds)
        """
        self.threshold = threshold
        self.cooldown = cooldown
        self.last_trigger_time = 0

    def detect_gesture(self, dx, dy):
        """
        dx : change in x position
        dy : change in y position
        returns : gesture string or None
        """

        current_time = time.time()

        # Cooldown check
        if current_time - self.last_trigger_time < self.cooldown:
            return None

        gesture = None

        # Horizontal movement priority
        if dx > self.threshold:
            gesture = "RIGHT"

        elif dx < -self.threshold:
            gesture = "LEFT"

        # Vertical movement
        elif dy < -self.threshold:
            gesture = "JUMP"

        elif dy > self.threshold:
            gesture = "SLIDE"

        if gesture:
            self.last_trigger_time = current_time

        return gesture


# ----------------------------
# Dummy test (remove later)
# ----------------------------
if __name__ == "__main__":
    gl = GestureLogic(threshold=40, cooldown=0.5)

    test_movements = [
        (50, 0),    # RIGHT
        (-60, 0),   # LEFT
        (0, -70),   # JUMP
        (0, 80),    # SLIDE
    ]

    for dx, dy in test_movements:
        gesture = gl.detect_gesture(dx, dy)
        print("dx:", dx, "dy:", dy, "=>", gesture)
        time.sleep(0.6)