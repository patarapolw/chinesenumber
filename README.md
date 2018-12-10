# ChineseNumber

[![PyPI version shields.io](https://img.shields.io/pypi/v/chinesenumber.svg)](https://pypi.python.org/pypi/chinesenumber/)
[![PyPI license](https://img.shields.io/pypi/l/chinesenumber.svg)](https://pypi.python.org/pypi/chinesenumber/)
[![Examples tested with pytest-readme](http://img.shields.io/badge/readme-tested-brightgreen.svg)](https://github.com/boxed/pytest-readme)

Convert Chinese (or Japanese) numbers (e.g. 二十一) to numeric digits (21).

Similar in idea to https://github.com/akshaynagpal/w2n

The resulting numbers can be sorted using https://github.com/SethMMorton/natsort

If you want to sort non-numeral, some best options are https://github.com/avian2/unidecode

## Usage

```pydocstring
>>> from chinesenumber import NumberParser
>>> parser = NumberParser()
>>> parser.numberify('第二十二课')
'第22课'
>>> parser.simple_parse('百六十五')
165
>>> parser.numberify('二〇一三', simple=True)
'2013'
```

## Installation

```
pip install chinesenumber
```
