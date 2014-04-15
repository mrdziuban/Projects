def count_words(string):
  print('Total words: ' + str(len(string.split(' '))))
  words = {}
  for word in string.split(' '):
    words.setdefault(word, 0)
    words[word] += 1
  return words

string = input('Enter string: ')
print(count_words(string))