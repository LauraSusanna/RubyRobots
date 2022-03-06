import sys

from ruby_robot_mission.input_processor import InputProcessor
from ruby_robot_mission.mission_control import MissionControl
from ruby_robot_mission.ruby_robot import RubyRobot

if __name__ == '__main__':
    field, robot_data = InputProcessor().get_input()

    # Create a specific kind of robots here, for example ruby robots (dependency injection)
    robots = [RubyRobot(startposition, instructions) for startposition, instructions in robot_data]

    final_positions = MissionControl.run_mission(field, robots)

    for i, pos in enumerate(final_positions, start=1):
        print(f'Final Position of Robot {i}: {pos}')

    sys.exit(0)
