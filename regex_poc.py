import re

print(bool(re.match(r"^\d*$", "123s")))
if re.match(r"^\d*$", "123"):
    print("match")



