def is_palindrome(input_string):
  for i in range(len(input_string) // 2):
    if(input_string[i].lower() != input_string[len(input_string) - i - 1].lower()):
      return False
  return True