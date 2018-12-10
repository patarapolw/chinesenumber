import re

number_prefix = {
    1: '１一弌壱壹幺',
    2: '２二弍贰貳两兩',
    3: '３三参叁叄仨',
    4: '４四肆',
    5: '５五伍',
    6: '６六陆陸',
    7: '７七柒拐',
    8: '８八捌',
    9: '９九玖勾'
}

number_multiplier = {
    10**(-6): '微',
    0.001: '毫毛',
    0.01: '厘釐',
    0.1: '分割',
    0: '０〇零洞',
    10: '十拾呀',
    # 20: '廿念',
    # 30: '卅',
    # 40: '卌',
    100: '百佰',
    # 200: '皕',
    1000: '千仟',
    10**4: '万萬',
    10**8: '亿億',
    10**12: '兆',
    10**16: '京',
    10**20: '垓',
    10**24: '𥝱秭',
    10**28: '穣',
    10**32: '溝',
    10**36: '澗',
    10**40: '正',
    10**44: '載',
    10**48: '極'
}


class NumberParser:
    def __init__(self):
        self.pre = dict()
        for k, v in number_prefix.items():
            for c in v:
                self.pre[c] = k

        self.mul = dict()
        for k, v in number_multiplier.items():
            for c in v:
                self.mul[c] = k

    def simple_parse(self, s):
        v_str_array = re.findall(r'[{pre}]?[{mul}]?'.format(
            pre=''.join(self.pre.keys()),
            mul=''.join(self.mul.keys())
        ), s)

        output = 0
        for v_str in v_str_array:
            if len(v_str) == 1:
                output += float(self.pre.get(v_str[0], self.mul.get(v_str[0])))
            elif len(v_str) == 2:
                output += int(self.pre[v_str[0]]) * float(self.mul[v_str[1]])

        return self._coerce_int(output)

    def numberify(self, s):
        return re.sub(r'[%s]+' % (
            ''.join(self.pre.keys()) + ''.join(self.mul.keys())
        ), lambda x: str(self.simple_parse(x.group(0))), s)

    @staticmethod
    def _coerce_int(i: float):
        if i.is_integer():
            return int(i)
        else:
            return i
