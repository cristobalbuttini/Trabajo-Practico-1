from xml.etree import ElementTree as ET                      #manejo de XML
from models import Localidad                              
from repositories.localidad_repository import LocalidadRepository

class LocalidadService:
    def __init__(self, repository: LocalidadRepository):      #el inicilizador recibe una instancia de repositorio para que despues pueda usarlo en los metodos de la clase
        self.repository = repository

    def cargar_xml(self, ruta_xml: str = 'xml_data/localidades.xml'):         
        try:
            # Abrimos el XML en mode read con la codificacion 1252 no UTF-8
            with open(ruta_xml, mode='r', encoding='windows-1252') as f:
                xml_content = f.read()

            # Parseamos desde el string
            root = ET.fromstring(xml_content)

            #cada iteracion lee un grado
            for localidad_element in root.findall('_exportar'):
                _id = int(localidad_element.find('codigo').text)
                ciudad = localidad_element.find('ciudad').text.strip()
                provincia = localidad_element.find('provincia').text.strip()
                pais = localidad_element.find('pais_del_c').text.strip()

                localidad = Localidad(id=_id, ciudad=ciudad, provincia=provincia, pais=pais)
                print(f"CARGANDO: id={localidad.id}, ciudad={localidad.ciudad}, provincia={localidad.provincia}, pais={localidad.pais}")

                #usamos el repositorio para persisitir cada localidad en la BD
                self.repository.persistir(localidad)

            print("Localidades cargadas correctamente (services).")


        except UnicodeDecodeError as e:                             #manejo de errores por caracteres no validos
            print(f"[ERROR] Error de codificación: {e}")
        except ET.ParseError as e:                                  #manejo de errores por etiquetas mal formadas en el XML
            print(f"[ERROR] XML mal formado: {e}")
        except Exception as e:                                      #manejo de errores generales
            print(f"[ERROR] Error inesperado: {e}")
