
# Random Wire Antenna Calculator

This program helps you to calculate the optimal length of wire for
building a random length antenna.

## Installation

```
$ pip install randwire
```

## Usage

```
usage: randwire.py [-h] [-D] [-b BANDS [BANDS ...]] [-f FILE]
                   [-u {meter,feet}]

Wire length to avoid

optional arguments:
  -h, --help            show this help message and exit
  -D, --debug           Print information useful for debugging
  -b BANDS [BANDS ...], --bands BANDS [BANDS ...]
                        List of bands [default: [40, 20, 15, 10]]
  -f FILE, --file FILE  Graph filename [default: wire.png]
  -u {meter,feet}, --unit {meter,feet}
                        Wire length [default: meter]
```

## Example

```
√ % randwire
13:45:27 INFO: Bands: 40, 20, 15, 10
13:45:27 INFO: "wire.png" saved
```

This will generate the following image. Where the blue blocks
represent the length of wire to avoid.

![Wire Length](https://raw.githubusercontent.com/0x9900/randwire/main/misc/wire.png)

More info on my blog post [Random-Wire antenna][1] related to this program.

[1]: https://0x9900.com/random-wire-antenna/
