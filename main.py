import time
print("🚀 Starting pipeline...")

from src.search import search_semantic_scholar
from src.filter import filter_papers
from src.utils import save_csv, remove_duplicates
from config import QUERIES, KEYWORDS, MIN_RELEVANCE_SCORE, OUTPUT_DIR

import pandas as pd


def run_pipeline():
    all_papers = []

    for query in QUERIES:
        print(f"\n🔍 Searching: {query}")
        
        papers = search_semantic_scholar(query, limit=30)
        print(f"Papers found: {len(papers)}")

        filtered = filter_papers(papers, KEYWORDS, MIN_RELEVANCE_SCORE)
        print(f"After filtering: {len(filtered)}")

        all_papers.extend(filtered)

        time.sleep(3)

    df = pd.DataFrame(all_papers)
    df = remove_duplicates(df)

    output_file = OUTPUT_DIR + "filtered_papers.csv"

    # ✅ SAFE SAVE (prevents overwriting with empty results)
    if df.empty:
        print("⚠️ No papers found. Keeping existing dataset.")
    else:
        save_csv(df, output_file)
        print(f"✅ Saved {len(df)} relevant papers to {output_file}")


if __name__ == "__main__":
    run_pipeline()
