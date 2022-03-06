import unittest

from ruby_robot_mission.field import Field


class TestField(unittest.TestCase):

    def setUp(self):
        self.Field = Field(5, 5)

    def tearDown(self):
        self.Field = None

    def test_field_exists(self):
        self.assertIsInstance(self.Field, Field, "Mission class is missing or initiated incorrectly")

    def test_field_size_can_be_valid_and_narrow_x0(self):
        self.assertTrue(Field(0, 3))

    def test_field_size_can_be_valid_and_narrow_y0(self):
        self.assertTrue(Field(1, 0))

    def test_field_size_can_be_valid_and_allow_no_movement_x0_y0(self):
        self.assertTrue(Field(0, 0))

    def test_field_size_cannot_be_invalid_negative_x(self):
        x = -1
        y = 5
        with self.assertRaises(ValueError):
            Field(x, y)

    def test_field_size_cannot_be_invalid_negative_y(self):
        x = 1
        y = -5
        with self.assertRaises(ValueError):
            Field(x, y)

    def test_field_size_cannot_be_invalid_negative_x_and_y(self):
        x = -2
        y = -3
        with self.assertRaises(ValueError):
            Field(x, y)

    def test_field_size_cannot_be_invalid_floats(self):
        x = 0.5
        y = 3.7
        with self.assertRaises(ValueError):
            Field(x, y)

    def test_add_valid_position_to_currently_occupied_positions(self):
        self.Field.add_to_currently_occupied_positions(3, 3)
        expected = [[3, 3]]
        self.assertEqual(self.Field.currently_occupied_positions, expected)

    def test_add_valid_positions_to_currently_occupied_positions(self):
        self.Field.add_to_currently_occupied_positions(3, 3)
        self.Field.add_to_currently_occupied_positions(1, 3)
        self.Field.add_to_currently_occupied_positions(2, 2)
        self.Field.add_to_currently_occupied_positions(1, 0)
        expected = [[3, 3], [1, 3], [2, 2], [1, 0]]
        self.assertEqual(self.Field.currently_occupied_positions, expected)

    def test_add_valid_position_on_bottom_left_corner_to_currently_occupied_positions(self):
        self.assertTrue(self.Field.add_to_currently_occupied_positions(0, 0))
        expected = [[0, 0]]
        self.assertEqual(self.Field.currently_occupied_positions, expected)

    def test_add_valid_position_on_top_right_corner_to_currently_occupied_positions(self):
        self.assertTrue(self.Field.add_to_currently_occupied_positions(5, 5))
        expected = [[5, 5]]
        self.assertEqual(self.Field.currently_occupied_positions, expected)

    def test_add_invalid_too_large_x_position_to_currently_occupied_positions_returns_false(self):
        self.assertFalse(self.Field.add_to_currently_occupied_positions(6, 3))

    def test_add_invalid_too_large_y_position_to_currently_occupied_positions_returns_false(self):
        self.assertFalse(self.Field.add_to_currently_occupied_positions(3, 6))

    def test_add_invalid_too_large_x_and_y_position_to_currently_occupied_positions_returns_false(self):
        self.assertFalse(self.Field.add_to_currently_occupied_positions(6, 6))

    def test_add_invalid_negative_x_position_to_currently_occupied_positions_returns_false(self):
        self.assertFalse(self.Field.add_to_currently_occupied_positions(-1, 3))

    def test_add_invalid_negative_y_position_to_currently_occupied_positions_returns_false(self):
        self.assertFalse(self.Field.add_to_currently_occupied_positions(3, -1))

    def test_add_invalid_negative_x_and_y_position_to_currently_occupied_positions_returns_false(self):
        self.assertFalse(self.Field.add_to_currently_occupied_positions(-1, -6))

    def test_add_invalid_float_x_position_to_currently_occupied_positions_returns_false(self):
        self.assertFalse(self.Field.add_to_currently_occupied_positions(0.5, 3))

    def test_add_invalid_float_y_position_to_currently_occupied_positions_returns_false(self):
        self.assertFalse(self.Field.add_to_currently_occupied_positions(3, 1.7))

    def test_add_invalid_float_x_and_y_position_to_currently_occupied_positions_returns_false(self):
        self.assertFalse(self.Field.add_to_currently_occupied_positions(3.3, 4.4))

    def test_update_currently_occupied_positions_from_valid_to_valid(self):
        start_x = 3
        start_y = 3
        self.Field.add_to_currently_occupied_positions(start_x, start_y)  # valid 'from' position
        new_x = 3
        new_y = 4
        self.assertTrue(self.Field.update_currently_occupied_positions(start_x, start_y, new_x, new_y))

    def test_update_currently_occupied_positions_from_valid_to_invalid_because_occupied(self):
        start_x = 3
        start_y = 3
        self.Field.add_to_currently_occupied_positions(start_x, start_y)  # valid 'from' position
        new_x = 3
        new_y = 4
        # occupy the 'to' position and thereby making it invalid to move to:
        self.Field.add_to_currently_occupied_positions(new_x, new_y)
        self.assertFalse(self.Field.update_currently_occupied_positions(start_x, start_y, new_x, new_y))

    def test_update_currently_occupied_positions_from_valid_to_invalid_because_not_on_field(self):
        start_x = 5
        start_y = 5
        self.Field.add_to_currently_occupied_positions(start_x, start_y)  # valid 'from' position
        new_x = 5
        new_y = 6  # value is outside of Field
        self.assertFalse(self.Field.update_currently_occupied_positions(start_x, start_y, new_x, new_y))

    def test_update_currently_occupied_positions_from_valid_to_invalid_because_float(self):
        start_x = 5
        start_y = 5
        self.Field.add_to_currently_occupied_positions(start_x, start_y)  # valid 'from' position
        new_x = 5
        new_y = 4.5  # float values are not valid Field coordinates
        self.assertFalse(self.Field.update_currently_occupied_positions(start_x, start_y, new_x, new_y))


if __name__ == '__main__':
    unittest.main()
