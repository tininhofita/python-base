#!/usr/bin/env python3
"""Calculadora infix

Funcionamento:

[operacao] [n1] [n2]

Operacoes:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operacao: sum
n1: 5
n2: 4
9
"""
__version__ = "0.1.0"

import sys

arguments = sys.argv[1:]


# TODO exceptions
if not arguments:
    operation = input("operacao:")
    n1 = input("n1:")
    n2 = input("n2:")
    arguments = [operation, n1, n2]
if len(arguments) != 3:
    print("Numero de argumentos inválido")
    print("ex: `sum 5 5`")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print(f"Operacao inválida: {operation}")
    print(f"Operacoes válidas: {', '.join(valid_operations)}")
    sys.exit(1)

validated_nums = []
for num in nums:
    # TODO: usar repeticao while + exceptions
    if not num.replace(".", "").isdigit():
        print(f"Numero inválido: {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

ni, n2 = validated_nums

# TODO usar dict de funcoes
if operation == "sum":
    result = ni + n2
elif operation == "sub":
    result = ni - n2
elif operation == "mul":
    result = ni * n2
elif operation == "div":
    result = ni / n2

print(f"O resultado é {result}")
