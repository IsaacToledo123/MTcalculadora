import tkinter as tk

def convertir_a_unos(numero):
    return '1' * numero

def contar_unos(cadena):
    return len(cadena)

def procesar_operacion(operacion):
    try:
        if '+' in operacion:
            numeros = operacion.split('+')
            numeros_unos = [convertir_a_unos(int(n.strip())) for n in numeros]
            resultado = ''.join(numeros_unos)
            return f"Resultado: {contar_unos(resultado)} -> {resultado}"

        elif '-' in operacion:
            numeros = operacion.split('-')
            num1 = convertir_a_unos(int(numeros[0].strip()))
            num2 = convertir_a_unos(int(numeros[1].strip()))
            resta = len(num1) - len(num2)
            resultado = convertir_a_unos(resta) if resta > 0 else '0'
            return f"Resultado: {contar_unos(resultado)} -> {resultado}"

        elif '*' in operacion:
            numeros = operacion.split('*')
            num1 = convertir_a_unos(int(numeros[0].strip()))
            num2 = convertir_a_unos(int(numeros[1].strip()))
            multiplicacion = len(num1) * len(num2)
            resultado = convertir_a_unos(multiplicacion)
            return f"Resultado: {contar_unos(resultado)} -> {resultado}"

        else:
            return "Error: Operación no válida. Usa +, - o *."

    except ValueError:
        return "Error: Ingresa solo números y operadores válidos."

root = tk.Tk()
root.title("Calculadora de Números en 1's")

label_instruccion = tk.Label(root, text="Ingresa la operación (Ej: 4 + 3 + 2):")
label_instruccion.pack(pady=5)

entry_operacion = tk.Entry(root, width=30)
entry_operacion.pack(pady=5)

resultado_label = tk.Label(root, text="Resultado:")
resultado_label.pack(pady=5)

def calcular():
    operacion = entry_operacion.get()
    resultado = procesar_operacion(operacion)
    resultado_label.config(text=resultado)

boton_calcular = tk.Button(root, text="Calcular", command=calcular)
boton_calcular.pack(pady=10)

root.mainloop()
