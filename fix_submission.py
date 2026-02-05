import pandas as pd

# Read the CSV
df = pd.read_csv('submission.csv')

# Keep only first 418 rows
df_trimmed = df.head(418)

# Save back
df_trimmed.to_csv('submission.csv', index=False)

print(f"✓ Fixed submission.csv")
print(f"  Rows: {len(df_trimmed)}")
print(f"  Columns: {list(df_trimmed.columns)}")
