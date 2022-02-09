from click import prompt
import db
import csv

import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def write_recs_to_csv(result):
    with open('database/show_recs.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for id in result:
            writer.writerow([id, result[id]])


def main():
    prompt("Continue? ")

    df = db.get_all_shows()
    #df.director = df.director.fillna("")
    #df.cast = df.cast.fillna("")

    new_df = pd.DataFrame(df, columns=[
                          'id', 'type', 'title', 'director', 'cast', 'release_year', 'listed_in', 'description'])

    new_df['release_year'] = new_df['release_year'].astype(str)
    new_df['description_all'] = new_df['type'] + " " + new_df['title'] + " " + new_df['director'] + " " + \
        new_df['cast'] + " " + new_df['release_year'] + " " + \
        new_df['listed_in'] + " " + new_df['description']

    description_all_tfidf = TfidfVectorizer()
    description_all_matrix = description_all_tfidf.fit_transform(
        new_df['description_all'])

    cosine_sim = cosine_similarity(description_all_matrix)
    cosine_df = pd.DataFrame(cosine_sim)

    print("Ranking and collecting recommendations, this may take a while...")

    result = {}
    for loc, row in new_df.iterrows():
        similar_shows = list(enumerate(cosine_df.iloc[loc]))
        similar_shows = sorted(similar_shows, key=lambda x: x[1], reverse=True)

        similar_show_ids = []
        for loc, similarity in similar_shows[1:21]:
            if similarity > 0:
                similar_show_ids.append(str(new_df.iloc[loc]['id']))
        result[row['id']] = ",".join(similar_show_ids)

    print("Writing results into CSV")
    write_recs_to_csv(result)

    print("Done!")
    print("")

    print("Recommendations are ready and saved inside database/recs.csv file")
    print("To import into database, do next steps:")
    print("1. Open sqlite3 database, sqlite3 database/showrec.db")
    print("2. Delete previous recommendations by running SQL:")
    print("  2a. delete from recs;")
    print("3. Import data")
    print("  3a. .mode csv")
    print("  3b. .import database/recs.csv recs")
    print("4. Verify that the data is imported:")
    print("  4a. select * from recs limit 10;")


main()
