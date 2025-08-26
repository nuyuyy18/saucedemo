import pandas as pd

def to_csv(result, path):
    df = pd.DataFrame(result)
    df.to_csv(path, index=False)
    print(f"saved result to {path}")