#!/usr/bin/python3
"""Test User"""
import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.user import User


def test_pep8_conformance_user(self):
    """Test that we conform to PEP8."""
    pep8style = pep8.StyleGuide(quiet=True)
    result = pep8style.check_files(['models/user.py'])
    self.assertEqual(result.total_errors, 0, (
                "Found code style errors (and warnings)."))


class Testuser(unittest.TestCase):
    """test class user"""
    @classmethod
    def setUpClass(cls):
        """class method"""
        cls.my_user = User()
        cls.my_user.first_name = 'Holberton'
        cls.my_user.last_name = 'School'
        cls.my_user.email = '2020@holbertonschool.com'
        cls.my_user.password = "peer"

    def test_User(self):
        """ Test attributes of Class Use"""
        self.assertEqual(self.my_user.first_name, 'Holberton')
        self.assertEqual(self.my_user.last_name, 'School')
        self.assertEqual(self.my_user.email, '2020@holbertonschool.com')
        self.assertEqual(self.my_user.password, 'peer')

    def test_strings(self):
        """ Test if it's string"""
        self.assertEqual(type(self.my_user.email), str)
        self.assertEqual(type(self.my_user.password), str)
        self.assertEqual(type(self.my_user.first_name), str)
        self.assertEqual(type(self.my_user.first_name), str)

    def test_save(self):
        """ Test if saves"""
        self.my_user.save()
        self.assertNotEqual(self.my_user.created_at, self.my_user.updated_at)

    def test_to_dict(self):
        """ Test if in dict"""
        self.assertEqual('to_dict' in dir(self.my_user), True)

    def test_attr(self):
        """Check Attributes"""
        self.assertTrue('email' in self.my_user.__dict__)
        self.assertTrue('id' in self.my_user.__dict__)
        self.assertTrue('created_at' in self.my_user.__dict__)
        self.assertTrue('updated_at' in self.my_user.__dict__)
        self.assertTrue('password' in self.my_user.__dict__)
        self.assertTrue('first_name' in self.my_user.__dict__)
        self.assertTrue('last_name' in self.my_user.__dict__)


if __name__ == "__main__":
    unittest.main()
