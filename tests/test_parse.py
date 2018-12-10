import pytest

from chinesenumber import NumberParser


class TestNumberParser:
    parser = NumberParser()

    @pytest.mark.parametrize('in_, out_', [
        ('两', 2),
        ('二十', 20),
        ('百六十五', 165),
        ('一百六', 106)
    ])
    def test_simple_parse(self, in_, out_):
        assert self.parser.simple_parse(in_) == out_

    @pytest.mark.parametrize('in_, out_', [
        ('第二课', '第2课'),
        ('第十课', '第10课'),
        ('第十二课', '第12课'),
        ('第二十二课', '第22课')
    ])
    def test_numberify(self, in_, out_):
        assert self.parser.numberify(in_) == out_
