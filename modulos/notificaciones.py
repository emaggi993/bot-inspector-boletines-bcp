from notifypy import Notify
import os
class Notificacion ():
    url_base = os.path.join(os.getcwd(), "assets", "audios")

    def __init__(self, icono= None):
        self.notificacion = Notify()
        if icono:
            self.notificacion.icon = icono
    def mostrar_notificacion(self, titulo = "Notificacion", mensaje = "Este es un mensaje", sonido = "sound_notification.wav" ):
        self.notificacion.title = titulo
        self.notificacion.message = mensaje
        self.notificacion.audio= os.path.join(self.url_base,sonido)
        self.notificacion.send()
