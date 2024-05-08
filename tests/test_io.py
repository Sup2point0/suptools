import sys, os
print(f"path = {sys.path}")
print(f"cwd = {os.getcwd()}")

import base64

import suptools as sup


def test_decode_base64_lines():
  c = base64.b64encode("sup\nsuppety sup\nsup sup’s sups sup sup’s sup sup sup sup’s sup sups".encode())
  e = base64.b64decode(c).decode().split("\n")
  t = list(sup.io.decode_base64_lines(c))
  assert t == e
