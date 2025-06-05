from xml.etree import ElementTree as ET  # Manejo de XML
from models import Plan
from repositories.plan_repository import PlanRepository


class PlanService:
    def __init__(self, repository: PlanRepository):
        self.repository = repository

    def cargar_xml(self, ruta_xml: str = 'xml_data/planes.xml'):

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
            for plan_element in root.findall('_expxml'):
                try:
                    # Id no lo especifico porque es autoincremental 
                    especialidad = safe_int(plan_element.find('especialidad').text)
                    plan = safe_int(plan_element.find('plan').text)
                    nombre = safe_str(plan_element.find('nombre').text)

                    # Crear la instancia de Plan sin id porque es autoincremental
                    plan = Plan(
                        especialidad=especialidad,
                        plan=plan,
                        nombre=nombre)

                    # Mostrar en consola los datos cargados para seguimiento
                    print(f"CARGANDO: especialidad={plan.especialidad}, plan={plan.plan}, nombre={plan.nombre}")

                    # Persistir la plan en la base de datos a través del repositorio
                    self.repository.persistir(plan)

                except Exception as ex:
                    # Si falla guardar una plan, mostrar error y continuar con la siguiente
                    print(f"[ERROR] No se pudo guardar una plan: {ex}")

            print("Planes cargados correctamente (services).")

        except Exception as e:
            # Captura cualquier error inesperado que ocurra durante la carga completa del archivo XML
            print(f"[ERROR] Error inesperado durante la carga del XML: {e}")

                       