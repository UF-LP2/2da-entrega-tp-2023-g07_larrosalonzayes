from tkinter import *
from tkinter import PhotoImage
ventana = Tk()
ventana.geometry('500x600') # tamanyo en pixeles de la ventana
ventana.config(bg='grey') #asigno fondo blanco a la ventana
ventana.title('tp lp2')
etiqueta= Label(ventana, text='Hospital Favaloro', fg='white', bg='grey', font='Verdana')
etiqueta.place(x=180, y= 10)
#img=PhotoImage(file='logo.png')
#Label=(ventana,Image=imagen)
#lbl=(ventana, image= img)

boton= Button(ventana, text='Mostrar sala de espera', fg='black', font='Verdana')
boton2= Button(ventana, text='Riesgo vital',bg='red', fg='white', font='Verdana')
boton3= Button(ventana, text='Urgencia alta', bg='orange', fg='black',font='Verdana')
boton4= Button(ventana, text='Urgencia Media', bg='yellow', fg='black',font='Verdana')
boton5= Button(ventana, text='Normal', bg='green',fg='white', font='Verdana')
boton6= Button(ventana, text='No urgente', bg='blue', fg='white',font='Verdana')
              
              
#ubicacion de los botones 
boton.place(x=50, y= 70)
boton2.place(x= 50, y= 120 )
boton3.place(x= 50, y= 170 )
boton4.place(x= 50, y= 220 )
boton5.place(x= 50, y= 270 )
boton6.place(x= 50, y= 320 )

ventana.mainloop() # método que mantiene 24/7 activa a la ventana