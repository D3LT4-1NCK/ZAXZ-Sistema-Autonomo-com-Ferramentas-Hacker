# CÓDIGO 4 - OPÇÃO 2
# Possíveis retornos: 0, 1, 2, 6
# V.1 - Cada versão de cada código que não faça parte do sistema principal contribui em 0.1+ da versão principal.

# Bloco de inicialização:
# Modificar: Proibido
try:
    from z_bibliotecas import *
    from a_estilos import *
    block()
    def dois():
        try:
            block()
            class Pessoa():
                
                # Init:
                # Modificar: Negado
                def __init__(self, nome=None, id=None, numeracao=None):
                    self.nome = nome
                    self.id = id
                    self.numeracao = numeracao
                    self.erro_nome = 0
                    self.erro_impossivel = 0
                    
                    # Verificar nome:
                    # Modificar: Negado
                    try:
                        if nome == None:
                                self.erro_nome = 1
                        elif len(nome) >= 22:
                            print_slow(amarelo() + f"\nHm... O nome é grande demais, modificamos para um outro nome.\n")
                            print_slow(amarelo() + f"Você pode arrumar isso no código depois!\n")
                            self.erro_nome = 1
                        elif len(nome) == 0:
                            print_slow(amarelo() + f"\nHm... O nome é curto demais, modificamos para um outro nome.\n")
                            print_slow(amarelo() + f"Você pode arrumar isso no código depois!\n")
                            self.erro_nome = 1
                    except ValueError as erro_class_nome:
                        print_slow(vermelho() + "\nErro grave, o nome não pode ser 'int' (coloque entre aspas).\n")
                        print_slow(vermelho() + f"\nDetalhes do erro: {erro_class_nome}\n")
                        self.erro_impossivel = 1

                    # Verificar id:
                    # Modificar: Negado
                    try:
                        if id == None:
                            print_slow(vermelho() + f"\nPrecisamos de um id, impossível prosseguir sem (o 'id=' está como '{numeracao}').\n")
                            self.erro_impossivel = 1
                        elif int(len(id)) <=14 or int(len(id)) >=22:
                            print_slow(vermelho() + "\nO ID é pequeno/grande demais, se trata de um ID falso, impossível prosseguir.\n")
                            self.erro_impossivel = 1
                    except ValueError as erro_class_id:
                        print_slow(vermelho() + "\nErro grave, numeração só pode conter números.\n")
                        print_slow(vermelho() + f"\nDetalhes do erro: {erro_class_id}\n")
                        self.erro_impossivel = 1

                    # Verificar numeração:
                    # Modificar: Negado
                    try:
                        if numeracao == None:
                            print_slow(vermelho() + f"\nPrecisamos de uma numeração, impossível prosseguir sem (a 'numeração=' está como '{numeracao}').\n")
                            self.erro_impossivel = 1
                        elif int(len(numeracao)) > 13:
                            print_slow(vermelho() + "\nPrecisamos de uma numeração válida, impossível prosseguir sem.\n")
                            self.erro_impossivel = 1
                        elif int(len(numeracao)) == 0:
                            print_slow(vermelho() + "\nPrecisamos de uma numeração válida, impossível prosseguir sem.\n")
                            self.erro_impossivel = 0
                    except ValueError as erro_class_numeracao:
                        print_slow(vermelho() + "\nErro grave, na numeração só pode conter números.\n")
                        print_slow(amarelo() + f"\nDetalhes do erro: {erro_class_numeracao}\n")

                    if self.erro_nome == 1:
                        self.nome=f"User {numeracao}"
            
            # Verificar e criar lista de nomes:
            # Modificar: Restrito (Apenas dentro da lista)
            try:
                pessoas = [
                    # Exemplo:
                    # Pessoa(nome="Maria", id="9999999999999", "numeracao="1")
                    Pessoa(nome="Pessoa A", id="9999999999999", numeracao="1"),
                    Pessoa(nome="Pessoa B", id="9999999999999", numeracao="2")
                ]
            except Exception:
                print_slow(vermelho() + "\nErro crítico! Impossível continuar, verifique se os campos estão como no exemplo.\n")
                return 1 # Falha
            
            # Detecta duplicatas:
            # Modificar: Negado
            if len(set(c.numeracao for c in pessoas)) != len(pessoas) or len(set(c.id for c in pessoas)) != len(pessoas) or len(set(c.nome for c in pessoas)) != len(pessoas):
                    print_slow(vermelho() + "\nDados repetidos detectados!\n")
                    print_slow(vermelho() + "\nImpossível continuar.\n")
                    return 1 # Falha
            
            # Detecta erros impossíveis:
            # Modificar: Negado
            for coisa in pessoas:
                if coisa.erro_impossivel == 1:
                    print_slow(vermelho() + "\nErro, falha impossível detectada.\n")
                    return 1 # Falha
                else:
                    pass
            
            # Execução:
            # Modificar: Negado
            print_slow(amarelo() + "\nAtenção: Isso enviará uma mensagem real para a pessoa que você escolher.")
            print_slow(branco() + "Enviarei uma mensagem para uma dessas pessoas: \n")
            for coisa in pessoas:
                print_slow(branco() + f"\n{coisa.numeracao}- {coisa.nome}\n")
            while True:
                try:
                    insira = int(input_slow(branco() + "\nInsira (Aceita apenas números/'99' para voltar ao sistema base): "))
                    if insira == 99:
                        print_slow(amarelo() + "\nVoltando...\n")
                        return 2 # Cancelado
                    if insira < 1 or insira > len(pessoas):
                        print_slow(vermelho() + "\nInsira um número válido.\n")
                        continue
                except Exception:
                    print_slow(vermelho() + "\nErro grave, no campo só pode conter números.\n")
                    continue
                certeza = input_slow(amarelo() + f"\nProsseguir no {insira} (S/N)?\n(Para voltar ao sistema base, digite 'cancelar'): ").strip().capitalize()
                if certeza == "N":
                    print_slow(amarelo() + "\nRevertendo...\n")
                    continue
                elif certeza == "S":
                    id_coletado = pessoas[insira-1].id
                    numeracao_coletada = pessoas[insira-1].numeracao
                    break
                elif certeza in cancelar:
                    return 2 # Cancelado
                else:
                    print_slow(vermelho() + "\nNão compreendido, vamos reverter...\n")
                    continue

            # Escrever mensagem:
            # Modificar: Negado
            while True:
                mensagem = input_slow(branco() + "\nEscreva a mensagem que você quer enviar (4 - 1999 caracteres) (ou 'cancelar' para voltar ao sistema base): ")
                if len(mensagem) >=2000 or len(mensagem) <=3:
                    print_slow(vermelho() + "\nBarreira de caracteres quebrada, tente novamente.\n")
                    print_slow(vermelho() + f"\nPara não ter que reescrever tudo, sua mensagem foi: {mensagem}.\n")
                    continue
                elif mensagem.capitalize() in cancelar:
                    print_slow(amarelo() + "\nVoltando...\n")
                    return 2 # Cancelado
                else:
                    print_slow(verde() + "\nMensagem anotada!\n")
                    break

            # Automação:
            # Modificar: Permitido
            signal.signal(signal.SIGINT, signal.SIG_DFL)
            print_slow(amarelo() + "\n\nAtenção: Em casos de falha grave, mate o processo usando 'CTRL' + 'C' (no terminal).\n\nAtenção: Não use o seu teclado/mouse durante o processo.")
            print_slow(vermelho() + "\nAtenção: Certifique-se de que o 'CapsLock' está DESLIGADO.")
            dormir(5.5)
            print_slow(branco() + "\nIniciando...\n")
            print_slow(verde() + "\nAbrindo discord...\n")

            pyautogui.press("win")
            pyautogui.write("firefox")
            pyautogui.press("enter")
            dormir(4.5)
            pyautogui.hotkey("ctrl","shift","p") # Por que em guia anônima? -> Para que caso você não esteja logado, ele logue automaticamente.
            dormir(1)
            pyautogui.hotkey("ctrl","t")
            dormir(1)
            
            print_slow(verde() + f"\nEntrando no perfil '{numeracao_coletada}- {id_coletado}'...\n")
            dormir(2)
            pyautogui.write("https://discord.com/login")
            dormir(0.05)
            pyautogui.press("enter")
            dormir(4.5)
            pyautogui.write("seu-email@gmail.com") # Seu EMAIL.
            pyautogui.press("enter")
            pyautogui.write("123456") # Sua SENHA.
            pyautogui.press("enter")
            dormir(2)
            pyautogui.hotkey("ctrl","w")
            dormir(1)
            pyautogui.write(f"https://discord.com/channels/@me/{id_coletado}")
            pyautogui.press("enter")
            dormir(6.5)
            pyautogui.write(mensagem)
            pyautogui.press("enter")

            print_slow(verde() + "\nConcluído.\n")
            pyautogui.keyDown("alt")
            dormir(0.5)
            pyautogui.press("tab")
            dormir(0.5)
            pyautogui.press("right")
            dormir(0.5)
            pyautogui.press("enter")
            return 0 # Sucesso
        
        # Tratamento Falha Fatal:
        # Modificar: Negado
        except Exception as erro_fatal_c_dois:
            print_slow(vermelho() + f"\n\n\n\nERRO GRAVE! CÓDIGO 4 ('c_dois'), FALHA FATAL: {erro_fatal_c_dois}\n\n\n\n")
            return 1 # Falha

# Tratamento Falha Fatal Cruel:
# Modificar: Negado  
except Exception as erro_cruel_c_dois:
    def erro_c_dois_desconhecido():
        print(f"\n\n\n\nERRO DESCONHECIDO! CÓDIGO 4 ('c_dois'), FALHA FATAL CRUEL: {erro_cruel_c_dois}\n\n\n\n")
        return 6 # Desconhecido
    
# VERIFICADO: TUDO CERTO - FINALIZADO - V1.
