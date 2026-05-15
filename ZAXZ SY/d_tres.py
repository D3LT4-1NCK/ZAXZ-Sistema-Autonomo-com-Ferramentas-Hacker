# CÓDIGO 5 - OPÇÃO 3
# V.5 - Cada versão de cada código que não faça parte do sistema principal contribui em 0.1+ da versão principal.
# Possíveis retornos: 0, 1, 2, 4, 6

# Bloco de inicialização:
# Modificar: Proibido
try:
    from z_bibliotecas import *
    from a_estilos import *
    block()
    def tres():
        try:
            block()
            limpar_status()

            # Sistema URL:
            # Modificar: Negado
            pingar_falha_na_url = False

            def url(link=None):

                nonlocal pingar_falha_na_url
                print_slow(roxo() + f"\nBoa, vamos dar olhada nessa URL: '{link}' 😈...")
                print_slow(amarelo() + "\n\nAtenção: Em casos de falha grave, mate o processo usando 'CTRL' + 'C' (no terminal).\n\nAtenção: Não use o seu teclado/mouse durante o processo.")
                print_slow(vermelho() + "\nAtenção: Certifique-se de que o 'CapsLock' está DESLIGADO e que o seu terminal NÃO está em tela cheia 'F-11'.")
                dormir(10)
                print_slow(branco() + "\nIniciando...\n")
                dormir(1)
                signal.signal(signal.SIGINT, signal.SIG_DFL)

                # NSLOOKUP:
                pingar_falha_nslookup = None
                pyautogui.hotkey("win", "d")
                pyautogui.press("win")
                pyautogui.write("terminal")
                pyautogui.press("enter")
                dormir(0.5)
                pyautogui.hotkey("win", "right")
                pyautogui.keyDown("alt")
                dormir(0.5)
                pyautogui.press("tab")
                dormir(0.5)
                pyautogui.press("enter")
                pyautogui.keyUp("alt")
                pyautogui.hotkey("win", "left")
                print_slow(verde() + "\nVamos começar o trabalho!\n")
                pyautogui.click(x=1500, y=500)
                if link.startswith("https://"):
                    novo_link = link[8:]
                else:
                    pingar_falha_na_url = True
                    print_slow(vermelho() + f"\nErro no URL, coloque corretamente (com o 'https://').\n")
                    print_slow(vermelho() + f"\nTe retornando a força...\n")
                    dormir(2)
                    return 4 # Retornado a força para o "novamente".
                if novo_link.endswith("/"):
                    novo_link = novo_link[:-1]
                dormir(1)
                pyautogui.write(rf'nslookup {novo_link} > ~/ZAXZ\ SY/ZAXZ\ FERRAMENTAS/ZAXZ\ NSLOOKUP/RESULTADO_NSLOOKUP.txt 2>&1 && echo "Sucesso" > ~/ZAXZ\ SY/0_STATUS.txt || echo "Falha" > ~/ZAXZ\ SY/0_STATUS.txt')
                dormir(1)
                pyautogui.press("enter")
                dormir(5)
                pyautogui.hotkey("ctrl","c")
                with open(os.path.expanduser("~/ZAXZ SY/ZAXZ FERRAMENTAS/ZAXZ NSLOOKUP/RESULTADO_NSLOOKUP.txt"), "r") as anotar_nslookup:
                    conteudo_ip = anotar_nslookup.read()
                dormir(3)
                with open(os.path.expanduser("~/ZAXZ SY/0_STATUS.txt"), "r") as ler_status:
                    conteudo_status = ler_status.read()
                dormir(3)
                if conteudo_status == "Falha":
                    print_slow(vermelho() + "\nErro ao coletar o IP.\n")
                    print_slow(vermelho() + f"\nDetalhes do erro:\n\n{conteudo_ip}\n")
                    print_slow(branco() + "\nVamos prosseguir...\n")
                    pingar_falha_nslookup = True
            
                if "**" in conteudo_ip:
                    resultado = conteudo_ip.split("**", 1)[1]
                    print_slow(vermelho() + "\nErro no NSLOOKUP.\n")
                    print_slow(vermelho() + f"\nDetalhes do erro:\n\n{resultado}\n")
                    print_slow(branco() + "\nVamos prosseguir...\n")
                    pingar_falha_nslookup = True
                else:
                    ips = re.findall(r'\b(?!127)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', conteudo_ip)
                    print_slow(verde() + "\nIP/IPs coletados.\n")
                
                # DIG:
                limpar_status()

                pingar_falha_dig = None
                pyautogui.write(rf'dig {novo_link} > ~/ZAXZ\ SY/ZAXZ\ FERRAMENTAS/ZAXZ\ DIG/RESULTADO_DIG.txt 2>&1 && echo "Sucesso" > ~/ZAXZ\ SY/0_STATUS.txt || echo "Falha" > ~/ZAXZ\ SY/0_STATUS.txt')
                dormir(1)
                pyautogui.press("enter")
                dormir(3)
                with open(os.path.expanduser("~/ZAXZ SY/ZAXZ FERRAMENTAS/ZAXZ DIG/RESULTADO_DIG.txt"), "r") as anotar_dig:
                    conteudo_ip_2 = anotar_dig.read()
                dormir(3)
                with open(os.path.expanduser("~/ZAXZ SY/0_STATUS.txt"), "r") as ler_status_2:
                    conteudo_status_2 = ler_status_2.read()
                dormir(3)
                if conteudo_status_2 == "Falha":
                    print_slow(vermelho() + "\nErro ao reforçar a coleta de IP.\n")
                    print_slow(vermelho() + f"\nDetalhes do erro:\n\n{conteudo_ip_2}\n")
                    print_slow(branco() + "\nVamos prosseguir...\n")
                    pingar_falha_dig = True
            
                if "dig: " in conteudo_ip_2:
                    resultado_2 = conteudo_ip_2.split("dig: ", 1)[1]
                    print_slow(vermelho() + "\nErro no DIG.\n")
                    print_slow(vermelho() + f"\nDetalhes do erro:\n\n{resultado_2}\n")
                    print_slow(branco() + "\nVamos prosseguir...\n")
                    pingar_falha_dig = True
                else:
                    ips_reforce = re.findall(r'\b(?!127)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', conteudo_ip_2)
                    print_slow(verde() + "\nReforçamento de coleta de IP coletada.\n")

                # Gobuster
                limpar_status()
                # Sem tempo, isso varia.
                
                pingar_falha_gobuster = None
                pyautogui.write(rf'gobuster dir -u {link} -w ZAXZ\ SY/0_ZAXZ\ DIR.txt -t 13 -s 200 -b "" --no-progress > ZAXZ\ SY/ZAXZ\ FERRAMENTAS/ZAXZ\ GOBUSTER/RESULTADO_GOBUSTER.txt 2>&1 && echo "Sucesso" > ZAXZ\ SY/0_STATUS.txt || echo "Falha" > ZAXZ\ SY/0_STATUS.txt')
                dormir(1)
                pyautogui.press("enter")
                print_slow(verde() + "\nAguarde...\n")
                dormir(35)
                print_slow(verde() + "\nQuase lá...\n")
                dormir(30)
                pyautogui.hotkey("ctrl","c")
                print_slow(verde() + "\nVamos ver...\n")
                pyautogui.hotkey("alt", "f4")
                dormir(0.3)
                pyautogui.hotkey("alt", "f10")
                with open(os.path.expanduser("~/ZAXZ SY/ZAXZ FERRAMENTAS/ZAXZ GOBUSTER/RESULTADO_GOBUSTER.txt"), "r") as anotar_gobuster:
                    conteudo_gobuster = anotar_gobuster.read()
                dormir(3)
                with open(os.path.expanduser("~/ZAXZ SY/0_STATUS.txt"), "r") as ler_status_3:
                    conteudo_status_3 = ler_status_3.read()
                dormir(3)
                if conteudo_status_3 == "Falha":
                    print_slow(vermelho() + "\nErro ao coletar diretórios importantes.\n")
                    print_slow(vermelho() + f"\nDetalhes do erro:\n\n{conteudo_gobuster}\n")
                    print_slow(branco() + "\nVamos prosseguir...\n")
                    pingar_falha_gobuster = True
            
                if "Error: " in conteudo_gobuster:
                    print_slow(vermelho() + "\nErro no Gobuster.\n")
                    print_slow(vermelho() + f"\nDetalhes indisponíveis\n")
                    print_slow(branco() + "\nVamos prosseguir...\n")
                    pingar_falha_gobuster = True
                else:
                    diretorios = ([coisa.strip().replace("(", "") for coisa in re.findall(r"(\/.*?)\s*\(Status:\s*200", conteudo_gobuster)])
                    print_slow(verde() + "\nBusca de diretórios importantes concluída.\n")
                
                # Sistema dos resultados URL:
                # Modificar: Negado
                if pingar_falha_nslookup == True and pingar_falha_dig == True and pingar_falha_gobuster == True:
                    print_slow(vermelho() + "\nQue chato! Não obtivemos nenhum resultado... Aconteceu alguma coisa grave, reinstale o sistema.\n")
                    reinstale_o_sistema()

                elif pingar_falha_dig == True and pingar_falha_gobuster == True:
                    informações_coletadas = f"\n\nInformações coletadas:\n\nIP/IPs do URL: {ips}"

                elif pingar_falha_nslookup == True and pingar_falha_dig == True:
                    informações_coletadas = f"\n\nInformações coletadas:\n\nPossíveis diretórios vulneráveis: {diretorios}\n"

                elif pingar_falha_nslookup == True and pingar_falha_gobuster == True:
                    informações_coletadas = f"\n\nInformações coletadas:\n\nReforçamento de IP/IPs do URL: {ips_reforce}"
                
                elif pingar_falha_nslookup == True:
                    informações_coletadas = f"\n\nInformações coletadas:\n\nReforçamento de IP/IPs do URL: {ips_reforce}\nPossíveis diretórios vulneráveis: {diretorios}\n"
                
                elif pingar_falha_dig == True:
                    informações_coletadas = f"\n\nInformações coletadas:\n\nIP/IPs do URL: {ips}\nPossíveis diretórios vulneráveis: {diretorios}\n"
                
                elif pingar_falha_gobuster == True:
                    informações_coletadas = f"\n\nInformações coletadas:\n\nIP/IPs do URL: {ips}\nReforçamento de IP/IPs do URL: {ips_reforce}\n"
                                                                                                                                                                                                                                         
                else:
                    informações_coletadas = f"\n\nInformações coletadas:\n\nIP/IPs do URL: {ips}\nReforçamento de IP/IPs do URL: {ips_reforce}\nPossíveis diretórios vulneráveis: {diretorios}\n"

                print_slow(roxo() + informações_coletadas)
                print_slow(roxo() + "\nBusca concluída.\n")
                signal.signal(signal.SIGINT, signal.SIG_IGN)

                # Sistema que guarda a informação URL:
                # Modificar: Negado
                guardar = input_slow(branco() +"\nVocê quer guardar essas informações em um '.txt' (S/N): ").strip().capitalize()
                if guardar in cancelar:
                    pass
                elif guardar in ("N","Nao","Não"):
                    pass
                elif guardar in ("S","Sim"):
                    while True:
                        nomear_arquivo = input_slow(branco() + "\nQue nome você quer dar para o arquivo? Coloque aqui (sem '.txt'): ")

                        if nomear_arquivo in cancelar:
                            break
                        elif glob.glob(os.path.expanduser(f"~/{nomear_arquivo}.txt")):
                            print_slow(vermelho() + "\nJá existe um arquivo com esse nome.\n")
                            continue
                        elif "/" in nomear_arquivo:
                            print_slow(vermelho() + "\nOpa! O Linux não aceita esse tipo de nome para de arquivos ou documentos.\n")
                            continue
                        elif len(nomear_arquivo) >= 39 or len(nomear_arquivo) <= 3:
                            print_slow(vermelho() + "\nNome grande/pequeno demais.\n")
                            continue
                        else:
                            with open(os.path.expanduser(f"~/{nomear_arquivo}.txt"), "w") as criar_arquivo:
                                criar_arquivo.write(f"{informações_coletadas}\n\nEssas informações são do URL: {link}\n")
                            print_slow(verde() + "\nCriado com sucesso.\n")
                            break
                return 0

            # Sistema IP:
            # Modificar: Negado
            def ip(ip_alvo=None):
                print_slow(roxo() + f"\nBoa, vamos dar olhada nesse IP: '{ip_alvo}' 📡...")
                print_slow(amarelo() + "\n\nAtenção: Em casos de falha grave, mate o processo usando 'CTRL' + 'C' (no terminal).\n\nAtenção: Não use o seu teclado/mouse durante o processo.")
                print_slow(vermelho() + "\nAtenção: Certifique-se de que o 'CapsLock' está DESLIGADO e que o seu terminal NÃO está em tela cheia 'F-11'.")
                dormir(10)
                print_slow(branco() + "\nIniciando...\n")
                dormir(1)
                signal.signal(signal.SIGINT, signal.SIG_DFL)

                # NMAP:
                pingar_falha_nmap = None
                pyautogui.hotkey("win", "d")
                pyautogui.press("win")
                pyautogui.write("terminal")
                pyautogui.press("enter")
                dormir(0.5)
                pyautogui.hotkey("win", "right")
                pyautogui.keyDown("alt")
                dormir(0.5)
                pyautogui.press("tab")
                dormir(0.5)
                pyautogui.press("enter")
                pyautogui.keyUp("alt")
                pyautogui.hotkey("win", "left")
                limpar_status()
                iniciar_temp(segundos=50) # 3
                print_slow(verde() + "\nVamos começar o trabalho!\n")
                pyautogui.click(x=1500, y=500)
                dormir(1)
                pyautogui.write(rf'nmap -sV -Pn -sC -T3 --open {ip_alvo} > ~/ZAXZ\ SY/ZAXZ\ FERRAMENTAS/ZAXZ\ NMAP/RESULTADO_NMAP.txt 2>&1 && echo "Sucesso" > ~/ZAXZ\ SY/0_STATUS.txt || echo "Falha" > ~/ZAXZ\ SY/0_STATUS.txt')
                dormir(1)
                pyautogui.press("enter")
                print_slow(verde() + "\nAguarde...\n")
                dormir(25)
                print_slow(verde() + "\nQuase lá...\n")
                dormir(15)
                pyautogui.hotkey("ctrl","c")
                with open(os.path.expanduser("~/ZAXZ SY/ZAXZ FERRAMENTAS/ZAXZ NMAP/RESULTADO_NMAP.txt"), "r") as anotar_nmap:
                    conteudo_nmap = anotar_nmap.read()
                dormir(3)
                with open(os.path.expanduser("~/ZAXZ SY/0_STATUS.txt"), "r") as ler_status_4:
                    conteudo_status_4 = ler_status_4.read()
                dormir(3)

                if conteudo_status_4 == "Falha":
                    print_slow(vermelho() + "\nErro ao analisar o IP.\n")
                    print_slow(vermelho() + f"\nDetalhes do erro:\n\n{conteudo_nmap}\n")
                    print_slow(branco() + "\nVamos prosseguir...\n")
                    pingar_falha_nmap = True
            
                else:
                    nmapar = re.findall(r'\d+/\w+\s+open', conteudo_nmap)
                    print_slow(verde() + "\nPortas abertas do IP analisadas!\n")
                    for coisa, coisa2 in enumerate(nmapar):
                        nmapar[coisa] = coisa2.replace(" ", "").replace("open", "")
                
                # Whois:
                pingar_falha_whois = None
                limpar_status()
                iniciar_temp(segundos=15) # 4
                print_slow(verde() + "\nProsseguindo...\n")
                dormir(1)
                pyautogui.write(rf'whois {ip_alvo} > ~/ZAXZ\ SY/ZAXZ\ FERRAMENTAS/ZAXZ\ WHOIS/RESULTADO_WHOIS.txt 2>&1 && echo "Sucesso" > ~/ZAXZ\ SY/0_STATUS.txt || echo "Falha" > ~/ZAXZ\ SY/0_STATUS.txt')
                dormir(1)
                pyautogui.press("enter")
                print_slow(verde() + "\nAguarde...\n")
                dormir(10)
                print_slow(verde() + "\nTerminando...\n")
                dormir(5)
                pyautogui.hotkey("ctrl","c")
                print_slow(verde() + "\nVamos ver...\n")
                pyautogui.hotkey("alt", "f4")
                dormir(0.3)
                pyautogui.hotkey("alt", "f10")
                with open(os.path.expanduser("~/ZAXZ SY/ZAXZ FERRAMENTAS/ZAXZ WHOIS/RESULTADO_WHOIS.txt"), "r") as anotar_whois:
                    conteudo_whois = anotar_whois.read()
                dormir(3)
                with open(os.path.expanduser("~/ZAXZ SY/0_STATUS.txt"), "r") as ler_status_5:
                    conteudo_status_5 = ler_status_5.read()
                dormir(3)

                if conteudo_status_5 == "Falha":
                    print_slow(vermelho() + "\nErro ao analisar informações gerais.\n")
                    print_slow(vermelho() + f"\nDetalhes do erro:\n\n{conteudo_whois}\n")
                    print_slow(branco() + "\nVamos prosseguir...\n")
                    pingar_falha_whois = True
            
                else:
                    whois = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+|Country:\s+[A-Z]{2}|\+\d[\d\-\s]+', conteudo_whois)
                    print_slow(verde() + "\nInformações gerais adquiridas!\n")
                    for coisa3, coisa4 in enumerate(whois):
                        whois[coisa3] = coisa4.replace("Country:", "").replace("\n", "").replace(" ", "")

                # Sistema dos resultados IP:
                # Modificar: Negado
                if pingar_falha_nmap == True and pingar_falha_whois == True:
                    print_slow(vermelho() + "\nQue chato! Não obtivemos nenhum resultado (nem mesmo vazio)... Aconteceu alguma coisa grave, reinstale o sistema.\n")
                    reinstale_o_sistema()
                elif pingar_falha_nmap == True:
                    informações_coletadas_2 = f"\n\nInformações coletadas:\n\nInformações Gerais:  {whois}\n"

                elif pingar_falha_whois == True:
                    informações_coletadas_2 = f"\n\nInformações coletadas:\n\nPortas abertas do IP:  {nmapar}\n"
                                                                                                                                                                                                                                         
                else:
                    informações_coletadas_2 = f"\n\nInformações coletadas:\n\nPortas abertas do IP:  {nmapar}\n\nInformações Gerais:  {whois}\n"

                print_slow(roxo() + informações_coletadas_2)
                print_slow(roxo() + "\nBusca concluída.\n") 
                signal.signal(signal.SIGINT, signal.SIG_IGN)

                # Sistema que guarda a informação IP:
                # Modificar: Negado
                guardar = input_slow(branco() +"\nVocê quer guardar essas informações em um '.txt' (S/N): ").strip().capitalize()
                if guardar in cancelar:
                    pass
                elif guardar in ("N","Nao","Não"):
                    pass
                elif guardar in ("S","Sim"):
                    while True:
                        nomear_arquivo = input_slow(branco() + "\nQue nome você quer dar para o arquivo? Coloque aqui (sem '.txt'): ")

                        if nomear_arquivo in cancelar:
                            break
                        elif glob.glob(os.path.expanduser(f"~/{nomear_arquivo}.txt")):
                            print_slow(vermelho() + "\nJá existe um arquivo com esse nome.\n")
                            continue
                        elif "/" in nomear_arquivo:
                            print_slow(vermelho() + "\nOpa! O Linux não aceita esse tipo de nome para de arquivos ou documentos.\n")
                            continue
                        elif len(nomear_arquivo) >= 39 or len(nomear_arquivo) <= 3:
                            print_slow(vermelho() + "\nNome grande/pequeno demais.\n")
                            continue
                        else:
                            with open(os.path.expanduser(f"~/{nomear_arquivo}.txt"), "w") as criar_arquivo:
                                criar_arquivo.write(f"{informações_coletadas_2}\n\nEssas informações são do IP: {ip_alvo}\n")
                            print_slow(verde() + "\nCriado com sucesso.\n")
                            break
                return 0
            
            # Sistema nome de usuário:
            # Modificar: Negado
            def user(nick=None):
                print_slow(roxo() + f"\nBoa, vamos dar olhada nesse NICK: '{nick}' 🔎...")
                print_slow(amarelo() + "\n\nAtenção: Em casos de falha grave, mate o processo usando 'CTRL' + 'C' (no terminal).\n\nAtenção: Não use o seu teclado/mouse durante o processo.")
                print_slow(vermelho() + "\nAtenção: Certifique-se de que o 'CapsLock' está DESLIGADO e que o seu terminal NÃO está em tela cheia 'F-11'.")
                dormir(10)
                print_slow(branco() + "\nIniciando...\n")
                dormir(1)
                signal.signal(signal.SIGINT, signal.SIG_DFL)

                # Sherlock:
                pingar_falha_sherlock = None
                pyautogui.hotkey("win", "d")
                pyautogui.press("win")
                pyautogui.write("terminal")
                pyautogui.press("enter")
                dormir(0.5)
                pyautogui.hotkey("win", "right")
                pyautogui.keyDown("alt")
                dormir(0.5)
                pyautogui.press("tab")
                dormir(0.5)
                pyautogui.press("enter")
                pyautogui.keyUp("alt")
                pyautogui.hotkey("win", "left")
                limpar_status()
                print_slow(verde() + "\nVamos começar o trabalho!\n")
                pyautogui.click(x=1500, y=500)
                dormir(1)
                pyautogui.write(rf'sherlock {nick} > ~/ZAXZ\ SY/ZAXZ\ FERRAMENTAS/ZAXZ\ SHERLOCK/RESULTADO_SHERLOCK.txt 2>&1 && echo "Sucesso" > ~/ZAXZ\ SY/0_STATUS.txt || echo "Falha" > ~/ZAXZ\ SY/0_STATUS.txt')
                dormir(1)
                pyautogui.press("enter")
                print_slow(verde() + "\nAguarde...\n")
                dormir(32)
                print_slow(verde() + "\nFinalizando...\n")
                dormir(28)
                pyautogui.hotkey("ctrl","c")
                print_slow(verde() + "\nVamos ver...\n")
                pyautogui.hotkey("alt", "f4")
                dormir(0.3)
                pyautogui.hotkey("alt", "f10")
                with open(os.path.expanduser("~/ZAXZ SY/ZAXZ FERRAMENTAS/ZAXZ SHERLOCK/RESULTADO_SHERLOCK.txt"), "r") as anotar_sherlock:
                    conteudo_sherlock = anotar_sherlock.read()
                dormir(3)
                with open(os.path.expanduser("~/ZAXZ SY/0_STATUS.txt"), "r") as ler_status_6:
                    conteudo_status_6 = ler_status_6.read()
                dormir(3)

                if conteudo_status_6 == "Falha":
                    print_slow(vermelho() + "\nErro ao analisar o Nick.\n")
                    print_slow(vermelho() + f"\nDetalhes do erro:\n\n{conteudo_sherlock}\n")
                    print_slow(branco() + "\nVamos prosseguir...\n")
                    pingar_falha_sherlock = True
            
                else:
                    sherlockar = re.findall(r'\[\+\].*\n', conteudo_sherlock)
                    print_slow(verde() + "\nLugares onde o nick está logado identificados!\n")
                    for coisa, coisa2 in enumerate(sherlockar):
                        sherlockar[coisa] = coisa2.replace("[+] ", "")
                
                # Sistema dos resultados USER:
                # Modificar: Negado
                if pingar_falha_sherlock == True:
                    print_slow(vermelho() + "\nQue chato! Não obtivemos nenhum resultado (nem mesmo vazio)... Talvez seja normal, se isso acontecer muitas vezes, reinstale o sistema.\n")
                    return 2
                else:
                    informações_coletadas_3 = f"\n\nInformações coletadas:\n\nLugares aonde este nick está logado:  {sherlockar}\n"

                print_slow(roxo() + informações_coletadas_3)
                print_slow(roxo() + "\nBusca concluída.\n") 
                signal.signal(signal.SIGINT, signal.SIG_IGN)

                # Sistema que guarda a informação USER:
                # Modificar: Negado
                guardar = input_slow(branco() +"\nVocê quer guardar essas informações em um '.txt' (S/N): ").strip().capitalize()
                if guardar in cancelar:
                    pass
                elif guardar in ("N","Nao","Não"):
                    pass
                elif guardar in ("S","Sim"):
                    while True:
                        nomear_arquivo = input_slow(branco() + "\nQue nome você quer dar para o arquivo? Coloque aqui (sem '.txt'): ")

                        if nomear_arquivo in cancelar:
                            break
                        elif glob.glob(os.path.expanduser(f"~/{nomear_arquivo}.txt")):
                            print_slow(vermelho() + "\nJá existe um arquivo com esse nome.\n")
                            continue
                        elif "/" in nomear_arquivo:
                            print_slow(vermelho() + "\nOpa! O Linux não aceita esse tipo de nome para de arquivos ou documentos.\n")
                            continue
                        elif len(nomear_arquivo) >= 39 or len(nomear_arquivo) <= 3:
                            print_slow(vermelho() + "\nNome grande/pequeno demais.\n")
                            continue
                        else:
                            with open(os.path.expanduser(f"~/{nomear_arquivo}.txt"), "w") as criar_arquivo:
                                criar_arquivo.write(f"{informações_coletadas_3}\n\nEssas informações são do Nick: {nick}\n")
                            print_slow(verde() + "\nCriado com sucesso.\n")
                            break
                return 0  
            
            # Sistema normal:
            # Modificar: Negado
            print_slow(roxo() + "\nSeja muito bem vindo a ferramenta mais poderosa e sofisticada do sistema.")
            print_slow(roxo() + "\nEspero que seja útil.")

            # Sistema que verifica se o arquivo está existente antes de prosseguir:
            # Modificar: Proibido
            verificar = os.path.exists(os.path.expanduser(f"~/ZAXZ SY/ZAXZ FERRAMENTAS"))
            if verificar == True:
                pass
            elif verificar == False:
                return 4
                
            while True:
                try:
                    print_slow(branco() + "\nFerramentas necessárias (devem estar atualizadas):\n- Whois\n- Gobuster\n- Nslookup\n- Dig\n- Sherlock\n- Holehe (em breve)\n- Hydra (em breve)\n\n- Caso queira saber como baixá-las/atualizá-las, digite '77'.\n- Caso queira voltar ao sistema principal, digite '99'.", delay=0.02)
                    print_slow(branco() + "\nVocê quer fazer uma varredura completa em (selecione o número):\n1- URL\n2- IP\n3- Nick de Usuário\n", delay=0.02)
                    insira = int(input_slow(branco() + "Insira: ").strip())

                    # Opções diferentes:
                    # Modificar: Negado
                    if insira == 77:
                        print_slow(branco() + "\nAbaixo, tutorial de como baixar/atualizar cada uma delas.")
                        print_slow(branco() +"\n- Whois: sudo apt update && sudo apt install whois -y\n- Gobuster: sudo apt update && sudo apt install gobuster -y\n- Nslookup: sudo apt update && sudo apt install dnsutils -y\n- Dig: sudo apt update && sudo apt install dnsutils -y\n- Sherlock: sudo apt update && sudo apt install sherlock python3-numpy -y\n- Holehe: sudo apt update && pip install holehe --break-system-packages\n- Hydra: sudo apt update && sudo apt install hydra -y\n\n- Ou apenas tente: sudo apt update && sudo apt install python3-pip python3-numpy whois gobuster dnsutils sherlock hydra -y && pip install holehe --break-system-packages\n")
                        while True:
                            confirmar = input_slow(amarelo() + "\nQuando tiver instalado/atualizado tudo (em outro terminal), mande um 'Ok': ").strip().capitalize()
                            if confirmar == "Ok":
                                print_slow(verde() + "\nBoa... Vamos lá!\n")
                                break
                            elif confirmar in cancelar:
                                print_slow(amarelo() + "\nVoltando...\n")
                                break
                            else:
                                print_slow(vermelho() + "\nErro, o campo só aceita 'OK'.\n")
                                continue
                        continue
                    elif insira == 99:
                        print_slow(amarelo() + "\nVoltando...\n")
                        return 2 # Cancelado
                    
                    # Opção 1:
                    # Modificar: Negado
                    elif insira == 1:
                        while True:
                            signal.signal(signal.SIGINT, signal.SIG_DFL)
                            pingar_url = input_slow(branco() + "\nColoque a URL exata do site aqui (deve ser o da página principal, com HTTPS completo): ").strip().replace(" ", "")
                            signal.signal(signal.SIGINT, signal.SIG_IGN)
                            url_valida = validators.url(pingar_url)

                            if url_valida:
                                pass
                            else:
                                print_slow(vermelho() + "\nErro, URL inválida.\n")
                                print_slow(branco() + "Exemplo CORRETO do URL: https://www.google.com/\n", delay=0.02)
                                print_slow(branco() + "Exemplo ERRADO do URL: www.google.com/?zx=17785815812\n", delay=0.02)
                                continue
                            confirmar = input_slow(branco() + f"\nConfirmar URL como '{pingar_url}' (S/N ou 'cancelar'): ").strip()
                            
                            if pingar_url.capitalize() in cancelar or confirmar in cancelar:
                                print_slow(amarelo() + "\nVoltando...\n")
                                break

                            if confirmar.capitalize() in ("S","Sim"):

                                chamada_url = url(link=pingar_url)
                                if chamada_url == 4:
                                    return 4
                                    
                                while True:
                                    signal.signal(signal.SIGINT, signal.SIG_IGN)
                                    if pingar_falha_na_url == True:
                                        print_slow(vermelho() + "\nUau, você conseguiu encontrar um erro raro, a URL está com algum problema.\n")
                                    novamente = input_slow(branco() + "\nVocê quer continuar usando essas ferramentas (S/N): ").strip()
                                    if novamente.capitalize() in ("S","Sim"):
                                        break
                                    elif novamente.capitalize() in ("N","Não","Nao"):
                                        print_slow(amarelo() + "\nVoltando...\n")
                                        if chamada_url == 0:
                                            return 0 # Sucesso
                                        return 2 # Cancelado
                                    else:
                                        print_slow(vermelho() + "\nErro, opção inválida.\n")
                                        continue
                                break
                            elif confirmar.capitalize() in ("N","Não","Nao"):
                                    print_slow(amarelo() + "\nHm... Certo, vamos tentar novamente.\n")
                                    continue
                            else: 
                                print_slow(vermelho() + "\nErro, opção inválida.\n")
                                continue
                            
                        continue
                    
                    # Opção 2:
                    # Modificar: Negado
                    elif insira == 2:
                        while True:
                            signal.signal(signal.SIGINT, signal.SIG_IGN)
                            pingar_ip = input_slow(branco() + "\nColoque o IP exato do alvo: ").strip()
                            try:
                                ipaddress.ip_address(pingar_ip)
                            except ValueError:
                                print_slow(vermelho() + "\nIP inválido.\n")
                                continue
                            confirmar_ip = input_slow(branco() + f"\nConfirmar IP como {pingar_ip} (S/N ou 'cancelar'): ").strip()

                            if pingar_ip.capitalize() in cancelar or confirmar_ip in cancelar:
                                print_slow(amarelo() + "\nVoltando...\n")
                                break

                            if confirmar_ip.capitalize() in ("S","Sim"):
                                chamada_ip = ip(ip_alvo=pingar_ip)
                                if chamada_ip == 4:
                                    return 4
                                while True:
                                    novamente_ip = input_slow(branco() + "\nVocê quer continuar usando essas ferramentas (S/N): ").strip()
                                    if novamente_ip.capitalize() in ("S","Sim"):
                                        break
                                    elif novamente_ip.capitalize() in ("N","Não","Nao"):
                                        print_slow(amarelo() + "\nVoltando...\n")
                                        if chamada_ip == 0:
                                            return 0 # Sucesso
                                        return 2 # Cancelado
                                    else:
                                        print_slow(vermelho() + "\nErro, opção inválida.\n")
                                        continue
                                break
                            elif confirmar_ip.capitalize() in ("N","Não","Nao"):
                                    print_slow(amarelo() + "\nHm... Certo, vamos tentar novamente.\n")
                                    continue
                            else: 
                                print_slow(vermelho() + "\nErro, opção inválida.\n")
                                continue
                        continue

                    # Opção 3:
                    # Modificar: Negado
                    elif insira == 3:
                        while True:
                            signal.signal(signal.SIGINT, signal.SIG_IGN)
                            pingar_nick = input_slow(branco() + "\nColoque o Nick exato do alvo aqui: ").strip()
                            confirmar_nick = input_slow(branco() + f"\nConfirmar o Nick como {pingar_nick} (S/N ou 'cancelar'): ").strip()

                            if pingar_nick.capitalize() in cancelar or confirmar_nick in cancelar:
                                print_slow(amarelo() + "\nVoltando...\n")
                                break

                            if confirmar_nick.capitalize() in ("S","Sim"):
                                chamada_user = user(nick=pingar_nick)
                                if chamada_user == 4:
                                    return 4 
                                while True:
                                    novamente_nick = input_slow(branco() + "\nVocê quer continuar usando essas ferramentas (S/N): ").strip()
                                    if novamente_nick.capitalize() in ("S","Sim"):
                                        break
                                    elif novamente_nick.capitalize() in ("N","Não","Nao"):
                                        print_slow(amarelo() + "\nVoltando...\n")
                                        if chamada_user == 0:
                                            return 0 # Sucesso
                                        if chamada_user == 2:
                                            return 2 # Sem resultado - Cancelado improvisado
                                        return 2 # Cancelado
                                    else:
                                        print_slow(vermelho() + "\nErro, opção inválida.\n")
                                        continue
                                break
                            elif confirmar_nick.capitalize() in ("N","Não","Nao"):
                                    print_slow(amarelo() + "\nHm... Certo, vamos tentar novamente.\n")
                                    continue
                            else: 
                                print_slow(vermelho() + "\nErro, opção inválida.\n")
                                continue
                        continue
                
                # Tratamento de erro em caso STR:
                # Modificar: Negado
                except ValueError as value_error_d:
                    print_slow(vermelho() + "\nErro, o campo só aceita números, tente novamente.\n")
                    print_slow(amarelo() + f"\nDetalhes do erro: {value_error_d}\n")
                    continue

        # Tratamento Falha Fatal:
        # Modificar: Negado
        except Exception as erro_fatal_d_tres:
            print_slow(vermelho() + f"\n\n\n\nERRO GRAVE! CÓDIGO 5 ('d_três'), FALHA FATAL: {erro_fatal_d_tres}\n\n\n\n")
            return 1 # Falha

# Tratamento Falha Fatal Cruel:
# Modificar: Negado  
except Exception as erro_cruel_d_três:
    def erro_d_tres_desconhecido():
        print(f"\n\n\n\nERRO DESCONHECIDO! CÓDIGO 5 ('d_tres'), FALHA FATAL CRUEL: {erro_cruel_d_três}\n\n\n\n")
        return 6 # Desconhecido
    
# VERIFICADO: TUDO CERTO - FINALIZADO - V1.
# VERIFICADO: TUDO CERTO - ATUALIZADO - V2.
# VERIFICADO: TUDO CERTO - ATUALIZADO - V3.
# VERIFICADO: TUDO CERTO - ATUALIZADO - V4.
# VERIFICADO: TUDO CERTO - ATUALIZADO - V5.
