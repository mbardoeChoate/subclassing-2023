from baserobot import BaseRobot

import pytest

def test_baserobot(capsys):
    robbie = BaseRobot(1, 2)
    assert str(robbie) == "Robot is at position (1, 2)"
    robbie.move(3, 4)
    assert str(robbie) == "Robot is at position (4, 6)"
    robbie.beep()
    captured = capsys.readouterr()
    assert captured.out == "Beep\n"
    assert str(robbie) == "Robot is at position (4, 6)"