import tkinter as tk
import math

# Función principal para la lógica de la calculadora
def calculadora():
   
    #Esta función crea la ventana de la calculadora y maneja su lógica.
    
    
    # Esta variable global almacena la expresión que se está construyendo
    global expresion_actual
    expresion_actual = ""

    def clic_boton(simbolo):
      
        #Maneja los clics en los botones de números y operadores.
        
        global expresion_actual
        if simbolo == "=":
            try:
                # Usa eval() para calcular el resultado de la expresión
                resultado = str(eval(expresion_actual))
                entrada_texto.delete(0, tk.END)
                entrada_texto.insert(0, resultado)
                expresion_actual = resultado
            except:
                entrada_texto.delete(0, tk.END)
                entrada_texto.insert(0, "Error")
                expresion_actual = ""
        elif simbolo == "C":
            # Borra la pantalla y reinicia la expresión
            expresion_actual = ""
            entrada_texto.delete(0, tk.END)
        elif simbolo == "sqrt":
            try:
                # Calcula la raíz cuadrada del número actual
                valor = float(expresion_actual)
                resultado = str(math.sqrt(valor))
                entrada_texto.delete(0, tk.END)
                entrada_texto.insert(0, resultado)
                expresion_actual = resultado
            except:
                entrada_texto.delete(0, tk.END)
                entrada_texto.insert(0, "Error")
                expresion_actual = ""
        elif simbolo == "%":
            try:
                # Calcula el porcentaje del número actual (ej. 50% = 0.5)
                valor = float(expresion_actual)
                resultado = str(valor / 100)
                entrada_texto.delete(0, tk.END)
                entrada_texto.insert(0, resultado)
                expresion_actual = resultado
            except:
                entrada_texto.delete(0, tk.END)
                entrada_texto.insert(0, "Error")
                expresion_actual = ""
        else:
            # Agrega el símbolo al final de la expresión
            expresion_actual += str(simbolo)
            entrada_texto.delete(0, tk.END)
            entrada_texto.insert(0, expresion_actual)

    # Configuración de la ventana principal
    ventana = tk.Tk()
    ventana.title("Calculadora Básica")
    ventana.geometry("350x510")
    ventana.resizable(0, 0) # Deshabilita el redimensionamiento de la ventana

    # Pantalla de entrada de texto
    entrada_texto = tk.Entry(ventana, width=20, borderwidth=5, font=("Arial", 20))
    entrada_texto.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Definición de los botones
    botones = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ('C', 5, 0), ('sqrt', 5, 1), ('%', 5, 2)
    ]
    
    # Creación y posicionamiento de los botones en la cuadrícula
    for (texto, fila, columna) in botones:
        boton = tk.Button(ventana, text=texto, padx=20, pady=20, command=lambda t=texto: clic_boton(t), font=("Arial", 15))
        boton.grid(row=fila, column=columna, padx=5, pady=5)
    
    # Bucle principal de la aplicación
    ventana.mainloop()

# Ejecuta la función principal
if __name__ == "__main__":
    calculadora()