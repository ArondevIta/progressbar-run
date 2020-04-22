import PySimpleGUI as sg
import os
from random import randint

casas = 0
jogador1 = True
jogador2 = False
nome_jogador1 = 'Aron'
nome_jogador2 = 'Saulo'
aceleracao: int = 0
total1: int = 0
total2: int = 0
comecou = True

layout = [[sg.Text('Corrida maluca')],
          [sg.ProgressBar(40, orientation='h', size=(50, 50), key='progbar1'), sg.Button('acelerar')],
          [sg.ProgressBar(40, orientation='h', size=(50, 50), key='progbar2'), sg.Button('acelerar')],
          [sg.Cancel()]]

window = sg.Window('Corrida maluca', layout)

while comecou:
    if jogador1:
        aceleracao = randint(1, 6)
        total1 += aceleracao
        jogador1 = False
        jogador2 = True
        os.system('cls')
        event, values = window.read(timeout=0)
        if event == 'Cancel' or event is None:
            break
            # update bar with loop value +1 so that bar eventually reaches the maximum
        window['progbar1'].update_bar(total1)
        print(nome_jogador1, 'Voce acelerou ', aceleracao, ' seu total é de: ', total1)

        if total1 >= 40:
            print('jogador ' + nome_jogador1 + ' ganhou')
            print(total1)

            comecou = False

    elif jogador2:
        aceleracao = randint(1, 6)
        jogador2 = False
        jogador1 = True
        total2 += aceleracao
        os.system('cls')
        event, values = window.read(timeout=0)
        if event == 'Cancel' or event is None:
            break
            # update bar with loop value +1 so that bar eventually reaches the maximum
        window['progbar2'].update_bar(total2)
        print(nome_jogador2, 'Voce acelerou ', aceleracao, ' seu total é de: ', total2)
        if total2 >= 40:
            print('jogador ' + nome_jogador2 + ' ganhou')
            print(total2)

            comecou = False

