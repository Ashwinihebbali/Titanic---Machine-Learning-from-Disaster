import pandas as pd

df = pd.read_csv('submission.csv')

print("Shape:", df.shape)
print("\nColumn names:", list(df.columns))
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())
print("\nSurvived unique values:", df['Survived'].unique())
print("\nSurvived value counts:\n", df['Survived'].value_counts())
print("\nFirst PassengerId:", df['PassengerId'].iloc[0])
print("Last PassengerId:", df['PassengerId'].iloc[-1])
