# CÓDIGO 6 - OPÇÃO 4
# V.1 - Cada versão de cada código que não faça parte do sistema principal contribui em 0.1+ da versão principal.
# Possíveis retornos: 0, 1, 2, 4, 6, 7

# Bloco de inicialização:
# Modificar: Proibido
try:
    from z_bibliotecas import *
    from a_estilos import *
    block()
    def quatro():
        try:
            block()

            # Sistema de anotações:
            # Modificar: Negado
            print_slow(branco() + "\nVamos anotar uma informação detalhada sobre um alvo em um documento '.txt'.\n")
            print_slow(branco() + "\nAperte 'Enter' para pular etapas (caso você não tenha certa informação).\n")

            def pegar_informacoes():
                global informacoes
                pingar_pulamento = 0
                while True:
                    nome = input_slow(branco() + "Digite o nome/nick do alvo: ").strip().replace("  ", " ")
                    if nome.capitalize() in cancelar:
                        print_slow(amarelo() + "\nVoltando...\n")
                        return 2 # Cancelado
                    elif nome == "":
                        print_slow(verde() + "\nNome pulado.\n")
                        nome = "N/A"
                        pingar_pulamento += 1
                        break
                    elif len(nome) <= 3 or len(nome) >= 39:
                        print_slow(vermelho() + "\nNome curto/grande demais.\n")
                        continue
                    else:
                        print_slow(verde() + "\nAnotado.\n")
                        break

                while True:
                    try:
                        idade = input_slow(branco() + "Digite a idade do alvo (ou 'Enter' para pular): ").strip()
                        if idade.capitalize() in cancelar:
                            print_slow(amarelo() + "\nVoltando...\n")
                            return 2 # Cancelado
                        elif idade == "":
                            print_slow(verde() + "\nIdade pulada.\n")
                            idade = "N/A"
                            pingar_pulamento += 1
                            break
                        elif int(idade) <= 12 or int(idade) >= 101:
                            print_slow(vermelho() + "\nIdade inválida, insira uma idade realista.\n")
                            continue
                        else:
                            print_slow(verde() + "\nAnotada.\n")
                            break
                    except ValueError:
                        print_slow(vermelho() + "\nO campo só aceita 'Enter' ou números.\n")
                        continue

                while True:
                    sexo = input_slow(branco() + "Digite o sexo do alvo (ou 'Enter' para pular): ").strip().capitalize()
                    if sexo.capitalize() in cancelar:
                        print_slow(amarelo() + "\nVoltando...\n")
                        return 2 # Cancelado
                    elif sexo == "":
                        print_slow(verde() + "\nSexo pulado.\n")
                        sexo = "N/A"
                        pingar_pulamento += 1
                        break
                    elif len(sexo) <= 3 or len(sexo) >= 14:
                        print_slow(vermelho() + "\nInsira um sexo válido (Masculino/Feminino).\n")
                        continue
                    elif sexo in ("Masculino","Masc","Homem","Feminino","Fem","Mulher"):
                        print_slow(verde() + "\nAnotado.\n")
                        break
                    else:
                        print_slow(vermelho() + "\nInsira um sexo válido (Masculino/Feminino).\n")
                        continue

                while True:
                    loc = input_slow(branco() + "Digite a localização do alvo (ou 'Enter' para pular): ").strip().capitalize().replace("  ", " ")
                    if loc.capitalize() in cancelar:
                        print_slow(amarelo() + "\nVoltando...\n")
                        return 2 # Cancelado
                    elif loc == "":
                        print_slow(verde() + "\nLocalização pulada.\n")
                        loc = "N/A"
                        pingar_pulamento += 1
                        break
                    elif len(loc) <= 1 or len(loc) >= 49:
                        print_slow(vermelho() + "\nLocalização curta/grande demais.\n")
                        continue
                    else:
                        print_slow(verde() + "\nAnotado.\n")
                        break
                
                while True:
                    ip = input_slow(branco() + "Digite o ip do alvo (ou 'Enter' para pular): ").strip()
                    
                    if ip.capitalize() in cancelar:
                        print_slow(amarelo() + "\nVoltando...\n")
                        return 2 # Cancelado
                    elif ip == "":
                        print_slow(verde() + "\nIP pulado.\n")
                        ip = "N/A"
                        pingar_pulamento += 1
                        break

                    try:
                        ipaddress.ip_address(ip)
                    except ValueError:
                        print_slow(vermelho() + "\nInsira um IP válido.\n")
                        continue
                    print_slow(verde() + "\nAnotado.\n")
                    break

                while True:
                    email = input_slow(branco() + "Digite o email do alvo (ou 'Enter' para pular): ").strip()
                    if email.capitalize() in cancelar:
                        print_slow(amarelo() + "\nVoltando...\n")
                        return 2 # Cancelado
                    elif email == "":
                        print_slow(verde() + "\nEmail pulado.\n")
                        email = "N/A"
                        pingar_pulamento += 1
                        break
                    elif " " in email:
                        print_slow(vermelho() + "\nInsira um email válido.\n")
                        continue
                    elif email.startswith("."):
                        print_slow(vermelho() + "\nInsira um email válido.\n")
                        continue
                    elif "@" not in email or "." not in email:
                        print_slow(vermelho() + "\nInsira um email válido.\n")
                        continue
                    elif len(email) <= 9 or len(email) >= 53:
                        print_slow(vermelho() + "\nEmail curto/grande demais.\n")
                        continue
                    else:
                        print_slow(verde() + "\nAnotado.\n")
                        break

                while True:
                    senha = input_slow(branco() + "Digite a senha do alvo (ou 'Enter' para pular): ").strip()
                    if senha.capitalize() in cancelar:
                        print_slow(amarelo() + "\nVoltando...\n")
                        return 2 # Cancelado
                    elif senha == "":
                        print_slow(verde() + "\nSenha pulada.\n")
                        senha = "N/A"
                        pingar_pulamento += 1
                        break
                    elif len(senha) <= 5 or len(senha) >= 39:
                        print_slow(vermelho() + "\nSenha curta/grande demais.\n")
                        continue
                    else:
                        print_slow(verde() + "\nAnotada.\n")
                        break
                
                while True:
                    infos = input_slow(branco() + "Digite quaisquer informações extras sobre o alvo (ou 'Enter' para pular): ").strip().replace("  ", " ")
                    if infos.capitalize() in cancelar:
                        print_slow(amarelo() + "\nVoltando...\n")
                        return 2 # Cancelado
                    elif infos == "":
                        print_slow(verde() + "\nInformações extras puladas.\n")
                        infos = "N/A"
                        pingar_pulamento += 1
                        break
                    elif len(infos) <= 3:
                        print_slow(vermelho() + "\nInformações curtas demais.\n")
                        continue
                    elif len(infos) >= 903:
                        print_slow(vermelho() + "\nInformações grandes demais.\n")
                        print_slow(branco() + f"\nPara não perder o que você tinha escrito, aqui está o campo anterior: \n'\n{infos}\n'\n", delay=0.001)
                        continue
                    else:
                        print_slow(verde() + "\nInformações anotadas.\n")
                        break                    

                if pingar_pulamento == 8:
                    print_slow(vermelho() + "\nBoa tentativa, malandrão! O sistema não vai criar um arquivo com informações vazias.\nTe retornando a força...\n")
                    return 2 # Sem resultado - Cancelado improvisado

                informacoes = f"\n\nNome: {nome}\nIdade: {idade}\nSexo: {sexo}\nLocalização: {loc}\nIp: {ip}\nEmail: {email}\nSenha: {senha}\nInformações Extras: {infos}\n\n"

            if pegar_informacoes() == 2:
                return 2 # Cancelado
            print_slow(branco() + f"\nVerifique as informações: {informacoes}")

            confirmar = input_slow(branco() + "\nConfirmar essas informações (S/N): ").strip().capitalize()

            while True:
                if confirmar in cancelar or confirmar in ("N","Não","Nao"):
                    while True:
                        novamente = input_slow(branco() + "\nQuer escrever novamente ou sair da ferramenta (Novamente/Sair): ").strip().capitalize()
                        if novamente in cancelar or novamente in ("Sair","Voltar","2"):
                            return 2 # Cancelado
                        elif novamente in ("Novamente","De novo","Tentar novamente","1"):
                            return 7 # Sucesso + Tentar novamente
                        else:
                            print_slow(vermelho() + "\nNão compreendido, tente novamente.\n")
                            continue
                elif confirmar in ("S","Sim"):
                    while True:
                        nomeie = input_slow(branco() + "\nQue nome você quer dar para o arquivo? Coloque aqui (sem '.txt'): ")
                        if glob.glob(os.path.expanduser(f"~/{nomeie}.txt")):
                            print_slow(vermelho() + "\nJá existe um arquivo com esse nome.\n")
                            continue
                        elif "/" in nomeie:
                            print_slow(vermelho() + "\nOpa! O Linux não aceita esse tipo de nome para de arquivos ou documentos.\n")
                            continue
                        elif len(nomeie) <= 3 or len(nomeie) >= 39:
                            print_slow(vermelho() + "\nNome grande/pequeno demais.\n")
                            continue
                        else:                
                            with open(os.path.expanduser(f"~/{nomeie}.txt"), "w") as anotar:
                                anotar.write(f"{informacoes}")
                            print_slow(verde() + "\nCriado com sucesso.\n")
                            while True:
                                novamente_2 = input_slow(branco() + "\nQuer fazer mais um (S/N): \n").strip().capitalize()
                                if novamente_2 in cancelar or novamente_2 in ("N","Nao","Não"):
                                    return 0 # Sucesso
                                elif novamente_2 in ("S","Sim"):
                                    return 7 # Sucesso + Tentar novamente
                                else:
                                    print_slow(vermelho() + "\nNão compreendido, tente novamente.\n")
                                    continue
                else:
                    print_slow(vermelho() + "\nNão compreendido, tente novamente.\n")
                    continue

        # Tratamento Falha Fatal:
        # Modificar: Negado
        except Exception as erro_fatal_e_quatro:
            print_slow(vermelho() + f"\n\n\n\nERRO GRAVE! CÓDIGO 6 ('e_quatro'), FALHA FATAL: {erro_fatal_e_quatro}\n\n\n\n")
            return 1 # Falha

# Tratamento Falha Fatal Cruel:
# Modificar: Negado 
except Exception as erro_cruel_e_quatro:
    def erro_e_quatro_desconhecido():
        print(f"\n\n\n\nERRO DESCONHECIDO! CÓDIGO 6 ('e_quatro'), FALHA FATAL CRUEL: {erro_cruel_e_quatro}\n\n\n\n")
        return 6 # Desconhecido
    
# VERIFICADO: TUDO CERTO - FINALIZADO - V1.
