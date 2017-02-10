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
    try:
        src = [float(x) for x in sys.stdin.readline().split(",")]
    except:
        src = COORDS_CAMPUS_NORD

    print("Introduce coordenadas de destino")
    try:
        dst = [float(x) for x in sys.stdin.readline().split(",")]
    except:
        dst = COORDS_SAFA
    return src, dst


def free(station, type="bikes"):
    """
    Dado el xml ElementTree de una station, devuelve el numero de bicis o huecos disponibles
    si type es "bikes" se devolvera el numero de bicis
    si type es "slots" se devolvera el numero de huecos
    """
    return int(station.find(type).text)



def get_coords(station):
    """Devuelve las coordenadas (lat, long) de una estacion como floats"""
    return float(station.find('lat').text), float(station.find('long').text)



def nearest_station(coords, type):
    """
    Devuelve la id y las coordenadas de la estación mas cercana a coords
    que tenga como minimo una bici si type es "bikes" o un hueco si type es "slots"
    Si no existe ninguna estación o está a más de 1km se devolverá None
    """

    data = webclient.httpget(BICING_ENDPOINT)
    xml = ET.ElementTree(ET.fromstring(data))
    stations = [st for st in xml.findall(".//station")
                if free(st, type) >= 1
                and util.distance(coords, get_coords(st)) <= 1]
    # sort by distance
    stations = sorted(stations, key = lambda x: util.distance(coords, get_coords(x)))

    # print results
    #for st in stations:
    #    print(st.find('street').text, util.distance(coords, get_coords(st)))
    return stations[0] if stations else None



if __name__ == '__main__':
    src, dst = read_coordinates()
    src_station = nearest_station(src, "bikes")
    dst_station = nearest_station(dst, "slots")

    src_st_coords = get_coords(src_station)
    dst_st_coords = get_coords(dst_station)

    util.maps(src_st_coords, dst_st_coords)