import sys
from typing import Union

from ruby_robot_mission.field import Field
from ruby_robot_mission.position import Position


def is_positive_integer(integer: int):
    return integer > 0


def is_zero_or_positive_integer(integer: int):
    return integer >= 0


class InputProcessor:

    @staticmethod
    def _init_field(size: str) -> Union[Field, ValueError]:
        # casting raises ValueError if impossible
        if len(size.split()) != 2:
            raise ValueError
        else:
            max_x = int(size.split()[0])
            max_y = int(size.split()[1])
            if is_zero_or_positive_integer(max_x) and is_zero_or_positive_integer(max_y):
                return Field(max_x, max_y)
            else:
                raise ValueError

    def _get_valid_startposition(self, start_position: str, field: Field) -> Position:
        x, y, heading = start_position.split()
        x = int(x)
        y = int(y)
        if not is_zero_or_positive_integer(x) or x > field.max_x:
            raise ValueError
        if not is_zero_or_positive_integer(y) or y > field.max_y:
            raise ValueError
        if not self._is_valid_heading(heading):
            raise ValueError
        return Position(x, y, heading)

    @staticmethod
    def _get_validated_instructions(instructs: str) -> str:
        for letter in instructs.strip():
            if letter not in ['L', 'R', 'M']:
                raise ValueError
        return instructs

    @staticmethod
    def _is_valid_heading(heading: str) -> bool:
        return heading in ['N', 'E', 'S', 'W']

    def get_input(self) -> tuple[Field, list[tuple[Position, str]]]:
        print('Welcome to Robot Mission. Please enter the mission data: ')

        field = Field(0, 0)
        startposition = Position(0, 0, '')
        robot_data = []
        line_count = 0
        robot_count = 1

        for line in sys.stdin:
            line = line.rstrip()

            if line in ['q', 'f', '']:  # q' == line or 'f' == line or '' == line
                break

            if line_count == 0:
                try:
                    field = self._init_field(line)
                    print(f'Field: {field}')
                except ValueError:
                    print('Field size invalid. Please try again. Enter two positive integers separated by a space.')
                    sys.exit(1)

            if line_count >= 1 and line_count % 2 == 1:
                try:
                    startposition = self._get_valid_startposition(line, field)
                    print(f'Robot {robot_count} startposition: {startposition}')
                except ValueError:
                    print(f'Start position of Robot{robot_count} invalid. Please try again.')
                    sys.exit(1)

            if line_count >= 1 and line_count % 2 == 0:
                try:
                    instructions = self._get_validated_instructions(line)
                    print(f'Robot {robot_count} instructions: {instructions}')
                except ValueError:
                    print(f'Instructions of Robot{robot_count} invalid. Please try again.')
                    sys.exit(1)

                try:
                    if field.add_to_currently_occupied_positions(startposition.x, startposition.y):
                        robot_data.append((startposition, instructions))
                    else:
                        print('Robots cannot start at the same x y coordinates')
                except ValueError:
                    sys.exit(1)

                robot_count += 1

            line_count += 1

        return field, robot_data
