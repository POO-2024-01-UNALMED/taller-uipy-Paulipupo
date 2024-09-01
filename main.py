from tkinter import Tk, Button, Entry
 
# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("300x250")  # Tamaño de la ventana

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=100, padx=1, pady=0)   #pady, columspan es 100 para que se viera bien en pantalla, pero no tengo claro porque se tuesta si no

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

#Funciones para los botones

operacionTerminada = False #Esto es para saber si la operación ya terminó, para poder borrar la pantalla si se presiona un número después de obtener el resultado

def ingresar_valor(evento):
    global operacionTerminada
    if operacionTerminada == True:
        pantalla.delete(0, len(pantalla.get())) #Borrar el contenido de la pantalla
    pantalla.insert(len(pantalla.get()), evento.widget["text"]) #evento.widget["text"] es el texto del botón que se presionó
    operacionTerminada = False
    
def obtenerResultado(evento):
    global operacionTerminada
    try:
        resultado = eval(pantalla.get()) #eval() evalúa la expresión matemática, porque no explicaron esto claro en clase y me tocó investigar la librería
        pantalla.delete(0, len(pantalla.get())) #Borrar el contenido de la pantalla
        pantalla.insert(0, resultado) #Mostrar el resultado en la pantalla
        operacionTerminada = True
    except:
        pantalla.delete(0, len(pantalla.get())) #Borrar el contenido de la pantalla
        pantalla.insert(0, "Error") #Mostrar "Error" en la pantalla
        operacionTerminada = True
    
    
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


root.mainloop()
#Pude hacer que se limpie la pantalla si no hay operaciones pendientes, o después de obtener el resultado
#o si se presiona un número después de obtener el resultado
#o si se presiona un operador después de obtener el resultado
#o si hay un error
#o si se presiona un número después de un error