def count_vowels(string):
  vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
  for l in string:
    if l in vowels.keys():
      vowels[l] += 1
  return vowels
  vowels.keys().sort(key)

string = raw_input('Enter your string: ')
print count_vowels(string)
for vowel in vowels.keys().sort(by key):
  print str(vowel) + ': ' + vowels[vowel]