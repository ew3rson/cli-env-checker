#!/usr/bin/env python3  

import time
import os

# cores ANSI
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
CYAN = "\033[36m"
RESET = "\033[0m"

# limpa a tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# menu
def menu():
    print(f"{CYAN}┌──────────────────────────┐{RESET}")
    print(f"{CYAN}│      CALCULADORA CLI     │{RESET}")
    print(f"{CYAN}└──────────────────────────┘{RESET}\n")

    print(f"{'Soma':<15}{'+':>5}")
    print(f"{'Subtração':<15}{'-':>5}")
    print(f"{'Multiplicação':<15}{'*':>5}")
    print(f"{'Potenciação':<15}{'**':>5}")
    print(f"{'Divisão':<15}{'/':>5}\n")
    print(f"{'Sair':<15}{'0':>5}\n")

# inicia
limpar()

while True:
    menu()
    operador = input(f"{YELLOW}Digite o símbolo da operação: {RESET}")

    if operador == "0":
        print(f"\n{CYAN}Calculadora encerrada.{RESET}\n")
        break

    if operador not in ["+", "-", "*", "/", "**"]:
        print(f"\n{RED}Operador inválido. Tente novamente!{RESET}\n")
        time.sleep(1.5)
        limpar()
        continue

    try:
        num1 = float(input(f"\n{YELLOW}Digite o primeiro número: {RESET}"))
        num2 = float(input(f"\n{YELLOW}Digite o segundo número: {RESET}"))
    except ValueError:
        print(f"\n{RED}Digite um número válido. Tente novamente!{RESET}\n")
        time.sleep(1.5)
        limpar()
        continue

    if operador == "+":
        operacao = "soma"
        resultado = num1 + num2
    elif operador == "-":
        operacao = "subtração"
        resultado = num1 - num2
    elif operador == "*":
        operacao = "multiplicação"
        resultado = num1 * num2
    elif operador == "**":
        operacao = "potenciação"
        resultado = num1 ** num2
    else:  # operador "/"
        if num2 == 0:
            print(f"\n{RED}Não é possível dividir por zero.{RESET}\n")
            time.sleep(1.5)
            limpar()
            continue
        else:
            operacao = "divisão"
            resultado = num1 / num2

    print(f"\n{GREEN}Resultado da {operacao}:{RESET} {resultado}\n")
    input(f"{CYAN}Pressione ENTER para continuar {RESET}")
    limpar()
