import util
import webclient
import sys
import xml.etree.ElementTree as ET

COORDS_CAMPUS_NORD = (41.387453, 2.113686)
COORDS_SAFA = (41.403618, 2.174361)
BICING_ENDPOINT = "http://wservice.viabicing.cat/v1/getstations.php?v=1"


def read_coordinates():
    """
    Devuelve las coordenadas de origen y destino
    en como tuplas (lat, long)
    Ejemplo:
    get_coordinates() => (41.387453, 2.113686), (41.403618, 2.174361)
    """

    print("Introduce coordenadas de origen")
    # 1. Leer coordenadas de origen. Si hay algun error hay que usar COORDS_CAMPUS_NORD

    print("Introduce coordenadas de destino")
    # 2. Leer coordenadas de destino. Si hay algun error hay que usar COORDS_SAFA

    # 3. Devolver el resultado
    pass

def free(station, type="bikes"):
    """
    Dado el xml ElementTree de una station, devuelve el numero de bicis o huecos disponibles
    si type es "bikes" se devolvera el numero de bicis
    si type es "slots" se devolvera el numero de huecos
    """
    pass



def get_coords(station):
    """Devuelve las coordenadas (lat, long) de una estacion como floats"""
    pass



def nearest_station(coords, type):
    """
    Devuelve la id y las coordenadas de la estación mas cercana a coords
    que tenga como minimo una bici si type es "bikes" o un hueco si type es "slots"
    Si no existe ninguna estación o está a más de 1km se devolverá None
    """

    # 1. http get de los datos del endpoint
    # 2. parsear el xml
    # 3. filtrar las estaciones (list comprehensio)
    # 4. ordenar las estaciones por distancia
    # 5. devolver la primera
    pass



if __name__ == '__main__':
    # 1. read_coordinates()
    # 2. obtener las estaciones mas cercanas
    # 3. obtener las coordenadas de las estaciones
    # 4. abrir el maps con util.maps()
    pass
