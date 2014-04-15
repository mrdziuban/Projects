def is_palindrome(string):
  return string.replace(' ', '') == string[::-1].replace(' ', '')

print is_palindrome(raw_input('Enter string: '))