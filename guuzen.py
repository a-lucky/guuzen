# coding:utf-8
__author__ = 'masa'

import re
import Neologd


class Dodoitsu:

    def __init__(self, pattern):
        if pattern == 'senryu':
            self.dodoitsu = [[[5]], [[7]], [[5]]]
        elif pattern == 'tanka':
            self.dodoitsu = [[[5]], [[7], [8]], [[5]], [[7], [8]], [[7]]]
        elif pattern == 'dodoitsu':
            self.dodoitsu = [[[3, 4], [4, 4]], [[2, 5], [4, 3]], [[3, 4], [4, 4]], [[5]]]

        self.regs = {}
        self.brackets_start = {}
        self.brackets_end = {}

    def check_bracket(self, utf_str):

        if not self.brackets_start:
            self.brackets_start = {
                u"(": u")",
                u"[": u"]",
                u"{": u"}",
                u"「": u"」",
                u"【": u"】",
                u"『": u"』",
                u"〈": u"〉",
                u"《": u"》",
                u"〔": u"〕",
            }
            for k, v in self.brackets_start.items():
                self.brackets_end[v] = k

        stack = []
        for char in utf_str:
            if char in self.brackets_start:
                stack.append(char)
            elif char in self.brackets_end:
                if not stack or self.brackets_end[char] != stack[-1]:
                    return False
                stack.pop()

        return not stack

    def check_first_word(self, morph):
        if "first_1" not in self.regs:
            self.regs["first_1"] = re.compile(r'^(助詞|助動詞|記号)$')
        if self.regs["first_1"].search(morph["feature"]["品詞"]):
            return False

        if "first_2" not in self.regs:
            self.regs["first_2"] = re.compile(r'^(接尾|非自立)$')
        if self.regs["first_2"].search(morph["feature"]["品詞細分類1"]):
            return False

        if morph["surface"] == 'ー':
            return False

        return True

    def check_last_word(self, morph):
        if "last_1" not in self.regs:
            self.regs["last_1"] = re.compile(r'^(連体詞)$')
        if self.regs["last_1"].search(morph["feature"]["品詞"]):
            return False

        if "last_2" not in self.regs:
            self.regs["last_2"] = re.compile(r'^(名詞接続|格助詞|係助詞|連体化|接続助詞|並立助詞|副詞化|数接続)$')
        if self.regs["last_2"].search(morph["feature"]["品詞細分類1"]):
            return False

        if "last_3" not in self.regs:
            self.regs["last_3"] = re.compile(r'接続')
        if self.regs["last_3"].search(morph["feature"]["活用型"]):
            return False

        return True

    def check_dodoitsu(self, first_i, morphs, deph):
        if not deph < len(self.dodoitsu):
            if self.check_last_word(morphs[first_i - 1]):
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

                    if mo == 0 and not self.check_first_word(morphs[word_i]):
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

        document = Neologd.NormalizeNeologd.normalize_neologd(document.decode('utf-8')).encode('utf-8')

        sentences = [document]

        # sentences = filter(lambda w: len(w) > 0, re.split(r"\. |。", document))

        # print "sentences_num:", len(sentences)

        for sentence in sentences:
            morphs = Neologd.morphological_analysis(sentence)
            first_i = 0
            while first_i < len(morphs):
                if not self.check_first_word(morphs[first_i]):
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

                if self.check_bracket("".join(result_str).decode('utf-8')):
                    find_list.append(result_str)

                first_i += 1

                # for word_i in xrange(first_i, len(morphs)):
                #     moras += morphs[word_i]["count"]
                # print moras
                # break
        return find_list


if __name__ == '__main__':
    do = Dodoitsu('tanka')
    res = do.find_dodoitsu('春過ぎて夏きにけらしい!!白妙の衣干すのだよ天のかぐ山')
    print ' '.join(res[0])
