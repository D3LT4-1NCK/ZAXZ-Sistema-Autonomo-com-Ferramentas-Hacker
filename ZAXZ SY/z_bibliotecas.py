# CÓDIGO 1 - BIBLIOTECAS
# Possíveis retornos: N/A
# V.1 - Cada versão de cada código que não faça parte do sistema principal contribui em 0.1+ da versão principal.

# Sistema de bibliotecas:
# Modificar: Proibido
try:
    import pyautogui
    import ipaddress
    import validators
    import time
    import random
    import signal
    import sys
    import os
    import re
    import glob
    import termios
    import threading
    from pyfiglet import figlet_format
    from datetime import datetime
    from colorama import Fore, Style, init
    pyautogui.PAUSE = 0.2
    init()

except ImportError as erro_bibliotecas:
    print(f"\n\n\n\nBiblioteca Faltando: {erro_bibliotecas}\nInstale com: 'sudo apt install python3-biblioteca_aqui -y'\n\n\n\n")
    print("Use esse comando para funcionar:\n\n\n\n")
    print("'\n1: pip install pyautogui --break-system-packages\n2: sudo apt install python3-colorama -y\n3: sudo apt install python3-validators -y'")
    exit()

# VERIFICADO: TUDO CERTO - FINALIZADO - V1.
