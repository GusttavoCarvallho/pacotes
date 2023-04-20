while True:
    try:
        numero =int(input('entre com um um nimero:'))
        print(5/numero)
        break
    except ValueError:
        print('valor errado')
    except ZeroDivisionError:
        print('Desculpe nao posso dividir oor 0')
    except:
        print('nao sei o fazer...') 