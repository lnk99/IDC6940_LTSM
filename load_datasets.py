#!pip install gdown pandas numpy matplotlib seaborn scikit-learn tensorflow keras-tuner

import pandas as pd
import gdown
import os
# Google Drive file IDs
FILE_IDS = {
    "train": "1PT-8M-Nbw8aBGXXdonN7QCe59AqEBYOs",      
    "validation": "1o_211YxzPtY2_Gz2d9xRfOALu7AjPzF_",
    "test": "1y0OcL5_S0PtJW2aeUq5Qm7cy6ehdfuob"
}

def download_and_load_csv(file_id, name):
    filename = f"{name}_dataset.csv"

    if os.path.exists(filename):
        print(f"{filename} already exists - loading from disk")
    else:
        print(f"Downloading {name} dataset from Google Drive...")
        url = f"https://drive.google.com/uc?id={file_id}"
        try:
            gdown.download(url, filename, quiet=False)
        except Exception as e:
            raise ConnectionError(f"Failed to download {name} dataset: {str(e)}")

    try:
        return pd.read_csv(filename)
    except Exception as e:
        raise ValueError(f"Could not load {filename} as CSV: {str(e)}")

def load_all_datasets():
    """Load all datasets from Google Drive or local cache"""
    datasets = {}
    for name, file_id in FILE_IDS.items():
        datasets[name] = download_and_load_csv(file_id, name)
    return datasets
