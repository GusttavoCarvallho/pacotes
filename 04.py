while True:
    try:
        numero =int(input('entre com um numero inteiro'))
        print(5/numero)
        break
    except(ValueError,ZeroDivisionError):
        print('Valor errado ou nao é possiveldividir por zero')
    except:
        print('Desculpe ,algo errado aconteceu...')
        