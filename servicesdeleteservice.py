from serviceslistservices import list_services  # Importar la función list_services

def delete_service(services, save_function):
    if not services:
        print("No hay servicios disponibles para eliminar.")
        return services

    list_services(services)  # Llamar a la función para listar servicios
    try:
        index = int(input("Seleccione el número del servicio a eliminar: ")) - 1

        if 0 <= index < len(services):
            services.pop(index)
            print("Servicio eliminado exitosamente.")
            save_function(services)  # Guardar automáticamente después de eliminar
        else:
            print("Índice no válido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
    
    return services