import requests # Lib para enviar la solicitud al servidor
import platform # Lib para el serial
import os # Lib para el modelo
import psutil # Lib para identificar la RAM
import json

# Encabeza para la información
print ("Soporte Técnico Integeratic SAS  \n")


# Procesos para detectar los datos de computador
# Serial
if platform.system() == "Windows":
    c = os.popen("wmic bios get serialnumber").read()
    serial = c.split("\n")[2].strip()
    print("Serial: ", serial)


# Disco
# Obtener la información del disco
disks = psutil.disk_partitions()
disk_info = []
print("Discos :")
for disk in disks:
    try:
        disk_usage = psutil.disk_usage(disk.mountpoint)
        total = disk_usage.total / (1024 ** 3)
        disk_info.append({"mountpoint": disk.mountpoint, "capacity": "{:.2f} GB".format(total)})
    except PermissionError:
        # Ignorar errores de permisos y continuar con el siguiente disco
        continue
    
    
# Imprimir los valores de mountpoint y capacity para cada disco
for disk in disk_info:
    print("Unidad:", disk["mountpoint"])
    print("Capacidad:", disk["capacity"])

# Convertimos la lista a formato JSON
discos_json = json.dumps(disk_info)

# Local
url = "http://localhost/Disco soporte/proceso.php"


# Datos que quieres enviar
data = {
    
    "serial": serial,
    "discos": discos_json
}
 
# Enviar la solicitud POST
response = requests.post(url, data=data)

# Imprimir la respuesta del servidor
print(response.text)