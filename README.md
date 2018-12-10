# ChineseNumber

Convert Chinese (or Japanese) numbers (e.g. 二十一) to numeric digits (21).

Similar in idea to https://github.com/akshaynagpal/w2n

The resulting numbers can be sorted using https://github.com/SethMMorton/natsort

## Usage

```pydocstring
>>> from chinesenumber import NumberParser
>>> parser = NumberParser()
>>> parser.numberify('第二十二课')
'第22课'
>>> parser.simple_parse('百六十五')
165
```

## Installation

```
pip install chinesenumber
```
