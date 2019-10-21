import pandas as pd
import numpy as np
import os

# fifa csv process
fifa_file = 'input/fifa_ranking.csv'
fifa_df = pd.read_csv(fifa_file, encoding="ISO-8859-1")
del fifa_df['country_abrv']
del fifa_df['previous_points']
del fifa_df['rank_change']
del fifa_df['last_year_avg']
del fifa_df['last_year_avg_weighted']
del fifa_df['two_year_ago_avg']
del fifa_df['two_year_ago_weighted']
del fifa_df['three_year_ago_avg']
del fifa_df['three_year_ago_weighted']
del fifa_df['confederation']
fifa_df[fifa_df.rank_date == '2016-12-22']
fifa_df.to_csv('output/CleanFifa.csv', sep=',',index=None)

# freedom csv process
freedom_path = 'input/hfi_cc_2018.csv'
freedom_pd = pd.read_csv(freedom_path)
freedom_pd_modified = freedom_pd[[
    'year', 'countries', 'ef_score', 'ef_rank', 'hf_score', 'hf_rank']]
freedom_2016 = freedom_pd_modified.loc[freedom_pd_modified['year'] == 2016]
freedom_2016 = freedom_2016.drop(['year', 'ef_score', 'ef_rank'], axis=1)
freedom_2016.columns = ['Country', 'hf_score', 'hf_rank']
freedom_2016 = freedom_2016.set_index('Country')
freedom_2016.to_csv('output/CleanFreedom.csv')

# happiness csv process
happiness_path = "input/happinessrank.csv"
happiness_df = pd.read_csv(happiness_path)
happiness_df = happiness_df.drop(columns=['Lower Confidence Interval', 'Upper Confidence Interval',
                                          'Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)',
                                          'Freedom', 'Trust (Government Corruption)', 'Generosity', 'Dystopia Residual','Region'])
happiness_df = happiness_df.set_index('Country')
happiness_df.to_csv("output/CleanHappiness.csv")

# suicide data csv process
suicide_path = "input/suicidedata.csv"
suicide_table = pd.read_csv(suicide_path)
suicide_clean = suicide_table.drop(suicide_table.columns[[1, 3, 4, 5]], axis=1)
suicide_df = suicide_clean.iloc[::3, :].set_index("Country")
suicide_df.to_csv("output/CleanSuicide.csv")
