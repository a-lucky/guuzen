# coding:utf-8
import unicodedata

__author__ = 'masa'

import re
import MeCab


# 形態素解析前のテキストの正規化
# https://github.com/neologd/mecab-ipadic-neologd/wiki/Regexp.ja
class NormarizeNeologd:
    @staticmethod
    def unicode_normalize(cls, s):
        pt = re.compile(u'([{}]+)'.format(cls))

        def norm(c):
            return unicodedata.normalize(u'NFKC', c) if pt.match(c) else c

        s = ''.join(norm(x) for x in re.split(pt, s))
        return s

    @staticmethod
    def remove_extra_spaces(s):
        s = re.sub(u'[ 　]+', u' ', s)
        blocks = ''.join((u'\u4E00-\u9FFF',  # CJK UNIFIED IDEOGRAPHS
                          u'\u3040-\u309F',  # HIRAGANA
                          u'\u30A0-\u30FF',  # KATAKANA
                          u'\u3000-\u303F',  # CJK SYMBOLS AND PUNCTUATION
                          u'\uFF00-\uFFEF'   # HALFWIDTH AND FULLWIDTH FORMS
                          ))
        basic_latin = u'\u0000-\u007F'

        def remove_space_between(cls1, cls2, s):
            p = re.compile(u'([{}]) ([{}])'.format(cls1, cls2))

            while p.search(s):
                for gg in p.findall(s):
                    print "search:", gg
                s = p.sub(ur'\1\2', s)
            return s

        s = remove_space_between(blocks, blocks, s)
        s = remove_space_between(blocks, basic_latin, s)
        s = remove_space_between(basic_latin, blocks, s)
        return s

    @staticmethod
    def normalize_neologd(s):
        s = s.strip()
        s = NormarizeNeologd.unicode_normalize(u'０−９Ａ-Ｚａ-ｚ｡-ﾟ', s)

        def maketrans(f, t):
            return {ord(x): ord(y) for x, y in zip(f, t)}

        s = s.translate(
            maketrans(u'!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~｡､･｢｣',
                      u'！”＃＄％＆’（）＊＋，−．／：；＜＝＞？＠［￥］＾＿｀｛｜｝〜。、・「」')
        )

        s = re.sub(u'[˗֊‐‑‒–⁃⁻₋−]+', u'-', s)  # normalize hyphens
        s = re.sub(u'[﹣－ｰ—―─━ー]+', u'ー', s)  # normalize choonpus
        s = re.sub(u'[~∼∾〜〰～]', u'', s)  # remove tildes

        s = NormarizeNeologd.unicode_normalize(u'！”＃＄％＆’（）＊＋，−．／：；＜＞？＠［￥］＾＿｀｛｜｝〜', s)  # keep ＝,・,「,」
        return s

def morphological_analysis(string):
    """
    テキストを形態素解析してリストで返す
    :param str string:
    :rtype: list
    :return: 単語（名詞）のリスト
    """
    # mt = MeCab.Tagger("mecabrc")
    mt = MeCab.Tagger("-d /usr/local/Cellar/mecab/0.996/lib/mecab/dic/mecab-ipadic-neologd")
    mecabnode = mt.parseToNode(string)
    ret = []
    while mecabnode:
        features = mecabnode.feature.split(',')

        if features[0] == "BOS/EOS":
            mecabnode = mecabnode.next
            continue

        if features[0] in ['名詞', '形容詞', '動詞', '副詞', '感動詞']:

            if features[0] == '名詞':
                if features[1] in ['接尾', '接頭', '非自立', '代名詞','形容動詞語幹']:
                    mecabnode = mecabnode.next
                    continue
            elif features[0] == '動詞':
                if features[1] != '自立':
                    mecabnode = mecabnode.next
                    continue

            word = features[6] if features[6] != "*" else mecabnode.surface

            # # 「十二指腸原発悪性絨毛上皮腫の1例」等がうまくいかないので
            # if '数' in features[1]:
            #     if len(word) > 4 and not is_ascii(word):
            #         tmpret = morphological_analysis(word[2:])
            #         ret.extend(tmpret)
            #     mecabnode = mecabnode.next
            #     continue

            # 数字を除く
            regexp = re.compile(u'^[0-9]+$')
            if regexp.search(word):
                mecabnode = mecabnode.next
                continue

            # 記号で始まるものを除く
            regexp = re.compile(u'^[!"#$%&\'()*+,-./:;<=>?@\[\]^_`{|}~]')
            if regexp.search(word):
                mecabnode = mecabnode.next
                continue

            # # 空白をアンダーバーで置き換える(mallet対策)
            # word = word.replace(' ', '_')

            # # 変な日本語を除く(unicodeにしないとマッチしない)
            # regexp = re.compile(u'^(つの|とも|との|である)$')
            # if regexp.search(unicode(word, 'utf_8')):
            #     mecabnode = mecabnode.next
            #     continue

            if word is not "":
                ret.append((word,features[0]))

        mecabnode = mecabnode.next
    return ret