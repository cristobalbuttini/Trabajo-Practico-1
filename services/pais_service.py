from xml.etree import ElementTree as ET  # Manejo de XML
from models import Pais
from repositories.pais_repository import PaisRepository


class PaisService:
    def __init__(self, repository: PaisRepository):
        self.repository = repository

    def cargar_xml(self, ruta_xml: str = 'xml_data/paises.xml'):

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
            for pais_element in root.findall('_expxml'):
                try:
                    # Id no lo especifico porque es autoincremental   
                    pais_nro = safe_int(pais_element.find('pais').text)
                    nombre = safe_str(pais_element.find('nombre').text)

                    # Crear la instancia de Pais sin id porque es autoincremental
                    pais = Pais(
                        pais_nro=pais_nro,
                        nombre=nombre)

                    # Mostrar en consola los datos cargados para seguimiento
                    print(f"CARGANDO: pais_nro={pais.pais_nro}, nombre={pais.nombre}")

                    # Persistir la pais en la base de datos a través del repositorio
                    self.repository.persistir(pais)

                except Exception as ex:
                    # Si falla guardar una pais, mostrar error y continuar con la siguiente
                    print(f"[ERROR] No se pudo guardar una pais: {ex}")

            print("Paises cargados correctamente (services).")

        except Exception as e:
            # Captura cualquier error inesperado que ocurra durante la carga completa del archivo XML
            print(f"[ERROR] Error inesperado durante la carga del XML: {e}")

                       