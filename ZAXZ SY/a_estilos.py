# CÓDIGO 2 - ESTILOS.
# Possíveis retornos: 0, 1
# V.5 - Cada versão de cada código que não faça parte do sistema principal contribui em 0.1+ da versão principal.

try:
    from z_bibliotecas import *
    
    # Listas e Definições:
    # Modificar: Restrito (Apenas adicionar)
    cancelar = ("Cancelar","Encerrar","Sair","Quebrar","Finalizar","Voltar")

    # Detecção de Fatal Error (Death Code) para o sistema:
    # Modificar: Negado
    def check_a_estilos():
        return 0 # Tudo certo | Sucesso

    # Esperar:
    # Modificar: Negado
    def dormir(tempo):
        time.sleep(tempo)

    # Bloquear teclas (Visualmente):
    # Modificar: Negado
    # Feito por Claude
    def block():
        fd = sys.stdin.fileno()
        novo = termios.tcgetattr(fd)
        novo[3] &= ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, novo)

    # Liberar teclas (Visualmente):
    # Modificar: Negado
    # Feito por Claude
    def unblock():
        fd = sys.stdin.fileno()
        novo = termios.tcgetattr(fd)
        novo[3] |= termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, novo)
    
    # Apagar o buffer a cada chamada:
    # Modificar: Negado
    # Feito por Claude
    def ignore():
        termios.tcflush(sys.stdin, termios.TCIFLUSH)

    # Animação de Letras:
    # Modificar: Restrito (Apenas os 'delays')
    def print_slow(text, delay=0.025):
        for coisa in text:
            print(coisa, end="", flush=True)
            dormir(delay)
        print(Style.RESET_ALL)

    def input_slow(text, delay=0.02):
        for coisa in text:
            print(coisa, end="", flush=True)
            dormir(delay)
        print(Style.RESET_ALL, end="")
        unblock()
        ignore()
        inputar = input()
        block()
        return inputar
    
    # Sistema para frases muito repetidas:
    # Modificar: Negado
    def print_menu():
        print_slow(branco() + "\n1- Deixar tudo no jeito.\n2- Mandar uma mensagem para suas pessoas favoritas.\n3- Fazer uma sequência de ataques.\n4- Anotar informações importantes sobre alguém.\n5- Escolher uma tarefa para hoje.\n6- Sair do programa.", delay=0.005)

    def print_selado():
        print_slow(vermelho() + "\nComando selado, o código está quebrado.\n")
        print_slow(vermelho() + "\nImpossível abrir a força, tente outros comandos.\n")

    def reinstale_o_sistema():
        print_slow(azul() + "\nPara reinstalar o sistema, coloque isso no terminal: rm -rf ~/ZAXZ\ SY && git clone https://github.com/D3LT4-1NCK/ZAXZ-Sistema-Autonomo-com-Ferramentas-Hacker ~/ZAXZ_TEMP && mv ~/ZAXZ_TEMP/ZAXZ\ SY ~/ && rm -rf ~/ZAXZ_TEMP\n")
        print_slow(branco() + "\nCaso queira reportar esse erro, o discord do fundador é: 'floppzh'.\n")
        print_slow(branco() + "\nLembre-se que esse sistema foi criado em um Linux Mint, não há certeza do funcionamento em outros distros.\n") 
        exit()

    # Sistema completo que trata erros de acordo com o return:
    # Modificar: Proibido
    def return_check(resultados=None, qual=None, pings=None):

        # Verificação dos returns:
        if resultados == 0:
            print_slow(branco() + "\nVocê está de volta conectado ao sistema principal.\nO que iremos fazer agora?\n")
            print_menu()
        
        elif resultados == 1:
            print_slow(vermelho() + "\nParece que houve um erro na ferramenta anterior, ela será selada e não poderá ser acessada; reinstale o sistema ou arrume o código.\n")
            print_slow(branco() + "\nO que iremos fazer agora?")
            print_menu()
            if qual == "b_um":
                pings["pingar_selamento_b_um"] = True
            elif qual == "c_dois":
                pings["pingar_selamento_c_dois"] = True
            elif qual == "d_tres":
                pings["pingar_selamento_d_tres"] = True
            elif qual == "e_quatro":
                pings["pingar_selamento_e_quatro"] = True
            elif qual == "f_cinco":
                pings["pingar_selamento_f_cinco"] = True

        elif resultados == 2:
            print_slow(branco() + "\nParece que você cancelou a ferramenta anterior, tudo bem... O que gostaria de fazer agora?\n")
            print_menu()

        elif resultados == 4:
            print_slow(vermelho() + "\nHouve um erro em relação aos arquivos; caso você tenha mexido neles, reinstale o sistema.\n")
            print_slow(branco() + ("\nO que iremos fazer agora?\n"))
            print_menu()
            if qual == "b_um":
                pings["pingar_selamento_b_um"] = True
            elif qual == "c_dois":
                pings["pingar_selamento_c_dois"] = True
            elif qual == "d_tres":
                pings["pingar_selamento_d_tres"] = True
            elif qual == "e_quatro":
                pings["pingar_selamento_e_quatro"] = True
            elif qual == "f_cinco":
                pings["pingar_selamento_f_cinco"] = True

        elif resultados == 5:
            print_slow(branco() + "\nVocê está de volta conectado ao sistema principal.\nO que iremos fazer agora?\n")
            print_menu()
            if qual == "b_um":
                pings["pingar_fechamento_b_um"] = True

        elif resultados == 6: # Provavelmente não está em uso.
            print_slow(vermelho() + "\nHouve um erro desconhecido pelo sistema, por favor, reporte isso para o fundador do projeto (no discord: floppzh) e reinstale o sistema.")
            exit("\nEncerrado por segurança.\n")

        elif resultados == 7:
            pings["pingar_novamente_e_quatro"] = True
            

        elif resultados == None or resultados == False:
            print_slow(vermelho() + "\nFalha desconhecida, impossível manter um sistema assim com essa falha presente, reinstale o sistema.\n")
            reinstale_o_sistema()

    # Verificar se o pyautogui está dando certo:
    # Modificar: Negado
    verificar_ausencia = False
    def iniciar_temp(segundos=10):
        def checar():
            global verificar_ausencia
            with open(os.path.expanduser("~/ZAXZ SY/0_STATUS.txt"), "r") as arquivo:
                if not arquivo.read().strip():
                    verificar_ausencia = True
        threading.Timer(segundos, checar).start()

    def verificar_temp():
        try:
            if verificar_ausencia == True:
                global verificar_ausencia
                print_slow(vermelho() + "\n\nErro: Ausência de informações.\n\n")
                verificar_ausencia = False # Se não ficar eterno em "True"
                return True
        except Exception:
            pass
    
    # Limpador de STATUS:
    # Modificar: Proibido
    def limpar_status():
        with open(os.path.expanduser("~/ZAXZ SY/0_STATUS.txt"), "w"):
            pass

    # Cores:
    # Modificar: Restrito (Apenas adicionar - Com o mesmo modelo)
    def verde():
        return Fore.GREEN + Style.BRIGHT
    
    def amarelo():
        return Fore.YELLOW + Style.BRIGHT

    def vermelho():
        return Fore.RED + Style.BRIGHT
    
    def roxo():
        return Fore.MAGENTA + Style.BRIGHT

    def branco():
        return Fore.WHITE + Style.BRIGHT

    def azul():
        return Fore.BLUE + Style.BRIGHT

# Aviso de Fatal Error:
# Modeficicar: Negado
except Exception as erro_estilos:
    def erro_a_estilos_desconhecido():
        print(f"\n\n\n\nERRO GRAVE! CÓDIGO 2 ('a_estilos'), FALHA FATAL: {erro_estilos}\n\n\n\n")
        return 1 # Falha

# VERIFICADO: TUDO CERTO - FINALIZADO - V1.
# VERIFICADO: TUDO CERTO - ATUALIZADO - V2.
# VERIFICADO: TUDO CERTO - ATUALIZADO - V3.
# VERIFICADO: TUDO CERTO - ATUALIZADO - V4.
# VERIFICADO: TUDO CERTO - ATUALIZADO - V5.
