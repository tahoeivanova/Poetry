import string
import collections
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

# ________________________TOP 100 WORDS
    def top_100_words(self):
        lemmed_words = []
        morph = pymorphy2.MorphAnalyzer()
        lemmed_words = [word for word in self.poem if morph.parse(word)[0].tag.POS == 'NOUN' or morph.parse(word)[0].tag.POS == 'INFN' or morph.parse(word)[0].tag.POS == 'ADJF' or morph.parse(word)[0].tag.POS == 'ADJS' or morph.parse(word)[0].tag.POS == 'PRTF' or morph.parse(word)[0].tag.POS == 'GRND' or morph.parse(word)[0].tag.POS == 'ADVB'or morph.parse(word)[0].tag.POS == 'NPRO']
        c = collections.Counter(lemmed_words)
        self.result = c.most_common(100)
        return self.result

# ________________________PARTS OF SPEECH START
    def top_100_nouns(self):
        lemmed_words = []
        morph = pymorphy2.MorphAnalyzer()
        lemmed_words = [word for word in self.poem if morph.parse(word)[0].tag.POS == 'NOUN']
        c = collections.Counter(lemmed_words)
        self.result = c.most_common(100)
        return self.result

    def top_100_adjf(self):
        lemmed_words = []
        morph = pymorphy2.MorphAnalyzer()
        lemmed_words = [word for word in self.poem if morph.parse(word)[0].tag.POS == 'ADJF' or morph.parse(word)[0].tag.POS == 'ADJS']
        c = collections.Counter(lemmed_words)
        self.result = c.most_common(100)
        return self.result

    def top_100_nouns_and_adjf(self):
        lemmed_words = []
        morph = pymorphy2.MorphAnalyzer()
        lemmed_words = [word for word in self.poem if
                        morph.parse(word)[0].tag.POS == 'NOUN' or morph.parse(word)[0].tag.POS == 'ADJF'or morph.parse(word)[0].tag.POS == 'ADJS']
        c = collections.Counter(lemmed_words)
        self.result = c.most_common(100)
        return self.result

    def top_100_verbs(self):
        lemmed_words = []
        morph = pymorphy2.MorphAnalyzer()
        lemmed_words = [word for word in self.poem if morph.parse(word)[0].tag.POS == 'INFN']
        c = collections.Counter(lemmed_words)
        self.result = c.most_common(100)
        return self.result

    def top_100_nouns_and_verbs(self):
        lemmed_words = []
        morph = pymorphy2.MorphAnalyzer()
        lemmed_words = [word for word in self.poem if morph.parse(word)[0].tag.POS == 'INFN' or morph.parse(word)[0].tag.POS == 'NOUN']
        c = collections.Counter(lemmed_words)
        self.result = c.most_common(100)
        return self.result

    def top_100_nouns_and_verbs_and_adjf(self):
        lemmed_words = []
        morph = pymorphy2.MorphAnalyzer()
        lemmed_words = [word for word in self.poem if morph.parse(word)[0].tag.POS == 'INFN' or morph.parse(word)[0].tag.POS == 'NOUN' or morph.parse(word)[0].tag.POS == 'ADJF'or morph.parse(word)[0].tag.POS == 'ADJS']
        c = collections.Counter(lemmed_words)
        self.result = c.most_common(100)
        return self.result

    def top_100_verbs_and_adjf(self):
        lemmed_words = []
        morph = pymorphy2.MorphAnalyzer()
        lemmed_words = [word for word in self.poem if morph.parse(word)[0].tag.POS == 'INFN' or morph.parse(word)[0].tag.POS == 'ADJF'or morph.parse(word)[0].tag.POS == 'ADJS']
        c = collections.Counter(lemmed_words)
        self.result = c.most_common(100)
        return self.result
#________________________PARTS OF SPEECH END

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




# функция подсчета слов
def words_counter(poems):
    poems_all = len(poems)
    lemmed_words = []
    counter_all = 0
    counter_unique = 0
    for poem in poems:
        poem = str(poem.poem_text)
        meta_poem = MetaPoet(poem)  # создаем объект класса MetaPoet, куда передаем стихи
        meta_poem.remove_punctuation()
        meta_poem.split_words()
        counter_all += len(meta_poem)
        meta_poem.lower_case()
        lemmed_words += meta_poem.lemma()  # список всех лемматизированных слов
        meta_poem.unique_words()
        counter_unique += len(meta_poem)

    morph = pymorphy2.MorphAnalyzer()
    # список топ 100 из существительных, глаголов и др
    lemmed_words = [word for word in lemmed_words if
                    morph.parse(word)[0].tag.POS == 'NOUN' or morph.parse(word)[0].tag.POS == 'INFN' or
                    morph.parse(word)[0].tag.POS == 'ADJF' or morph.parse(word)[0].tag.POS == 'ADJS' or
                    morph.parse(word)[0].tag.POS == 'PRTF' or morph.parse(word)[0].tag.POS == 'GRND' or
                    morph.parse(word)[0].tag.POS == 'ADVB' or morph.parse(word)[0].tag.POS == 'NPRO']

    c = collections.Counter(lemmed_words)
    result = c.most_common(100)

    #  вывод кортежа

    # преобразовываем список кортежей в списки (слова и количество употреблений)

    results_list_words = []
    results_list_counts = []

    for tuple_ in result:
        for i in range(len(tuple_)):
            if i == 0:
                results_list_words.append(tuple_[i])
            if i == 1:
                results_list_counts.append(tuple_[i])
    return poems_all, counter_all, counter_unique, result, results_list_words,  results_list_counts

def top_100(poems):
    poems_all = len(poems)
    lemmed_words = []
    counter_all = 0
    counter_unique = 0
    for poem in poems:
        poem = str(poem.poem_text)
        meta_poem = MetaPoet(poem)  # создаем объект класса MetaPoet, куда передаем стихи
        meta_poem.remove_punctuation()
        meta_poem.split_words()
        counter_all += len(meta_poem)
        meta_poem.lower_case()
        lemmed_words += meta_poem.lemma()  # список всех лемматизированных слов
        meta_poem.unique_words()
        counter_unique += len(meta_poem)
    all_lemmed_words = MetaPoet(lemmed_words)
    return poems_all, counter_all,counter_unique, all_lemmed_words


