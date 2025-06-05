from xml.etree import ElementTree as ET  # Manejo de XML
from models import Universidad
from repositories.universidad_repository import UniversidadRepository


class UniversidadService:
    def __init__(self, repository: UniversidadRepository):
        self.repository = repository

    def cargar_xml(self, ruta_xml: str = 'xml_data/universidad.xml'):

        # Metodos para manejar conversiones seguras de tipos y evitar errores de datos null
        def safe_int(text):
            return int(text) if text and text.strip() else None
        def safe_str(text):
            return text if text and text.strip() else None

        try:
            # Abrir y leer el archivo XML con la codificación correcta
            with open(ruta_xml, mode='r', encoding='windows-1252') as f:
                xml_content = f.read()

            # Parsear el contenido XML a un árbol de elementos
            root = ET.fromstring(xml_content)

            # Iterar por cada elemento <_expxml> que contiene una universidad
            for universidad_element in root.findall('_expxml'):
                codigo_universidad = None  # Para usar en el manejo de errores
                
                try:
                    # Id no lo especifico porque es autoincremental 
                    codigo_universidad = safe_int(universidad_element.find('universida').text)
                    nombre = safe_str(universidad_element.find('nombre').text)
                    
                    # Crear la instancia de Universidad sin id porque es autoincremental
                    universidad_obj = Universidad(
                        universidad=codigo_universidad, 
                        nombre=nombre
                    )

                    # Mostrar en consola los datos cargados para seguimiento
                    print(f"CARGANDO: universidad={codigo_universidad}, nombre={nombre}")

                    # Persistir la universidad en la base de datos a través del repositorio
                    self.repository.persistir(universidad_obj)

                except Exception as ex:
                    # Si falla guardar una universidad, mostrar error y continuar con la siguiente
                    print(f"[ERROR] No se pudo guardar la universidad con código {codigo_universidad}: {ex}")

            print("Universidades cargadas correctamente (services).")

        except Exception as e:
            # Captura cualquier error inesperado que ocurra durante la carga completa del archivo XML
            print(f"[ERROR] Error inesperado durante la carga del XML: {e}")