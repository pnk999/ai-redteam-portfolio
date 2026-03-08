import pandas as pd
import sys

file = sys.argv[1]

df = pd.read_csv(file)

summary = (
    df.groupby(["category", "label"])
    .size()
    .unstack(fill_value=0)
)

print("\nEvaluation summary\n")
print(summary)