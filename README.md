### Homework

For homework let's practice subclasses. Use GitHub classroom to get a repository named ```subclassing-2023```. In this 
repository make two files. One named ```baserobot.py```. That file describes a class ```BaseRobot``` that needs to have 
the following methods.

* ```__init__```: The constructor should take in two numbers and set them to be the self.x and self.y of the Robot. 
* ```move```: Move takes in two numbers in increases that x and y coordinates of the robot by those numbers
* ```beep```: Beep prints the word **beep** to the console.
* ```__str__```: returns a string that says the position of the robot.

Then have another file, ```armbot.py```, that describes a subclass of BaseRobot called ```ArmBot```. An ```ArmBot```
can do all the things that BaseRobot can do, but with these differences:

* ```__init__```: In the init method it should call the init of the BaseRobot class using super, but also set a value for 
its arm position, ```self.arm_position``` to be zero. It also sets a value for the claw indicating that the claw is closed.
do this by setting ```self.claw``` to ```False```.
* ```move_arm```: This method takes in a number and increases the arm_position by that amount.
* ```grab_claw```: This method sets the value of ```self.claw``` to be ```False```.
*  ```release_claw```: This method sets the value of ```self.claw``` to be ```True```.
* ```__str___```: Reports the position of the robot and status of the arm and the claw.