from abc import ABC, abstractmethod

from ruby_robot_mission.field import Field
from ruby_robot_mission.position import Position


class Robot(ABC):
    @abstractmethod
    def __init__(self, position: Position, instructions: str):
        self.position = position
        self.instructions = instructions

    @abstractmethod
    def execute_instructions_get_final_position(self, field: Field) -> Position:
        ...


