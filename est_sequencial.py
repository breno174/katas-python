print('Estrutura sequencial\n')

print('\nexercicio 1')
print('alo mundo')

print('\nnexercicio 2')
def numero_informado(x: int) -> str:
   print(f'O numero informado foi {x}')


# numero_informado(7)

print('\nexercicio 3')
def soma(*args: int) -> int:
   resultado = sum(args)
   print(f'{resultado = }')


# soma(3, 5)

print('\nexercicio 4')
def return_media(*args: int) -> str:
   soma = sum(args)
   numero_de_alunos = len(args)
   print(f'media dos alunos {soma/numero_de_alunos}')


# return_media(5,6,7,8)

print('\nexercicio 5')
def metros_to_cm(metros: int) -> str:
   print('{} metros equivalem a {} cm'.format(metros, metros*100))

# metros_to_cm(3)

print('\nexercicio 6')
def return_área(raio: int) -> int:
   resultado = 3.14*(raio**2)
   print(f'{resultado = }')


# return_área(16)

print('\nexercicio 7')
def dobro_area_do_quadrado() -> str:
   lados = [
      int(input('1° lado do quadrado: ')),
      int(input('2° lado do quadrado: ')),
      int(input('3° lado do quadrado: ')),
      int(input('4° lado do quadrado: '))
   ]
   result = 2*(sum(lados))
   print(f'o dobro da area do quadrado é {result}')


# dobro_area_do_quadrado()