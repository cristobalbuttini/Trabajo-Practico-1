# Trabajo Practico 1 - Desarrollo de Software

Este proyecto es una aplicación de consola desarrollada como trabajo práctico, cuya finalidad es **persistir datos académicos** (facultades, especialidades, materias, etc.) en una base de datos PostgreSQL, **a partir de archivos XML provistos** por el profesor.

> ⚡ La arquitectura está estructurada en **tres capas**: `tests → services → repositories`, siguiendo buenas prácticas de separación de responsabilidades.

---

## 📂 Estructura del Proyecto

```
TP-1/
├── models/             # Definiciones de tablas como objetos gracias a SQLALCHEMY (ORM)
├── repositories/       # Acceso y persistencia en BD (SQLAlchemy puro)
├── services/           # Lógica de negocio (que debe hacer?) (carga desde los XML)
├── test/               # Pruebas unitarias (verifican solo la conexion con service)
├── xml_data/           # Archivos XML provistos por el profesor
├── db/                 # Configuración de sesión SQLAlchemy
├── config/             # Lectura de variables de entorno (.env)
├── scripts/            # Scripts de importación (invocan services)
├── .env                # Contiene la URI de conexión a PostgreSQL
├── requirements.txt    # Dependencias necesarias para que funcione
└── README.md           # Este archivo
```

---

## 🔧 Modulos del proyecto

### 1. **models/**

En esta carpeta se definen las **tablas como clases de Python**, utilizando la biblioteca **SQLAlchemy** como ORM (Object Relational Mapper). Cada clase representa una entidad académica (por ejemplo, `Facultad`, `Materia`, `Localidad`) y se mapea a una tabla real de PostgreSQL
* Utiliza `SQLAlchemy` sin usar de `Flask` (mas simple)

### 3. **services/**

* Contiene la **lógica de negocio (que debe hacer)**.
* Lee archivos XML (`ElementTree`) con codificación especial `Windows-1252`.
* Valida, transforma e instancia los modelos para ser guardados por la capa repository.

### 4. **test/**

* Solo se  ** verifica la conexión entre `test → service`**.
* No se valida persistencia ni consultas en la base (No tiene CRUD)

### 5. ** scripts**

Cada entidad tiene un script dedicado dentro de `scripts/`, que:

* Crea las tablas necesarias (si es que no existen, si ya existen solo actualiza el contenido con el metodo cargar de servivce).
* Llama al método `cargar_xml()` para cargar y persistir datos.
---

## ✅ Consideraciones

* El proyecto no es cliente servidor porque no es necesario hacer consultas o modificacion en DEV_SYSACAD. Solo se requeire la persistencia 
* La persistencia se prueba usando archivos reales `.xml`.
* El `Service` contiene la lógica de transformación de XML a objeto.
* El `Repository` encapsula el acceso a la base.
* El `Test` asegura que `Service` se puede instanciar correctamente.
* Los scripts de cada archivo realizan la peristencia
* Problemas de codificación XML resueltos con `windows-1252
* ⚡**En los casos donde los archivos xml tenian errores o los datos que podia usar como PK estaban incompletos o desordenados, use un ID AUTOINCREMENTAL como clave primaria (aparte de guardar los datos que estaban en el xml)**
---

## **Requerimientos y pasos para la ejecución**

1. **Crear el entorno virtual**  
   ➜ `python -m venv venv`

2. **Activar el entorno virtual (necesario para instalar las dependencias y librerias necesarias para que se ejecute)**  
   ➜ `.\venv\Scripts\Activate.ps1`

3. **Instalar las librerías que estan en requirements.txt**  
   ➜ `pip install -r requirements.txt`

4. **Crear un archivo `.env` en la raíz del directorio**  
   ➜ Archivo: `.env`

5. **Usar como modelo el archivo `env-example` y completar en `.env` los datos de conexión a la base de datos**  
   *(usuario, contraseña, nombre de la DB)*

6. **Ejecutar los scripts de carga desde la carpeta `scripts/`**  
   Cada script persiste los datos de un XML distinto.  
   ➜ Para que se creen todas las tablas y se carguen todos los datos, ejecutá cada uno:

   ```bash
   python scripts/facultad_persistencia.py
   python scripts/especialidad_persistencia.py
   python scripts/grado_persistencia.py
   python scripts/materia_persistencia.py
   ...
7. **Se pueden ver las tablas con su contenido usando la terminal de Docker**  
   ➜ Usando la terminal dentro del servidor de DOCKER:

   ```bash
   # Conectarse al usuario
   psql -U sysacad_cristobal -d postgres

   # Listar bases de datos disponibles
   \l

   # Conectarse a la base de datos de trabajo
   \c DEV_SYSACAD

   # Listar todas las tablas dentro de la base actual
   \dt

   # Mostrar el contenido de una tabla específica
   SELECT * FROM nombre_tabla; 
---

## 📅 Mejoras 

>En vez de tener un script de persistencia por archivo o modelo, seria mejor usar un solo script que persista los datos de TODOS los archivos XML. Esto para seguir el principio DRY consiste en que no repitamos bloques de codigo que hacen lo mismo en diferentes partes del proyecto

> Mejorar la importacion de algunos modulos como service y repos
---

## 📚 Tecnologías utilizadas

* **Python 3.13**
* **SQLAlchemy** (ORM)
* **PostgreSQL** como base de datos
* **Archivos XML** con codificación `Windows-1252`
* **Estructura de proyecto en capas** (sin Flask no es cliente-servidor)
* **Docker** (para base de datos local DEV_SYSACAD)
---


## ♻ Autor

Cristobal Buttini  Legajo n° 9976
Sosa Ricardp       Legajo n° 10255

