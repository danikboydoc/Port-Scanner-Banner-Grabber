import socket
ip_objetivo = '0.0.0.0' #Colocar ip objetivo
puerto_inicio = 1
puerto_fin = 200
puertos_disponibles=[]
banner_disponibles=[]

print(f'Escaneando {ip_objetivo} de puerto {puerto_inicio} a {puerto_fin}...')
print('-' * 50)
for puerto in range(puerto_inicio, puerto_fin + 1):
    try:
        socket_conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        resultado = socket_conexion.connect_ex((ip_objetivo, puerto))
        if resultado == 0:
            print(f'Puerto {puerto}: ABIERTO')
            puertos_disponibles.append(int(puerto))
            # Intentamos obtener el banner
            try:
                socket_conexion.settimeout(3) # Esperamos máximo 2 segundos
                banner = socket_conexion.recv(1024)
                banner_texto = banner.decode('utf-8', errors='ignore')
                print(f' Banner: {banner_texto.strip()}')
                banner_disponibles.append(banner_texto.strip())
            except:
                print(f' Banner: No disponible')
                banner_disponibles.append("No disponible")
        socket_conexion.close()
    except:
        pass
print('-' * 50)
print('Escaneo completado')
for puertos, banners in zip(puertos_disponibles,banner_disponibles):
    print(f"Puerto {puertos} con Banner: {banners}")
if puertos_disponibles == []:
    print("No hay puertos disponibles")
if banner_disponibles == []:
    print("No hay banners disponibles")