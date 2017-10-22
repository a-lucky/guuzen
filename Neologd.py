# coding:utf-8
import unicodedata

__author__ = 'masa'

import re
import MeCab


class NormalizeNeologd:
    @staticmethod
    def unicode_normalize(cls, s):
        pt = re.compile(u'([{}]+)'.format(cls))

        def norm(c):
            return unicodedata.normalize(u'NFKC', c) if pt.match(c) else c

        s = u''.join(norm(x) for x in re.split(pt, s))
        s = re.sub(u'－', u'-', s)
        return s

    @staticmethod
    def remove_extra_spaces(s):
        s = re.sub(u'[ 　]+', u' ', s)
        blocks = u''.join((u'\u4E00-\u9FFF',  # CJK UNIFIED IDEOGRAPHS
                           u'\u3040-\u309F',  # HIRAGANA
                           u'\u30A0-\u30FF',  # KATAKANA
                           u'\u3000-\u303F',  # CJK SYMBOLS AND PUNCTUATION
                           u'\uFF00-\uFFEF'   # HALFWIDTH AND FULLWIDTH FORMS
                           ))
        basic_latin = u'\u0000-\u007F'

        def remove_space_between(cls1, cls2, s):
            p = re.compile(u'([{}]) ([{}])'.format(cls1, cls2))
            while p.search(s):
                s = p.sub(ur'\1\2', s)
            return s

        s = remove_space_between(blocks, blocks, s)
        s = remove_space_between(blocks, basic_latin, s)
        s = remove_space_between(basic_latin, blocks, s)
        return s

    @staticmethod
    def normalize_neologd(s):
        """
        :param unicode s:
        :rtype:
        :return unicode:
        """
        s = s.strip()
        s = NormalizeNeologd.unicode_normalize(u'０-９Ａ-Ｚａ-ｚ｡-ﾟ', s)

        def maketrans(f, t):
            return {ord(x): ord(y) for x, y in zip(f, t)}

        s = re.sub(u'[˗֊‐‑‒–⁃⁻₋−]+', u'-', s)  # normalize hyphens
        s = re.sub(u'[﹣－ｰ—―─━ー]+', u'ー', s)  # normalize choonpus
        s = re.sub(u'[~∼∾〜〰～]', u'', s)  # remove tildes
        s = s.translate(
            maketrans(u'!"#$%&\'()*+,-./:;<=>?@[¥]^_`{|}~｡､･｢｣',
                      u'！”＃＄％＆’（）＊＋，－．／：；＜＝＞？＠［￥］＾＿｀｛｜｝〜。、・「」'))

        s = NormalizeNeologd.remove_extra_spaces(s)
        s = NormalizeNeologd.unicode_normalize(u'！”＃＄％＆’（）＊＋，－．／：；＜＞？＠［￥］＾＿｀｛｜｝〜', s)  # keep ＝,・,「,」
        s = re.sub(u'[’]', u'\'', s)
        s = re.sub(u'[”]', u'"', s)
        return s


def count_mora(word):
    word = word.decode("utf-8")
    # word = word.translate(string.maketrans('ぁ-ゔ', 'ァ-ヴ'))
    word = re.sub(u'[^アイウエオカ-モヤユヨラ-ロワヲンヴー]', '', word)
    return len(word)


mt = MeCab.Tagger("mecabrc")
# mt = MeCab.Tagger("-d /usr/local/Cellar/mecab/0.996/lib/mecab/dic/mecab-ipadic-neologd")


def morphological_analysis(text):

    mecabnode = mt.parseToNode(text)

    morphs = []

    while mecabnode:
        features = mecabnode.feature.split(',')

        if features[0] == "BOS/EOS":
            mecabnode = mecabnode.next
            continue

        yomi = ""

        # 読みが無い時
        if len(features) <= 7:
            regexp = re.compile(u'^[\u30A0-\u30FF]+$')
            if regexp.search(unicode(mecabnode.surface, 'utf_8')):
                yomi = mecabnode.surface
            else:
                mecabnode = mecabnode.next
                continue
        else:
            yomi = features[7]

        morphs.append({
            "surface": mecabnode.surface,
            "feature": {
                "品詞": features[0],
                "品詞細分類1": features[1],
                "品詞細分類2": features[2],
                "品詞細分類3": features[3],
                "活用形": features[4],
                "活用型": features[5],
                "読み": yomi
                },
            "count": count_mora(yomi)
        })
        mecabnode = mecabnode.next

    return morphs