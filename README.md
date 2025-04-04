## 🎨 PhotoCampus - Gestión de Servicios Fotográficos  

### Descripción del Proyecto  
PhotoCampus es un sistema de gestión de servicios fotográficos que permite registrar, editar, eliminar y listar paquetes fotográficos. Este proyecto facilita la administración de los servicios que ofrece un estudio o fotógrafo profesional.  

### 📌 ¿Qué hace el proyecto?  
- Agrega nuevos servicios fotográficos con detalles como nombre, precio, tipo de evento y duración.  
- Permite la edición de servicios existentes.  
- Elimina servicios que ya no se ofrecen.  
- Muestra una lista de los servicios registrados.  
- Guarda y carga los datos de los servicios en un archivo JSON para persistencia.  

### 🚀 ¿Por qué este proyecto es útil?  
- Optimiza la gestión de los servicios fotográficos.  
- Mantiene un registro estructurado y accesible.  
- Automatiza el almacenamiento y recuperación de datos.  

### 🛠️ ¿Qué problema resuelve?  
Evita la administración manual de los servicios fotográficos, permitiendo una organización eficiente y reduciendo errores en la gestión.  

---

## 🛠️ Instalación  

### 📌 Requisitos previos  
Asegúrate de tener instalado:  
- Python 3.10 o superior  

### 🛠️ Pasos de instalación  

```bash
# Clonar el repositorio
git clone https://github.com/SantiagoRomero7/Proyecto_Git_ApellidoNombre.git
cd Proyecto_Git_ApellidoNombre

# Crear un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias (si las hay)
pip install -r requirements.txt
```

---

## 📌 Uso  
Para ejecutar el sistema:  

```bash
python main.py
```

Una vez ejecutado, se mostrará un menú con las opciones disponibles:  
1️⃣ Agregar servicio  
2️⃣ Editar servicio  
3️⃣ Eliminar servicio  
4️⃣ Listar servicios  
5️⃣ Salir  

---

## 🔄 Estructura del Proyecto  

```
💻 Proyecto_Git_ApellidoNombre
│── main.py                   # Archivo principal de ejecución
│── servicesaddservice.py      # Agregar servicios
│── serviceseditservice.py     # Editar servicios
│── servicesdeleteservice.py   # Eliminar servicios
│── serviceslistservices.py    # Listar servicios
│── services.json              # Archivo JSON para almacenar los datos
│── README.md                  # Documentación del proyecto
```

---

## 🔀 Flujo de Trabajo en Git  

### 📌 Ramas utilizadas  
- `main` → Contiene la versión estable del proyecto.  
- `feature/add-services` → Desarrollo de la funcionalidad de agregar servicios.  
- `feature/edit-services` → Desarrollo de la funcionalidad de edición.  
- `feature/delete-services` → Desarrollo de la funcionalidad de eliminación.  

### 🔄 Manejo de Conflictos  
Durante la integración de ramas, se simuló un conflicto al fusionar `feature/edit-services` con `main`. Para resolverlo:  
1. Se identificaron las diferencias con `git diff`.  
2. Se editó manualmente el archivo afectado (`serviceseditservice.py`).  
3. Se validó que el código funcionara correctamente.  
4. Se hizo un commit con la solución:  

```bash
git add serviceseditservice.py
git commit -m "Resolviendo conflicto en edición de servicios"
git push origin main
```

---

## 🎓 ¿Qué aprendió el desarrollador?  
- Uso de Git y GitHub para control de versiones y trabajo colaborativo.  
- Manejo de archivos JSON para persistencia de datos.  
- Modularización del código para facilitar su mantenimiento.  
- Resolución manual de conflictos en Git.  

---

## 📌 Mantenimiento y Créditos  
**Desarrollador:** Santiago Romero - Javier Baez 
**GitHub:** [SantiagoRomero7](https://github.com/SantiagoRomero7?tab=repositories)  

---
