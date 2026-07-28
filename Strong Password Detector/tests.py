import unittest
import password_detector

class PasswaordTestCase(unittest.TestCase):
    """ Tests for password detector """
    def test_strong_password(self):
        result = password_detector.strength_detector('Password123')
        self.assertEqual(result, 'Strong')
    def test_medium_password(self):
        result = password_detector.strength_detector('123password123')
        self.assertEqual(result, 'Medium')
    def test_weak_password(self):
        result = password_detector.strength_detector('PASSWORD')
        self.assertEqual(result, 'Weak')
    def test_extra_strong(self):
        result = password_detector.strength_detector('passwordPASSWORD123@123/-=')
        self.assertEqual(result, 'Extra Strong')

unittest.main()