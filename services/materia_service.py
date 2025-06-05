from xml.etree import ElementTree as ET  # Manejo de XML
from models import Materia
from repositories.materia_repository import MateriaRepository


class MateriaService:
    def __init__(self, repository: MateriaRepository):      
        self.repository = repository                                               #despues lo uso en carfar_xml

    def cargar_xml(self, ruta_xml: str = 'xml_data/materias.xml'):
        
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

            # Iterar por cada elemento <_expxml> que contiene una materia
            for materia_element in root.findall('_expxml'):
                try:
                    # Id no lo especifico porque es autoincremental    (en el xml hay valore repetidos por lo que no podia usar como id algo que se repite)
                    codigo_materia = safe_int(materia_element.find('materia').text)
                    especialidad = safe_int(materia_element.find('especialidad').text)
                    plan = safe_int(materia_element.find('plan').text)
                    nombre = safe_str(materia_element.find('nombre').text)
                    ano = safe_int(materia_element.find('ano').text)

                    # Crear la instancia de Materia sin especificar id (autoincremental)
                    materia = Materia(
                        materia=codigo_materia,
                        especialidad=especialidad,
                        plan=plan,
                        nombre=nombre,
                        ano=ano
                    )

                    # Mostrar en consola los datos cargados para seguimiento
                    print(f"CARGANDO: materia={materia.materia}, especialidad={materia.especialidad}, plan={materia.plan}, nombre={materia.nombre}, ano={materia.ano}")

                    # Persistir la materia en la base de datos a través del repositorio
                    self.repository.persistir(materia)

                except Exception as ex:
                    # Si falla guardar una materia, mostrar error y continuar con la siguiente
                    print(f"[ERROR] No se pudo guardar la materia con código {codigo_materia}: {ex}")

            print("Materias cargadas correctamente (services).")

        except Exception as e:
            # Captura cualquier error inesperado que ocurra durante la carga completa del archivo XML
            print(f"[ERROR] Error inesperado durante la carga del XML: {e}")
