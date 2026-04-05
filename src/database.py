import pandas as pd

def build_dataframe(papers):
    return pd.DataFrame(papers)

def save_dataset(df, filename="results/papers.csv"):
    df.to_csv(filename, index=False)
