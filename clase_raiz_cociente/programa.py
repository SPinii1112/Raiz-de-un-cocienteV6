# -*- coding: utf-8 -*-
"""
Programa interactivo de Matematica para 7mo Grado
Tema: Propiedad de la radicacion - Raiz de un Cociente
"""

import sys
from fractions import Fraction

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stdin.reconfigure(encoding="utf-8")
    except Exception:
        pass

# 20 ejercicios que incluyen raices cubicas negativas con resultados lindos
EJERCICIOS = [
    {"index": 2, "num": 1,   "den": 4,   "ans": Fraction(1, 2),   "is_neg": False},
    {"index": 2, "num": 9,   "den": 16,  "ans": Fraction(3, 4),   "is_neg": False},
    {"index": 3, "num": 1,   "den": 8,   "ans": Fraction(-1, 2),  "is_neg": True},   # 3V(-1/8) = -1/2
    {"index": 2, "num": 1,   "den": 9,   "ans": Fraction(1, 3),   "is_neg": False},
    {"index": 2, "num": 16,  "den": 25,  "ans": Fraction(4, 5),   "is_neg": False},
    {"index": 3, "num": 8,   "den": 27,  "ans": Fraction(-2, 3),  "is_neg": True},   # 3V(-8/27) = -2/3
    {"index": 2, "num": 49,  "den": 64,  "ans": Fraction(7, 8),   "is_neg": False},
    {"index": 2, "num": 4,   "den": 25,  "ans": Fraction(2, 5),   "is_neg": False},
    {"index": 3, "num": 27,  "den": 64,  "ans": Fraction(-3, 4),  "is_neg": True},   # 3V(-27/64) = -3/4
    {"index": 2, "num": 81,  "den": 100, "ans": Fraction(9, 10),  "is_neg": False},
    {"index": 3, "num": 1,   "den": 8,   "ans": Fraction(1, 2),   "is_neg": False},
    {"index": 3, "num": 8,   "den": 27,  "ans": Fraction(2, 3),   "is_neg": False},
    {"index": 3, "num": 1,   "den": 125, "ans": Fraction(-1, 5),  "is_neg": True},   # 3V(-1/125) = -1/5
    {"index": 2, "num": 25,  "den": 49,  "ans": Fraction(5, 7),   "is_neg": False},
    {"index": 3, "num": 64,  "den": 125, "ans": Fraction(-4, 5),  "is_neg": True},   # 3V(-64/125) = -4/5
    {"index": 2, "num": 100, "den": 9,   "ans": Fraction(10, 3),  "is_neg": False},
    {"index": 2, "num": 121, "den": 144, "ans": Fraction(11, 12), "is_neg": False},
    {"index": 2, "num": 64,  "den": 4,   "ans": Fraction(4, 1),   "is_neg": False},
    {"index": 2, "num": 1,   "den": 36,  "ans": Fraction(1, 6),   "is_neg": False},
    {"index": 3, "num": 1,   "den": 27,  "ans": Fraction(-1, 3),  "is_neg": True},   # 3V(-1/27) = -1/3
]

def mostrar_teoria():
    print("\n" + "="*65)
    print("  [1] TEORIA: PROPIEDAD DE LA RAIZ DE UN COCIENTE (7mo GRADO)")
    print("="*65)
    print("Formula general:")
    print("      n ________       n ____")
    print("       /   a            / a  ")
    print("      /  -----   =   ------- ")
    print("    \\/     b           n ____")
    print("                        / b  ")
    print("                      \\/     ")
    print("\nConjuntos numericos a los que pertenecen:")
    print("-> a pertenece a Z (numeros enteros).")
    print("-> b pertenece a Z - {0} (numeros enteros excluyendo el 0).")
    print("-> n pertenece a N (numeros naturales, con n >= 2).")
    print("\nNota:")
    print("- Si n es par, el radicando debe ser no negativo (a/b >= 0).")
    print("- Si n es impar, el radicando puede ser positivo o negativo.")
    print("="*65 + "\n")

def mostrar_ejemplos():
    print("\n" + "="*65)
    print("  [2] TRES EJEMPLOS PASO A PASO (Numeros en Q y resultados lindos)")
    print("="*65)
    print("\nEJEMPLO 1: Raiz cuadrada de una fraccion")
    print("    ______")
    print("   /  4       V4     2")
    print("  /  ---  =  ---- = ---")
    print(" \\/   9       V9     3")
    print("  Paso 1: Repartimos la raiz: V4 en el numerador y V9 en el denominador.")
    print("  Paso 2: Calculamos V4 = 2 (porque 2 x 2 = 4).")
    print("  Paso 3: Calculamos V9 = 3 (porque 3 x 3 = 9).")
    print("  Resultado: 2/3 (dos tercios).")

    print("\nEJEMPLO 2: Raiz cubica de una fraccion positiva")
    print("   3 ______")
    print("    /  8      3V8     2")
    print("   / ---- =  ----- = ---")
    print(" \\/   27      3V27    3")
    print("  Paso 1: Repartimos la raiz cubica al numerador 8 y al denominador 27.")
    print("  Paso 2: La raiz cubica de 8 es 2 (porque 2 x 2 x 2 = 8).")
    print("  Paso 3: La raiz cubica de 27 es 3 (porque 3 x 3 x 3 = 27).")
    print("  Resultado: 2/3 (dos tercios).")

    print("\nEJEMPLO 3: Raiz cubica de una fraccion negativa")
    print("   3 ________")
    print("    /   8       3V(-8)     -2        2")
    print("   / - ---- =  -------- = ---- = - ---")
    print(" \\/     27       3V27       3        3")
    print("  Paso 1: Repartimos la raiz cubica: 3V(-8) en el numerador y 3V27 en el denominador.")
    print("  Paso 2: La raiz cubica de -8 es -2 (porque (-2) x (-2) x (-2) = -8).")
    print("  Paso 3: La raiz cubica de 27 es 3 (porque 3 x 3 x 3 = 27).")
    print("  Resultado: -2/3 (menos dos tercios).")
    print("="*65 + "\n")

def format_radicando(index, num, den, is_neg):
    prefix = "-" if is_neg else ""
    if index == 2:
        return f"V({prefix}{num}/{den})"
    else:
        return f"3V({prefix}{num}/{den})"

def parse_respuesta(texto):
    texto = texto.strip().replace(" ", "")
    if not texto:
        return None
    try:
        if "/" in texto:
            partes = texto.split("/")
            if len(partes) != 2:
                return None
            n = int(partes[0])
            d = int(partes[1])
            if d == 0:
                return None
            return Fraction(n, d)
        else:
            return Fraction(int(texto), 1)
    except ValueError:
        return None

def iniciar_ejercicios():
    print("\n" + "="*65)
    print("  [3] PRACTICA: 20 EJERCICIOS INTERACTIVOS")
    print("="*65)
    print("Instrucciones:")
    print("- Escribe tu respuesta como fraccion (ejemplo: 2/3 o -2/3)")
    print("- O como numero entero si corresponde (ejemplo: 4 o -2)")
    print("- Escribe 'salir' para volver al menu principal.")
    print("="*65 + "\n")

    total = len(EJERCICIOS)

    for i, ej in enumerate(EJERCICIOS, 1):
        exp = format_radicando(ej["index"], ej["num"], ej["den"], ej["is_neg"])
        print(f"\n--- Ejercicio {i} de {total} ---")
        
        while True:
            try:
                resp_str = input(f"Calcula:  {exp} = ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nOperacion cancelada.")
                return

            if resp_str.lower() in ["salir", "exit", "q"]:
                print("\nRegresando al menu principal...")
                return

            parsed = parse_respuesta(resp_str)
            if parsed is None:
                print("[!] Formato no valido. Escribe una fraccion (ej: 3/4 o -2/3) o un entero (ej: 2 o -1).")
                continue

            if parsed == ej["ans"]:
                print(">>> [CORRECTO] !Esta muy bien! Excelente trabajo.")
                break
            else:
                print(">>> [INCORRECTO] Esta mal. !Intenta otra vez! Revisa tus cuentas.")

    print("\n" + "*"*65)
    print(f"FELICITACIONES: Has completado los {total} ejercicios exitosamente.")
    print("*"*65 + "\n")

def menu():
    while True:
        print("\n" + "="*45)
        print("  CLASE DE MATEMATICA: RAIZ DE UN COCIENTE")
        print("="*45)
        print("1. Ver explicacion teorica")
        print("2. Ver los 3 ejemplos paso a paso")
        print("3. Resolver los 20 ejercicios interactivos")
        print("4. Salir")
        print("-" * 45)
        try:
            opcion = input("Elige una opcion (1-4): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nHasta luego.")
            break

        if opcion == "1":
            mostrar_teoria()
            try:
                input("Presiona Enter para continuar...")
            except (EOFError, KeyboardInterrupt):
                pass
        elif opcion == "2":
            mostrar_ejemplos()
            try:
                input("Presiona Enter para continuar...")
            except (EOFError, KeyboardInterrupt):
                pass
        elif opcion == "3":
            iniciar_ejercicios()
        elif opcion == "4":
            print("\n!Muchos exitos en tu clase del miercoles! Hasta luego.\n")
            break
        else:
            print("Opcion no valida. Por favor ingresa 1, 2, 3 o 4.")

if __name__ == "__main__":
    menu()
