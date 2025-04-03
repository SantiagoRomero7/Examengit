from serviceslistservices import list_services  # Importar la función list_services

def edit_service(services, save_function):
    if not services:
        print("No hay servicios disponibles para editar.")
        return services

    list_services(services)  # Llamar a la función para listar servicios
    try:
        index = int(input("Seleccione el número del servicio a editar: ")) - 1

        if 0 <= index < len(services):
            print("Editando servicio:", services[index])
            name = input("Nuevo nombre del paquete (dejar vacío para no cambiar): ")
            price = input("Nuevo precio (dejar vacío para no cambiar): ")
            event_type = input("Nuevo tipo de evento (dejar vacío para no cambiar): ")
            duration = input("Nueva duración estimada (horas) (dejar vacío para no cambiar): ")

            if name:
                services[index]['name'] = name
            if price:
                services[index]['price'] = float(price)
            if event_type:
                services[index]['event_type'] = event_type
            if duration:
                services[index]['duration'] = int(duration)

            print("Servicio editado exitosamente.")
            save_function(services)  # Guardar automáticamente después de editar
        else:
            print("Índice no válido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
    
    return services