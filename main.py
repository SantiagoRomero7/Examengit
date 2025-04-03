import json
from servicesaddservice import add_service
from serviceseditservice import edit_service
from servicesdeleteservice import delete_service
from serviceslistservices import list_services

def load_services():
    try:
        with open('services.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_services(services):
    with open('services.json', 'w') as file:
        json.dump(services, file, indent=4)

def main():
    services = load_services()
    while True:
        print("\n--- Menú de Servicios Fotográficos ---")
        print("1. Agregar servicio")
        print("2. Editar servicio")
        print("3. Eliminar servicio")
        print("4. Listar servicios")
        print("5. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            services = add_service(services, save_services)
        elif choice == '2':
            services = edit_service(services, save_services)
        elif choice == '3':
            services = delete_service(services, save_services)
        elif choice == '4':
            list_services(services)
        elif choice == '5':
            save_services(services)  # Guardar antes de salir
            print("Datos guardados. Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()