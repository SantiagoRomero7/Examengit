def list_services(services):
    if not services:
        print("No hay servicios disponibles.")
        return

    print("\n--- Lista de Servicios ---")
    for i, service in enumerate(services, start=1):
        print(f"{i}. Nombre: {service['name']}, Precio: {service['price']}, Tipo de Evento: {service['event_type']}, Duración: {service['duration']} horas")