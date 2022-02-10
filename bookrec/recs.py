from click import prompt
import db
import csv
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def write_recs_to_csv(result):
    with open('database/recs.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for book_id in result:
            writer.writerow([book_id, result[book_id]])


def main():
    prompt("Continue? ")

    print("Creating data frame")
    data = db.get_all_books()
    main_df = pd.DataFrame(data, columns=[
        'id', 'title', 'description', 'rating', 'pages', 'numRatings'])

    print("First 3 rows")
    print(main_df.head(3))

    print("Preparing similarity calculations")
    sim_df = pd.DataFrame(main_df, columns=['title', 'description'])
    sim_df['title_desc'] = sim_df['title'] + " " + sim_df['description']
    print(sim_df.head(3))

    print("Vectorizing")
    vectorizer = TfidfVectorizer()
    title_matrix = vectorizer.fit_transform(sim_df['title_desc'])

    print("Calculating similarities")
    cosine_sim = cosine_similarity(title_matrix)
    cosine_df = pd.DataFrame(cosine_sim)

    print("First 3 rows of recs")
    print(cosine_df.head(3))

    print("Ranking and collecting recommendations, this may take a while...")
    result = {}  # this will be a dict {book_id:"rec_ids"}
    for loc, row in main_df.iterrows():
        book_id = row['id']

        # order cosine_df rows by the similarity desc,
        # but do not lose information about to which row they belong to
        similar_books = list(enumerate(cosine_df.iloc[loc]))
        similar_books = sorted(similar_books, key=lambda x: x[1], reverse=True)

        # once we have ordered the similarities we want to take the top 20
        similar_book_ids = []
        for loc, similarity in similar_books[1:21]:
            if similarity > 0:
                similar_book_ids.append(str(main_df.iloc[loc]['id']))

        # collect the results into one big dictionary
        # this will join all ints into a comma separated string [1,2,3] -> "1,2,3"
        result[book_id] = ",".join(similar_book_ids)

    # once we are done with iterating, take the big dictionary and write the contents into a CSV file
    print("Writing results into CSV")
    write_recs_to_csv(result)

    print("Done!")
    print("")

    print("Recommendations are ready and saved inside database/recs.csv file")
    print("To import into database, do next steps:")
    print("1. Open sqlite3 database:")
    print("   sqlite3 database/bookrec.db")
    print("2. Delete previous recommendations by running SQL:")
    print("   delete from recs;")
    print("3. Import data")
    print("   .mode csv")
    print("   .import database/recs.csv recs")
    print("4. Verify that the data is imported:")
    print("   select * from recs limit 10;")


# start the main function when this file is ran directly from python3 interpreter
main()
