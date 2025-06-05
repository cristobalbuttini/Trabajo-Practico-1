from xml.etree import ElementTree as ET                      #manejo de XML
from models import Facultad                                  
from repositories.facultad_repository import FacultadRepository

class FacultadService:
    def __init__(self, repository: FacultadRepository):      #el inicilizador recibe una instancia de repositorio para que despues pueda usarlo en los metodos de la clase
        self.repository = repository

    def cargar_xml(self, ruta_xml: str = 'xml_data/facultades.xml'):         
        try:
            # Abrimos el XML en mode read con la codificacion 1252 no UTF-8
            with open(ruta_xml, mode='r', encoding='windows-1252') as f:
                xml_content = f.read()

            # Parseamos desde el string
            root = ET.fromstring(xml_content)

            #cada iteracion lee una facultad
            for facultad_element in root.findall('_expxml'):
                _id = int(facultad_element.find('facultad').text)
                nombre = facultad_element.find('nombre').text.strip()

                facultad = Facultad(id=_id, nombre=nombre)
                print(f"CARGANDO: id={facultad.id}, nombre={facultad.nombre}")


                #usamos el repositorio para persisitir cada facultad en la BD
                self.repository.persistir(facultad)

            print("Facultades cargadas correctamente (services).")


        except UnicodeDecodeError as e:                             #manejo de errores por caracteres no validos
            print(f"[ERROR] Error de codificación: {e}")
        except ET.ParseError as e:                                  #manejo de errores por etiquetas mal formadas en el XML
            print(f"[ERROR] XML mal formado: {e}")
        except Exception as e:                                      #manejo de errores generales
            print(f"[ERROR] Error inesperado: {e}")
