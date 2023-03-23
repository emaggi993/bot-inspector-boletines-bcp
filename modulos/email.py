import yagmail

email_emisor = 'esrma3010@gmail.com'
email_contrasenha= 'elias3660210'
pass_app = 'qltalfjftzsyhplh'

email_receptor = ['emaggi@mf.com.py']

asunto = 'Prueba'
cuerpo = '''
ESTO ES una prueba


fasdfasd

'''
yag = yagmail.SMTP(user= email_emisor, password= pass_app)


class Email():
    def __init__(self, emisor, pass_app, host=None, port = None) -> None:
        self.emisor= emisor
        self.pass_app = pass_app
        self.host= host
        self.port= port
        self.gmail = yagmail.SMTP(user= emisor, password= pass_app)
    def set_mensaje( self, asunto, mensaje ):
        self.asunto = asunto
        self.mensaje = mensaje
    def send(self, receptores, sep= ","):
        if isinstance(receptores, str):
            receptores = receptores.split(sep)
        elif isinstance(receptores, list) or isinstance(receptores, tuple):
            pass
        else:
            raise Exception("No se pudo enviar el correo")
        for r in receptores:
            # print(r)
            self.gmail.send(r.strip(), self.asunto, self.mensaje)
            print(f"correo enviado a {r}..")
        return True
        