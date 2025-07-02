
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns # viz
import matplotlib.pyplot as plt # viz
from scipy import stats
import json
from typing import List, Tuple
from load_datasets import load_all_datasets
from sklearn.ensemble import IsolationForest
from sklearn.metrics import f1_score, balanced_accuracy_score, roc_auc_score, precision_recall_fscore_support
from sklearn import metrics, linear_model

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import TensorDataset, DataLoader

# Load dataset
# Charger tous les fichiers
datasets = load_all_datasets()

train_df = datasets["training"]
test_df = datasets["test"]
val_df= datasets["validation"]

# Convert timestamp columns to datetime objects
train_df['timestamp'] = pd.to_datetime(train_df['timestamp'], unit='s', errors='coerce')
val_df['timestamp'] = pd.to_datetime(val_df['timestamp'], unit='s', errors='coerce')
test_df['timestamp'] = pd.to_datetime(test_df['timestamp'], unit='s', errors='coerce')

# Optional: set plotting style
sns.set(style="whitegrid")

#Part 3 : ANALYSIS AND RESULTS#
# ---- FIGURE 1: Most common event names in training data ----
plt.figure(figsize=(10, 5))
top_events = train_df['eventName'].value_counts().nlargest(10)
sns.barplot(x=top_events.values, y=top_events.index, palette='Blues_r')
plt.title("Top 10 Event Names in Training Data")
plt.xlabel("Frequency")
plt.ylabel("Event Name")
plt.tight_layout()
plt.show()

# ---- FIGURE 2: Event frequency by hour ----
train_df['hour'] = train_df['timestamp'].dt.hour
plt.figure(figsize=(10, 5))
sns.countplot(data=train_df, x='hour', palette='viridis')
plt.title("System Events Distribution by Hour (Training Data)")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Events")
plt.tight_layout()
plt.show()

# ---- FIGURE 3: Count of evil vs. benign events in test set ----
plt.figure(figsize=(6, 4))
sns.countplot(data=test_df, x='evil', palette='coolwarm')
plt.title("Malicious vs. Benign Events (Test Set)")
plt.xlabel("Evil Label")
plt.ylabel("Count")
plt.xticks([0, 1], ['Benign (0)', 'Malicious (1)'])
plt.tight_layout()
plt.show()
