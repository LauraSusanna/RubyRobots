import unittest

from ruby_robot_mission.field import Field
from ruby_robot_mission.position import Position
from ruby_robot_mission.ruby_robot import RubyRobot


class TestRubyRobot(unittest.TestCase):

    def setUp(self):
        self.field = Field(5, 5)
        self.ruby_robot = RubyRobot(Position(1, 2, 'N'), 'LMLMLMLMM')
        self.field.add_to_currently_occupied_positions(1, 2)

    def tearDown(self):
        self.field = None
        self.ruby_robot = None

    def test_ruby_robot_exists(self):
        self.assertIsInstance(self.ruby_robot, RubyRobot, "RubyRobot class is missing or initiated incorrectly")

    def test_turn_left_start_N(self):
        self.ruby_robot._turn_left()
        heading_after_turning_left = self.ruby_robot.position.heading
        expected_heading = 'W'
        self.assertEqual(expected_heading, heading_after_turning_left)

    def test_turn_left_four_times_start_N(self):
        self.ruby_robot._turn_left()
        heading_after_turning_left = self.ruby_robot.position.heading
        expected_heading = 'W'
        self.assertEqual(expected_heading, heading_after_turning_left)
        self.ruby_robot._turn_left()
        heading_after_turning_left = self.ruby_robot.position.heading
        expected_heading = 'S'
        self.assertEqual(expected_heading, heading_after_turning_left)
        self.ruby_robot._turn_left()
        heading_after_turning_left = self.ruby_robot.position.heading
        expected_heading = 'E'
        self.assertEqual(expected_heading, heading_after_turning_left)
        self.ruby_robot._turn_left()
        heading_after_turning_left = self.ruby_robot.position.heading
        expected_heading = 'N'
        self.assertEqual(expected_heading, heading_after_turning_left)

    def test_turn_right_start_N(self):
        self.ruby_robot._turn_right()
        heading_after_turning_left = self.ruby_robot.position.heading
        expected_heading = 'E'
        self.assertEqual(expected_heading, heading_after_turning_left)

    def test_turn_right_four_times_start_N(self):
        self.ruby_robot._turn_right()
        heading_after_turning_left = self.ruby_robot.position.heading
        expected_heading = 'E'
        self.assertEqual(expected_heading, heading_after_turning_left)
        self.ruby_robot._turn_right()
        heading_after_turning_left = self.ruby_robot.position.heading
        expected_heading = 'S'
        self.assertEqual(expected_heading, heading_after_turning_left)
        self.ruby_robot._turn_right()
        heading_after_turning_left = self.ruby_robot.position.heading
        expected_heading = 'W'
        self.assertEqual(expected_heading, heading_after_turning_left)
        self.ruby_robot._turn_right()
        heading_after_turning_left = self.ruby_robot.position.heading
        expected_heading = 'N'
        self.assertEqual(expected_heading, heading_after_turning_left)

    def test_move_to_valid_position_North(self):
        ruby_robot_heading_north = RubyRobot(Position(3, 3, 'N'), '')
        self.field.add_to_currently_occupied_positions(3, 3)

        ruby_robot_heading_north._move_forward_if_possible(self.field)
        expected_x = 3
        expected_y = 4
        actual_x = ruby_robot_heading_north.position.x
        actual_y = ruby_robot_heading_north.position.y
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_move_to_valid_position_East(self):
        ruby_robot_heading_east = RubyRobot(Position(3, 3, 'E'), '')
        self.field.add_to_currently_occupied_positions(3, 3)

        ruby_robot_heading_east._move_forward_if_possible(self.field)
        expected_x = 4
        expected_y = 3
        actual_x = ruby_robot_heading_east.position.x
        actual_y = ruby_robot_heading_east.position.y
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_move_to_valid_position_South(self):
        ruby_robot_heading_south = RubyRobot(Position(3, 3, 'S'), '')
        self.field.add_to_currently_occupied_positions(3, 3)

        ruby_robot_heading_south._move_forward_if_possible(self.field)
        expected_x = 3
        expected_y = 2
        actual_x = ruby_robot_heading_south.position.x
        actual_y = ruby_robot_heading_south.position.y
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_move_to_valid_position_West(self):
        ruby_robot_heading_west = RubyRobot(Position(3, 3, 'W'), '')
        self.field.add_to_currently_occupied_positions(3, 3)

        ruby_robot_heading_west._move_forward_if_possible(self.field)
        expected_x = 2
        expected_y = 3
        actual_x = ruby_robot_heading_west.position.x
        actual_y = ruby_robot_heading_west.position.y
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_doesnt_move_to_invalid_position_not_on_field_top_right_north(self):
        ruby_robot_heading_north_on_top_right_edge = RubyRobot(Position(5, 5, 'N'), '')
        self.field.add_to_currently_occupied_positions(5, 5)

        ruby_robot_heading_north_on_top_right_edge._move_forward_if_possible(self.field)
        expected_x = 5
        expected_y = 5
        actual_x = ruby_robot_heading_north_on_top_right_edge.position.x
        actual_y = ruby_robot_heading_north_on_top_right_edge.position.y
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_doesnt_move_to_invalid_position_not_on_field_top_right_east(self):
        ruby_robot_heading_east_on_top_right_edge = RubyRobot(Position(5, 5, 'E'), '')
        self.field.add_to_currently_occupied_positions(5, 5)

        ruby_robot_heading_east_on_top_right_edge._move_forward_if_possible(self.field)
        expected_x = 5
        expected_y = 5
        actual_x = ruby_robot_heading_east_on_top_right_edge.position.x
        actual_y = ruby_robot_heading_east_on_top_right_edge.position.y
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_doesnt_move_to_invalid_position_not_on_field_bottom_left_south(self):
        ruby_robot_heading_east_on_top_right_edge = RubyRobot(Position(0, 0, 'S'), '')
        self.field.add_to_currently_occupied_positions(0, 0)

        ruby_robot_heading_east_on_top_right_edge._move_forward_if_possible(self.field)
        expected_x = 0
        expected_y = 0
        actual_x = ruby_robot_heading_east_on_top_right_edge.position.x
        actual_y = ruby_robot_heading_east_on_top_right_edge.position.y
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_doesnt_move_to_invalid_position_not_on_field_bottom_left_west(self):
        ruby_robot_heading_east_on_top_right_edge = RubyRobot(Position(0, 0, 'W'), '')
        self.field.add_to_currently_occupied_positions(0, 0)

        ruby_robot_heading_east_on_top_right_edge._move_forward_if_possible(self.field)
        expected_x = 0
        expected_y = 0
        actual_x = ruby_robot_heading_east_on_top_right_edge.position.x
        actual_y = ruby_robot_heading_east_on_top_right_edge.position.y
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_move_to_invalid_position_already_occupied(self):
        ruby_robot_2 = RubyRobot(Position(1, 1, 'N'), '')
        self.field.add_to_currently_occupied_positions(1, 1)

        # position forward would be (x=1, y=2)
        # --> invalid for this robot to move to, since this position is already occupied by the robot in the setUp
        ruby_robot_2._move_forward_if_possible(self.field)
        expected_x = 1
        expected_y = 1
        actual_x = ruby_robot_2.position.x
        actual_y = ruby_robot_2.position.y
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_explore_field_by_following_instructions_and_finish_in_correct_position_example_1(self):
        actual_position = self.ruby_robot.execute_instructions_get_final_position(self.field)
        expected_position = Position(x=1, y=3, heading='N')
        self.assertEqual(expected_position, actual_position)

    def test_explore_field_example_1_with_2nd_ruby_robot_on_field(self):
        ruby_robot_2 = RubyRobot(Position(3, 3, 'E'), 'MMRMMRMRRM')
        self.field.add_to_currently_occupied_positions(3, 3)

        self.assertTrue(isinstance(ruby_robot_2, RubyRobot))
        actual_position = self.ruby_robot.execute_instructions_get_final_position(self.field)
        expected_position = Position(x=1, y=3, heading='N')
        self.assertEqual(expected_position, actual_position)

    def test_explore_field_by_following_instructions_and_finish_in_correct_position_example_2(self):
        ruby_robot_2 = RubyRobot(Position(3, 3, 'E'), 'MMRMMRMRRM')
        self.field.add_to_currently_occupied_positions(3, 3)

        actual_position = ruby_robot_2.execute_instructions_get_final_position(self.field)
        expected_position = Position(x=5, y=1, heading='E')
        self.assertEqual(expected_position, actual_position)

    def test_execute_assignment_instructions(self):
        field = Field(10, 10)
        ruby_robot_1 = RubyRobot(Position(2, 3, 'E'), 'RMRMRLMRMRMRMR')
        ruby_robot_2 = RubyRobot(Position(5, 4, 'W'), 'LMRMLMRMRLMRRM')
        field.add_to_currently_occupied_positions(2, 3)
        field.add_to_currently_occupied_positions(5, 4)

        actual_position_1 = ruby_robot_1.execute_instructions_get_final_position(field)
        actual_position_2 = ruby_robot_2.execute_instructions_get_final_position(field)
        expected_position_1 = Position(x=1, y=2, heading='W')
        expected_position_2 = Position(x=3, y=2, heading='E')
        self.assertEqual(expected_position_1, actual_position_1)
        self.assertEqual(expected_position_2, actual_position_2)


if __name__ == '__main__':
    unittest.main()
