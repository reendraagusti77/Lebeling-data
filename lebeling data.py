import pandas as pd

# =========================
# 1. BUAT 1000 DATA DUMMY
# =========================

kalimat = []

# 350 kalimat positif
for i in range(350):
    kalimat.append(f"Film ini sangat bagus dan menarik ke-{i+1}")

# 350 kalimat negatif
for i in range(350):
    kalimat.append(f"Film ini sangat buruk dan mengecewakan ke-{i+1}")

# 300 kalimat netral
for i in range(300):
    kalimat.append(f"Film ini cukup biasa saja ke-{i+1}")

df = pd.DataFrame({"kalimat": kalimat})

# SIMPAN DATA MENTAH
df.to_csv("dataset_1000_variasi_sentimen.csv", index=False)

# =========================
# 2. LABELING DATA
# =========================

df["label"] = ""

# MANUAL LABEL
df.loc[0:99, "label"] = "positif"
df.loc[100:199, "label"] = "negatif"
df.loc[200:249, "label"] = "netral"

# AUTO LABEL (SIMPLE RULE)
positive_words = ["bagus", "menarik"]
negative_words = ["buruk", "mengecewakan"]

def auto_label(text):
    text = text.lower()
    
    pos = sum(word in text for word in positive_words)
    neg = sum(word in text for word in negative_words)

    if pos > neg:
        return "positif"
    elif neg > pos:
        return "negatif"
    else:
        return "netral"

for i in range(250, len(df)):
    df.loc[i,"label"] = auto_label(df.loc[i,"kalimat"])

# =========================
# 3. SIMPAN HASIL FINAL
# =========================

df.to_csv("dataset_1000_sudah_label.csv", index=False)

# =========================
# 4. OUTPUT INFO
# =========================

print("✅ FILE DATA MENTAH   : dataset_1000_variasi_sentimen.csv")
print("✅ FILE HASIL LABEL  : dataset_1000_sudah_label.csv")
print("\nDistribusi Label:")
print(df["label"].value_counts())
