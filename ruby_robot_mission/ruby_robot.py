from typing import Tuple

from ruby_robot_mission.field import Field
from ruby_robot_mission.position import Position
from ruby_robot_mission.robot import Robot

TURN_LEFT_MAPPING = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
TURN_RIGHT_MAPPING = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}


class RubyRobot(Robot):
    def __init__(self, position: Position, instructions: str):
        self.position = position
        self.instructions = instructions

    def execute_instructions_get_final_position(self, field: Field) -> Position:
        for order in self.instructions:
            if order == 'L':
                self._turn_left()
            if order == 'R':
                self._turn_right()
            if order == 'M':
                self._move_forward_if_possible(field)
        return self.position

    def _move_forward_if_possible(self, field: Field):
        new_x, new_y = self.__calc_new_x_y()
        # Update position if valid, else the 'M' order is ignored
        if field.update_currently_occupied_positions(self.position.x, self.position.y, new_x, new_y):
            self.position.x = new_x
            self.position.y = new_y

    def _turn_left(self):
        self.position.heading = TURN_LEFT_MAPPING[self.position.heading]

    def _turn_right(self):
        self.position.heading = TURN_RIGHT_MAPPING[self.position.heading]

    def __calc_new_x_y(self) -> Tuple[int, int]:
        new_x = self.position.x
        new_y = self.position.y
        heading = self.position.heading
        if heading == 'N':
            new_y += 1
        if heading == 'E':
            new_x += 1
        if heading == 'S':
            new_y -= 1
        if heading == 'W':
            new_x -= 1
        return new_x, new_y
