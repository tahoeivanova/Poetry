from django.db import models



# Create your models here.
class DictionaryForm(models.Model):
    is_noun = models.BooleanField("Существительные", default=False)  # NOUN имя существительное хомяк
    is_adjf = models.BooleanField("Прилагательные", default=False) #ADJF имя прилагательное (полное) хороший + краткие прилагательные
    is_verb = models.BooleanField("Глаголы", default=False) #ADJF имя прилагательное (полное) хороший

'''
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
unknown_part = []  # не определенные pymorphy2 части речи
'''

