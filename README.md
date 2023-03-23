
# BOT-INSPECTOR-BOLETINES-BCP

Es un script diseñado exclusivamente para la detección de cambios en boletines informativos de Bancos y Financieras publicados en la página del Banco Central del Paraguay.

Al detectar cambios (modificacion de archivo, nuevo archivo) envia una alerta al usuario y un correo electrónico a las direcciones proveídas en el archivo de configuraciones.json

Para el envio de correo se debe configurar un correo gmail habilitado con la verificación de 2 pasos y crear un archivo .env con la clave GOOGLE_APP_PASS y el valor sera la contraseña que genera google para el uso de aplicaciones.

Este script puede ser automatizado como tarea programada ejecutando en cierto horario el archivo ejecutar.bat en Windows



## Autor

- [Elías Maggi @emaggi993](https://github.com/emaggi993)