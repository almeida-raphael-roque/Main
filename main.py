import time
import os
import sys
import logging
import datetime as dt
import traceback
import threading

start_time = time.time()

from relatorio_inadimplencia.py.ETL import ETL_relat_inadimp
from conjuntos_informacoes.ETL import ETL_conj_info
from ativacoes_placas.python.ETL import Load_relat_ativ_pend

class Main:

    def __init__(self) -> None:
        pass


    def structure_routines():

        # Armazenando nome de cada rotina em uma variável
        name_rout_1 = "RELATÓRIO DE INADIMPLÊNCIA"
        name_rout_2 = "RELATÓRIO DE INFORMAÇÕES DE CONJUNTOS"
        name_rout_3 = "RELATÓRIO DE ATIVAÇÕES DE PLACAS"

        

        # CRIANDO A LISTA COM TODAS AS ROTINAS EXISTENTES E SEUS REFERENTES NOMES IDENTIFICADORES
        routines = [
            (lambda: ETL_relat_inadimp.ETL_inadimp(), name_rout_1),
            (lambda: ETL_conj_info.ETL_conj(), name_rout_2),
            (lambda: Load_relat_ativ_pend.load_files(), name_rout_3)
        ]

        return routines

    def run_all_routines():
        max_attempts = 3
        attempts = 0

        def execute_all_routines():
            
            logging.debug('\n ----------------------------------------------------------------------------------')
            logging.debug('\n Tempo esgotado. Executando todas as rotinas...')

            for routine, name in routines:
                try:
                    routine()
                    logging.debug('\n ----------------------------------------------------------------------------------')
                    logging.debug(f'\n Rotina {name} executada com sucesso')

                except Exception as e:

                    logging.debug('\n ----------------------------------------------------------------------------------')
                    logging.error(f'\n Erro ao executar rotina {name}: {e}')
            sys.exit()

        while attempts < max_attempts:
            try:
                routines = Main.structure_routines()
                print('\n Olá, você está no painel central de execuções de Rotinas Diárias.')
                print('\n Por favor, verifique as opções abaixo:')
                print('\n ----------------------------------------------------------------------------------')

                for idx, (_, name) in enumerate(routines, start=1):
                    print(f'{idx} - {name}')

                print('\n ----------------------------------------------------------------------------------')

                # Iniciando o temporizador para execução automática
                timer = threading.Timer(30, execute_all_routines)
                timer.start()

                resposta = input('Qual Rotina você gostaria de executar? (digite apenas o número referente à rotina desejada): ')

                # Cancelando o temporizador se uma resposta for dada a tempo
                timer.cancel()

                if resposta.isdigit() and 1 <= int(resposta) <= len(routines):
                    selected_index = int(resposta) - 1
                    routine, name = routines[selected_index]

                    logging.debug('\n ----------------------------------------------------------------------------------')
                    logging.debug(f'Executando Rotina {name}')

                    routine()

                    logging.debug('\n ----------------------------------------------------------------------------------')
                    logging.debug(f'Rotina {name} executada com sucesso')

                else:

                    logging.debug('\n ----------------------------------------------------------------------------------')
                    logging.debug('Resposta inválida. Executando todas as rotinas...')

                    execute_all_routines()

                break

            except Exception as e:
                attempts += 1
                logging.error(f'Erro na tentativa {attempts}: {e}')
                logging.error(traceback.format_exc())
                time.sleep(2)
                continue

        if attempts == max_attempts:
            
            logging.error('Todas as tentativas falharam. Verifique o código para solucionar problemas.')

        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Tempo de execução: {execution_time} segundos")

if __name__ == '__main__':
    Main.run_all_routines()

