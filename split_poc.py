x = "123.45".split(".")
print(len(x))

y = "123".split(".")
print(y)

content_type = "application/json; charset=utf-8, application/json+*".replace(";", ",").split(",")

print("application/json" in content_type)
# print(True in [("application/json" in c.split(";")) for c in content_type])
