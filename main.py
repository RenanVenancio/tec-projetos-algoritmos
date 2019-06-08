comp = int(input('Digite o comprimento do cartão em caracateres: '))
if(comp >= 8 and comp <=1000):
    print('ok')
else:
    print('Tam invalido')

#Pegando a quantidade de frases
frColetadas = int(input('Quantidade de frases coletadas: '))

frDados = []
for i in range(frColetadas):
    print(8 * '*' + 'FRASE ' + str(i+1) + 8 * '*')
    numCaracteres = int(input('Quantidade de caracteres da frase: '))
    numExp = int(input('Quantidade de expressões: '))
    frDados.append(list([numCaracteres, numExp]))
    print(20 * '*')


for i in frDados:
    print(str(i[0]) + '|' + str(i[0]))