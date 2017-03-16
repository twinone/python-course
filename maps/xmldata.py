from xml.etree import ElementTree as ET


in_str = """

<station>
  <id>1</id>
  <lat>41.397952</lat>
  <long>2.180042</long>
  <street>Gran Via</street>
  <slots>21</slots>
  <bikes>1</bikes>
</station>


"""


xml = ET.ElementTree(ET.fromstring(in_str))

# find returns the first match, use findall to get all matching elements
lat = float(xml.find("lat").text)
long = float(xml.find("long").text)


print((lat, long))
