import hashlib
import os
import sys
import random

for i in range(int(sys.argv[1])):
  with open("secret", "w") as wfile:
    _hash = hashlib.sha1(str(random.randint(1,1000)).encode("UTF-8")).hexdigest()
    wfile.write(_hash)
  os.system(f"git add secret && git commit -m {_hash}")
# Automagically push to Github
os.system("git push origin master")