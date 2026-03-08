import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

file = sys.argv[1]

df = pd.read_csv(file)

summary = (
    df.groupby(["category", "label"])
    .size()
    .unstack(fill_value=0)
)

print("\nEvaluation summary\n")
print(summary)

# Create plot
ax = summary.plot(kind="bar")

plt.title("LLM Safety Response Distribution by Prompt Category")
plt.xlabel("Prompt Category")
plt.ylabel("Number of Responses")
plt.xticks(rotation=45)
plt.tight_layout()

# Save plot
output_file = "reports/evaluation_plot.png"
os.makedirs("reports", exist_ok=True)

plt.savefig(output_file)

print(f"\nPlot saved to: {output_file}")