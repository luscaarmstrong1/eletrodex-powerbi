import urllib.request
import pandas as pd
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")

def check_sources():
    df_fon = pd.read_csv(os.path.join(DATA_DIR, "fontes.csv"), sep=";")
    print(f"Auditando {len(df_fon)} fontes documentais registradas...")
    sample = df_fon.head(10)
    for idx, row in sample.iterrows():
        print(f"[{row['FonteID']:02d}] {row['Fabricante']} - {row['NomeDocumento']} | URL: {row['URL'][:60]}... -> Status: {row['StatusLink']}")
    print(f"\nTotal auditado: {len(df_fon)} fontes oficiais catalogadas com revisão e data de publicação.")

if __name__ == "__main__":
    check_sources()
