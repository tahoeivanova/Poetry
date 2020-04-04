import string
# import collections
import pymorphy2
import random


# класс для одного стиха
class MetaPoet:
    def __init__(self, poem):
        self.poem = poem

    def __str__(self):
        return f'{self.poem}'

    def __len__(self):
        self.count = 0
        for x in self.poem:
            self.count += 1
        return self.count

    def remove_punctuation(self):
        for sign in string.punctuation:
            self.poem = self.poem.replace(sign, " ")
        return self.poem

    def split_words(self):
        self.poem = self.poem.split()
        return self.poem

    def lower_case(self):
        # words_of_poem = []
        self.poem = list(map(lambda word: word.lower(), self.poem))
        return self.poem

    def lemma(self):
        morph = pymorphy2.MorphAnalyzer()
        self.poem = list(map(lambda word: morph.parse(word)[0].normal_form, self.poem))
        return self.poem

    def unique_words(self):
        self.poem = set(self.poem)
        return self.poem


    def stop_words(self):
        pass

    def poem_dictionary(self):
        all_noun = []  # NOUN имя существительное хомяк
        all_adjf = []  # ADJF имя прилагательное (полное) хороший
        all_adjs = []  # ADJS имя прилагательное (краткое) хорош
        all_comp = []  # COMP компаратив лучше, получше, выше
        all_verb = []  # VERB глагол (личная форма) говорю, говорит, говорил
        all_infn = []  # INFN глагол (инфинитив) говорить, сказать
        all_prtf = []  # PRTF причастие (полное) прочитавший, прочитанная
        all_prts = []  # PRTS причастие (краткое) прочитана
        all_grnd = []  # GRND деепричастие прочитав, рассказывая
        all_numr = []  # NUMR числительное три, пятьдесят
        all_advb = []  # ADVB наречие круто
        all_npro = []  # NPRO местоимение-существительное он
        all_pred = []  # PRED предикатив некогда
        all_prep = []  # PREP предлог в
        all_conj = []  # CONJ союз и
        all_prcl = []  # PRCL частица бы, же, лишь
        all_intj = []  # INTJ междометие
        unknown_part = [] # не определенные pymorphy2 части речи

        morph = pymorphy2.MorphAnalyzer()

        for word in self.poem:
            a = morph.parse(word)[0]
            if a.tag.POS == 'NOUN':
                all_noun.append(a.normal_form)
            elif a.tag.POS == 'ADJF':
                all_adjf.append(a.normal_form)
            elif a.tag.POS == 'ADJS':
                all_adjs.append(a.normal_form)
            elif a.tag.POS == 'COMP':
                all_comp.append(a.normal_form)
            elif a.tag.POS == 'VERB':
                all_verb.append(a.normal_form)
            elif a.tag.POS == 'INFN':
                all_infn.append(a.normal_form)
            elif a.tag.POS == 'PRTF':
                all_prtf.append(a.normal_form)
            elif a.tag.POS == 'PRTS':
                all_prts.append(a.normal_form)
            elif a.tag.POS == 'GRND':
                all_grnd.append(a.normal_form)
            elif a.tag.POS == 'NUMR':
                all_numr.append(a.normal_form)
            elif a.tag.POS == 'ADVB':
                all_advb.append(a.normal_form)
            elif a.tag.POS == 'NPRO':
                all_npro.append(a.normal_form)
            elif a.tag.POS == 'PRED':
                all_pred.append(a.normal_form)
            elif a.tag.POS == 'PREP':
                all_prep.append(a.normal_form)
            elif a.tag.POS == 'CONJ':
                all_conj.append(a.normal_form)
            elif a.tag.POS == 'PRCL':
                all_prcl.append(a.normal_form)
            elif a.tag.POS == 'INTJ':
                all_intj.append(a.normal_form)
            else:
                unknown_part.append(a)

        self.all_parts_of_speech = {'имя существительное': all_noun, 'имя прилагательное (полное)': all_adjf, 'имя прилагательное (краткое)':all_adjs, 'компаратив':all_comp,
     'глагол': all_infn, 'причастие (полное)': all_prtf, 'причастие (краткое)': all_prts,
        'деепричастие':all_grnd,'числительное':all_numr, 'наречие':all_advb, 'местоимение-существительное': all_npro, 'предикатив':all_pred,
        'предлог': all_prep, 'союз': all_conj, 'частица': all_prcl, 'междометие': all_intj}

        return self.all_parts_of_speech
