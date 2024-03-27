### Homework

For homework let's practice subclasses.  In your 
repository make two files. One named ```baserobot.py```. That file describes a class ```BaseRobot``` that needs to have 
the following properties and methods.

The ```BaseRobot``` class should have the following properties:

* ```self.x```: The x position of the robot
* ```self.y```: The y position of the robot

And the following methods:

* ```__init__```: The constructor should take in two numbers and set them to be the x position of the robot (```self.x```) and the y position of the robot (```self.y```). 
* ```move```: Move takes in two numbers in increases that x and y positions of the robot by those numbers
* ```beep```: Beep prints the word **beep** to the console.
* ```__str__```: returns a string that says the position of the robot.

The code for the ```__str__``` method should look like this:

```python
def __str__(self):
    return f"Robot is at position ({self.x}, {self.y})"
```

Then have another file, ```armbot.py```, that describes a subclass of BaseRobot called ```ArmBot```. An ```ArmBot```
can do all the things that BaseRobot can do, but with these differences:

The ArmBot class should have properties it inherits from the BaseRobot and the following properties:

* ```self.arm_position```: The position of the arm of the robot
* ```self.claw```: A boolean value indicating if the claw is open or closed

The Armbot should have the following methods:

* ```__init__```: In the init method it should call the init of the BaseRobot class using super, but also set a value for 
its arm position, ```self.arm_position``` to be zero. Also, it sets a value for the claw indicating that the claw is closed.
Do this by setting ```self.claw``` to ```False```.
* ```move_arm```: This method takes in a number and increases the arm_position by that amount.
* ```grab_claw```: This method sets the value of ```self.claw``` to be ```False```.
*  ```release_claw```: This method sets the value of ```self.claw``` to be ```True```.
* ```__str__```: Reports the position of the robot and status of the arm and the claw.

The code for the ```__str__``` method should look like this:

```python
def __str__(self):
    return super().__str__()+" with arm at position {self.arm_position} and claw is {'open' if self.claw else 'closed'}"
```