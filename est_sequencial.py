from pprint import pprint


print('Estrutura sequencial\n')

# print('\nexercicio 1')
print('alo mundo')

# print('\nexercicio 2')
def numero_informado(x: int) -> str:
   """Programa que peça um número e então mostre a mensagem O número informado foi [número].

   Args:
       x (int): numero

   Returns:
       str: frase com o numero inserido
   """
   print(f'O numero informado foi {x}')
   # return x


# numero_informado(7)

# print('\nexercicio 3')
def soma(*args: int) -> int:
   """Programa que peça dois números e imprima a soma.

   Returns:
       int: soma dos dois numeros
   """
   resultado = sum(args)
   print(f'{resultado = }')
   # return resultado


# soma(3, 5)

# print('\nexercicio 4')
def retorno_media(*args: int) -> int:
   """Programa que peça as 4 notas bimestrais e mostre a média.

   Returns:
       int: media dos alunos
   """
   soma = sum(args)
   numero_de_alunos = len(args)
   print(f'media dos alunos {soma/numero_de_alunos}')
   # return soma/numero_de_alunos


# retorno_media(5,6,7,8)

# print('\nexercicio 5')
def metros_to_cm(metros: int) -> int:
   """Programa que converta metros para centímetros.

   Args:
       metros (int): metros capitados

   Returns:
       int: converção dos metros para centimetros
   """
   print('{} metros equivalem a {} cm'.format(metros, metros*100))
   # return metros*100

# metros_to_cm(3)

# print('\nexercicio 6')
def retorno_da_área(raio: int) -> int:
   """Programa que peça o raio de um círculo, calcule e mostre sua área.
   """
   resultado = 3.14*(raio**2)
   print(f'{resultado = }')
   # return resultado


# retorno_da_área(16)

# print('\nexercicio 7')
def dobro_area_do_quadrado() -> int:
   """Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

   Returns:
       int: dobro da area dada
   """
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
   """Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

   Returns:
       int: o valor no mês que a pessoa recebe
   """
   value: int = int(input('valor por hora: '))
   horas_trabalhadas: int = int(input('quantidade de horas trabalhadas: '))
   salario = value*horas_trabalhadas
   print(f'Seu salario nesse mês é de R$ {salario}')
   # return salario

# workaholic_hein()

# C = 5 * ((F-32) / 9).
# print('\nexercicio 9')
def Fahrenheit_to_Celsius(temp: int) -> int:
   """Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
   Args:
       temp (int): temperatura em Fahrenheit

   Returns:
       int: converção dela para celcios
   """
   celsios = 5 * ((temp - 32) / 9)
   celsios = round(celsios, 3)
   print(f'{celsios = }')
   # return celsios


# Fahrenheit_to_Celsius(44)

# print('\nexercicio 10')
def Celsios_to_Fahrenheit(temp: int) -> int:
   """Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

   Args:
       temp (int): temperatura em Celsios

   Returns:
       int: temperatura em Fahrenheit
   """
   Fahrenheit = ((temp/5)*9) + 32
   Fahrenheit = round(Fahrenheit, 3)
   print(f'{Fahrenheit = }')
   # return Fahrenheit


# Celsios_to_Fahrenheit(6.667)

# print('\nexercicio 11')
def tres_etapas_de_construcao(first: int, second: int, real: float) -> list[float]:
   """Programa que peça 2 números inteiros e um número real. Calcule e mostre:

   Args:
       first (int): primeiro numero (inteiro)
       second (int): segundo numero (inteiro)
        real (float): terceiro numero (real)

   Returns:
       list[float]: resultados: 
            - 1° o produto do dobro do primeiro com metade do segundo. 
            - 2° a soma do triplo do primeiro com o terceiro. 
            - 3° o terceiro elevado ao cubo. 
   """
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
    """Tendo como dado de entrada a altura (h) de uma pessoa, algoritmo que calcula seu peso ideal, utilizando a seguinte fórmula:
     (72.7*h) - 58.3

    Returns:
        float: _description_
    """
    alt = float(input('Sua altura: '))
    deal_weigth = round((72.7*alt) - 58, 3)
    print(f'{deal_weigth = } kg')
    return deal_weigth


# deal_weigth()

# print('\nexercicio 13')
def deal_weigth_womans_mans() -> list[float]:
    """Tendo como dado de entrada a altura (h) de uma pessoa, algoritmo que calcula seu peso ideal, utilizando as seguintes fórmulas com base no biotipo:
    man = (72.7*h) - 58.3
    woman = (62.1*alt) - 44.7, 3

    Returns:
        float: peso ideal para homem e mulher
    """
    alt = float(input('Sua altura: '))
    deal_weigth_man = round((72.7*alt) - 58, 3)
    deal_weigth_woman = round((62.1*alt) - 44.7, 3)
    print([deal_weigth_man, deal_weigth_woman])
    return [deal_weigth_man, deal_weigth_woman]

# deal_weigth_womans_mans()

# print('\nexercicio 14')
def fish_weigth(peso: float) -> str:
    """Algoritmo que recebe um peso de peixes, em kilogramas, e calcula o excesso se for maior que 50 kilos. Para cada kilo excedente deve-se pagar uma multa de R$ 4,00/kg.
    O algoritmo retorna uma string avisando se o pescador pagara multa ou o peso não atingiu os 50 kilos e não precisar pagar multa.

    Args:
        peso (float): peso de peixe fornecido pelo pescador

    Returns:
        str: resposta para o pescador se deve pagar e quanto por cada kilo de peixe excedente a 50 kilos
    """
    if peso <= 50:
        return 'sem excesso de peso'
    else:
        excesso = peso - 50
        multa = round(4*excesso, 2)
        return 'Foram {} kg, o pescador deve pagar uma multa de R$ {}.'.format(round(excesso, 3), multa)

# pprint(fish_weigth(73.155))

# print('\nexercicio 15')
def salario_liquido():
    reais_hora = int(input('quanto voce ganha por hora: '))
    horas_trab = int(input('horas trabalhadas por mês: '))
    salario_bruto = reais_hora*horas_trab
    imptRenda = (11*salario_bruto)/100
    inss = (8*salario_bruto)/100
    sindicato = (5*salario_bruto)/100
    liquido = round(salario_bruto - inss - imptRenda - sindicato, 2)
    print("salario bruto: {} \nimposto de renda:{} \ninss: {} \nsindicato: {} \nsalario liquido: {}".format(salario_bruto, imptRenda, inss, sindicato, liquido))

salario_liquido()
