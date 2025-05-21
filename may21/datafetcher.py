import pandas as pd


def fetch_data(filepath,show_head=False):
    try:
        df= pd.read_csv(filepath)
        if show_head:
            print(df.head())
        return df
    except FileNotFoundError:
        print(f"File {filepath} not found.")
        return None
    except Exception as e:
        print(f"an error acoourred while fetching data: {e}")
        return None
