import base64

import source as sup


def test_decode_base64_lines():
  c = "sup\nsuppety sup\nsup sup’s sups sup sup’s sup sup sup sup’s sup sups".encode()
  t = list(sup.io.decode_base64_lines(c))
  e = base64.b64decode(c).decode().split("\n")
  assert t == e
