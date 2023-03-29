from baseRobot import BaseRobot
from armbot import ArmBot


if __name__=="__main__":
    robbie=BaseRobot(1,2)
    print(robbie)
    robbie.move(3,4)
    print(robbie)
    robbie.beep()
    jodie=ArmBot(3,5)
    jodie.move(2,3)
    print(jodie)
    jodie.move_arm(10)
    print(jodie)
    jodie.release_claw()
    print(jodie)
    jodie.grab_claw()
    print(jodie)
    jodie.beep()