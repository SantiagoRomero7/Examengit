def edit_service(services):
    if not services:
        print("No hay servicios disponibles para editar.")
        return services

    def print_services():
    list_services (services)
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
    else:
        print("Índice no válido.")
    
    return services