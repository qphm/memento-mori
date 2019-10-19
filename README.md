# ETL: Global Suicide Analysis
![](https://images.unsplash.com/photo-1525120334885-38cc03a6ec77?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80 )Credit: [Kristina Tripkovic](https://unsplash.com/@tinamosquito)

## Introduction
According to the World Health Organization:

> "Close to 800,000 people die due to suicide every year, which is one person every 40 seconds. Suicide is a global phenomenon and occurs throughout the lifespan. Effective and evidence-based interventions can be implemented at population, sub-population and individual levels to prevent suicide and suicide attempts. There are indications that for each adult who died by suicide there may have been more than 20 others attempting suicide."

## Data Sources

[Human Freedom Index](https://www.kaggle.com/gsutters/the-human-freedom-index) (.csv)

[FIFA World Rankings](https://www.kaggle.com/tadhgfitzgerald/fifa-international-soccer-mens-ranking-1993now) (.csv)

[World Happiness Report](https://www.kaggle.com/unsdsn/world-happiness) (.csv)

[World Health Organization](https://www.who.int/mental_health/prevention/suicide/suicideprevent/en/) (.csv)


## Pipeline
1. Download data from "Data Sources"

2. Transformations / Generation
   * Jupyter Notebook`
       1. Import Original CSVs
       1. Filter columns ("Country", "Freedom Rank", "Freedom Score", "Suicide Rate per 100k", "Happiness Rank", "Happiness Score", "Fifa Score", "Fifa Total Points")
       1. Sort Null Value rows onto a different dataframe
       1. Fix duplicate country names with different spelling and combine rows
       1. Concatenate above data set with original data set so that both only contain full rows and exclude countries with incomplete information
       1. Export to CSV
        
   * Postgres 
     1. Import Original CSVs
     1. Utilize Full Outer Join to identify inconsistency in country names
     1. Rename identified countries
     1. Store country - `Clean Data/CleanFifa.csv`, `Clean Data/CleanSuicide.csv`, `Clean Data/CleanHappiness.csv`, `Clean Data/CleanFreedom.csv`
     
3. Load
   * Schema - `sql/schema.sql`
