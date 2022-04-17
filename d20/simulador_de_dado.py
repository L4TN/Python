## Dice Simulator
# Simulator of a Dice throw in a table
import random
import threading
import PySimpleGUI as sg
from playsound import playsound
sg.theme('DarkAmber') # Add a touch of color


class SimuladorDeDado:

    #Init is Constructor Method,means an object instance of the class that initializes the attributes of the class.
    #Self refers to object instance of this class.
    # see "https://wiki.python.org.br/SignificadoDoSelf#Classes.2C_fun.2BAOcA9Q-es_e_m.2BAOk-todos"
    def __init__(self):
        #Attribute inicialized with value 1 by Constructor Method
        self.valor_minimo = 1
        #Attribute inicialized with value 20 by Constructor Method
        self.valor_maximo = 20
        
        #Variable Layout receive a text and 2 buttons with text 'sim' and 'não'
        #This layout variable will indicate the form of the window that will be created by PySimpleGUI
        self.layout = [
                [sg.Text('Jogar o dado ?')],
                [sg.Button('sim'), sg.Button('não')]
        ]
    
    #This Method create the window that will be shown by PySimpleGUI 
    def Iniciar(self):
        self.janela = sg.Window('Dice Simulator', layout=self.layout, size=(200, 200))
        self.evento , self.valores = self.janela.Read()
        
        while self.evento == 'sim':
            threading.Thread(target=playsound, args=(['dice.mp3']), daemon=True).start()
            self.GerarValorDoDado()
            self.evento , self.valores = self.janela.Read()
   
        print("Obrigado por jogar !")
    #This Method will be called when the button 'sim' is clicked
    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


    #Faz com que o programa seja executado de modo assincrono, ou seja, não espera a execução do programa para continuar
    def MusicBackGround(self):
        threading.Thread(target=playsound, args=(['soundTES.mp3']), daemon=True).start()



simulador = SimuladorDeDado()
simulador.MusicBackGround()
simulador.Iniciar()

