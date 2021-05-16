def calc(input_string):
  # Special case for empty string, or if just whitespace.
  if len(input_string.strip()) == 0:
    return 0
  
  words = 1

  # Remove any trailing and leading whitespace.
  for char in input_string.strip():
    if char == ' ':
      words += 1
  
  return words
