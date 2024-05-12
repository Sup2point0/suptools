import base64

import suptools as sup


def test_decode_base64_lines():
  tests = [
    "short\nconsiderable length\nthe quick brown fox jumps over the lazy dog",
    "short\nvarying length\nquick\nsignificantly longer\ntesting the chunk length\nplease work\ndon't break",
    "sup\nsuppety sup\nsup sup’s sups sup sup’s sup sup sup sup’s sup sups",
    "\n".join(str(i) * i for i in range(1, 10)),
  ]

  for each in tests:
    c = base64.b64encode(each.encode())
    e = base64.b64decode(c).decode().split("\n")
    t = list(sup.io.decode_base64_lines(c))
    assert t == e
