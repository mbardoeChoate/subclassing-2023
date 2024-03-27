from armbot import ArmBot

import pytest


def test_armbot(capsys):
    jodie = ArmBot(3, 5)
    jodie.move(2, 3)
    assert str(jodie) == "Robot is at position (5, 8) with arm at position 0 and claw closed"
    jodie.move_arm(10)
    assert str(jodie) == "Robot is at position (5, 8) with arm at position 10 and claw closed"
    jodie.release_claw()
    assert str(jodie) == "Robot is at position (5, 8) with arm at position 10 and claw open"
    jodie.grab_claw()
    assert str(jodie) == "Robot is at position (5, 8) with arm at position 10 and claw closed"
    jodie.beep()
    captured = capsys.readouterr()
    # Create an assertion about the console output and make sure it says "Beep".
    assert "Beep\n" in captured or "beep\n" in captured
    assert str(jodie) == "Robot is at position (5, 8) with arm at position 10 and claw closed"
