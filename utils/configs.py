class Configuracoes():
    def __init__(self):
        self.__file_pacientes = './dados/pacientes.csv'
        self.__file_consultas = './dados/consultas.csv'
        self.__file_procedimentos = './dados/procedimentos.csv'
        self.__file_ult_id_consulta = './dados/ultimo_id_consulta.txt'
        self.__file_ult_id_paciente = './dados/ultimo_id_paciente.txt'
        self.__file_ult_id_procedimento = './dados/ultimo_id_procedimento.txt'
        self.__file_logs = './logs/log.txt' 
    
    @property
    def file_pacientes(self):
        return self.__file_pacientes
    
    @property
    def file_consultas(self):
        return self.__file_consultas

    @property
    def file_procedimentos(self):
        return self.__file_procedimentos

    @property
    def file_ult_id_consulta(self):
        return self.__file_ult_id_consulta

    @property
    def file_ult_id_paciente(self):
        return self.__file_ult_id_paciente

    @property
    def file_ult_id_procedimento(self):
        return self.__file_ult_id_procedimento

    @property
    def file_logs(self):
        return self.__file_logs
    
  