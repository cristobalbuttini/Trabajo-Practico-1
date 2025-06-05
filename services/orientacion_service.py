from xml.etree import ElementTree as ET  # Manejo de XML
from models import Orientacion 
from repositories.orientacion_repository import OrientacionRepository


class OrientacionService:
    def __init__(self, repository: OrientacionRepository):
        self.repository = repository

    def cargar_xml(self, ruta_xml: str = 'xml_data/orientaciones.xml'):

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

            # Iterar por cada elemento <_expxml> que contiene una orientacion
            for orientacion_element in root.findall('_expxml'):
                try:
                    # Id no lo especifico porque es autoincremental    (en el xml hay valore repetidos por lo que no podia usar como id algo que se repite)
                    especialidad = safe_int(orientacion_element.find('especialidad').text)
                    plan = safe_int(orientacion_element.find('plan').text)
                    orientacion = safe_int(orientacion_element.find('orientacion').text)
                    nombre = safe_str(orientacion_element.find('nombre').text)

                    # Crear la instancia de Orientacion sin id porque es autoincremental
                    orientacion = Orientacion(
                        especialidad=especialidad,
                        plan=plan,
                        orientacion=orientacion,
                        nombre=nombre
                    )

                    # Mostrar en consola los datos cargados para seguimiento
                    print(f"CARGANDO: especialidad={orientacion.especialidad}, plan={orientacion.plan}, orientacion={orientacion.orientacion}, nombre={orientacion.nombre}")

                    # Persistir la orientacion en la base de datos a través del repositorio
                    self.repository.persistir(orientacion)

                
                except Exception as ex:
                    # Si falla guardar una orientacion, mostrar error y continuar con la siguiente
                    print(f"[ERROR] No se pudo guardar una orientacion: {ex}")

            print("Orientaciones cargadas correctamente (services).")

        except Exception as e:
            # Captura cualquier error inesperado que ocurra durante la carga completa del archivo XML
            print(f"[ERROR] Error inesperado durante la carga del XML: {e}")
