# This should be used with pytest.

import wordcount

def test_empty():
  assert wordcount.calc("") == 0

def test_just_whitespace():
  assert wordcount.calc("        ") == 0

def test_normal1():
  assert wordcount.calc("hello world") == 2

def test_normal2():
  assert wordcount.calc("a b c d e f g h i j k l m n o p q r s t u v w x y z") == 26

def test_extra_whitespace():
  assert wordcount.calc("  hello world        ") == 2
