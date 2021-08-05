import random

class Random():
    def __init__():  
        random.seed()    # inicialização fixa da semente de geração de números aleatórios
        
        set_var = True
        while (set_var == True):
            lim_inf = 1
            lim_sup = 100
            intervalo = (lim_inf, lim_sup)
            rodada = 1
            contador_dica = 0

            numero_sorteado = random.randint(1,100)
            numero = 0
            lim_inf = 1
            lim_sup = 100
            rodada = 1
            contador_dica = 0
            print('Este programa simula um jogo de adivinhação!')
            print(f'Será sorteado um número de {lim_inf} a {lim_sup} e você deverá descobrir qual...!')
            numero = int(input('Qual é o seu palpite? '))

            while(numero<=lim_inf or numero>lim_sup):
                print(f'Palpite inválido! Intervalo: [{lim_inf},{lim_sup}]')
                numero = int(input('Qual é o seu palpite? '))
            while(numero>lim_inf and numero<=lim_sup):
                while(numero != numero_sorteado):
                    if((numero>lim_sup or numero<lim_inf)):
                        print(f'Palpite inválido! Intervalo: [{lim_inf},{lim_sup}]')
                        numero = int(input('Qual é o seu palpite? '))

                    if(numero_sorteado<numero):
                        lim_sup = numero-1
                        intervalo == (lim_inf, lim_sup)
                        contador_dica = contador_dica+1
                        rodada = rodada+1
                        print(f'Dica numero {contador_dica}: o número sorteado é menor que {numero}' %(contador_dica, numero))
                        numero = int(input(f'Qual é o seu palpite? [INTERVALO: {lim_inf}, {lim_sup}] : \n'))

                    elif(numero_sorteado>numero):
                        lim_inf = numero+1
                        intervalo == (lim_inf, lim_sup)
                        contador_dica = contador_dica+1
                        rodada = rodada+1
                        print(f'Dica numero {contador_dica}: o número sorteado é maior que {numero}')
                        numero = int(input(f'Qual é o seu palpite? [INTERVALO: {lim_inf}, {lim_sup}] : \n'))

                if(numero == numero_sorteado):
                    print(f'Número sorteado= {numero_sorteado}')
                    print(f'Você acertou na {rodada} a tentativa')
                    reset = str(input('Deseja jogar de novo? (S/n)').upper())


                if (reset=='SIM' or reset=='S'):
                    set_var = True
                else:
                    set_var = False

if __name__ == '__main__':
    Random.__init__()	   
