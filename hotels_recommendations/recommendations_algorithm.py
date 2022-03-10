from click import prompt
import db
import csv

import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def write_recs_to_csv(result):
    pass

def main():
    prompt("Continue? ")

    df = db.get_all_hotels()

    # type your code here

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