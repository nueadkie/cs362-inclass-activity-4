import unittest
import wordcount

class Tester(unittest.TestCase):
  def test_empty(self):
    result = wordcount.calc("")
    self.assertEqual(result, 0)

  def test_just_whitespace(self):
    result = wordcount.calc("        ")
    self.assertEqual(result, 0)
  
  def test_normal1(self):
    result = wordcount.calc("hello world")
    self.assertEqual(result, 2)
  
  def test_normal2(self):
    result = wordcount.calc("a b c d e f g h i j k l m n o p q r s t u v w x y z")
    self.assertEqual(result, 26)
  
  def test_extra_whitespace(self):
    result = wordcount.calc("  hello world        ")
    self.assertEqual(result, 2)

if __name__ == '__main__':
  unittest.main()
