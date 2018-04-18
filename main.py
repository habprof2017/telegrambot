from algoritmos import *
from telegram.ext import Updater, CommandHandler
import logger


def main():
    miToken = '523275871:AAF-k2MiPzgiIwCL_vt539C3T0pi-RBILMM'
    updater = Updater(token=miToken)
    dispatcher = updater.dispatcher

    # https://api.telegram.org/bot523275871:AAF-k2MiPzgiIwCL_vt539C3T0pi-RBILMM/getMe

    handlers = [  # saludar es la funcion. /saluda es el comando en telegram
        CommandHandler('start', start),
        CommandHandler('saluda', saludar),
        CommandHandler('met1', metCuadradosMedios, pass_args=True),
        CommandHandler('met2', metProductosMedios, pass_args=True),
        CommandHandler('met3', metMultiplicadorCte, pass_args=True),
        CommandHandler('met4', metAlgoritmoLineal, pass_args=True)
    ]

    for handler in handlers:
        dispatcher.add_handler(handler)

    updater.start_polling()  # Start the bot

    updater.idle()  # Run the bot until you press Ctrl-C

    '''
    /setdescription

    Bot para la generacion de numeros pseudoaleatorios

    Metodos disponibles:
    * Cuadrados Medios
    * Productos Medios
    * Multiplicador Constante
    * Algoritmo Lineal
    * Algoritmo Congruencial Multiplicativo

    /setcommands
    met1 - semilla --> Cuadrados Medios
    met2 - semilla1 semilla2 --> Productos Medios
    met3 - semilla1 constante --> Multiplicador Constante
    met4 - semilla a c m tamaño --> Algoritmo Lineal
    '''


if __name__ == '__main__':
    main()
    logger.logging.debug('Comienza el programa')
