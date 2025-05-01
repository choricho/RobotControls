import time

class RobotMotors:
    def __init__(self):
        self.speed = 0

    def set_speed(self, target_speed):
        while self.speed != target_speed:
            if self.speed < target_speed:
                self.speed += 1
            else:
                self.speed -= 1
            print(f"Motor speed: {self.speed}%")
            time.sleep(0.1)  

if __name__ == "__main__":
    robot = RobotMotors()
    target_speed = int(input("Enter target speed (0-100): "))
    robot.set_speed(target_speed)

