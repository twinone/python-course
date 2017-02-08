import jsondata

# Serialization (object to string)
out_obj = {
    'name': 'John',
    'cities': ['Barcelona', 'London'],
    'test': None,
    'fav_num': 6.2831,
}

out_str = jsondata.dumps(out_obj, indent=2)
print("JSON output:")
print(out_str)
print()


# Deserialization (string to object)
in_str = """
{
  "name": "John",
  "fav_num": 6.2831,
  "test": null,
  "cities": [
    "Barcelona",
    "London"
  ]
}
"""

in_obj = jsondata.loads(in_str)
print("Loaded value of in_str:")
print(in_obj)
