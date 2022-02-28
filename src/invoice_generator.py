from datetime import datetime, timedelta
from time import sleep, time
from random import randint
from src.invoice.create_invoices import create_invoice
import logging


def __get_initial_and_limit_time():  # pegando o inicio e o final de cada periodo de 3 horas
    now = datetime.now()
    return now, now + timedelta(minutes=1)


def __roll_invoice_quantity_per_period(): # sorteia um numero inteiro de 8 a 12
    return randint(8, 12)

# entre o inicio e o fim geramos UM momento aleatorio
def __create_random_time_per_period(min_time, max_time): # convertendo o datetime para timestamp em inteiro
    min_timestamp = int(datetime.timestamp(min_time)) # sorteia um numero entre o tempo do começo e o fim
    max_timestamp = int(datetime.timestamp(max_time)) - 5   
    random_timestamp = randint(min_timestamp, max_timestamp)
    return random_timestamp


# pega a quantidade de invoices, colocando os momentos sorteados dentro de uma lista na quantidade certa
# executando a funcao acima na quantidade certa e guardando em uma lista e ordenando eles
def __create_invoice_time_moments(time_range):
    invoice_qty = __roll_invoice_quantity_per_period() # quantidade de invoices
    moments = [
        __create_random_time_per_period(*time_range) # escolhendo os tempos da criação das invoices
        for _ in range(invoice_qty) # 
    ]
    moments.sort()
    return moments


# cria a invoice
def __create_invoice(moment):
    create_invoice()
    logging.info(
        f'Invoice {datetime.fromtimestamp(moment)} created at {datetime.now()}'
    )


def run_a_schedule():
    time_range = __get_initial_and_limit_time() # pega o tempo total, começo e fim do ciclo
    moments = __create_invoice_time_moments(time_range) # pega a lista gerada na funcao acima

    while datetime.now() <= time_range[1]: # enquanto a hora de agora for menor que a hora final
        if moments[-1] > int(time()): # se o ultimo tempo escolhido que esta na lista for maior que o tempo atual em time stamp
            for moment in moments: # para cada momento na lista momentos
                while int(time()) < moment: # enquanto o tempo atual em timestamp for menor que o momento
                    logging.info(
                        f'waiting next invoice...'
                    )
                    sleep(1)

                __create_invoice(moment) # exibe mensagem e cria uma invoice
                sleep(1)
                    
        else: # se nao, motre a mensagem
            logging.info('all completed, waiting the next schedule')
            sleep(1)


def scheduler():
    end = datetime.now() + timedelta(hours=24) # tempo de agora mais o total do tempo dos ciclos
    logging.info('Started scheduler') # mensagem

    while datetime.now() < end: # enquanto a hora de agora é menor que o tempo taotal dos ciclos
        logging.info('Started new cycle') # mensagem
        run_a_schedule() # chama a funcao para criar as invoices
    
    logging.info('End') # terminando as mensagens


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    scheduler() # chama a funcao do tempo total de 24 horas, e dentro dela tem a funcao que cria as invoices
