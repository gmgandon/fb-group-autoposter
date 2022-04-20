import pyautogui
import time
import webbrowser
import random
from pynput.keyboard import Controller

keyboard = Controller()

#group list 
lista = ['24800687503', '257473194355479', '696110120759488', '234680926691981', '178364032707564',  '3172990279434595', '877482505680161', '1592085671006634','1951461934887074', '1573056792984796', '222631315134474', '1624513204522185', '176853886993179', '1687779291539028']

#mi own group for debugging
test = ['2916511921932512']


webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(r"C:\Users\Guido\AppData\Local\Programs\Opera GX\opera.exe"))

pyautogui.hotkey('ctrl','t')

def prueba(lista):
    for grupo in lista:
        print(f'Entrando a https://www.facebook.com/groups/{grupo}/buy_sell_discussion')


def post_grupos(lista):
        print(f'Entrando a grupos')
        for grupo in lista:
            print(f'Entrando a https://www.facebook.com/groups/{grupo}/buy_sell_discussion')
            link = 'https://www.facebook.com/groups/' + grupo + '/buy_sell_discussion'
            webbrowser.get('chrome').open_new(link)
            time.sleep(5)
            pyautogui.hotkey('ctrl','f')
            time.sleep(3)
            keyboard.type('Foto/Video')
            pyautogui.hotkey('ctrl','enter')
            time.sleep(3)
            keyboard.type("""Hola vecinos. ¿Cómo están?\nPasaba a recordarles que estoy dando clases de guitarra, lenguaje y producción musical.\n1hs por semana en mi casa a algunas cuadras de la estación Munro, a domicilio u online.\n\nSe agradece mucho la difusión.\n¡Gracias!""")
            time.sleep(5)
            pyautogui.hotkey('ctrl','f')
            keyboard.type('añadir')
            pyautogui.hotkey('ctrl','enter')

            
            time.sleep(3)

            #flip a coin to change video file
            coin = random.randint(1,10)
            if coin<6:
                keyboard.type(r'"D:\Posts grupos\Flyer stories-01.png" "D:\Posts grupos\vid-blackbird.mp4"')
            elif coin>=6:
                keyboard.type(r'"D:\Posts grupos\Flyer stories-01.png" "D:\Posts grupos\Toe.mp4"')
            pyautogui.hotkey('enter')
            time.sleep(5)
            pyautogui.hotkey('ctrl','f')
            keyboard.type('publicar')
            pyautogui.hotkey('ctrl','enter')

            print('listo')





post_grupos(lista)

