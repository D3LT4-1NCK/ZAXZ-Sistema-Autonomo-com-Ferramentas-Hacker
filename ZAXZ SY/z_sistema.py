# CÓDIGO ORIGINAL - SISTEMA.
# V.1.6 [BETA] - PT-BR-1.0.
# Discord do fundador: floppzh

# ATENÇÃO: Ferramenta de automatação com ferramentas de ataque, use por sua conta e risco.
# Nota: Esse é meu primeiro grande projeto, então caso você tenha sugestões/achou problemas, por favor, me mande.
# Nota: Caso queira ajudar com projetos parecidos, estou a desposição para criar uma equipe organizada, basta me mandar mensagem no discord.

# Retornos Possíveis (Funciona para todos os códigos):
# 0 = Sucesso
# 1 = Falha (Quem mandou pede para bloquear o comando - Selar)
# 2 = Cancelou
# 3 = Código Morto (Não responde - Nem abre)
# 4 = Arquivo Corrompido (Quem mandou pede para bloquear o comando - Selar)
# 5 = Sucesso + Comando fechado (Quem mandou pede para bloquear o comando - Fechar)
# 6 = Indefinido (Erro desconhecido)
# 7 = Sucesso + Iniciar novamente (Quem mandou pede reiniciar a própria ferramenta)

# Detecções dos erros mais perigosos:
# Modificar: Negado
try:
    from z_bibliotecas import *
    from a_estilos import *
    from b_um import *
    from c_dois import *
    from d_tres import *
    from e_quatro import *
    from f_cinco import *
    data = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) # Pega a data do ligamento sem os milésimos.
    signal.signal(signal.SIGINT, signal.SIG_IGN) # Bloqueia CTRL + C para o código todo até que seja liberado.
    block()
except Exception as erro:
    print(f"\nERRO CATASTRÓFICO: Os códigos estão com problemas em se conectar. Reinstale o sistema.\n")
    print(f"\nDetalhes do erro: {erro}.\n")
    exit()

arquivos = ["z_bibliotecas.py", "a_estilos.py", "b_um.py", "c_dois.py", "d_tres.py", "e_quatro.py", "f_cinco.py", "0_ZAXZ DIR.txt","ZAXZ FERRAMENTAS"]
if os.path.exists(os.path.expanduser("~/ZAXZ SY/a_estilos.py")):
    for coisa in arquivos:
        if not os.path.exists(os.path.expanduser(f"~/ZAXZ SY/{coisa}")):
            print_slow(vermelho() + f"\nERRO CATASTRÓFICO: Código '{coisa}' não encontrado. Reinstale o sistema.\n")
            reinstale_o_sistema()
elif not os.path.exists(os.path.expanduser("~/ZAXZ SY/a_estilos.py")):
    for coisa in arquivos:
        if not os.path.exists(os.path.expanduser(f"~/ZAXZ SY/{coisa}")):
            print(f"\nERRO CATASTRÓFICO: Código '{coisa}' não encontrado. Reinstale o sistema.\n")
            reinstale_o_sistema()

# Definições de segurança:
# Modificar: Negado
pings = {
    "pingar_fechamento_b_um": False,
    "pingar_selamento_b_um": False,
    "pingar_selamento_c_dois": False,
    "pingar_selamento_d_tres": False,
    "pingar_selamento_e_quatro": False,
    "pingar_selamento_f_cinco": False,
    "pingar_novamente_e_quatro": False,
}

# Código fonte:
# Modificar: Negado
def iniciar(nome=None):

    # Caso nome inválido, será alterado para host:
    try:
        if len(nome) >= 28 or len(nome) <= 1:
            nome = "host"
            with open(os.path.expanduser("~/ZAXZ SY/0_NOME.txt"), "w"):
                pass
    except Exception:
        if isinstance(nome, int):
            nome = "host"
            with open(os.path.expanduser("~/ZAXZ SY/0_NOME.txt"), "w"):
                pass
        elif nome == None:
            nome = "host"
            with open(os.path.expanduser("~/ZAXZ SY/0_NOME.txt"), "w"):
                pass
    
    # Tela inicial:
    print_slow(branco() + f"\nBoas vindas, {nome.title()}.\nIniciando programa na data de: " + data)
    print_slow(branco() + "\nO que iremos fazer?\n")
    print_menu()
    while True:
        block()

        # Bloqueamentos seguros sempre que voltar:
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        block()

        # Sistema de pingamentos para coisas que devem fechar ao serem usadas uma vez ou apresentar falhas formidáveis:
        receber_fechamento_b_um = pings["pingar_fechamento_b_um"]

        receber_selamento_b_um = pings["pingar_selamento_b_um"]
        receber_selamento_c_dois = pings["pingar_selamento_c_dois"]
        receber_selamento_d_tres = pings["pingar_selamento_d_tres"]
        receber_selamento_e_quatro = pings["pingar_selamento_e_quatro"]
        receber_selamento_f_cinco = pings["pingar_selamento_f_cinco"]

        receber_novamente_e_quatro = pings["pingar_novamente_e_quatro"]

        # Detecção de falha no código dois:
        try:
            resultado_estilo = check_a_estilos()
        except Exception:
            resultado_estilo = 3 # Morto
        
        if resultado_estilo == 3:
            print(f"\nFalha Fatal detectada no código dois (a_estilos).\n")
            print(f"\nTodo o sistema depende do código dois para funcionar com fluidez; recomendamos que você reinstale o sistema.\n")
            exit("\nEncerrado por segurança.\n")

        # Sistema de direcionamentos:
        try:
            insira = int(input_slow(branco() + "\nInsira: ", delay=0.001))

            # LEVA PARA CÓDIGO TRÊS (b_um):
            if insira == 1 or insira == 100:
                
                if receber_fechamento_b_um == True:
                    print_slow(vermelho() + "\nComando bloqueado, você já usou ele antes.\n")
                    print_slow(vermelho() + "\nCaso queira usar a força, use '100'.\n")
                    print_slow(branco() + "\nO que quer fazer agora?\n")
                    print_menu()
                    continue
                
                if receber_selamento_b_um == True:
                    print_selado()
                    continue

                print_slow(branco() + "\nCarregando...", delay=0.01)
                
                return_check(resultados=um(), qual="b_um", pings=pings)

            # LEVA PARA CÓDIGO QUATRO (c_dois):
            elif insira == 2:
                if receber_selamento_c_dois == True:
                    print_selado()
                    continue
                 
                print_slow(branco() + "\nCarregando...", delay=0.01)

                return_check(resultados=dois(), qual="c_dois", pings=pings)


            # LEVA PARA CÓDIGO CINCO (d_tres):
            elif insira == 3:
                if receber_selamento_d_tres == True:
                    print_selado()
                    continue

                print_slow(branco() + "\nCarregando...", delay=0.01)

                return_check(resultados=tres(), qual="d_tres", pings=pings)

            # LEVA PARA O CÓDIGO SEIS (e_quatro):
            elif insira == 4:
                if receber_selamento_e_quatro == True:
                    print_selado()
                    continue

                else:
                    print_slow(branco() + "\nCarregando...", delay=0.01)

                    return_check(resultados=quatro(), qual="e_quatro", pings=pings)
                    while True:
                        if pings["pingar_novamente_e_quatro"] == True:
                            print_slow(branco() + "\nCarregando...", delay=0.01)
                            pings["pingar_novamente_e_quatro"] = False

                            return_check(resultados=quatro(), qual="e_quatro", pings=pings)
                        else:
                            break

            # LEVA PARA O CÓDIGO SETE (f_cinco):
            elif insira == 5:
                if receber_selamento_f_cinco == True:
                    print_selado()
                    continue
                 
                print_slow(branco() + "\nCarregando...", delay=0.01)

                return_check(resultados=cinco(), qual="f_cinco", pings=pings)

            # Encerramento do sistema - desligamento correto:
            elif insira == 6:
                print_slow(amarelo() + "\nEncerrando sistema...\n", delay=0.01)
                exit()

            else:
                print_slow(vermelho() + "\nErro, escolha uma opção válida!\n", delay=0.03)
            
            try:
                if erro_b_um_desconhecido() == 6:
                    exit()
                if erro_c_dois_desconhecido() == 6:
                    exit()
                if erro_d_tres_desconhecido() == 6:
                    exit()
                if erro_e_quatro_desconhecido() == 6:
                    exit()
                if erro_f_cinco_desconhecido() == 6:
                    exit()
            except Exception:
                pass

        except ValueError as value_error_sistema:
            print_slow(vermelho() + "\nErro, o campo só aceita números, tente novamente.\n")
            print_slow(amarelo() + f"\nDetalhes do erro: {value_error_sistema}\n")

# Sistema de nome:
# Modificar: Proibido
if os.path.exists(os.path.expanduser("~/ZAXZ SY/0_NOME.txt")):
    with open(os.path.expanduser("~/ZAXZ SY/0_NOME.txt"), "r") as nome:
        nome_final = nome.read()
else:
    nome_final = input_slow(branco() + "\nDigite seu nome: ")
    with open(os.path.expanduser("~/ZAXZ SY/0_NOME.txt"), "w") as nomear:
        nomear.write(nome_final)

# Tela de Entrada:
# Modificar: Negado
os.system("clear")
print(branco() + figlet_format("ZAXZ"))
print_slow(branco() + "\nSistema ZAXZ.\nVersão: 1.5\nIdioma: PT-BR-1.0\nCaso tenha sugestões/queira fazer parte, discord do criador: floppzh", delay=0.02)
print_slow(branco() + "--------------------------------------------------------------------", delay=0.01)

# Inicialização/Partida absoluta do sistema:
# Modificar: Proibido
try:
    iniciar(nome_final)
except Exception:
    dormir(5)
    print_slow(vermelho() + "\nVocê caiu no erro mais raro do sistema, impossível continuar...\n")
    exit(branco() + "\nMande uma mensagem para esse perfil no discord caso queira que isso seja reparado: floppzh\n")

# VERIFICADO: TUDO CERTO - FINALIZADO.
