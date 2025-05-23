import os
import pandas as pd

from datetime import datetime
from tabulate import tabulate
from utils.configs import Configuracoes
from utils.log import Logs 

class Paciente:
    def __init__(self):
        self.__configurations = Configuracoes()
        self.logs = Logs();
        self.arquivo_csv = self.__configurations.file_pacientes
        self.arquivo_id = self.__configurations.file_ult_id_paciente

        # Criar arquivo CSV se não existir
        if not os.path.exists(self.arquivo_csv):
            df = pd.DataFrame(columns=['id', 'nome', 'cpf', 'data_nasc', 'sexo'])
            df.to_csv(self.arquivo_csv, index=False)

        # Criar arquivo de ID se não existir ou estiver vazio
        if not os.path.exists(self.arquivo_id) or os.path.getsize(self.arquivo_id) == 0:
            with open(self.arquivo_id, 'w') as f:
                f.write('0')

    def gerar_novo_id(self):
        with open(self.arquivo_id, 'r') as f:
            conteudo = f.read().strip()
            ultimo_id = int(conteudo) if conteudo else 0
        
        novo_id = ultimo_id + 1
        with open(self.arquivo_id, 'w') as f:
            f.write(str(novo_id))
        return novo_id

    def validar_data(self, data_str):
        try:
            datetime.strptime(data_str, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def cadastrar(self):
        df = pd.read_csv(self.arquivo_csv)
        nome = input('Informe nome e sobrenome do paciente: ')
        cpf = input('Informe o cpf (somente números): ')

        if cpf in df['cpf'].astype(str).values:
            print('CPF já cadastrado!')
            return

        while len(cpf) != 11 or not cpf.isdigit():
                print('CPF inválido! Deve conter exatamento 11 dígitos numéricos.')
                cpf = input('Informe novamente o CPF (somente números): ')
           
        data = input('Informe  data de nascimento (dd/mm/aaaa): ')
        while not self.validar_data(data):
                print("Formato inválido. Tente novamente.")
                data = input('Data da consulta (dd/mm/aaaa): ')
        sexo = input('Informe o sexo M / F: ')

        novo_id = self.gerar_novo_id()
        novo_paciente = pd.DataFrame([[novo_id, nome, cpf, data, sexo]], 
                                    columns=['id', 'nome', 'cpf', 'data_nascimento', 'sexo'])
        
        novo_paciente.to_csv(self.arquivo_csv, mode='a', header=False, index=False)
        print(f'Paciente cadastrado com sucesso! ID: {novo_id}')
        print(tabulate(novo_paciente, headers='keys', tablefmt='fancy_grid', showindex=False))
       
        # LINHA ADICIONADA
        self.logs.registrar_log("Paciente", "Cadastro", f"CPF: {cpf}")

    def listar(self):
        df = pd.read_csv(self.arquivo_csv)
        
        if df.empty:
            print('Nenhum paciente cadastrado.')
        else:
            print('\nLista de Pacientes:')
            df_formatado = df[['id', 'nome', 'cpf', 'data_nasc', 'sexo']]
            print(tabulate(df_formatado, headers='keys', tablefmt='grid', showindex=False))

    def excluir(self):
        from models.consulta import Consulta
        from models.procedimento import Procedimento

        df = pd.read_csv(self.arquivo_csv)
        
        if df.empty:
            print('Nenhum paciente para excluir.')
            return

        cpf_excluir = input('Digite o CPF do paciente que deseja excluir: ').strip()
        
        df['cpf'] = df['cpf'].astype(str)
        
        if cpf_excluir not in df['cpf'].values:
            print('CPF não encontrado.')
            return
        
        paciente = df[df['cpf'] == cpf_excluir].iloc[0]
        id_paciente = paciente['id']

        # Verifica se tem consulta
        consulta_service = Consulta()
        df_consultas = pd.read_csv(consulta_service.arquivo_csv)
        consultas_paciente = df_consultas[df_consultas['id_paciente']== id_paciente]

        procedimento_service = Procedimento()
        df_procedimento = pd.read_csv(procedimento_service.arquivo_csv)
        procedimento_paciente = df_procedimento[df_procedimento['id_paciente'] == id_paciente]

        if not consultas_paciente.empty or not procedimento_paciente.empty:
            print(' O paciente possui agendamentos ou procedimentos agendados')
            if not consultas_paciente.empty:
                print(f' - {len(consultas_paciente)} consulta(s) agendada(s)')

            if not procedimento_paciente.empty:
                print(f' - {len(procedimento_paciente)} procedimento(s) agendado(s) ')
            
            confirma = input ('Deseja continuar mesmo assim? (s/n)').strip().lower()
            if confirma != 's' :
                print ('Acão cancelada.')
                return
            
            #Excluir consulta
            if not consultas_paciente.empty:
                df_consultas = df_consultas[df_consultas['id_paciente'] != id_paciente]
                df_consultas.to_csv(consulta_service.arquivo_csv, index=False)
                print('Consulas associadas ao paciente foram excluidas')

            #Excluir procedimento
            if not procedimento_paciente.empty:
                df_procedimento = df_procedimento[df_procedimento['id_paciente']!= id_paciente]
                df_procedimento.to_csv(procedimento_service.arquivo_csv, index=False)
                print('Procedimento associado ao paciente foram excluidos')

        df = df[df['cpf'] != cpf_excluir]
        df.to_csv(self.arquivo_csv, index=False)
        print(f'Paciente com CPF {cpf_excluir} removido com sucesso. ')
        
        # LINHA ADICIONADA
        self.logs.registrar_log("Paciente", "Exclusão", f"CPF: {cpf_excluir}")

    def editar(self):
        df = pd.read_csv(self.arquivo_csv)
        
        if df.empty:
            print('Nenhum paciente cadastrado para editar.')
            return
       
        cpf_editar = input('Digite o CPF do paciente que deseja editar: ').strip()
        
        df['cpf'] = df['cpf'].astype(str)
        
        if cpf_editar not in df['cpf'].values:
            print('CPF não encontrado.')
            return
            
        paciente = df[df['cpf'] == cpf_editar].iloc[0]
        print("\nDados atuais do paciente:")
        print(f"1. Nome: {paciente['nome']}")
        print(f"2. CPF: {paciente['cpf']}")
        print(f"3. Data de Nascimento: {paciente['data_nasc']}")
        print(f"4. Sexo: {paciente['sexo']}")
        
        campo = input("\nDigite o número do campo que deseja editar (1-4): ")
        
        if campo == '1':
            novo_campo = 'Nome'
            novo_valor = input("Digite o novo " + novo_campo + ": ")
            df.loc[df['cpf'] == cpf_editar, 'nome'] = novo_valor
        elif campo == '2':
            novo_campo = 'CPF'
            novo_valor = input("Digite o novo " + novo_campo + ": ")
            df.loc[df['cpf'] == cpf_editar, 'cpf'] = novo_valor
        elif campo == '3':
            novo_campo = 'Data de Nascimento'
            novo_valor = input("Digite a nova " + novo_campo + ": ")
            df.loc[df['cpf'] == cpf_editar, 'data_nasc'] = novo_valor
        elif campo == '4':
            novo_campo = 'Sexo'
            novo_valor = input("Digite o novo " + novo_campo + ": ")                        
            df.loc[df['cpf'] == cpf_editar, 'sexo'] = novo_valor
        else:
            print("Opção inválida.")
            return
            
        df.to_csv(self.arquivo_csv, index=False)
        print("Paciente atualizado com sucesso!")
        
        # LINHA ADICIONADA
        self.logs.registrar_log("Paciente", "Edição", f"CPF: {cpf_editar} - Campo Editado: {novo_campo}")

    def buscar(self, cpf):
         df = pd.read_csv(self.arquivo_csv)

         if df.empty:
            print('Nenhum paciente cadastrado para consultas.')
            return 0

         df['cpf'] = df['cpf'].astype(str)
         cpf=cpf.strip()  

         if cpf not in df['cpf'].values:
            print('Paciente não encontrado.')
            return 0

         paciente = df[df['cpf'] == cpf].iloc[0]
         return paciente['id']
    