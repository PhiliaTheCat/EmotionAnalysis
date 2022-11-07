# -*- coding: utf-8 -*-

import pandas as pd
import polarity as pl
import OpenHowNet

comment = pd.read_csv('外卖评论.csv')
seeds = pd.read_csv('seed.csv')

tendency_table = pd.DataFrame(columns=['word', 'tendency'])
OpenHowNet.download()
hownet_dict_advanced = OpenHowNet.HowNetDict(init_sim=True)

for index, row in comment.iterrows():
    '''对每条评论进行处理'''
    tendency_table = pl.tendency(row, tendency_table, seeds, hownet_dict_advanced)

tendency_table = tendency_table.drop_duplicates(['word'])
for seed in seeds['good_word'][seeds['good_word'].notnull()]:
    tendency_table = tendency_table[tendency_table['word'] != seed]
    
for seed in seeds['bad_word'][seeds['bad_word'].notnull()]:
    tendency_table = tendency_table[tendency_table['word'] != seed]
    
tendency_table = tendency_table.sort_values(by='tendency', ascending=False)
tendency_table = pd.concat([tendency_table.iloc[0:51], tendency_table.iloc[-50:]], ignore_index=True)
tendency_table.to_csv('result.csv')


