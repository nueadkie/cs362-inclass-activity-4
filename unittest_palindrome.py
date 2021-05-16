import unittest
import palindrome

class Tester(unittest.TestCase):
  def test_true(self):
    result = palindrome.is_palindrome("racecar")
    self.assertEqual(result, True)

  def test_false(self):
    result = palindrome.is_palindrome("hello")
    self.assertEqual(result, False)
  
  def test_type_error(self):
    with self.assertRaises(TypeError):
      palindrome.is_palindrome(123)

if __name__ == '__main__':
  unittest.main()