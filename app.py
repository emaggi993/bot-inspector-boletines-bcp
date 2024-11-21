import requests
from bs4 import BeautifulSoup
from modulos.notificaciones import Notificacion
import json
from modulos.email import Email
from datetime import datetime
from decouple import config, UndefinedValueError
from urllib.parse import unquote

def main():
 
    current_dateTime = datetime.now()
   
    url = "https://www.bcp.gov.py/boletines-estadistico-financieros-formato-anterior-i1404"
    url_base = "https://www.bcp.gov.py"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    content = requests.get(url, headers={'User-Agent': user_agent}).text
    soup = BeautifulSoup(content, 'html.parser')
    with open('datos.json') as json_file:
        data = json.load(json_file)
    with open('configuraciones.json') as json_file:
        configuraciones = json.load(json_file)
    correos = configuraciones['correos']
    archivos = []
    nuevo = False
    descargas = []
    all_a = soup.find_all('a', href=True)
    try:
        password = config('GOOGLE_APP_PASS')
    except UndefinedValueError:
        raise Exception("No se encuentra la variable de entorno google_app_pass")
        exit


    email = Email(configuraciones['email_emisor'], password )
    for a in all_a:
        temp = a['href']
        boletines = a.text
        if  boletines.lower().strip() in ['bancos', 'financieras']:
            
            aux = temp.split("/")[-1]
            if aux not in data['archivos']:
                nuevo = True
                descargas.append((aux, url_base+temp))
                print(aux)
            archivos.append(temp.split("/")[-1])
            # print(temp.split("/")[-1])
    datos = {
        "archivos": archivos,
        "cantidad": len(archivos)
    }
    alerta = Notificacion()
    if nuevo:
        print("archivo nuevo !!!!!!!!!!!!!!!!!!!!!!!!!")
        alerta.mostrar_notificacion(titulo="Boletin encontrado", mensaje="Se ha detectado un cambio en uno o mas boletines")
        mensaje = """
        Se encontraron las siguientes modificaciones en los boletines del BCP, preciona en el/los enlace/s para descargar la información:


        """
        for descarga in descargas:
            mensaje += f'\t\t\t* {unquote( descarga[0])} -> <a href="{descarga[1]}" target="_blank">{descarga[1]}</a>\n\n'
        mensaje +="Saludos\nEste es un mensaje automático 🤖, No responder"

        asunto = f"Notificación modificación en boletines del BCP {current_dateTime.day}-{current_dateTime.month}-{current_dateTime.year}"  
        email.set_mensaje(asunto, mensaje)
        # if email.send(["emaggi@mf.com.py", "iherrera@mf.com.py"]):
        if email.send(correos):
            "Correos enviados correctamente"
    else:
        
        alerta.mostrar_notificacion(titulo="Boletines", mensaje="no se encontraron cambios en los boletines del BCP")

    with open('datos.json', 'w') as outfile:
        outfile.write(json.dumps(datos))


def test_request():
    import requests
    from bs4 import BeautifulSoup
    url = "https://www.bcp.gov.py/boletines-estadistico-financieros-formato-anterior-i1404"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    response = requests.get(url, headers={'User-Agent': user_agent})
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    all_a = soup.find_all('a', href=True)
    for a in all_a:
        print(a['href'])
        print(a.text)
    # main()
    #
if __name__ == "__main__":
    main()
    # test_request()