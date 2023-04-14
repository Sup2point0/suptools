# functions relating to Antarctica


from datetime import datetime


def antect(day = None):
  decates = (
    37 * ["Arteria"]   + 36 * ["Vitida"]
  + 37 * ["Arrikta"]   + 36 * ["Valia"]
  + 37 * ["Aliquanda"] + 36 * ["Verita"]
  + 37 * ["Arteva"]    + 36 * ["Vepida"]
  + 37 * ["Aeva"]      + 36 * ["Verena"]
  )

  if not day: day = datetime.now()
  idx = (day.timetuple().tm_yday + 273) % 365
  dec = decates[idx]
  idx -= decates.index(dec) - 1

  if idx == 1:
    idx = "Prime"
  elif idx == decates.count(dec):
    idx = "Fine"

  return dec, idx
