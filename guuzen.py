# coding:utf-8
__author__ = 'masa'

import re
import MeCab

def count_mora(word):
    word = word.decode("utf-8")
    # word = word.translate(string.maketrans('ぁ-ゔ', 'ァ-ヴ'))
    word = re.sub(u'[^アイウエオカ-モヤユヨラ-ロワヲンヴー]', '', word)
    return len(word)


def morphological_analysis(text):
    # mt = MeCab.Tagger("-d /usr/local/Cellar/mecab/0.996/lib/mecab/dic/mecab-ipadic-neologd")
    mt = MeCab.Tagger("mecabrc")
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


class Dodoitsu:

    def __init__(self, pattern):
        if pattern == 'senryu':
            self.dodoitsu = [[[5]], [[7]], [[5]]]
        elif pattern == 'tanka':
            self.dodoitsu = [[[5]], [[7]], [[5]], [[7]], [[7]]]
        elif pattern == 'dodoitsu':
            self.dodoitsu = [[[3, 4], [4, 4]], [[2, 5], [4, 3]], [[3, 4], [4, 4]], [[5]]]

    @staticmethod
    def check_first_word(morph):
        regexp = re.compile(r'^(助詞|助動詞|記号)$')
        if regexp.search(morph["feature"]["品詞"]):
            return False
        regexp = re.compile(r'^(接尾|非自立)$')
        if regexp.search(morph["feature"]["品詞細分類1"]):
            return False
        if morph["surface"] == 'ー':
            return False

        return True

    @staticmethod
    def check_last_word(morph):
        regexp = re.compile(r'^(連体詞)$')
        if regexp.search(morph["feature"]["品詞"]):
            return False
        regexp = re.compile(r'^(名詞接続|格助詞|係助詞|連体化|接続助詞|並立助詞|副詞化|数接続)$')
        if regexp.search(morph["feature"]["品詞細分類1"]):
            return False
        regexp = re.compile(r'接続')
        if regexp.search(morph["feature"]["活用型"]):
            return False

        return True

    def check_dodoitsu(self, first_i, morphs, deph):
        if not deph < len(self.dodoitsu):
            if Dodoitsu.check_last_word(morphs[first_i - 1]):
                return [first_i, []]
            else:
                return [-1, []]

        for doitsu in self.dodoitsu[deph]:
            word_i = first_i
            for lim in doitsu:
                mo = 0
                while mo < lim:
                    if not word_i < len(morphs):
                        break

                    if mo == 0 and not Dodoitsu.check_first_word(morphs[word_i]):
                        # print morphs[word_i]["surface"]
                        break

                    mo += morphs[word_i]["count"]
                    word_i += 1
                if not mo == lim:
                    break
            else:
                res = self.check_dodoitsu(word_i, morphs, deph+1)
                if res[0] != -1:
                    res[1].append(first_i)
                    return res

        return [-1, []]

    # dodoit = [[7, 7, 7, 5], [8, 7, 7, 5], [7, 7, 8, 5], [8, 7, 8, 5]]

    # def check_dodoitsu1(first_i, morphs):
    #     for dodo in dodoit:
    #         word_i = first_i
    #         for lim in dodo:
    #             mo = 0
    #             while mo < lim:
    #                 if not word_i < len(morphs):
    #                     break
    #                 mo += morphs[word_i]["count"]
    #                 word_i += 1
    #
    #             if not mo == lim:
    #                 break
    #         else:
    #             return word_i
    #     return -1

    def find_dodoitsu(self, document):

        find_list = []

        sentences = filter(lambda w: len(w) > 0, re.split(r"\. |｡|．|。", document))

        # print "sentences_num:", len(sentences)

        for sentence in sentences:
            morphs = morphological_analysis(sentence)
            first_i = 0
            while first_i < len(morphs):
                if not Dodoitsu.check_first_word(morphs[first_i]):
                    first_i += 1
                    continue

                result = self.check_dodoitsu(first_i, morphs, 0)
                last_i = result[0]
                result[1].reverse()
                result[1].append(last_i)

                if last_i < 0:
                    # print "miss"
                    first_i += 1
                    continue

                result_str = []
                i = first_i
                j = 1
                count = 0
                surface = ''
                while i < last_i:
                    count += morphs[i]["count"]
                    surface += morphs[i]["surface"]
                    i += 1
                    if i == result[1][j]:
                        result_str.append(surface)
                        j += 1
                        count = 0
                        surface = ''
                find_list.append(result_str)
                first_i += 1

                # for word_i in xrange(first_i, len(morphs)):
                #     moras += morphs[word_i]["count"]
                # print moras
                # break
        return find_list

# if __name__ == '__main__':
#     do = Dodoitsu('dodoitsu')
#     res = do.find_dodoitsu('あるじーあるじーあるじーあるじーあるじーあるじーあるじーあるじー')
#     print ' '.join(res[0])