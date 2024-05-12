from suptools import search


def test_search_dict():
  source = {"sup": 2.0, "super": {"nova": 4.2}}

  assert search.in_dict(source, "sup") == 2.0
  assert search.in_dict(source, "nova") == 4.2
