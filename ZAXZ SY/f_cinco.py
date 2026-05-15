# CÓDIGO 7 - OPÇÃO 5
# V.1 - Cada versão de cada código que não faça parte do sistema principal contribui em 0.1+ da versão principal.
# Possíveis retornos: 0, 1, 2, 6

# Bloco de inicialização:
# Modificar: Proibido
try:
    from z_bibliotecas import *
    from a_estilos import *
    block()
    def cinco():
        try:
            block()

            # Sistema de seleção:
            # Modificar: Negado
            print_slow(branco() + "\nVamos sortear uma tarefa para você fazer hoje!\n")
            print_slow(branco() + "\n(Caso queira cancelar basta digitar 'cancelar'!)\n")
            lista_tarefas = []
            while True:
                
                selecionar = input_slow(branco() + "\nSelecione a tarefa UM que você quer que seja roletada (Necessário): ").strip().title()
                if selecionar.capitalize() in cancelar:
                    print_slow(amarelo() + "\nVoltando...\n")
                    return 2 # Cancelado
                elif selecionar in lista_tarefas:
                    print_slow(vermelho() + "\nEssa tarefa já existe.\n")
                    continue
                elif len(selecionar) <= 3 or len(selecionar) >= 35:
                    print_slow(vermelho() + "\nTarefa curta/grande demais.\n")
                    continue
                else:
                    print_slow(verde() + "\nTarefa anotada.\n")
                    lista_tarefas.append(selecionar)
                    break

            while True:
                selecionar_dois = input_slow(branco() + "\nSelecione a tarefa DOIS que você quer que seja roletada (Necessário): ").strip().title()
                if selecionar_dois.capitalize() in cancelar:
                    print_slow(amarelo() + "\nVoltando...\n")
                    return 2 # Cancelado
                elif selecionar_dois in lista_tarefas:
                    print_slow(vermelho() + "\nEssa tarefa já existe.\n")
                    continue
                elif len(selecionar_dois) <= 3 or len(selecionar_dois) >= 35:
                    print_slow(vermelho() + "\nTarefa curta/grande demais.\n")
                    continue
                else:
                    print_slow(verde() + "\nTarefa anotada.\n")
                    print_slow(verde() + "\nAgora você pode pressionar 'Enter' para sortear, ou pode ficar adicionando mais coisas.\n")
                    lista_tarefas.append(selecionar_dois)
                    break

            while True:
                selecionar_coisas = input_slow(branco() + "\nSelecione mais uma tarefa que você quer que seja roletada: ").strip().title()
                if selecionar_coisas.capitalize() in cancelar:
                    print_slow(amarelo() + "\nVoltando...\n")
                    return 2 # Cancelado
                elif selecionar_coisas in lista_tarefas:
                    print_slow(vermelho() + "\nEssa tarefa já existe.\n")
                    continue
                elif len(selecionar_coisas) <= 3 or len(selecionar_coisas) >= 35:
                    print_slow(vermelho() + "\nTarefa curta/grande demais.\n")
                    continue
                elif selecionar_coisas == "":
                    print_slow(verde() + "\nVamos iniciar...\n")
                    dormir(2)
                    break
                else:
                    print_slow(verde() + "\nTarefa anotada.\n")
                    print_slow(verde() + "\nCaso queira iniciar o sorteio, basta apertar 'Enter'.\n")
                    lista_tarefas.append(selecionar_coisas)
                    continue

            randomizar = random.choice(lista_tarefas)
            print_slow(verde() + f"\nA tarefa selecionada foi... -> '{randomizar}'!\n")
            print_slow(verde() + "\nFinalizado.\n")
            return 0

        # Tratamento Falha Fatal:
        # Modificar: Negado
        except Exception as erro_fatal_f_cinco:
            print_slow(vermelho() + f"\n\n\n\nERRO GRAVE! CÓDIGO 7 ('f_cinco'), FALHA FATAL: {erro_fatal_f_cinco}\n\n\n\n")
            return 1 # Falha

# Tratamento Falha Fatal Cruel:
# Modificar: Negado 
except Exception as erro_cruel_f_cinco:
    def erro_f_cinco_desconhecido():
        print(f"\n\n\n\nERRO DESCONHECIDO! CÓDIGO 7 ('f_cinco'), FALHA FATAL CRUEL: {erro_cruel_f_cinco}\n\n\n\n")
        return 6 # Desconhecido
    
# VERIFICADO: TUDO CERTO - FINALIZADO - V1.
