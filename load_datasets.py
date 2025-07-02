import pandas as pd
import gdown
import os

# === Mapping noms/logiques vers IDs Google Drive ===
files = {
    "training": "1PT-8M-Nbw8aBGXXdonN7QCe59AqEBYOs",      
    "test": "1y0OcL5_S0PtJW2aeUq5Qm7cy6ehdfuob",
    "validation": "1o_211YxzPtY2_Gz2d9xRfOALu7AjPzF_"
}

def download_and_load_csv(file_id, name):
    filename = f"{name}_dataset.csv"

    if os.path.exists(filename):
        print(f" {filename} already exists.")
    else:
        print(f"⬇ Downloading {name} dataset from Google Drive...")
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, filename, quiet=False)

    try:
        return pd.read_csv(filename)
    except Exception as e:
        raise ValueError(f"Could not load {filename} as CSV: {e}")

def load_all_datasets():
    datasets = {}
    for name, file_id in files.items():
        datasets[name] = download_and_load_csv(file_id, name)
    return datasets
