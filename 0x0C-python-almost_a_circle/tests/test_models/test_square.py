#!/usr/bin/python3
"""Tests for the ``Square`` class in the ``square`` module
The ``square`` module is in the ``models`` package"""

import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    """Test cases for the ``Square`` class"""

    def test_inheritance(self):
        """Testing if the class properly inherits from its base class"""

        base1 = Base()
        rect1 = Rectangle(1, 2)
        sq1 = Square(1)
        sq2 = Square(2)

        self.assertTrue(type(base1) == Base)
        self.assertTrue(isinstance(base1, Base))

        self.assertTrue(type(rect1) == Rectangle)
        self.assertTrue(isinstance(rect1, Rectangle))
        self.assertFalse(rect1 is Rectangle)
        self.assertTrue(type(sq1) == Square)

        self.assertTrue(isinstance(rect1, Base))
        self.assertTrue(isinstance(sq1, Base))
        self.assertTrue(isinstance(sq1, Rectangle))
        self.assertTrue(isinstance(sq2, Rectangle))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertFalse(issubclass(Base, Rectangle))
        self.assertFalse(issubclass(Rectangle, Square))
        self.assertFalse(str(rect1) == str(sq1))
        self.assertFalse(str(sq2) == str(sq1))

        self.assertFalse(sq1 is sq2)
        self.assertFalse(sq1 is rect1)

    def test_getters_setters(self):
        """Testing the getter/setter methods for private instance attributes"""
        sq1 = Square(1, 2, 3, 4)
        sq2 = Square(5, 6)

        self.assertEqual(sq1.size, 1)
        self.assertEqual(sq1.x, 2)
        self.assertEqual(sq1.y, 3)
        self.assertEqual(sq1.id, 4)

        self.assertEqual(sq2.size, 5)
        sq2.size = 6
        self.assertEqual(sq2.width, 6)
        self.assertEqual(sq2.height, 6)
        self.assertEqual(sq2.size, 6)

        sq1.x = 4
        self.assertEqual(sq1.x, 4)

        sq2.y = 1
        self.assertEqual(sq2.y, 1)

        sq2.id = 10
        self.assertEqual(sq2.id, 10)

    def test_validate_attributes(self):
        """Check types and values of all attributes with error messages"""

        width_type_error_msg = 'width must be an integer'
        width_value_error_msg = 'width must be > 0'

        x_type_error_msg = 'x must be an integer'
        x_value_error_msg = 'x must be >= 0'

        y_type_error_msg = 'y must be an integer'
        y_value_error_msg = 'y must be >= 0'

        invalid_literal_int = "invalid literal for int() with base 10: 'nan'"

        # # 'width' attribute
        # check string
        with self.assertRaises(TypeError) as e:
            Square('1', '2')
        self.assertEqual(str(e.exception), width_type_error_msg)

        # check list
        with self.assertRaises(TypeError) as e:
            Square([1], '2')
        self.assertEqual(str(e.exception), width_type_error_msg)

        # check tuple
        with self.assertRaises(TypeError) as e:
            Square((1,), '2')
        self.assertEqual(str(e.exception), width_type_error_msg)

        # check dict
        with self.assertRaises(TypeError) as e:
            Square({1: '2'}, '2')
        self.assertEqual(str(e.exception), width_type_error_msg)

        with self.assertRaises(TypeError) as e:
            Square(x=1)
        self.assertEqual(
            "__init__() missing 1 required positional argument: "
            "'size'", str(e.exception)
            )

        # Missing argument
        # with self.assertRaises(SyntaxError):
        #     Rectangle(, 1)

        # check Not a Number
        with self.assertRaises(ValueError) as e:
            Square(int('nan'), 2)
        self.assertEqual(str(e.exception), invalid_literal_int)

        # check  0 value of width with error message
        with self.assertRaises(ValueError) as e:
            Square(0, 2)
        self.assertEqual(str(e.exception), width_value_error_msg)

        # check negative value of width with error message
        with self.assertRaises(ValueError) as e:
            Square(-1, 2)
        self.assertEqual(str(e.exception), width_value_error_msg)

        # # 'x' attribute
        # check string
        with self.assertRaises(TypeError) as e:
            Square(1, '')
        self.assertEqual(str(e.exception), x_type_error_msg)

        # check dict
        with self.assertRaises(TypeError) as e:
            Square(1, {})
        self.assertEqual(str(e.exception), x_type_error_msg)

        # check list
        with self.assertRaises(TypeError) as e:
            Square(1, [])
        self.assertEqual(str(e.exception), x_type_error_msg)

        # check tuple
        with self.assertRaises(TypeError) as e:
            Square(1, (1, ))
        self.assertEqual(str(e.exception), x_type_error_msg)

        # check Not a Number
        with self.assertRaises(ValueError) as e:
            Square(1, int('nan'))
        self.assertEqual(str(e.exception), invalid_literal_int)

        # check negative number
        with self.assertRaises(ValueError) as e:
            Square(1, -1)
        self.assertEqual(str(e.exception), x_value_error_msg)

        # # 'y' attribute
        # check string
        with self.assertRaises(TypeError) as e:
            Square(1, 1, '')
        self.assertEqual(str(e.exception), y_type_error_msg)

        # check dict
        with self.assertRaises(TypeError) as e:
            Square(1, 1, {})
        self.assertEqual(str(e.exception), y_type_error_msg)

        # check list
        with self.assertRaises(TypeError) as e:
            Square(1, 1, [])
        self.assertEqual(str(e.exception), y_type_error_msg)

        # check tuple
        with self.assertRaises(TypeError) as e:
            Square(1, 1, (1, ))
        self.assertEqual(str(e.exception), y_type_error_msg)

        # check Not a Number
        with self.assertRaises(ValueError) as e:
            Square(1, 1, int('nan'))
        self.assertEqual(str(e.exception), invalid_literal_int)

        # check negative number
        with self.assertRaises(ValueError) as e:
            Square(1, 1, -1)
        self.assertEqual(str(e.exception), y_value_error_msg)

    def test_area(self):
        """Test for the area method"""

        sq1 = Square(1)
        self.assertEqual(sq1.area(), 1)

    def test_str(self):
        """Test the `__str__` method"""

        sq1 = Square(1, 2)
        sq1.id = 1
        str_expected = "[Square] (1) 2/0 - 1"
        self.assertEqual(str(sq1), str_expected)

    @patch('builtins.print')
    def test_display(self, mock_print):
        """Test the display method inherited from `Rectangle`"""

        sq1 = Square(2)
        sq1.display()
        mock_print.assert_called_with('##\n##\n', end='')

    def test_update(self):
        """Test for the `update` method"""

        sq1 = Square(5, 6, 7, 8)
        self.assertEqual(sq1.id, 8)
        sq1.update(id=10)
        self.assertEqual(sq1.id, 10)

        self.assertEqual(sq1.size, 5)
        with self.assertRaises(TypeError) as e:
            sq1.update(size='11')
        self.assertEqual(str(e.exception), "width must be an integer")

        self.assertEqual(sq1.y, 7)
        with self.assertRaises(ValueError) as e:
            sq1.update(y=-1)
        self.assertEqual(str(e.exception), 'y must be >= 0')

        # args exist and is not empty
        self.assertEqual(sq1.size, 5)
        sq1.update(1, 2, id=4, size=3)
        self.assertEqual(sq1.id, 1)

        # args does not exist
        args = None
        self.assertEqual(sq1.id, 1)
        with self.assertRaises(TypeError) as e:
            sq1.update(*args, id=4)
        self.assertEqual(
                str(e.exception),
                "update() argument after * must be a sequence, not NoneType"
                )

        # args exist and is empty
        args = []
        sq1.update(*args, id=4, x=8)
        self.assertEqual(sq1.id, 4)
        self.assertEqual(sq1.x, 8)
        self.assertEqual(sq1.area(), 4)

        # args has too many arguments
        args = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        sq1.update(*args)
        self.assertEqual(sq1.id, 4)

        # args contains a non int
        args = [1, '2']
        with self.assertRaises(TypeError) as e:
            sq1.update(*args)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_to_dictionary(self):
        """Test for the public method `to_dictionary`.
        Returns the dictionary representation of a `Square`
        """

        sq1 = Square(2, 1, 2, 1)
        the_dict = {'id': 1, 'size': 2, 'x': 1, 'y': 2}
        self.assertEqual(sq1.to_dictionary(), the_dict)

        sq1.update(id=3, x=6)
        the_dict = {'id': 3, 'size': 2, 'x': 6, 'y': 2}
        self.assertEqual(sq1.to_dictionary(), the_dict)

        args = [8, 9]
        sq1.update(*args)
        the_dict = {'id': 8, 'size': 9, 'x': 6, 'y': 2}
        self.assertEqual(sq1.to_dictionary(), the_dict)


if __name__ == "__main__":
    unittest.main()
