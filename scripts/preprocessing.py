import pandas as pd
import re

# Load dataset
df = pd.read_csv("data/IPL_2022_tweets.csv")

# Keep required columns
df = df[["user_name", "date", "text"]]

# Remove missing text
df = df.dropna(subset=["text"])

df["hashtags"] = df["text"].apply(lambda x: re.findall(r"#(\w+)", str(x)))
# Extract mentions
df["mentions"] = df["text"].apply(
    lambda x: re.findall(r"@(\w+)", str(x))
)
# Clean text
def clean_text(text):

    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#", "", text)
    text = re.sub(r"[^A-Za-z0-9\s]", "", text)
    text = text.lower()
    text = re.sub(r"\s+", " ", text).strip()

    return text

# Apply cleaning
df["clean_text"] = df["text"].apply(clean_text)

# Save cleaned dataset
df.to_csv("data/cleaned_ipl_tweets.csv", index=False)

print(df.head())