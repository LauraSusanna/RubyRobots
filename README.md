# Coding Challenge

## Ruby Robots
I made a sketch of the architecture and included it in mission_sketch.jpeg

### Running the application
This solution runs in Python 3.9 and needs no further third-party libraries.

##### Start a new mission
To start a mission, run main.py and paste or type the mission input into the console. 

The input is expected to be in a very particular shape, as given in the assignment.
You may use input_example.txt. It is important to conclude the instructions with a newline (or 'ENTER' or 'f').

### Running tests
Run ```python3.9 -m unittest ruby_robot_tests.test_field.TestField``` in /RubyRobotChallenge/

Run ```python3.9 -m unittest ruby_robot_tests.test_ruby_robot.TestRubyRobot``` in /RubyRobotChallenge/

Run ```python3.9 -m unittest ruby_robot_tests.test_input_processor.TestInputProcessor``` in /RubyRobotChallenge/

The test input from the assignment is tested in test_execute_assignment_instructions(), 
which is the last test in TestRubyRobot.
Alternatively, you can start the application by running main.py and paste the input from assignment 
into the standard input (or any other set of instructions you would like to test).