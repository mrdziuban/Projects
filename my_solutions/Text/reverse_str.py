def reverse(string):
  last_idx = len(string) - 1
  res = ''
  while last_idx >= 0:
    res += string[last_idx]
    last_idx -= 1
  return res

def reverse_easy(string):
  return string[::-1]

string = input('Enter string: ')
print(reverse_easy(string))