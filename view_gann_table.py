import pandas as pd

# CSV file वाचा
df = pd.read_csv('Gann_Square_7x7.csv', header=None)

# Column names द्या (0 ते 6)
df.columns = [f'Col_{i}' for i in range(7)]

# Row numbers द्या (0 ते 6)
df.index = [f'Row_{i}' for i in range(7)]

print("=" * 80)
print("GANN SQUARE 7x7 - TABULAR VIEW")
print("=" * 80)
print()

# Tabular format मध्ये print करा
print(df.to_string())

print()
print("=" * 80)
print("Data Info:")
print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
print(f"Min Value: {df.min().min():.2f}")
print(f"Max Value: {df.max().max():.2f}")
print("=" * 80)
