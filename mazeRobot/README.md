# Name, Area, Mentor
Hoang N. Connie L., Robotics, Mentor: David Le

#UPDATE 8/29/16
##Description
We have created a robot that will solve a maze using the right hand rule. However, to prove the adaptability of our robot, we aim to have it run through the maze once and learn the path. The second time through, it should be able to solve the maze faster. If we have time, we also want to use some sort of sound sensor so that the robot will only start its journey solving the maze when it hears a certain song.
##Stages
1. Assemble a robot with line sensors. (Completed)
2. Create test functions for sensors that help ease us into the code for step 3. Tune the sensors as we go along (Completed)
3. Create a function that allows the robot to sense its surrounding and move in the direction where there is no "wall." (Completed)
4. Robot solves maze. (Completed)
5. Write a function that makes robot remember correct path to destination. Perhaps use graph algorithms (need to ask Diba for more info).
6. Add sound sensor.
7. Write code to make robot start moving when hears certain song.

#From 8/25/16
## Brief Description
We want to create a robot that will solve a maze. However, the robot will only start when music is played. The robot will be capable of learning how to solve any maze. It will run through the maze once to learn the path to solve the maze. The second time through, it will be able to solve the maze faster. Also to further prove the adaptability of our robot, it will be able to solve any maze.

## Stages
1. Determine the different sensors needed to detect lines and sound (in this case, music). Music will be used to tell the robot to starts its journey. A specific song might need to be used so as to train the robot to detect it.
2. Create a function that allows the robots to sense its surrounding and move in the direction where there is no "wall." The code will be somewhat similar to those used in picobot.
3. Get robot to solve a maze. Then generalize to make sure the robot can solve any maze and not just a specific maze formation
4. Figure out how to make the robot store the correct path in its memory and use that to get through the same maze quicker.
5. Program robot so it correlates "melody playing" to "start." We will use this song: tbd

## Note on solving the maze:
* need a method to let robot tell the difference between a deadend and the exit
* ideas: timed path, placing something for robot to detect at exit
