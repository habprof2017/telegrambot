import os
import logging

fichero_log = os.path.join(os.getenv('HOME'), 'simulacion.log')

FORM = '%(asctime)s : %(pathname)s : %(filename)s : %(module)s : %(message)s'

logging.basicConfig(level=logging.INFO,
                    format=FORM,
                    datefmt='%d/%m/%Y %H:%M:%S',
                    filename=fichero_log)  # filemode='w'


logging.info('Procesando con normalidad')
logging.info('Agregando nueva linea')
