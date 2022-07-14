# Name: Muhammad Abrar Bajwa
# Section: SE-B
# Roll Number: 20B-017-SE
# Data Mining Assignment 2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('titles.csv')
df.sort_values(by='release_year', inplace=True)
print('Done..')
print(df.head())

"""'id', 'title', 'type', 'description', 'release_year', 'age_certification', 'runtime', 'genres', 'production_countries', 'seasons', 'imdb_id', 'imdb_score', 'imdb_votes', 'tmdb_popularity', 'tmdb_score'"""


print("\n\n")
print("Null values:",np.where(df.isnull()),"and",sum(df.isnull().any()))
dup_bool = df.duplicated(['id'])
dups = sum(dup_bool)
print("Total duplicates :", dups)

remove_dups = df[~dup_bool]
print("\n\n")
print("Total data: ")
print("\nTotal ratings :",len(np.unique(remove_dups.imdb_score)))
print("Total movies  :", len(np.unique(remove_dups.id)))
print("Total seasons  :", len(np.unique(remove_dups.seasons)))
print("Total genres  :", len(np.unique(remove_dups.genres)))
print("Total countries :", len(np.unique(remove_dups.production_countries)))


#plot distribution of ratings
plt.hist(remove_dups.imdb_score, bins=100)
plt.title("Distribution of ratings")
plt.xlabel("Ratings")
plt.ylabel("Frequency")
plt.show()


#plot distribution of seasons
plt.hist(remove_dups.seasons, bins=100)
plt.title("Distribution of seasons")
plt.xlabel("Seasons")
plt.ylabel("Frequency")
plt.show()

#plot by movie or show bar graph
plt.bar(remove_dups.type, remove_dups.imdb_score)
plt.title("Distribution of ratings by movie or show")
plt.xlabel("Type")
plt.ylabel("Ratings")
plt.show()
