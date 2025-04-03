import json
from addservices import add_service
from editservice import edit_service
from deleteservice import delete_service
from list_services import list_services

def load_services():
    try:
        with open('data/services.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_services(services):
    with open('data/services.json', 'w') as file:
        json.dump(services, file, indent=4)

def main():
    services = load_services()
    while True:
        print("1. Agregar servicio")
        print("2. Editar servicio")
        print("3. Eliminar servicio")
        print("4. Listar servicios")
        print("5. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            services = add_service(services)
        elif choice == '2':
            services = edit_service(services)
        elif choice == '3':
            services = delete_service(services)
        elif choice == '4':
            list_services(services)
        elif choice == '5':
            save_services(services)
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()