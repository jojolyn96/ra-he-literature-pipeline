from src.search import search_semantic_scholar
from src.filter import filter_papers
from src.dataset import initialize_dataset
from src.utils import save_csv, remove_duplicates
from config import QUERIES, KEYWORDS, MIN_RELEVANCE_SCORE, OUTPUT_DIR

import pandas as pd

def run_pipeline():
    all_papers = []

    for query in QUERIES:
        print(f"Searching: {query}")
        papers = search_semantic_scholar(query, limit=30)
        filtered = filter_papers(papers, KEYWORDS, MIN_RELEVANCE_SCORE)
        all_papers.extend(filtered)

    df = pd.DataFrame(all_papers)
    df = remove_duplicates(df)

    save_csv(df, OUTPUT_DIR + "filtered_papers.csv")

    print(f"Saved {len(df)} relevant papers.")

if __name__ == "__main__":
    run_pipeline()
