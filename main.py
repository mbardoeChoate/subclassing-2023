from armbot import ArmBot
from baseRobot import BaseRobot

if __name__ == "__main__":
    # This code should run and produce the following output:
    # Robot is at position (1, 2)
    # Robot is at position (4, 6)
    # Beep
    # Robot is at position (5, 8) with arm at position 0 and claw closed
    # Robot is at position (5, 8) with arm at position 10 and claw closed
    # Robot is at position (5, 8) with arm at position 10 and claw open
    # Robot is at position (5, 8) with arm at position 10 and claw closed
    # Beep

    robbie = BaseRobot(1, 2)
    print(robbie)
    robbie.move(3, 4)
    print(robbie)
    robbie.beep()
    jodie = ArmBot(3, 5)
    jodie.move(2, 3)
    print(jodie)
    jodie.move_arm(10)
    print(jodie)
    jodie.release_claw()
    print(jodie)
    jodie.grab_claw()
    print(jodie)
    jodie.beep()
