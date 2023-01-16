#!/usr/bin/python3
"""This is a test module for the `Base` class in the ``models`` package"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """TestCase subclass"""

    def setUp(self):
        """Method to run at the start of each test method"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Check if `id` atttribute is accurate"""

        b1 = Base()
        b2 = Base(4)
        b3 = Base(-1)
        sq1 = Square(2)
        b4 = Base(0)
        rect1 = Rectangle(1, 2)
        b5 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 4)
        self.assertEqual(b3.id, -1)
        self.assertEqual(sq1.id, 2)
        self.assertEqual(b4.id, 0)
        self.assertEqual(rect1.id, 3)
        self.assertEqual(b5.id, 4)
        b5.id = 5
        self.assertEqual(b5.id, 5)

    def test_inheritance(self):
        """Test `Square` and `Rectangle` inheritance from `Base`"""

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

        sq1 = Square(1)
        sq2 = Square(1)

        self.assertTrue(type(base1) == Base)
        self.assertTrue(isinstance(base1, Base))

        self.assertTrue(type(sq1) == Square)
        self.assertTrue(isinstance(sq1, Square))
        self.assertTrue(isinstance(sq1, Rectangle))
        self.assertFalse(sq1 is Square)

        self.assertTrue(isinstance(sq1, Base))
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertFalse(issubclass(Base, Square))
        self.assertFalse(issubclass(Rectangle, Square))
        self.assertFalse(str(sq1) == str(base1))

        self.assertFalse(str(sq1) == str(sq2))
        self.assertFalse(sq1 is sq2)
        self.assertFalse(base1 is sq1)

        self.assertFalse(sq1 is rect1)

    def test_to_json_string(self):
        """Test for method `to_json_string` with expected input"""

        the_dict = {'x': 5, 'width': 1, 'id': 1, 'height': 2, 'y': 9}
        json_dict = Base.to_json_string([the_dict])
        self.assertTrue(isinstance(the_dict, dict))
        self.assertTrue(isinstance(json_dict, str))
        self.assertCountEqual(
            json_dict, '[{"x": 5, "width": 1, "id": 1, "height": 2, "y": 9}]')
        json_dict = Base.to_json_string([])
        self.assertEqual(json_dict, "[]")
        json_dict = Base.to_json_string(None)
        self.assertEqual(json_dict, "[]")

    def test_to_json_string_1(self):
        """Test with invalid types"""

        with self.assertRaises(TypeError) as e:
            Base.to_json_string(2)
        self.assertEqual(
                str(e.exception),
                "'list_dictionaries' must be a list of dicts"
                )

        with self.assertRaises(TypeError) as e:
            Base.to_json_string("A string")
        self.assertEqual(
                str(e.exception),
                "'list_dictionaries' must be a list of dicts"
                )

        with self.assertRaises(TypeError) as e:
            Base.to_json_string({1: 2})
        self.assertEqual(
                str(e.exception),
                "'list_dictionaries' must be a list of dicts"
                )

        with self.assertRaises(TypeError) as e:
            Base.to_json_string([1, "str"])
        self.assertEqual(
                str(e.exception),
                "'list_dictionaries' must be a list of dicts"
                )

        with self.assertRaises(TypeError) as e:
            Base.to_json_string({1: 'A', 2: 'dict'})
        self.assertEqual(
                str(e.exception),
                "'list_dictionaries' must be a list of dicts"
                )

        with self.assertRaises(TypeError) as e:
            Base.to_json_string((9, 0))
        self.assertEqual(
                str(e.exception),
                "'list_dictionaries' must be a list of dicts"
                )

        with self.assertRaises(TypeError) as e:
            Base.to_json_string(True)
        self.assertEqual(
                str(e.exception),
                "'list_dictionaries' must be a list of dicts"
                )

    def test_to_json_string_2(self):
        """Test with invalid number of arguments"""

        msg = "to_json_string() missing 1 required positional argument: "\
              + "'list_dictionaries'"

        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        self.assertEqual(str(e.exception), msg)

        msg = "to_json_string() takes 1 positional argument " + \
            "but 2 were given"

        with self.assertRaises(TypeError) as e:
            Base.to_json_string([{}], [{}])
        self.assertEqual(str(e.exception), msg)

    def test_save_to_file(self):
        """Test method `save_to_file` with expected input"""

        rect1 = Rectangle(10, 7, 2, 8)
        rect2 = Rectangle(2, 4)
        Rectangle.save_to_file([rect1, rect2])
        res = ('[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},' +
               ' {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]')

        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), len(res))

        Rectangle.save_to_file(None)
        res = "[]"
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), res)

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        Rectangle.save_to_file([])

        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), res)
        sq1 = Square(9, 3, 1, 12)
        sq2 = Square(6, 7)
        Square.save_to_file([sq1, sq2])
        res = ('[{"id": 12, "size": 9, "x": 3, "y": 1},' +
               ' {"id": 3, "size": 6, "x": 7, "y": 0}]')

        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), len(res))
        Square.save_to_file(None)
        res = "[]"

        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), res)
        os.remove("Square.json")
        Square.save_to_file([])

        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), res)

    def test_save_to_file_1(self):
        """Test with wrong number of arguments"""

        msg = "save_to_file() missing 1 required" + \
              " positional argument: 'list_objs'"

        with self.assertRaises(TypeError) as e:
            Rectangle.save_to_file()
        self.assertEqual(msg, str(e.exception))
        err_msg = "save_to_file() takes 2 positional " + \
                  "arguments but 3 were given"

        with self.assertRaises(TypeError) as e:
            Rectangle.save_to_file([Rectangle(9, 4), Rectangle(8, 9)], 98)
        self.assertEqual(err_msg, str(e.exception))

    def test_from_json_string(self):
        """Test method `from_json_string` with expected input"""

        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        res = [{'width': 10, 'height': 4, 'id': 89},
               {'width': 1, 'height': 7, 'id': 7}]
        self.assertCountEqual(list_output, res)
        self.assertEqual(type(list_output), list)

        list_output_1 = Rectangle.from_json_string('')
        self.assertEqual(list_output_1, [])

        list_output_2 = Rectangle.from_json_string(None)
        self.assertEqual(list_output_2, [])

    def test_from_json_string_1(self):
        """Test method `from_json_string` with invalid types"""

        json_err_msg = "'json_string' must be a string"

        with self.assertRaises(TypeError) as e:
            Rectangle.from_json_string([8, 9])
        self.assertEqual(json_err_msg, str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle.from_json_string(8)
        self.assertEqual(json_err_msg, str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle.from_json_string(9.6)
        self.assertEqual(json_err_msg, str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle.from_json_string((4, 5))
        self.assertEqual(json_err_msg, str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle.from_json_string({1: 'Hello', 2: 'Hi'})
        self.assertEqual(json_err_msg, str(e.exception))

    def test_from_json_string_2(self):
        """Test with invalid number of arguments"""

        err_msg = "from_json_string() missing 1 required " + \
                  "positional argument: 'json_string'"
        with self.assertRaises(TypeError) as e:
            Rectangle.from_json_string()
        self.assertEqual(err_msg, str(e.exception))
        err_msg = "from_json_string() takes 1 positional argument " + \
            "but 2 were given"
        with self.assertRaises(TypeError) as e:
            Rectangle.from_json_string("Hi", 98)
        self.assertEqual(err_msg, str(e.exception))

    def test_18_0(self):
        """Test class method create with normal types."""

        rect2 = Rectangle(3, 5, 1)
        rect2_dictionary = rect2.to_dictionary()
        rect3 = Rectangle.create(**rect2_dictionary)
        self.assertEqual(str(rect2), str(rect3))
        self.assertFalse(rect2 is rect3)
        self.assertFalse(rect2 == rect3)
        sq2 = Square(3, 5)
        sq2_dictionary = sq2.to_dictionary()
        sq1 = Square.create(**sq2_dictionary)
        self.assertEqual(str(sq2), str(sq1))
        self.assertFalse(sq2 is sq1)
        self.assertFalse(sq2 == sq1)

    def test_18_1(self):
        """Test class method create with wrong types."""

        with self.assertRaises(TypeError) as e:
            rect2 = "A string"
            Rectangle.create(rect2)
        self.assertEqual(
            "create() takes 1 positional argument but 2 were given",
            str(e.exception))

    def test_load_from_file_0(self):
        """Test class method load_from_file with normal types."""

        rect2 = Rectangle(10, 7, 2, 8)
        rect3 = Rectangle(2, 4)
        list_rectangles_input = [rect2, rect3]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        for x in zip(list_rectangles_input, list_rectangles_output):
            self.assertEqual(str(x[0]), str(x[1]))

        sq2 = Square(10, 2)
        sq1 = Square(9)
        list_squares_input = [sq2, sq1]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        for x in zip(list_squares_input, list_squares_output):
            self.assertEqual(str(x[0]), str(x[1]))

    def test_load_from_file_1(self):
        """Test class method load_from_file with missing files."""

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output, [])
        list_squares_output = Square.load_from_file()
        self.assertEqual(list_squares_output, [])

    def test_load_from_file_2(self):
        """Test class method load_from_file with wrong args."""

        s = "load_from_file() takes 1 positional argument but " + \
            "2 were given"
        with self.assertRaises(TypeError) as e:
            Rectangle.load_from_file("Hello")
        self.assertEqual(s, str(e.exception))

    def test_save_and_load_csv_0(self):
        """Test class method save_to_file_csv with normal types."""

        rect1 = Rectangle(10, 7, 2, 8)
        rect2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([rect1, rect2])
        res = "id,width,height,x,y\n1,10,7,2,8\n2,2,4,0,0\n"
        with open("Rectangle.csv", "r") as f:
            self.assertEqual(len(f.read()), len(res))
        sq1 = Square(9, 3, 1, 12)
        sq2 = Square(6, 7)
        Square.save_to_file_csv([sq1, sq2])
        res = "id,size,x,y\n12,9,3,1\n3,6,7,0\n"
        with open("Square.csv", "r") as f:
            self.assertEqual(len(f.read()), len(res))

    def test_save_and_load_csv_2(self):
        """Test class method save_to_file_csv with wrong args."""

        err_msg = "save_to_file_csv() missing 1 required" + \
                  " positional argument: 'list_objs'"
        with self.assertRaises(TypeError) as e:
            Rectangle.save_to_file_csv()
        self.assertEqual(err_msg, str(e.exception))
        err_msg = "save_to_file_csv() takes 2 positional arguments " + \
                  "but 3 were given"
        with self.assertRaises(TypeError) as e:
            Rectangle.save_to_file_csv([Rectangle(9, 4), Rectangle(8, 9)], 98)
        self.assertEqual(err_msg, str(e.exception))

    def test_save_and_load_csv_3(self):
        """Test class method `load_from_file_csv` with expected input"""

        rect2 = Rectangle(10, 7, 2, 8)
        rect3 = Rectangle(2, 4)
        list_rectangles_input = [rect2, rect3]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        for x in zip(list_rectangles_input, list_rectangles_output):
            self.assertEqual(str(x[0]), str(x[1]))

        sq2 = Square(10, 2)
        sq1 = Square(9)
        list_squares_input = [sq2, sq1]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        for x in zip(list_squares_input, list_squares_output):
            self.assertEqual(str(x[0]), str(x[1]))

    def test_save_and_load_csv_4(self):
        """Test class method load_from_file_csv with missing files."""

        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")
        if os.path.exists("Base.csv"):
            os.remove("Base.csv")
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(list_rectangles_output, [])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(list_squares_output, [])

    def test_save_and_load_csv_5(self):
        """Test class method load_from_file_csv with wrong args."""

        s = "load_from_file_csv() takes 1 positional argument " + \
            "but 2 were given"
        with self.assertRaises(TypeError) as e:
            Rectangle.load_from_file_csv("Hello")
        self.assertEqual(s, str(e.exception))


if __name__ == "__main__":
    unittest.main()
