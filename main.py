from tkinter import Tk, Button, Entry
 
# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("500x250")  # Tamaño de la ventana

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=0)   #pady, columspan is

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_1.grid(row=1, column=0, padx=1, pady=1)  #column=***, pady=***
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_2.grid(row=1, column=1, padx=1, pady=1) #row=***, column=***, padx=***
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_3.grid(row=1, column=2, padx=1, pady=1) #column=***, padx=***
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_4.grid(row=2, column=0, padx=1, pady=1) #row=***, column=***, pady=***
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_5.grid(row=2, column=1, padx=1, pady=1) #row=***, padx=***, pady=***
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_6.grid(row=2, column=2, padx=1, pady=1) #column=***, padx=***
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_7.grid(row=3, column=0, padx=1, pady=1) #row=***, column=***, pady=***
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_8.grid(row=3, column=1, padx=1, pady=1) #row=***, column=***, pady=1
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_9.grid(row=3, column=2, padx=1, pady=1) #padx=***, pady=***
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2")
boton_igual.grid(row=4, column=0, columnspan=2, padx=1, pady=1) #column=***, columnspan=***, 
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0)
boton_punto.grid(row=4, column=2, padx=1, pady=1) #row=***, column=***
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_mas.grid(row=1, column=3, padx=1, pady=1) #column=***, padx=***
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_menos.grid(row=2, column=3, padx=1, pady=1) #row=***
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_multiplicacion.grid(row=3, column=3, padx=1, pady=1) #row=***, column=***
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_division.grid(row=4, column=3, padx=1, pady=1) #row=***, column=***, pady=***

root.mainloop()

#Funciones para los botones

def ingresar_valor(evento):
    pantalla.insert(len(pantalla.get()), evento.widget["text"]) #evento.widget["text"] es el texto del botón que se presionó
    print(pantalla.get())
    
def obtenerResultado(evento):
    try:
        resultado = eval(pantalla.get()) #eval() evalúa la expresión matemática
        pantalla.delete(0, len(pantalla.get())) #Borrar el contenido de la pantalla
        pantalla.insert(0, resultado) #Mostrar el resultado en la pantalla
    except:
        pantalla.delete(0, len(pantalla.get())) #Borrar el contenido de la pantalla
        pantalla.insert(0, "Error") #Mostrar "Error" en la pantalla
        
def limpiar_pantalla(evento):
    pantalla.delete(0, len(pantalla.get())) #Borrar el contenido de la pantalla
    
    
#Asociar los botones con las funciones
    
boton_1.bind("<Button-1>", ingresar_valor) #<Button-1> es el evento de clic izquierdo
boton_2.bind("<Button-1>", ingresar_valor)
boton_3.bind("<Button-1>", ingresar_valor)
boton_4.bind("<Button-1>", ingresar_valor)
boton_5.bind("<Button-1>", ingresar_valor)
boton_6.bind("<Button-1>", ingresar_valor)
boton_7.bind("<Button-1>", ingresar_valor)
boton_8.bind("<Button-1>", ingresar_valor)
boton_9.bind("<Button-1>", ingresar_valor)
boton_punto.bind("<Button-1>", ingresar_valor)
boton_mas.bind("<Button-1>", ingresar_valor)
boton_menos.bind("<Button-1>", ingresar_valor)
boton_multiplicacion.bind("<Button-1>", ingresar_valor)
boton_division.bind("<Button-1>", ingresar_valor)

boton_igual.bind("<Button-1>", obtenerResultado)

#No me deja agregar el valor de los botones que presiono en la pantalla
#No me deja obtener el resultado de la operación