import json

JSON = """\
        {
          "name": "John",
          "age": 30,
          "city": "New York"
        }
    """

print(JSON)

y = json.loads(JSON)
print(y)

z = json.dumps(JSON)
print(z)
