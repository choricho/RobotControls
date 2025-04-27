# motors_control.py

class RobotMotors:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed):
        if speed < 0:
            self.speed = 0
        elif speed > 100:
            self.speed = 100
        else:
            self.speed = speed
        print(f"Motor speed set to {self.speed}%")

if __name__ == "__main__":
    robot = RobotMotors()
    robot.set_speed(50)
