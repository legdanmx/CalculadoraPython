# Calculadora Básica en Python 

Esta es una calculadora de escritorio simple desarrollada con Python, que te permite realizar operaciones aritméticas básicas como suma, resta, multiplicación, división, porcentaje y raíz cuadrada.

---

###  Tecnologías

* **Python**
* Librería **tkinter** para la interfaz gráfica.
* Librería **math** para funciones matemáticas.

---

###  Características Principales

* **Librerías:** El proyecto importa `tkinter` (con el alias `tk`) para crear la interfaz gráfica y la librería `math` para utilizar la función de raíz cuadrada (`math.sqrt`).
* **Variable Global:** La variable `expresion_actual` almacena la cadena de caracteres de la operación que el usuario está construyendo, por ejemplo: `"10+5"`.
* **Manejo de Lógica:** La función `clic_boton(simbolo)` es el núcleo de la aplicación. Se ejecuta cada vez que se presiona un botón.
* **Función `eval()`:** Esta función integrada de Python evalúa una cadena de texto como si fuera una expresión matemática, lo que simplifica enormemente la lógica de cálculo. Por ejemplo, `eval("10+5")` retorna `15`.
* **Manejo de Errores:** Se implementa un bloque `try...except` para capturar y gestionar errores, como la división por cero, lo que previene que la aplicación se cierre inesperadamente y muestra un mensaje de "Error" en pantalla.

---

###  Instalación

#### Opción A: Ejecutable

1.  Dirígete a la carpeta `dist`.
2.  Ejecuta el archivo `Calculadora.exe`.

#### Opción B: Código Fuente

1.  Asegúrate de tener **Python** instalado en tu sistema.
2.  Abre el archivo `main.py` en tu editor de código preferido.

**Nota:** Si necesitas ayuda para configurar tu entorno, se incluye una guía para instalar y configurar **VS Code** (IDE) y **Python** (intérprete) [aquí](https://rodokizzzdev.com/archivos/Instalación%20y%20Config%20VSCyPython.pdf).

---

###  Uso

La interfaz de la calculadora es intuitiva. Simplemente haz clic en los botones para construir tu operación:
1.  Haz clic en los **dígitos** (`0-9`) para escribir un número.
2.  Haz clic en el **botón de punto** (`.`) para usar decimales.
3.  Selecciona un **operador** (`+`, `-`, `*`, `/`, `%`, `sqrt`) para realizar una operación.
4.  Usa el **botón "C"** para limpiar la pantalla.
5.  Finalmente, presiona el **botón de igual (`=`)** para obtener el resultado.

---

###  Contribuciones

¡Las contribuciones son bienvenidas! Si deseas ayudar a mejorar este proyecto, por favor sigue los siguientes pasos:

1.  **Haz un *fork*** del repositorio.
2.  **Clona tu *fork*** a tu máquina local:
    ```bash
    git clone [https://github.com/rodokizzzdev/calculadoraPython.git](https://github.com/rodokizzzdev/calculadoraPython.git)
    ```
3.  **Crea una nueva rama** para tus cambios:
    ```bash
    git checkout -b nombre-de-tu-rama
    ```
4.  **Haz tus cambios y haz *commit***:
    ```bash
    git add .
    git commit -m "Descripción clara de tus cambios"
    ```
5.  **Envía los cambios** a tu *fork* en GitHub:
    ```bash
    git push origin nombre-de-tu-rama
    ```
6.  **Abre un *pull request*** hacia la rama `main` del repositorio original, explicando tus cambios.

Revisaré tu *pull request* tan pronto como sea posible. ¡Gracias por tu interés en mejorar este proyecto!

---

###  Licencia

Este proyecto está bajo la Licencia **MIT**.
