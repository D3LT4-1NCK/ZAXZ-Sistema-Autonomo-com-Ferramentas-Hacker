# CÓDIGO 3 - OPÇÃO 1
# Possíveis retornos: 0, 1, 2, 5, 6
# V.1 - Cada versão de cada código que não faça parte do sistema principal contribui em 0.1+ da versão principal.

# Bloco de inicialização:
# Modificar: Proibido
try:
    from z_bibliotecas import *
    from a_estilos import *
    block()
    def um():
        try:
            block()

            # Código fonte:
            # Modificar: Permitido
            print_slow(amarelo() + "\nAtenção: Isso fecherá todas as janelas do firefox.")
            print_slow(branco() + "\nDeixarei tudo no jeito, tem algo que eu não deveria abrir?\n\nIrei abrir: (1) MODIFIQUE ISSO | (2) MODIFIQUE ISSO | (3) MODIFIQUE ISSO | (4) MODIFIQUE ISSO | (5) MODIFIQUE ISSO | (6) Outro terminal.\n\nSe não, aperte 'Enter' para pular isso, se sim, digite o que eu não devo abrir!\n(e caso queira sair dessa tela, digite 'cancelar').\n")
            preferencias = []
            buffer = 1
            while True:
                insira = input_slow(branco() + "Insira: ").strip().capitalize()
                if insira in ("1", "2", "3", "4", "5", "6"):
                    print_slow(verde() + "\nAnotado.\n")
                    preferencias.append(insira)
                    pingar = 1
                elif insira == "":
                    pingar = 0
                    break
                elif insira in cancelar:
                        print_slow(amarelo() + "\nVoltando...\n")
                        return 2 # Cancelado
                else:
                    print_slow(vermelho() + "\nInsira um número válido.\n")
                    continue
                break

            if pingar == 1:
                while True:
                    mais_um = input_slow(branco() + "\nMais algum? Se não, aperte 'Enter'. Se sim, insira: ").strip().capitalize()
                    if buffer == 6:
                        print_slow(vermelho() + "\nHaha, boa tentativa, você ficou sem saída, vamos voltar ao sistema base.\n")
                        return 2 # Cancelado
                    elif mais_um in preferencias:
                        print_slow(vermelho() + "\nVocê já pediu para não adicionar esse app.\n")
                    elif mais_um in ("1", "2", "3", "4", "5", "6"):
                        print_slow(verde() + "\nAnotado.\n")
                        buffer += 1
                        preferencias.append(mais_um)
                        preferencias.sort()
                        continue
                    elif mais_um == "":
                        break
                    elif mais_um in cancelar:
                        print_slow(amarelo() + "\nVoltando...\n")
                        return 2 # Cancelado
                    else:
                        print_slow(vermelho() + "\nInsira um número válido.\n")
                        continue
            else:
                pass
            
            signal.signal(signal.SIGINT, signal.SIG_DFL)
            print_slow(amarelo() + "\n\nAtenção: Em casos de falha grave, mate o processo usando 'CTRL' + 'C' (no terminal).\n\nAtenção: Não use o seu teclado/mouse durante o processo.")
            print_slow(vermelho() + "\nAtenção: Certifique-se de que o 'CapsLock' está DESLIGADO.")
            dormir(5.5)
            print_slow(branco() + "\nIniciando...\n")
            if not "6" in preferencias:
                print_slow(verde() + "\nAbrindo terminal...\n")
                pyautogui.hotkey("ctrl", "alt", "t")
                dormir(0.5)
                pyautogui.hotkey("alt","f10")
                print_slow(verde() + "\nTerminal aberto!\n")
            else:
                print_slow(verde() + "\nTerminal pulado!\n")

            # MODIFIQUE ISSO!
            if not ("1" in preferencias and "2" in preferencias and "3" in preferencias and "4" in preferencias and "5" in preferencias):
                print_slow(verde() + "\nDeixando o firefox no jeito...\n")
                os.system("pkill -f firefox")
                # FAÇA SEU PYAUTOGUI AQUI!
            else:
                print_slow(verde() + "\nApp pulado!\n")
                print_slow(verde() + "\nApp pulado!\n")
                print_slow(verde() + "\nApp pulado!\n")
                print_slow(verde() + "\nApp pulado!\n")
                print_slow(verde() + "\nApp pulado!\n")
                return 0 # Sucesso
            
            # MODIFIQUE ISSO!
            if not "1" in preferencias:
                # FAÇA SEU PYAUTOGUI AQUI!
                print_slow(verde() + "\nApp aberto!\n")
            else:
                print_slow(verde() + "\nApp pulado!\n")
            
            # MODIFIQUE ISSO!
            if not "2" in preferencias:
                # FAÇA SEU PYAUTOGUI AQUI!
                print_slow(verde() + "\nApp aberto!\n")
            else:
                print_slow(verde() + "\nApp pulado!\n")

            # MODIFIQUE ISSO!
            if not "3" in preferencias:
                # FAÇA SEU PYAUTOGUI AQUI!
                print_slow(verde() + "\nApp aberto!\n")
            else:
                print_slow(verde() + "\nApp pulado!\n")
            
            # MODIFIQUE ISSO!
            if not "4" in preferencias:
                # FAÇA SEU PYAUTOGUI AQUI!
                print_slow(verde() + "\nApp aberto!\n")
            else:
                print_slow(verde() + "\nApp pulado!\n")
            
            # MODIFIQUE ISSO!
            if not "5" in preferencias:
                # FAÇA SEU PYAUTOGUI AQUI!
                print_slow(verde() + "\nApp aberto!\n")
            else:
                print_slow(verde() + "\nApp pulado!\n")

            print_slow(verde() + "\n\nConcluído!\n\n")
            dormir(0.5)
            return 5 # Sucesso | Fechar

        # Tratamento Falha Fatal:
        # Modificar: Negado      
        except Exception as erro_fatal_b_um:
            print_slow(vermelho() + f"\n\n\n\nERRO GRAVE! CÓDIGO 3 ('b_um'), FALHA FATAL: {erro_fatal_b_um}\n\n\n\n")
            return 1 # Falha
        
# Tratamento Falha Fatal Cruel:
# Modificar: Negado  
except Exception as erro_cruel_b_um:
    def erro_b_um_desconhecido():
        print(f"\n\n\n\nERRO DESCONHECIDO! CÓDIGO 3 ('b_um'), FALHA FATAL CRUEL: {erro_cruel_b_um}\n\n\n\n")
        return 6 # Desconhecido  
    
# VERIFICADO: TUDO CERTO - FINALIZADO - V1.
