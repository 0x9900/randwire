
# Random Wire Antenna Calculator

This program helps you to calculate the optimal length of wire for
building a random length antenna.

You can find more info on my blog post related to this program:
[Random-Wire antenna][1].

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
  -f FILE, --file FILE  Graph filename, then extention can be (.png, .pdf,
                        .svg) [default: wire.png]
  -u {meter,feet}, --unit {meter,feet}
                        Wire length [default: meter]
```

## Example

```
√ % randwire
13:45:27 INFO: Bands: 40, 20, 15, 10
13:45:27 INFO: "wire.png" saved
```

The program generates an image showing the length of the wire to
avoid. The blue blocks represent the length of the wire that might
cause tuning problems.

![Wire Length](https://raw.githubusercontent.com/0x9900/randwire/main/misc/wire.png)


[1]: https://0x9900.com/random-wire-antenna/
