#!/usr/bin/env python3
import argparse
import logging

import matplotlib.pyplot as plt

from matplotlib.ticker import (MultipleLocator, FormatStrFormatter)

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)
logger = logging.getLogger('WLEN')

UNITS = ['meter', 'feet']

BANDS = {
  160: (1800., 2000., 1),
  80: (3500., 4000., 2),
  60: (5330.5, 5405., 2),
  40: (7000., 7300., 3),
  30: (10100., 10150., 3),
  20: (14000., 14350., 4),
  17: (18068., 18168., 4),
  15: (21000., 21450., 4),
  12: (24890., 24990., 5),
  10: (28000., 29700., 6),
   6: (50000., 54000., 6),
}

class Unit:
  pass

def wire_length(min_khz, max_khz, nb_harmonics):
  data = []
  half_wl = Unit.light_speed / 2

  qtr = half_wl / (min_khz * 1e-3) / 2
  data = [(0, qtr)]

  for harmonic in range(2, 2+nb_harmonics):
    lambda0 = harmonic * half_wl / (max_khz * 1e-3)
    lambda1 = harmonic * half_wl / (min_khz * 1e-3)
    data.append((lambda0, lambda1-lambda0))

  logger.debug(data)
  return data

def plot(filename, bands):
  band_names = ', '.join([str(b) for b in sorted(bands.keys(), reverse=True)])
  logging.info("Bands: %s", band_names)

  fig, axis = plt.subplots(figsize=(15, 1.5))
  fig.set_tight_layout("w_pad")

  for band in bands.values():
    axis.broken_barh(wire_length(*band), (0, 1), facecolors='navy')

  axis.xaxis.set_major_locator(MultipleLocator(Unit.xlabels))
  axis.xaxis.set_major_formatter(FormatStrFormatter('%d'))
  axis.xaxis.set_minor_locator(MultipleLocator(5))
  axis.set_xlabel('Wires length in {}'.format(Unit.name))

  axis.margins(0.0, 0.0)
  axis.set_yticks([0, 1])
  axis.set_yticklabels([])
  axis.set_title('Wire length to avoid for ({}) meter'.format(band_names))
  plt.savefig(filename, dpi=100)
  logger.info('"%s" saved', filename)

def main():
  parser = argparse.ArgumentParser(description='Wire length to avoid')
  parser.add_argument('-D', '--debug', action='store_true', default=False,
                      help='Print information useful for debugging')
  parser.add_argument('-b', '--bands', nargs="+", type=int, default=[40, 20, 15, 10],
                      help=('List of bands [default: %(default)s]'))
  parser.add_argument('-f', '--file', default='wire.png',
                      help='Graph filename [default: %(default)s]')
  parser.add_argument('-u', '--unit', choices=UNITS, default=UNITS[0],
                      help='Wire length [default: %(default)s]')

  pargs = parser.parse_args()

  if pargs.debug:
    logger.setLevel(logging.DEBUG)
  logger.debug(pargs)

  # select bands
  bands = {}
  for band in pargs.bands:
    try:
      bands[band] = BANDS[band]
    except KeyError:
      logger.error('%d m is not an HF or amateur band', band)

  # unit
  Unit.name = pargs.unit
  if pargs.unit == 'meter':
    Unit.light_speed = 299.80
    Unit.xlabels = 10
  elif pargs.unit == 'feet':
    Unit.light_speed = 983
    Unit.xlabels = 30
  else:
    raise argparse.ArgumentError

  plot(pargs.file, bands)

if __name__ == "__main__":
  main()
