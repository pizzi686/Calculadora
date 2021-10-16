from tkinter import Event

ac=int()
first=int()
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import T, WIDTH_LOCALS, WINDOW_CLOSED, Button
sg.theme('Red')
#sg.InputText(size=(10,500)) 
print("hola")

Layout=[  

    [sg.Text("                                              ",text_color="black",background_color="white",key="pantalla")],
    [sg.Button("7",size=(4,4),key="seven"),sg.Button("8",size=(4,4),key="eight"),sg.Button("9",size=(4,4),key="nine"),sg.Button("x",size=(4,4),key="por")],
    [sg.Button("4",size=(4,4),key="four"),sg.Button("5",size=(4,4),key="five"),sg.Button("6",size=(4,4),key="six"),sg.Button("+",size=(4,4),key="mas")],
    [sg.Button("1",size=(4,4),key="one"),sg.Button("2",size=(4,4),key="two"),sg.Button("3",size=(4,4),key="tree"),sg.Button("/",size=(4,4),key="div")],
    [sg.Button("C", size=(4,4),key="reset"), sg.Button("0",size=(4,4),key="zero"),sg.Button("=",size=(4,4),key="igual"),sg.Button("-",size=(4,4),key="menos")],
    
    
    [sg.Text("v1.0")]
    
    ]
#ver como realizar la op matematica guardada en el string 

operacion=""
window=sg.Window("calcu",Layout,size=(300,400))
while True:
    event, values = window.read()   
    if event==WINDOW_CLOSED:
        break
    if event=="one":
            operacion=operacion+"1"
            window["pantalla"].update(operacion)
    if event=="two":
            operacion=operacion+"2"
            window["pantalla"].update(operacion)
    if event=="tree":
            window["pantalla"].update(operacion)
            operacion=operacion+"3"
    if event=="four":
            operacion=operacion+"4"
            window["pantalla"].update(operacion)
    if event=="five":
            operacion=operacion+"5"
            window["pantalla"].update(operacion)
    if event=="six":
            operacion=operacion+"6"
            window["pantalla"].update(operacion)
    if event=="seven":
            operacion=operacion+"7"
            window["pantalla"].update(operacion)
    if event=="eight":
            operacion=operacion+"8"
            window["pantalla"].update(operacion)
    if event=="nine":
            operacion=operacion+"9"
            window["pantalla"].update(operacion)
    if event=="zero":
            operacion=operacion+"0"
            window["pantalla"].update(operacion)
    if event=="reset":
            operacion=""
            window["pantalla"].update(operacion)
    
    if event=="mas":
        operacion=operacion+"+"
        window["pantalla"].update(operacion)    

    if event=="menos":
        
        operacion=operacion+"-"
        window["pantalla"].update(operacion)
       
        
        
    if event=="por":
       
        operacion=operacion+"*"
        window["pantalla"].update(operacion)
        
    if event=="div":
       
        operacion=operacion+"/"
        window["pantalla"].update(operacion)    
        

    if event=="igual":
        operadores=["-","+","/","*"]
        if operacion!="":
                if  (operacion[len(operacion)-1]) in operadores:
                        print("si")
                        window["pantalla"].update("error")
                        operacion=""
                else:
                        print("no")
                        window["pantalla"].update(str(eval(operacion)))
                        operacion=str(eval(operacion))
        else:
                window["pantalla"].update("") 
        
       
        