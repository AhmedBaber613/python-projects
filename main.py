def emoji_converter(message):
  words = message.split(' ')
  emojis = {
  ':)': '😀',
  ':(': '😥',
  ':/': '😕',
  ':D': '😁',
  ':P': '😛',
  'XD': '😆',
  'X_X': '😠',
  'O_O': '😲',
  'O.O': '😲',
  'B_B': '😳',
  'B.B': '😳',
  ':|': '😐',
  ':-)': '😀',
  ':-(': '😥',
  ':-/': '😕',
  ':-D': '😁',
  ':-P': '😛',
  ':-X': '😆',
  ':-x': '😆',
  ':-O': '😲',
  ':-o': '😲',
  ':-B': '😳',
  ':-b': '😳',
  }
  output = ''
  for word in words:
    output += emojis.get(word, word) + ' '
  return output


message = input('> ')
print(emoji_converter(message))