from baseRobot import BaseRobot
from armbot import ArmBot


if __name__=="__main__":
    # This code should run and produce the following output:
    # x: 1 y: 2
    # x: 4 y: 6
    # beep
    # x: 5 y: 8 arm: 0, claw: False
    # x: 5 y: 8 arm: 10, claw: False
    # x: 5 y: 8 arm: 10, claw: True
    # x: 5 y: 8 arm: 10, claw: False
    # beep

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