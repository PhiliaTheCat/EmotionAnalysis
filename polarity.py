# -*- coding: utf-8 -*-

import pandas as pd
import jieba 

def tendency(row_Series, tendency_table, seeds, hownet_dict_advanced):
    '''对每句话中的单词计算情感倾向'''
    words = jieba.cut(row_Series['review'], cut_all=False)
    for word in words:
        T = sim(word, seeds, hownet_dict_advanced)
        if T == 0:
            continue
        else:
            temp_table = pd.DataFrame([[word, T]], columns=['word', 'tendency'])
            tendency_table = pd.concat([tendency_table, temp_table], ignore_index=True)
    return tendency_table

# 计算出单词word的情感倾向值
def sim(word, seeds, hownet_dict_advanced):
    '''计算单词的情感倾向'''
    good_sum = 0
    bad_sum = 0
    
    for seed in seeds['good_word'][seeds['good_word'].notnull()]:
        t = hownet_dict_advanced.calculate_word_similarity(word, seed)
        if t != -1:
            good_sum = good_sum + t
        else:
            break
    good_sum = good_sum / seeds['good_word'].count()
    
    for seed in seeds['bad_word'][seeds['bad_word'].notnull()]:
        t = hownet_dict_advanced.calculate_word_similarity(word, seed)
        if t != -1:
            bad_sum = bad_sum + t
        else:
            break
    bad_sum = bad_sum / seeds['bad_word'].count()
    
    return good_sum - bad_sum