import pandas as pd
import os

freedom = "Clean Data/CleanFreedom.csv"
suicide = "Clean Data/CleanSuicide.csv"
happiness = "Clean Data/CleanHappiness.csv"
fifa = "Clean Data/CleanFifa.csv"

freedom_pd = pd.read_csv(freedom)
suicide_pd = pd.read_csv(suicide)
happiness_pd = pd.read_csv(happiness)
fifa_pd = pd.read_csv(fifa)

freedom_suicide_pd = pd.merge(freedom_pd,suicide_pd, on='Country', how='outer')
happiness_freedom_suicide_pd = pd.merge(freedom_suicide_pd, happiness_pd, on='Country', how='outer')
happiness_freedom_suicide_pd.columns = ['Country', 'Freedom Score', 'Freedom Rank', 'Suicide Rate per 100k', 'Happiness Rank','Happiness Score']
happiness_freedom_suicide_fifa = pd.merge(happiness_freedom_suicide_pd, fifa_pd_col, on='Country',how='outer')
happiness_freedom_suicide_fifa.columns = ['Country', 'Freedom Score', 'Freedom Rank', 'Suicide Rate per 100k', 'Happiness Rank','Happiness Score', 'Fifa Rank','Fifa Total Points']
happiness_freedom_suicide_fifa.to_csv('Raw Data/DirtyMerged.csv')

null_data = happiness_freedom_suicide_fifa[happiness_freedom_suicide_fifa.isnull().any(axis=1)]
null_data = null_data.reset_index(drop=True)
null_data['Country'].replace(
                  {"CÃƒÂ´te d'Ivoire":"Ivory Coast",
                   "Cote d'Ivoire":"Ivory Coast",
                   "CÃ´te d'Ivoire":"Ivory Coast",
                   "China PR":"China",
                   "IR Iran":"Iran",
                   "Iran (Islamic Republic of)":"Iran",
                   "Congo, Dem. R.":"Congo DR",
                   "Democratic Republic of the Congo":"Congo DR",
                   "Congo (Kinshasa)":"Congo DR",
                   "Congo (Brazzaville)":"Republic of the Congo",
                   "Congo, Rep. Of":"Republic of the Congo",
                   "Congo":"Republic of the Congo",
                   "Czech Rep.":"Czech Republic",
                   "Czechia":"Czech Republic",
                   "Venezuela (Bolivarian Republic of)":"Venezuela",
                   "United States":"United States of America",
                   "USA":"United States of America",
                   "United Kingdom of Great Britain and Northern Ireland":"United Kingdom",
                   "England":"United Kingdom",
                   "Dominican Rep.":"Dominican Republic",
                   "Bolivia (Plurinational State of)":"Bolivia",
                   "Democratic People's Republic of Korea":"North Korea",
                   "Korea DPR":"North Korea",
                   "Korea, South":"South Korea",
                   "Republic of Korea":"South Korea",
                   "Korea Republic":"South Korea",
                   "Pap. New Guinea":"Papua New Guinea",
                   "Viet Nam":"Vietnam",
                   "Yemen, Rep.":"Yemen",
                   "United Republic of Tanzania":"Tanzania",
                   "Syrian Arab Republic":"Syria",
                   "Russian Federation":"Russia",
                   "Republic of Ireland":"Ireland",
                   "Central Afr. Rep.":"Central African Republic",
                   "Cabo Verde":"Cape Verde",
                   "Cape Verde Islands":"Cape Verde",
                   "Gambia, The":"Gambia",
                   "Kyrgyz Republic":"Kyrgyzstan",
                   "Lao People's Democratic Republic":"Laos",
                   "Chinese Taipei":"Taiwan",
                   "Republic of Moldova":"Moldova",
                   "Republic of North Macedonia":"Macedonia",
                   "FYR Macedonia":"Macedonia"}, value=None, inplace=True)
null_data = null_data.groupby('Country')[['Freedom Score', 'Freedom Rank', 'Suicide Rate per 100k', 'Happiness Rank','Happiness Score','Fifa Rank','Fifa Total Points']].first()
null_data = null_data.reset_index()
null_data = null_data.dropna()

freedom_suicide_pd = pd.merge(freedom_pd,suicide_pd, on='Country', how='inner')
happiness_freedom_suicide_pd = pd.merge(freedom_suicide_pd, happiness_pd, on='Country', how='inner')
happiness_freedom_suicide_pd.columns = ['Country', 'Freedom Score', 'Freedom Rank', 'Suicide Rate per 100k', 'Happiness Rank','Happiness Score']
happiness_freedom_suicide_fifa = pd.merge(happiness_freedom_suicide_pd, fifa_pd_col, on='Country',how='inner')
happiness_freedom_suicide_fifa.columns = ['Country', 'Freedom Score', 'Freedom Rank', 'Suicide Rate per 100k', 'Happiness Rank','Happiness Score', 'Fifa Rank','Fifa Total Points']
clean_merge_df = pd.concat([happiness_freedom_suicide_fifa, null_data])
clean_merge_df = clean_merge_df.reset_index(drop=True)
clean_merge_df.to_csv('Clean Data/CleanMerge.csv')
