import unittest

from ruby_robot_mission.field import Field
from ruby_robot_mission.input_processor import InputProcessor
from ruby_robot_mission.position import Position


class TestInputProcessor(unittest.TestCase):

    def setUp(self):
        self.input_processor = InputProcessor()
        self.field = Field(5, 5)

    def tearDown(self):
        self.input_processor = None

    def test_input_processor_exists(self):
        self.assertIsInstance(self.input_processor, InputProcessor,
                              "InputProcessor class is missing or initiated incorrectly")

    def test_init_field_with_positive_integers(self):
        expected_field = Field(5, 5)
        actual_field = self.input_processor._init_field('5 5')
        self.assertEqual(expected_field, actual_field)

    def test_cannot_init_field_with_neg_integer_x(self):
        with self.assertRaises(ValueError):
            self.input_processor._init_field('-5 5')

    def test_cannot_init_field_with_neg_integer_y(self):
        with self.assertRaises(ValueError):
            self.input_processor._init_field('5 -5')

    def test_cannot_init_field_with_neg_integers_x_and_y(self):
        with self.assertRaises(ValueError):
            self.input_processor._init_field('-5 -5')

    def test_cannot_init_field_with_floats_x(self):
        with self.assertRaises(ValueError):
            self.input_processor._init_field('1.5 5')

    def test_cannot_init_field_with_floats_y(self):
        with self.assertRaises(ValueError):
            self.input_processor._init_field('5 1.5')

    def test_cannot_init_field_with_floats_x_and_y(self):
        with self.assertRaises(ValueError):
            self.input_processor._init_field('1.5 5.3')

    def test_cannot_init_field_with_incorrect_format_too_few(self):
        # correct format is a string of two integers separated by a space
        with self.assertRaises(ValueError):
            self.input_processor._init_field('5')

    def test_cannot_init_field_with_incorrect_format_too_many(self):
        # correct format is a string of two integers separated by a space
        with self.assertRaises(ValueError):
            self.input_processor._init_field('5 5 5')

    def test_get_startposition(self):
        expected_position = Position(1, 2, 'N')
        actual_position = self.input_processor._get_valid_startposition('1 2 N', self.field)
        self.assertEqual(expected_position, actual_position)

    def test_invalid_starting_position_x_not_on_field(self):
        # x not on the field
        start_str = '6 3 N'
        with self.assertRaises(ValueError):
            self.input_processor._get_valid_startposition(start_str, self.field)

    def test_invalid_starting_position_y_not_on_field(self):
        # y not on the field
        start_str = '3 6 N'
        with self.assertRaises(ValueError):
            self.input_processor._get_valid_startposition(start_str, self.field)

    def test_invalid_starting_position_x_and_y_not_on_field(self):
        # x & y not on the field
        start_str = '6 6 N'
        with self.assertRaises(ValueError):
            self.input_processor._get_valid_startposition(start_str, self.field)

    def test_heading_is_valid(self):
        valid_heading = 'N'
        self.assertIsNotNone(self.input_processor._is_valid_heading(valid_heading))

    def test_invalid_heading_returns_false(self):
        invalid_heading = 'X'
        self.assertFalse(self.input_processor._is_valid_heading(invalid_heading))

    def test_valid_instructions(self):
        valid_instructions1 = ''
        valid_instructions2 = 'L'
        valid_instructions3 = 'R'
        valid_instructions4 = 'M'
        valid_instructions5 = 'LRM'
        valid_instructions6 = 'LMRRMLLLMMMRR'
        valid_instructions7 = 'LMLMLMLMM '
        valid_instructions8 = 'MMRMMRMRRM\n'
        self.assertIsNotNone(self.input_processor._get_validated_instructions(valid_instructions1))
        self.assertIsNotNone(self.input_processor._get_validated_instructions(valid_instructions2))
        self.assertIsNotNone(self.input_processor._get_validated_instructions(valid_instructions3))
        self.assertIsNotNone(self.input_processor._get_validated_instructions(valid_instructions4))
        self.assertIsNotNone(self.input_processor._get_validated_instructions(valid_instructions5))
        self.assertIsNotNone(self.input_processor._get_validated_instructions(valid_instructions6))
        self.assertIsNotNone(self.input_processor._get_validated_instructions(valid_instructions7))
        self.assertIsNotNone(self.input_processor._get_validated_instructions(valid_instructions8))

    def test_invalid_instructions_raise_value_error(self):
        invalid_instructions1 = 'X'
        invalid_instructions2 = 'LMXR'
        invalid_instructions3 = 'LM R'
        invalid_instructions4 = ' '
        invalid_instructions5 = 'lmr'
        invalid_instructions6 = 1
        invalid_instructions7 = '1'
        invalid_instructions8 = 'None'
        invalid_instructions9 = None
        with self.assertRaises(ValueError):
            self.input_processor._get_validated_instructions(invalid_instructions1)
            self.input_processor._get_validated_instructions(invalid_instructions2)
            self.input_processor._get_validated_instructions(invalid_instructions3)
            self.input_processor._get_validated_instructions(invalid_instructions4)
            self.input_processor._get_validated_instructions(invalid_instructions5)
            self.input_processor._get_validated_instructions(invalid_instructions6)
            self.input_processor._get_validated_instructions(invalid_instructions7)
            self.input_processor._get_validated_instructions(invalid_instructions8)
            self.input_processor._get_validated_instructions(invalid_instructions9)


if __name__ == '__main__':
    unittest.main()
