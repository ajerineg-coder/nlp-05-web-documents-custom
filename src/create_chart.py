"""Create a chart comparing abstract word counts for two research papers."""

from pathlib import Path

import matplotlib.pyplot as plt

papers = ["Agents of Chaos", "Elder Fraud"]
word_counts = [177, 220]

plt.figure(figsize=(8, 5))
bars = plt.bar(papers, word_counts, color=["steelblue", "cornflowerblue"])

plt.title("Abstract Word Count Comparison")
plt.ylabel("Number of Words")
plt.ylim(0, 250)

for bar, count in zip(bars, word_counts):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        count + 3,
        str(count),
        ha="center",
    )

output = Path("docs/images/abstract_comparison.png")
output.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(output, bbox_inches="tight")
plt.close()

print(f"Chart saved to {output}")
