def delete_service(services):
    if not services:
        print("No hay servicios disponibles para eliminar.")
        return services

    list_services (services)
    index = int(input("Seleccione el número del servicio a eliminar: ")) - 1

    if 0 <= index < len(services):
        services.pop(index)
        print("Servicio eliminado exitosamente.")
    else:
        print("Índice no válido.")
    
    return services