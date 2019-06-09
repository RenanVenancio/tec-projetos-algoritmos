sair = False
nrTetse = 0
while sair == False:

    entradaValida = False
    while entradaValida == False:

        maxCarac = int(input('Quantidade de caracteres do cartão->'))
        qtdFrases = int(input('Quantidade de frases->'))
        if(maxCarac >= 8 and maxCarac <=1000) and (qtdFrases >= 1 and qtdFrases <=50):
            entradaValida = True
        else:
            print('Entradas inválidas\n C precisa ser >= 8 e <= 1000\n F precisa ser > 1 e <=50\n TENTE NOVAMENTE!')



    frDados = []
    for i in range(qtdFrases):
        print(8 * '*' + 'FRASE ' + str(i+1) + 8 * '*')

        dadosValidos = False
        while dadosValidos == False:

            numCaracteres = int(input('Quantidade de caracteres da frase: '))
            numExp = int(input('Quantidade de expressões: '))

            if(numCaracteres >= 8 and numCaracteres <= 200) and (numExp >= 1 and numExp <=25):
                dadosValidos = True
                frDados.append([numCaracteres, numExp])
            else:
                print('Entradas inválidas\n A Quantidade de caracteres da frase precisa ser >= 8 e <= 200\n Quantidade de expressões precisa ser > 1 e <=25\n TENTE NOVAMENTE!')

        print(23 * '*')

    def estrategiaGulosa(dados):
        caracteres = maxCarac
        solucao = 0
        parar = False
        maior = 0
        maiorIndex = -1

        while parar == False:

            for i in range(len(dados)):
                if(dados[i][1] > maior):
                    maior = dados[i][1]
                    maiorIndex = [i][0]
                    maiorCacteres = dados[i][0]

            if(maiorIndex > -1):
                del(dados[maiorIndex])
                maiorIndex = -1


            if(caracteres - maiorCacteres) >= 0:
                caracteres -= maiorCacteres
                solucao += maior
                maior = 0
            else:
                parar = True

        return solucao

    nrTetse += 1


    print('Teste ' + str(nrTetse))
    print('Solução Gulosa: ' + str(estrategiaGulosa(frDados)) + '\n')