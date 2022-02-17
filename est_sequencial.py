print('Estrutura sequencial\n')

# print('\nexercicio 1')
print('alo mundo')

# print('\nexercicio 2')
def numero_informado(x: int) -> int:
   print(f'O numero informado foi {x}')
   # return x


# numero_informado(7)

# print('\nexercicio 3')
def soma(*args: int) -> int:
   resultado = sum(args)
   print(f'{resultado = }')
   # return resultado


# soma(3, 5)

# print('\nexercicio 4')
def retorno_media(*args: int) -> int:
   soma = sum(args)
   numero_de_alunos = len(args)
   print(f'media dos alunos {soma/numero_de_alunos}')
   # return soma/numero_de_alunos


# retorno_media(5,6,7,8)

# print('\nexercicio 5')
def metros_to_cm(metros: int) -> int:
   print('{} metros equivalem a {} cm'.format(metros, metros*100))
   # return metros*100

# metros_to_cm(3)

# print('\nexercicio 6')
def retorno_da_área(raio: int) -> int:
   resultado = 3.14*(raio**2)
   print(f'{resultado = }')
   # return resultado


# retorno_da_área(16)

# print('\nexercicio 7')
def dobro_area_do_quadrado() -> int:
   lados: list[int] = [
      int(input('1° lado do quadrado: ')),
      int(input('2° lado do quadrado: ')),
      int(input('3° lado do quadrado: ')),
      int(input('4° lado do quadrado: '))
   ]
   result: int = 2*(sum(lados))
   print(f'o dobro da area do quadrado é {result}')
   # return result


# dobro_area_do_quadrado()

# print('\nexercicio 8')
def workaholic_hein() -> int:
   value: int = int(input('valor por hora: '))
   horas_trabalhadas: int = int(input('quantidade de horas trabalhadas: '))
   salario = value*horas_trabalhadas
   print(f'Seu salario nesse mês é de R$ {salario}')
   # return salario

# workaholic_hein()

# C = 5 * ((F-32) / 9).
# print('\nexercicio 9')
def Fahrenheit_to_Celsius(temp: int) -> int:
   celsios = 5 * ((temp - 32) / 9)
   celsios = round(celsios, 3)
   print(f'{celsios = }')
   # return celsios


# Fahrenheit_to_Celsius(44)

# print('\nexercicio 10')
def Celsios_to_Fahrenheit(temp: int) -> int:
   Fahrenheit = ((temp/5)*9) + 32
   Fahrenheit = round(Fahrenheit, 3)
   print(f'{Fahrenheit = }')
   # return Fahrenheit


# Celsios_to_Fahrenheit(6.667)

# print('\nexercicio 11')
def tres_etapas_de_construcao(first: int, second: int, real: float) -> list[float]:
   doble_one_half_another = (2*first)*(second/2)
   triple_one_more_real = (3*first)+real
   real_cube = (real**2)*real
   result = [ doble_one_half_another, triple_one_more_real, real_cube] 
   print(f'{result = }')
   # return result


# tres_etapas_de_construcao(7,2,4.38)

# print('\nexercicio 12')
# (72.7*altura) - 58
def deal_weigth() -> float:
   alt: float = float(input('Sua altura: '))
   deal_weigth = round((72.7*alt) - 58, 3)
   print(f'{deal_weigth = } kg')
   # return deal_weigth


deal_weigth()


