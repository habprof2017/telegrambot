import os
import platform
import logging

if platform.platform().startswith('Windows'):
    fichero_log = os.path.join(os.getenv('HOMEDRIVE'),
                               os.getenv("HOMEPATH"),
                               'simulacion.log')
else:
    fichero_log = os.path.join('/app', 'simulacion.log')


FORM = '%(asctime)s : %(pathname)s : %(filename)s : %(module)s : %(message)s'

logging.basicConfig(level=logging.DEBUG,
                    format=FORM,
                    datefmt='%d/%m/%Y %H:%M:%S',
                    filename=fichero_log)  # filemode='w'

logging.debug('Comienza el programa')
logging.info("SO Actual: " + platform.platform())
logging.info('Procesando con normalidad')
logging.warning('Advertencia')
