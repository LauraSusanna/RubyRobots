from ruby_robot_mission.field import Field
from ruby_robot_mission.position import Position
from ruby_robot_mission.robot import Robot


class MissionControl:
    @staticmethod
    def run_mission(field: Field, robots: list[Robot]) -> list[Position]:
        final_positions = []
        for robot in robots:
            final_positions.append(robot.execute_instructions_get_final_position(field))
        return final_positions
