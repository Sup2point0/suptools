from source import iterate


def test_chunked():
  c = list(range(7))
  t = list(iterate.chunked(c, 3))
  e = [(0, 1, 2), (3, 4, 5), (6,)]
  assert t == e
