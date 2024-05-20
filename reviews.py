import pandas as pd

reviews = pd.read_csv('winemag-data-130k-v2.csv.zip')
summary_by_country = reviews.groupby('country').agg({'country': 'count', 'points': 'mean'}).round(1)
summary_by_country = summary_by_country.rename(columns={'country': 'count'}).sort_values(by='count', ascending=False)
summary_by_country.to_csv('reviews-per-country.csv', index=True)
summary_by_country