import sys


class Sistema_bancario:

    def __init__(self):
    
        self.SAQUES_POR_DIA = 3
        self.VALOR_DE_SAQUE_DIARIO = 500
        self.contador_de_saque = 0
        self.contador_de_deposito = 0
        self.extrato = 0
        self.deposito = 0
        self.saque = 0
        self.agencia = '0001'
        self.conta = 0
        self.ultimo_saque = 0
        self.ultimo_deposito = 0
        self.clientes_cadastrados = {}
        self.contas_cadastradas = {}
        
        
 
    
    def cadastrar_cliente(self, nome, data_nascimento, endereco, cpf): 


        self.nome = nome
        self.endereco = endereco
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        campos_vazios = []



        if not self.nome: 
             campos_vazios.append("nome")
        if not self.endereco: 
             campos_vazios.append("endereco")
        if not self.data_nascimento: 
             campos_vazios.append("data_nascimento")
        if not self.cpf: 
             campos_vazios.append("cpf")

        
        if campos_vazios:
            print("\n @@ Campos obrigatórios vazios: \n")
            for x in campos_vazios:
                print(x)
            print()
            
        else:
            if not cpf in self.clientes_cadastrados: 
                
                self.clientes_cadastrados[cpf] = {
                    'nome': nome,
                    'data_nascimento': data_nascimento,
                    'endereco': endereco
                }

                print("\n ** Cliente cadastrado com sucesso!\n")

            else: 
                print("\n @@ O cliente já possui cadastro.\n")
        

        
        
        
        
        
        
    def cadastrar_conta_corrente(self, cpf): 
           
            self.contas_por_cliente = []
         
            if cpf in self.clientes_cadastrados: 
                    self.conta += 1

                    conta_info = {
                        
                        'agencia': self.agencia,
                        'conta': self.conta ,
                        'extrato': self.extrato, 
                        'contador_de_saque': self.contador_de_saque, 
                        'contador_de_deposito': self.contador_de_deposito, 
                        'ultimo_saque': self.ultimo_saque, 
                        'ultimo_deposito': self.ultimo_deposito, 
                        'VALOR_DE_SAQUE_DIARIO': self.VALOR_DE_SAQUE_DIARIO, 
                        'SAQUES_POR_DIA': self.SAQUES_POR_DIA
                        
                    }
                    
                    if cpf in self.contas_cadastradas:
                        
                        self.contas_cadastradas[cpf].append(conta_info)
                        print("\n ** Conta corrente criada com sucesso! \n")
                    else:

                        self.contas_cadastradas[cpf] = [conta_info]
                        print("\n ** Conta corrente criada com sucesso de novo! \n")


            else: 
                print("\n @@ Erro ao abrir conta. Cadastre-se primeiro \n")
            



            
    def ver_dados_da_conta(self, cpf): 
        

        if cpf in self.contas_cadastradas:
            cliente = self.clientes_cadastrados[cpf]
            for conta in self.contas_cadastradas[cpf]:
            
                print(f"""\n
                    ------------------------------------
                    --------- Dados da conta ----------- : 
                        Titular: {cliente['nome']}
                        Agencia: {conta['agencia']}
                        Conta: {conta['conta']}
                    ------------------------------------
                    --------- Movimentações ------------ 
                        Saldo em conta: {conta['extrato']}
                        Saques realizados: {conta['contador_de_saque']}
                        Ultimo valor sacado: {conta['ultimo_saque']}
                        Depositos realizados: {conta['contador_de_deposito']}
                        Ultimo valor depositado: {conta['ultimo_deposito']}
                    --------------########---------------
                \n """)
    
                if cpf in self.contas_por_cliente: 
                    for nova_conta in self.contas_por_cliente: 
                        print(nova_conta)
        else: 
            print("\n @@ Cliente não possui conta vinculada a este CPF. \n")





    def listar_contas(self): 
         
            
        if self.contas_cadastradas: 
            print("-------------------------------------------------")
            print("| * Titular                  | Agencia  |   Conta  | Saldo R$ |")
            print("-------------------------------------------------")
            
            for cpf, contas in self.contas_cadastradas.items():
                cliente = self.clientes_cadastrados[cpf]
                for conta in contas:
                    print(f"| {cliente['nome']: <27} | {conta['agencia']: <8} | {conta['conta']: <8} | {conta['extrato']: <9} |")
                
                print("-------------------------------------------------")
        else: 
            print("\n @@ Nenhuma conta cadastrada.")




    def sacar(self, cpf, numero_da_conta, valor):
        
        if cpf in self.contas_cadastradas:
            numero_da_conta = int(numero_da_conta) - 1
            contas_cliente = self.contas_cadastradas[cpf]
            
            if numero_da_conta >= len(contas_cliente) or numero_da_conta < 0:
                print("\n @@ Número da conta inválido.\n")
                return
            
            conta = contas_cliente[numero_da_conta]
    
            if valor > conta['extrato'] or valor <= 0:
                print("\n @@ Operação não permitida ou saldo insuficiente.\n")
            elif valor > conta['VALOR_DE_SAQUE_DIARIO']:
                print("\n @@ Você não pode sacar este valor\n")
            elif conta['contador_de_saque'] >= conta['SAQUES_POR_DIA']:
                print("\n @@ Limite de saque atingido. Volte amanhã\n")
            else:
                conta['extrato'] -= valor
                conta['contador_de_saque'] += 1
                conta['ultimo_saque'] = valor
                print(f"\n -- Valor de {valor} R$ sacado com sucesso\n")
        else:
            print("\n @@ CPF incorreto ou não vinculado a uma conta. \n")
    
    
        
        
            
    def depositar(self, cpf, numero_da_conta, valor):
        if cpf in self.contas_cadastradas:
            numero_da_conta = int(numero_da_conta) - 1
            contas_cliente = self.contas_cadastradas[cpf]
    
            if numero_da_conta >= len(contas_cliente) or numero_da_conta < 0:
                print("\n @@ Número da conta inválido.\n")
                return
            
            conta = contas_cliente[numero_da_conta]
    
            if valor <= 0:
                print("\n -- Valor não suportado\n")
            else:
                conta['extrato'] += valor
                conta['contador_de_deposito'] += 1
                conta['ultimo_deposito'] = valor
                print(f"\n -- Valor de {valor} R$ depositado em conta \n")
        else:
            print("\n @@ CPF incorreto ou não vinculado a uma conta. \n")
    
    
    
        
    def mostrar_extrato(self, cpf, numero_da_conta):
        if cpf in self.contas_cadastradas:
            numero_da_conta = int(numero_da_conta) - 1
            contas_cliente = self.contas_cadastradas[cpf]
    
            if numero_da_conta >= len(contas_cliente) or numero_da_conta < 0:
                print("\n @@ Número da conta inválido.\n")
                return
            
            conta = contas_cliente[numero_da_conta]
    
            print(f"\n -- Valor em conta: {conta['extrato']} R$\n")
        else:
            print("\n @@ CPF incorreto ou não vinculado a uma conta. \n")
    
    

    def menu_de_opcoes(self): 
        print(
            """\n
                ######### Menu de opcoes #############: 
                [1]-Saque 
                [2]-Deposito 
                [3]-Extrato
                [4]-Cadastrar cliente
                [5]-Abrir conta corrente
                [6]-Ver dados da conta
                [7]-Listar contas
                [8]-Sair 
                ######################################
            
    \n """)

        
        opcao = int(input("\n -> Insira a opcao desejada: "))

        while opcao:

           
            if opcao == 1: 
                cpf = input("Insira o CPF vinculado a conta: \n")
                numero_da_conta = input("\n Informe o numero da conta: \n")
                valor_de_saque = input("\n -> Insira o valor para saque: \n")
                self.sacar(cpf, int(numero_da_conta), float(valor_de_saque))
                self.menu_de_opcoes()

            if opcao == 2: 
                cpf = input("Insira o CPF vinculado a conta: \n")
                numero_da_conta = input("Informe o numero da conta: \n")
                valor_de_deposito = input("-> Insira o valor para deposito: \n") 
                self.depositar(cpf, int(numero_da_conta),float(valor_de_deposito))
                self.menu_de_opcoes()

            if opcao == 3: 
                cpf = input("Insira o CPF vinculado a conta: \n")
                numero_da_conta = input("Informe o numero da conta: \n")
                self.mostrar_extrato(cpf, numero_da_conta)
                self.menu_de_opcoes()

            if opcao == 4: 
                
                nome = input("\n-> Insira o seu nome completo: \n")
                data_nascimento = input("\n-> Informe sua data de nascimento no formato: (dd/mm/aa) \n")
                endereco = input("\n-> Informe o seu endereco no seguinte formato: (Logradouro, Numero - Bairro - Cidade/Estado)\n")
                cpf = input("\n-> Informe o seu CPF no formato: (123.456.789-09): \n")
                self.cadastrar_cliente(nome, data_nascimento, endereco, cpf)
                self.menu_de_opcoes()
            
            if opcao == 5: 
                cpf = input("\n ** Insira seu CPF para abrir uma conta corrente: \n")
                self.cadastrar_conta_corrente(cpf)
                self.menu_de_opcoes()
            

            if opcao == 6: 
                cpf = input("\n ** Insira o CPF vinculado a sua conta: \n")
                self.ver_dados_da_conta(cpf)
                self.menu_de_opcoes()


            if opcao == 7: 
                 self.listar_contas()
                 self.menu_de_opcoes()


            if opcao == 8: 
                print(" @@ Sessao finalizada.")
                sys.exit()
            else: 
                 print("@@ Opcao invalida.")
                 self.menu_de_opcoes()

        
    
user = Sistema_bancario()
user.menu_de_opcoes()










            


