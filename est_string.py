from pprint import pprint

print('exercicios 1: tamanho de strings')
def strig_length(first: str, second: str) -> str:
   if first == second:
      return 'As duas strings são iguais'
   elif (len(first) == len(second)) and (first != second):
      return 'tamanhos iguais, strings diferentes'
   else:
      return 'strings diferentes em conteudo e tamanho'

# pprint(strig_length('breno', 'bruno'))

def reverse_upper(word: str) -> str:
   return (word.upper())[::-1]

# pprint(reverse_upper('breno'))

def vertical_word(word: str) -> str:
   for x in word:
      print(x)

# vertical_word('jhon Felon')

def vertical_word_scale(word: str) -> str:
   result = ''
   for x in word:
      result += x
      print(result)

# vertical_word_scale('jhon felon')

def reverse_vertical_word_scale(word: str) -> str:
   result = word
   for x in result:
      result = result[:-1]
      print(result)

# reverse_vertical_word_scale('jhon felon')

