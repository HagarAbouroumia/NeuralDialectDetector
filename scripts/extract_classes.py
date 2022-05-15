import os 
import numpy as np
import pandas as pd 

if __name__ == "__main__":
    
    
#     classes_22 for province while classes_12 is for country
    # path = "NADI2021_DEV.1.0/NADI2021_DEV.1.0/Subtask_1.2+2.2_DA/DA_dev_labeled.tsv"
#     path = "/content/NADI2021_DEV.1.0/NADI2021_DEV.1.0/Subtask_1.2+2.2_DA/DA_train_labeled.tsv"
    path = "/content/qadi/DA_train_labeled.tsv"

    df = pd.read_csv(path, delimiter='\t')
    class_name = "classes_12.txt"
    labels_1 = sorted(df["country_label"].unique().tolist())
#     labels_2 = sorted(df["#4_province_label"].unique().tolist())

#     print(f"n1={len(labels_1)} | n2={len(labels_2)}")
    print(f"n1={len(labels_1)}")

    path = os.path.join(os.path.dirname(path), class_name)
    with open(path, 'w') as fout:
        fout.write('\n'.join(labels_1))
    
#     path = os.path.join(os.path.dirname(path), "classes_22.txt")
#     with open(path, 'w') as fout:
#         fout.write('\n'.join(labels_2))
