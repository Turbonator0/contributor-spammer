import hashlib
import os
import sys

for i in range(int(sys.argv[1])):
  with open("secret", "r+") as file:
    content = file.read()
    _hash = hashlib.sha256(content.encode("UTF-8")).hexdigest()
    file.write(_hash)
    os.system(f"git add secret && git commit -m {_hash}")