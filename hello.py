#!/usr/bin/env python3
"""Hello world multi linguas.

Dependendo da lingua configurada no ambiente, o programa o programa exibe a mensagem
correspondente

como usar:

tenha a variável de ambiente LANG configurada exemplo:

    export LANG=pt_BR

ou informe atraves do CLI argument `--lang`

ou o usuário digitar.

Execucão:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__ = "Tininho Fita"
__license__ = "Unlicense"

import os
import sys

arguments: dict[str, str | int | None] = {"lang": None, "count": 1}

for arg in sys.argv[1:]:
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()

    if key not in arguments:
        print(f"invalid option `{key}`")
        sys.exit()

    if key == "count":
        try:
            value = int(value)
        except ValueError:
            print(f"Valor inválido para count: {value}")
            sys.exit()

    arguments[key] = value


current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repeticao
    if "LANG" in os.environ:
        current_language = os.environ["LANG"]
    else:
        current_language = input("Choose a language:")

current_language = str(current_language)[:5]

msg = {
    "en_US": "Hello World!",
    "pt_BR": "Olá Mundo!",
    "it_IT": "Ciao Mondo!",
    "es_ES": "¡Hola Mundo!",
    "fr_FR": "Bonjour le monde!",
}

print(msg[current_language] * int(arguments["count"] or 1))
