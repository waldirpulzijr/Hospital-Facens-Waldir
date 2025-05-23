from utils.log import Logs 
from models.paciente import Paciente
from models.consulta import Consulta
from models.procedimento import Procedimento

class Initialize():
    def __init__(self):
        self.pacientes = Paciente()
        self.cons = Consulta()
        self.proc = Procedimento()
        self.logs = Logs();

    def show_menu(self): 
        print('\n')
        print(50 * '-')
        print('Bem-vindo ao Sistema do Hospital!')
        print(50 * '-')
        print('1 - Pacientes')
        print('2 - Consultas')
        print('3 - Procedimentos')
        print('4 - Listar logs')
        print('5 - Sair') 

    def choose_option(self):
        option = input('\nEscolha uma das opções: ')
        if option not in ['1', '2', '3', '4', '5']:
            print('\nOpção inválida!')
        return option

    def show_sub_menu(self, option):
        print('\n')
        print(50 * '-')
        if option == '1':  
            print('Pacientes:')
        elif option == '2':
            print('Consultas:')
        elif option == '3':
            print('Procedimentos:')
        print(50 * '-')
        print('1 - Cadastrar')
        print('2 - Editar')
        print('3 - Listar')
        print('4 - Excluir') 
        print('5 - Voltar') 

    def choose_sub_option(self):
        sub_option = input('\nEscolha uma das opções: ')
        if sub_option not in ['1', '2', '3', '4', '5']:
            print('\nOpção inválida!')
        return sub_option

    def handle_logs(self):
        self.logs.handle_logs();

    def to_sub_menu(self, option, sub_option):
        if option == '1':
            if sub_option == '1':
                self.pacientes.cadastrar()
            elif sub_option == '2':
                self.pacientes.editar()
            elif sub_option == '3':
                self.pacientes.listar()
            elif sub_option == '4':
                self.pacientes.excluir()
        elif option == '2':
            if sub_option == '1':
                self.cons.cadastrar()
            elif sub_option == '2':
                self.cons.editar()
            elif sub_option == '3':
                self.cons.listar()
            elif sub_option == '4':
                self.cons.excluir()
        elif option == '3':
            if sub_option == '1':
                self.proc.cadastrar()
            elif sub_option == '2':
                self.proc.editar()
            elif sub_option == '3':
                self.proc.listar()
            elif sub_option == '4':
                self.proc.excluir()

    def to_go_out(self):
        print('\nObrigado, volte sempre!')

if __name__ == "__main__":
    init = Initialize()
    option = ''

    while option != '5':
        init.show_menu()
        option = init.choose_option()

        if option in ('1','2','3'):  
            sub_option = ''
            
            while sub_option != '5':
                init.show_sub_menu(option)
                sub_option = init.choose_sub_option()
                init.to_sub_menu(option, sub_option)

        elif option == '4':
            init.handle_logs()  # Chama o método específico para logs
            
        elif option == '5':
            init.to_go_out()