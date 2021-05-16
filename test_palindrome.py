# This should be used with pytest.

import palindrome

def test_true1():
  assert palindrome.is_palindrome("racecar")

def test_true2():
  assert palindrome.is_palindrome("Neveroddoreven")

def test_false1():
  assert not(palindrome.is_palindrome("hello"))

def test_false2():
  assert not(palindrome.is_palindrome("Never odd or even"))
