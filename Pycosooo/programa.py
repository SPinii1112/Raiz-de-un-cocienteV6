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

EJERCICIOS = [
    {"index": 2, "num": 1,   "den": 4,   "ans": Fraction(1, 2)},
    {"index": 2, "num": 9,   "den": 16,  "ans": Fraction(3, 4)},
    {"index": 2, "num": 25,  "den": 49,  "ans": Fraction(5, 7)},
    {"index": 2, "num": 1,   "den": 9,   "ans": Fraction(1, 3)},
    {"index": 2, "num": 16,  "den": 25,  "ans": Fraction(4, 5)},
    {"index": 2, "num": 36,  "den": 81,  "ans": Fraction(2, 3)},
    {"index": 2, "num": 49,  "den": 64,  "ans": Fraction(7, 8)},
    {"index": 2, "num": 4,   "den": 25,  "ans": Fraction(2, 5)},
    {"index": 2, "num": 9,   "den": 100, "ans": Fraction(3, 10)},
    {"index": 2, "num": 81,  "den": 100, "ans": Fraction(9, 10)},
    {"index": 3, "num": 1,   "den": 8,   "ans": Fraction(1, 2)},
    {"index": 3, "num": 8,   "den": 27,  "ans": Fraction(2, 3)},
    {"index": 3, "num": 27,  "den": 64,  "ans": Fraction(3, 4)},
    {"index": 3, "num": 1,   "den": 125, "ans": Fraction(1, 5)},
    {"index": 3, "num": 64,  "den": 125, "ans": Fraction(4, 5)},
    {"index": 2, "num": 100, "den": 9,   "ans": Fraction(10, 3)},
    {"index": 2, "num": 121, "den": 144, "ans": Fraction(11, 12)},
    {"index": 2, "num": 64,  "den": 4,   "ans": Fraction(4, 1)},
    {"index": 2, "num": 1,   "den": 36,  "ans": Fraction(1, 6)},
    {"index": 3, "num": 1,   "den": 27,  "ans": Fraction(1, 3)},
]

def mostrar_teoria():
    print("\n" + "="*60)
    print("  [1] TEORIA: PROPIEDAD DE LA RAIZ DE UN COCIENTE (7mo GRADO)")
    print("="*60)
    print("Un 'cociente' es una division o, lo que es lo mismo, una fraccion.")
    print("\nFormula general:")
    print("      n ________       n ____")
    print("       /   a            / a  ")
    print("      /  -----   =   ------- ")
    print("    \\/     b           n ____")
    print("                        / b  ")
    print("                      \\/     ")
    print("                      (con b distinto de 0)")
    print("\nEn palabras sencillas:")
    print("-> Arriba: la raiz del numerador va arriba.")
    print("-> Abajo: la raiz del denominador va abajo.")
    print("="*60 + "\n")

def mostrar_ejemplos():
    print("\n" + "="*60)
    print("  [2] TRES EJEMPLOS PASO A PASO (Numeros en Q y resultados lindos)")
    print("="*60)
    print("\nEJEMPLO 1: Raiz cuadrada de una fraccion")
    print("    ______")
    print("   /  4       V4     2")
    print("  /  ---  =  ---- = ---")
    print(" \\/   9       V9     3")
    print("  Paso 1: Repartimos la raiz: V4 en el numerador y V9 en el denominador.")
    print("  Paso 2: Calculamos V4 = 2 (porque 2 x 2 = 4).")
    print("  Paso 3: Calculamos V9 = 3 (porque 3 x 3 = 9).")
    print("  Resultado: 2/3 (dos tercios).")

    print("\nEJEMPLO 2: Raiz cubica de una fraccion")
    print("   3 ______")
    print("    /  8      3V8     2")
    print("   / ---- =  ----- = ---")
    print(" \\/   27      3V27    3")
    print("  Paso 1: Repartimos la raiz cubica al 8 y al 27.")
    print("  Paso 2: La raiz cubica de 8 es 2 (porque 2 x 2 x 2 = 8).")
    print("  Paso 3: La raiz cubica de 27 es 3 (porque 3 x 3 x 3 = 27).")
    print("  Resultado: 2/3 (dos tercios).")

    print("\nEJEMPLO 3: Raiz cuadrada con numeros mayores")
    print("    _______")
    print("   /  25      V25     5")
    print("  /  ----  =  ---  = ---")
    print(" \\/   36      V36     6")
    print("  Paso 1: Distribuimos la raiz: V25 arriba y V36 abajo.")
    print("  Paso 2: V25 = 5 (5 x 5 = 25).")
    print("  Paso 3: V36 = 6 (6 x 6 = 36).")
    print("  Resultado: 5/6 (cinco sextos).")
    print("="*60 + "\n")

def format_radicando(index, num, den):
    if index == 2:
        return f"V({num}/{den})"
    else:
        return f"3V({num}/{den})"

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
    print("\n" + "="*60)
    print("  [3] PRACTICA: 20 EJERCICIOS INTERACTIVOS")
    print("="*60)
    print("Instrucciones:")
    print("- Escribe tu respuesta como fraccion (ejemplo: 2/3)")
    print("- O como numero entero si corresponde (ejemplo: 4)")
    print("- Escribe 'salir' para volver al menu principal.")
    print("="*60 + "\n")

    total = len(EJERCICIOS)

    for i, ej in enumerate(EJERCICIOS, 1):
        exp = format_radicando(ej["index"], ej["num"], ej["den"])
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
                print("[!] Formato no valido. Escribe una fraccion (ej: 3/4) o un entero (ej: 2).")
                continue

            if parsed == ej["ans"]:
                print(">>> [CORRECTO] !Esta muy bien! Excelente trabajo.")
                break
            else:
                print(">>> [INCORRECTO] Esta mal. !Intenta otra vez! Revisa tus cuentas.")

    print("\n" + "*"*60)
    print(f"FELICITACIONES: Has completado los {total} ejercicios exitosamente.")
    print("*"*60 + "\n")

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
