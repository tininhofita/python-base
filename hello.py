#!/usr/bin/env python3

""" Hello world multi linguas.

Dependendo da lingua configurada no ambiente, o programa irá imprimir "Hello World" na língua correspondente.

como usar: 

tenha a variável de ambiente LANG configurada para a língua desejada.

Exemplo:    
    export LANG=pt_BR

Execuão: 
    python3 hello.py
    ou
    ./hello.py

Versão: 0.0.1
"""
__version__ = "0.0.1"
__author__ = "Tininho Fita"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]
msg = "Hello World!"

if current_language == "pt_BR":
    msg = "Olá Mundo!"
elif current_language == "es_ES":
    msg = "¡Hola Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour le monde!"
elif current_language == "de_DE":
    msg = "Hallo Welt!"
elif current_language == "it_IT":
    msg = "Ciao Mondo!"
elif current_language == "ja_JP":
    msg = "こんにちは世界！"
elif current_language == "zh_CN":
    msg = "你好，世界！"
elif current_language == "ru_RU":
    msg = "Привет, мир!"

print(msg)
