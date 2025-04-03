def add_service(services, save_function):
    name = input("Nombre del paquete: ")
    price = float(input("Precio: "))
    event_type = input("Tipo de evento: ")
    duration = int(input("Duración estimada (horas): "))
    
    services.append({
        "name": name,
        "price": price,
        "event_type": event_type,
        "duration": duration
    })
    
    print("Servicio agregado exitosamente.")
    save_function(services)  # Guardar automáticamente después de agregar
    return services