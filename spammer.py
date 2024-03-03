import hashlib
import os
import sys

for i in range(int(sys.argv[1])):
  with open("secret", "r") as file:
    content = file.read()
    with open("secret", "w") as wfile:
      _hash = hashlib.sha1(content.encode("UTF-8")).hexdigest()
      wfile.write(_hash)
      os.system(f"git add secret && git commit -m {_hash}")