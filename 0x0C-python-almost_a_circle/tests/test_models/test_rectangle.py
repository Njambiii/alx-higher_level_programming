#!/usr/bin/python3
"""Tests for the ``Rectangle`` class in the ``rectangle`` module
The ``rectangle`` module is in the ``models`` package"""

import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the ``Rectangle`` class"""

    def test_inheritance(self):
        """Testing if the class properly inherits from its base class"""

        base1 = Base()
        rect1 = Rectangle(1, 2)
        rect2 = Rectangle(1, 2)

        self.assertTrue(type(base1) == Base)
        self.assertTrue(isinstance(base1, Base))

        self.assertTrue(type(rect1) == Rectangle)
        self.assertTrue(isinstance(rect1, Rectangle))
        self.assertFalse(rect1 is Rectangle)

        self.assertTrue(isinstance(rect1, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(issubclass(Base, Rectangle))
        self.assertFalse(str(rect1) == str(base1))

        self.assertFalse(str(rect1) == str(rect2))
        self.assertFalse(rect1 is rect2)
        self.assertFalse(base1 is rect1)

    def test_getters_setters(self):
        """Testing the getter/setter methods for private instance attributes"""
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(5, 6)

        self.assertEqual(rect1.width, 1)
        rect1.width = 2
        self.assertEqual(rect1.width, 2)

        self.assertEqual(rect2.width, 5)
        rect2.width = 6
        self.assertEqual(rect2.width, 6)

        self.assertEqual(rect1.x, 3)
        rect1.x = 4
        self.assertEqual(rect1.x, 4)

        self.assertEqual(rect2.x, 0)
        rect2.x = 1
        self.assertEqual(rect2.x, 1)

        self.assertEqual(rect1.y, 4)
        rect1.y = 5
        self.assertEqual(rect1.y, 5)

        self.assertEqual(rect2.y, 0)
        rect2.y = 1
        self.assertEqual(rect2.y, 1)

    def test_validate_attributes(self):
        """Check types and values of all attributes with error messages"""

        width_type_error_msg = 'width must be an integer'
        width_value_error_msg = 'width must be > 0'

        height_type_error_msg = 'height must be an integer'
        height_value_error_msg = 'height must be > 0'

        x_type_error_msg = 'x must be an integer'
        x_value_error_msg = 'x must be >= 0'

        y_type_error_msg = 'y must be an integer'
        y_value_error_msg = 'y must be >= 0'

        invalid_literal_int = "invalid literal for int() with base 10: 'nan'"

        # # 'width' attribute
        # check string
        with self.assertRaises(TypeError) as e:
            Rectangle('1', '2')
        self.assertEqual(str(e.exception), width_type_error_msg)

        # check list
        with self.assertRaises(TypeError) as e:
            Rectangle([1], '2')
        self.assertEqual(str(e.exception), width_type_error_msg)

        # check tuple
        with self.assertRaises(TypeError) as e:
            Rectangle((1,), '2')
        self.assertEqual(str(e.exception), width_type_error_msg)

        # check dict
        with self.assertRaises(TypeError) as e:
            Rectangle({1: '2'}, '2')
        self.assertEqual(str(e.exception), width_type_error_msg)

        with self.assertRaises(TypeError) as e:
            Rectangle(height=1)
        self.assertEqual(
                str(e.exception),
                "__init__() missing 1 required positional argument: "
                "'width'", str(e.exception)
                )

        # Missing argument
        # with self.assertRaises(SyntaxError):
        #     Rectangle(, 1)

        # check Not a Number
        with self.assertRaises(ValueError) as e:
            Rectangle(int('nan'), 2)
        self.assertEqual(str(e.exception), invalid_literal_int)

        # check  0 value of width with error message
        with self.assertRaises(ValueError) as e:
            Rectangle(0, 2)
        self.assertEqual(str(e.exception), width_value_error_msg)

        # check negative value of width with error message
        with self.assertRaises(ValueError) as e:
            Rectangle(-1, 2)
        self.assertEqual(str(e.exception), width_value_error_msg)

        # # 'height' attribute
        # check string
        with self.assertRaises(TypeError) as e:
            Rectangle(1, '')
        self.assertEqual(str(e.exception), height_type_error_msg)

        # check dict
        with self.assertRaises(TypeError) as e:
            Rectangle(1, {})
        self.assertEqual(str(e.exception), height_type_error_msg)

        # check list
        with self.assertRaises(TypeError) as e:
            Rectangle(1, [])
        self.assertEqual(str(e.exception), height_type_error_msg)

        # check tuple
        with self.assertRaises(TypeError) as e:
            Rectangle(1, (1, ))
        self.assertEqual(str(e.exception), height_type_error_msg)

        with self.assertRaises(TypeError) as e:
            Rectangle(1, )
        self.assertEqual(
                str(e.exception),
                "__init__() missing 1 required positional argument: 'height'"
                )

        with self.assertRaises(TypeError) as e:
            Rectangle()
        self.assertEqual(
            "__init__() missing 2 required positional arguments: "
            "'width' and 'height'", str(e.exception)
            )

        # check Not a Number
        with self.assertRaises(ValueError) as e:
            Rectangle(1, int('nan'))
        self.assertEqual(str(e.exception), invalid_literal_int)

        # check 0
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 0)
        self.assertEqual(str(e.exception), height_value_error_msg)

        # check negative number
        with self.assertRaises(ValueError) as e:
            Rectangle(1, -1)
        self.assertEqual(str(e.exception), height_value_error_msg)

        # # 'x' attribute
        # check string
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 1, '')
        self.assertEqual(str(e.exception), x_type_error_msg)

        # check dict
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 1, {})
        self.assertEqual(str(e.exception), x_type_error_msg)

        # check list
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 1, [])
        self.assertEqual(str(e.exception), x_type_error_msg)

        # check tuple
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 1, (1, ))
        self.assertEqual(str(e.exception), x_type_error_msg)

        # check Not a Number
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 1, int('nan'))
        self.assertEqual(str(e.exception), invalid_literal_int)

        # check negative number
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 1, -1)
        self.assertEqual(str(e.exception), x_value_error_msg)

        # # 'y' attribute
        # check string
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 1, 0, '')
        self.assertEqual(str(e.exception), y_type_error_msg)

        # check dict
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 1, 0, {})
        self.assertEqual(str(e.exception), y_type_error_msg)

        # check list
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 1, 0, [])
        self.assertEqual(str(e.exception), y_type_error_msg)

        # check tuple
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 1, 0, (1, ))
        self.assertEqual(str(e.exception), y_type_error_msg)

        # check Not a Number
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 1, 0, int('nan'))
        self.assertEqual(str(e.exception), invalid_literal_int)

        # check negative number
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 1, 0, -1)
        self.assertEqual(str(e.exception), y_value_error_msg)

    def test_area(self):
        """Test for the area method"""

        rect1 = Rectangle(1, 2)
        self.assertEqual(rect1.area(), 2)

        with self.assertRaises(TypeError) as e:
            rect1.area(1)
        self.assertEqual(
                str(e.exception),
                "area() takes 1 positional argument but 2 were given"
                )

    @patch('builtins.print')
    def test_display(self, mock_print):
        """Test for the display method"""

        rect1 = Rectangle(1, 2)
        rect1.display()

        mock_print.assert_called_with('#\n#\n', end='')

        rect2 = Rectangle(2, 1, 1, 2)
        rect2.display()
        mock_print.assert_called_with('\n\n ##\n', end='')

        with self.assertRaises(TypeError) as e:
            rect1.display(1)
        self.assertEqual(
                str(e.exception),
                "display() takes 1 positional argument but 2 were given"
                )

    def test_str(self):
        """Test the `__str__` method"""

        rect1 = Rectangle(1, 2)
        rect1.id = 1
        str_expected = "[Rectangle] (1) 0/0 - 1/2"
        self.assertEqual(str(rect1), str_expected)

    def test_update(self):
        """Test for the `update` method"""

        rect1 = Rectangle(5, 6, 7, 8, 9)
        self.assertEqual(rect1.id, 9)
        rect1.update(id=10)
        self.assertEqual(rect1.id, 10)

        self.assertEqual(rect1.width, 5)
        with self.assertRaises(TypeError) as e:
            rect1.update(width='11')
        self.assertEqual(str(e.exception), "width must be an integer")

        self.assertEqual(rect1.y, 8)
        with self.assertRaises(ValueError) as e:
            rect1.update(y=-1)
        self.assertEqual(str(e.exception), 'y must be >= 0')

        # args exist and is not empty
        self.assertEqual(rect1.width, 5)
        rect1.update(1, 2, id=4, width=3)
        self.assertEqual(rect1.id, 1)
        self.assertEqual(rect1.width, 2)

        # args does not exist
        args = None
        self.assertEqual(rect1.id, 1)
        with self.assertRaises(TypeError) as e:
            rect1.update(*args, id=4, width=3, height=2)
        self.assertEqual(
                str(e.exception),
                "update() argument after * must be a sequence, not NoneType"
                )

        # args exist and is empty
        args = []
        rect1.update(*args, id=4, width=3, height=2)
        self.assertEqual(rect1.id, 4)
        self.assertEqual(rect1.width, 3)
        self.assertEqual(rect1.height, 2)

        # args has too many arguments
        args = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        rect1.update(*args)
        self.assertEqual(rect1.id, 4)

        # args contains a non int
        args = [1, '2']
        with self.assertRaises(TypeError) as e:
            rect1.update(*args)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_to_dictionary(self):
        """Test for the public method `to_dictionary`.
        Returns the dictionary representation of a `Rectangle`
        """

        rect1 = Rectangle(2, 1, 2, 1, 2)
        the_dict = {'id': 2, 'width': 2, 'height': 1, 'x': 2, 'y': 1}
        self.assertEqual(rect1.to_dictionary(), the_dict)

        rect1.update(id=3, x=6)
        the_dict = {'id': 3, 'width': 2, 'height': 1, 'x': 6, 'y': 1}
        self.assertEqual(rect1.to_dictionary(), the_dict)

        args = [8, 9]
        rect1.update(*args)
        the_dict = {'id': 8, 'width': 9, 'height': 1, 'x': 6, 'y': 1}
        self.assertEqual(rect1.to_dictionary(), the_dict)


if __name__ == "__main__":
    unittest.main()
