# functions relating to Antarctica


from datetime import datetime


def antect(day = None, *, style = True) -> Tuple[str, int | str]:
  '''Convert a date in the Gregorian calendar to the Antarctican calendar.

  If `style` is True, the first and last days of the decate will become ‘Prime’ and ‘Fine’, respectively.

  ```py
  >>> antect(datetime(2020, 4, 2))
  ('Arteria', 'Prime')
  >>> antect(datetime(2020, 4, 2), style = False)
  ('Arteria', 1)
  >>> antect(datetime(2020, 4, 1))
  ('Verena', 'Fine')
  ```
  '''
  
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

  if style:
    if idx == 1:
      idx = "Prime"
    elif idx == decates.count(dec):
      idx = "Fine"

  return dec, idx
