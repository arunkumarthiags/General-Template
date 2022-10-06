import os
import glob
import pandas as pd

df_list = []

for csv in glob.glob('**/*.csv', recursive=True):
    parent_folder = os.path.split(os.path.dirname(csv))[-1]
    top_folder = os.path.split(os.path.dirname(csv))[-2]
    df = pd.read_csv(csv)
    df['module'] = parent_folder
    df['phase'] = top_folder
    df_list.append(df)

combined_df = pd.concat(df_list)
combined_df.to_csv("general_3.csv", index=False)