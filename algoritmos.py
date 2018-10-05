import random

def start(bot, update):
    va = 'estoy vivo!'
    msj = 'Hola {} {}'.format(update.message.from_user.first_name, va)
    bot.send_message(chat_id=update.message.chat_id, text=msj)
   
def unRandom(bot, update):
    msj = []
    for i in range(10):
        msj.append(round(random.random(),2))
    
    bot.send_message(chat_id=update.message.chat_id, text=msj)


def armarNumero(digitos):
    x = str(digitos)[2] + str(digitos)[3]  # posicion 2 y 3 son fijas
    if len(str(digitos)) == 8:
        x = x + str(digitos)[4] + str(digitos)[5]
    elif len(str(digitos)) == 5:
        x = str(digitos)[0] + str(digitos)[1] + x
    else:
        x = str(digitos)[1] + x + str(digitos)[4]

    return x


def saludar(bot, update):
    va = 'estoy vivo!'
    msj = 'Hola {} {}'.format(update.message.from_user.first_name, va)
    bot.send_message(chat_id=update.message.chat_id, text=msj)


def cuadradosMedios(args):
    semilla = int(args[0])

    salida = []

    for i in range(10):
        y = semilla**2
        x = armarNumero(y)
        r = "0.{}".format(x)

        salida.append(float(r))
        semilla = int(x)

    return salida


def productosMedios(args):
    semilla1 = int(args[0])
    semilla2 = int(args[1])
    salida = []

    for i in range(10):
        y = semilla1 * semilla2
        x = armarNumero(y)
        r = "0.{}".format(x)
        salida.append(float(r))
        semilla1 = semilla2
        semilla2 = int(x)

    print(salida)
    return salida


def multiplicadorCte(args):
    semilla = int(args[0])
    constante = int(args[1])
    salida = []

    for i in range(10):
        y = semilla * constante
        x = armarNumero(y)
        r = "0.{}".format(x)
        salida.append(float(r))
        semilla = int(x)

    return salida


def algoritmoLineal(args):
    semilla = int(args[0])
    cteA = int(args[1])
    cteC = int(args[2])
    cteM = int(args[3])
    repe = int(args[4])

    salida = []

    for i in range(repe):
        x = (cteA * semilla + cteC) % cteM

        r = round((x / (cteM - 1)), 4)

        salida.append(r)
        semilla = int(x)

    return salida


def metCuadradosMedios(bot, update, args):  # /met1
    if not len(args) == 0:
        metodo = 'Metodo de Cuadrados Medios'
        bot.send_message(chat_id=update.message.chat_id, text=metodo)
        titulo = "Xo = {} | D = 4 | Tamaño de la muestra = 10".format(args[0])
        bot.send_message(chat_id=update.message.chat_id, text=titulo)
        numeros = cuadradosMedios(args)
        bot.send_message(chat_id=update.message.chat_id, text=numeros)
    else:
        m1 = 'Error faltan valores'
        txt = "Semilla: 5015"
        ej = "/met1 5015"
        bot.send_message(chat_id=update.message.chat_id, text=m1)
        bot.send_message(chat_id=update.message.chat_id, text='Ejemplo:')
        bot.send_message(chat_id=update.message.chat_id, text=txt)
        bot.send_message(chat_id=update.message.chat_id, text=ej)


def metProductosMedios(bot, update, args):  # /met2
    if not len(args) == 0:
        numeros = productosMedios(args)
        metodo = 'Metodo de Productos Medios'
        titulo = "Xo = {} | X1 = {}".format(args[0], args[1])
        bot.send_message(chat_id=update.message.chat_id, text=metodo)
        bot.send_message(chat_id=update.message.chat_id, text="D = 4 | n = 10")
        bot.send_message(chat_id=update.message.chat_id, text=titulo)
        bot.send_message(chat_id=update.message.chat_id, text=numeros)
    else:
        m1 = 'Error faltan valores'
        txt = "Semilla1: 5115, Semilla2 = 5736"
        ej = '/met2 5115 5736'
        bot.send_message(chat_id=update.message.chat_id, text=m1)
        bot.send_message(chat_id=update.message.chat_id, text='Ejemplo:')
        bot.send_message(chat_id=update.message.chat_id, text=txt)
        bot.send_message(chat_id=update.message.chat_id, text=ej)


def metMultiplicadorCte(bot, update, args):  # /met3
    if not len(args) == 0:
        numeros = multiplicadorCte(args)
        metodo = 'Metodo de Multiplicador Constante'
        titulo = "Xo = {} | a = {}".format(args[0], args[1])
        bot.send_message(chat_id=update.message.chat_id, text=metodo)
        bot.send_message(chat_id=update.message.chat_id, text="D = 4 | n = 10")
        bot.send_message(chat_id=update.message.chat_id, text=titulo)
        bot.send_message(chat_id=update.message.chat_id, text=numeros)
    else:
        m1 = 'Error faltan valores'
        ej = '/met3 5115 3624'
        txt = "Semilla: 5115, Cte = 3624"
        bot.send_message(chat_id=update.message.chat_id, text=m1)
        bot.send_message(chat_id=update.message.chat_id, text='Ejemplo:')
        bot.send_message(chat_id=update.message.chat_id, text=txt)
        bot.send_message(chat_id=update.message.chat_id, text=ej)


def metAlgoritmoLineal(bot, update, args):  # /met4
    if not len(args) == 0:
        metodo = 'Metodo del Algoritmo Lineal'
        titulo = "Xo = {} | a = {} | c = {} | m = {} | n = {}".format(
            args[0], args[1], args[2], args[3], args[4])  # semilla a c m cant
        numeros = algoritmoLineal(args)
        bot.send_message(chat_id=update.message.chat_id, text=metodo)
        bot.send_message(chat_id=update.message.chat_id, text="D = 4 | n = 10")
        bot.send_message(chat_id=update.message.chat_id, text=titulo)
        bot.send_message(chat_id=update.message.chat_id, text=numeros)
    else:
        m1 = 'Error faltan valores'
        ej = '/met4 18 17 13 64 10'
        txt = "Semilla: 18, a: 17, c: 13, m: 64 ,n: 10"
        bot.send_message(chat_id=update.message.chat_id, text=m1)
        bot.send_message(chat_id=update.message.chat_id, text='Ejemplo:')
        bot.send_message(chat_id=update.message.chat_id, text=txt)
        bot.send_message(chat_id=update.message.chat_id, text=ej)
