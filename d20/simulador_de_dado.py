#Simulador de dado
import random
import PySimpleGUI as sg

class SimuladorDeDado:

    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 20
        
        self.layout = [
                [sg.Text('Jogar o dado ?')],
                [sg.Button('sim'), sg.Button('não')]
        ]
    

    def Iniciar(self):
        self.janela = sg.Window('Simulador de dado', layout=self.layout)
        self.evento , self.valores = self.janela.Read()

        
        try:
            if self.evento == 'sim' or self.evento == 's':
                        self.GerarValorDoDado() 
            elif self.evento == 'não' or self.evento == 'n':
                        print('Agradecemos a sua participação')
            else:
                    print('Opção inválida,favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')



    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()
