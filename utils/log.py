import os
import sys
import time

from datetime import datetime
from utils.configs import Configuracoes

class Logs:
    def __init__(self):
        self.__configurations = Configuracoes()
        self.arquivo_logs = self.__configurations.file_logs

    def registrar_log(self, entidade: str, acao: str, identificador: str):
        """
        Registra ações do sistema em arquivo de log.
        Formato: [DATA HORA] AÇÃO - ENTIDADE - IDENTIFICADOR
        """
        try:
            data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            linha = f"[{data_hora}] {acao.upper().ljust(15)} - {entidade.upper().ljust(15)} - {identificador}\n"

            # Cria o diretório se não existir
            diretorio = os.path.dirname(self.arquivo_logs)
            if not os.path.exists(diretorio):
                os.makedirs(diretorio)
        
            # Abre o arquivo forçando a escrita imediata (flush)
            with open(self.arquivo_logs, "a", encoding="utf-8") as arquivo:
                arquivo.write(linha)
                arquivo.flush()  # FORÇA A ESCRITA IMEDIATA
        except Exception:
            pass

    def handle_logs(self):
        """Método específico para tratar a exibição de logs"""
        try:
            sys.stdout.flush()
            time.sleep(0.1)
            
            print("\n" + 50 * '-')
            print("REGISTROS DE LOG".center(50))
            print(50 * '-')

            with open(self.arquivo_logs , "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read()

            print(conteudo.strip() if conteudo else "Nenhum registro encontrado")
            print(50 * '-')

        except FileNotFoundError:
            print("\nNenhum registro de log encontrado.")

        input("\nPressione Enter para voltar...")

    