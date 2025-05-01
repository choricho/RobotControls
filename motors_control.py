import time

class Robot:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed):
        if 0 <= speed <= 100:
            while self.speed != speed:
                if self.speed < speed:
                    self.speed += 1
                else:
                    self.speed -= 1
                print(f"Speed set to {self.speed}%")
                time.sleep(0.1)
        else:
            print("Speed must be between 0 and 100.")

    def stop(self):
        self.set_speed(0)
        print("Robot stopped.")

