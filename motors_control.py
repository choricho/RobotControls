# motors_control.py

class Robot:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed):
        if 0 <= speed <= 100:
            self.speed = speed
            print(f"Speed set to {self.speed}%")
        else:
            print("Speed must be between 0 and 100.")

    def stop(self):
        self.speed = 0
        print("Robot stopped.")

if __name__ == "__main__":
    robot = Robot()
    robot.set_speed(50)
    robot.stop()

