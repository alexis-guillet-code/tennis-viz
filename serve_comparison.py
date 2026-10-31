"""
Serve comparison: Medvedev vs Tsitsipas, Shanghai Masters 2026 (R16).
Medvedev won 6-4 7-5 without facing a single break point.

Run:  python serve_comparison.py
Output: serve_comparison.png (saved next to this script)
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# --- 1. Data (source: ATP Tour / Tennis Tonic match stats) ---------------
data = pd.DataFrame({
    "stat": ["1st serve in", "1st serve pts won", "2nd serve pts won"],
    "Medvedev": [39 / 62, 33 / 39, 12 / 23],
    "Tsitsipas": [44 / 63, 30 / 44, 10 / 19],
})
data[["Medvedev", "Tsitsipas"]] = (data[["Medvedev", "Tsitsipas"]] * 100).round(0)
print(data)  # quick check in the terminal

# --- 2. Chart --------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 4.5))
y = range(len(data))
h = 0.38
ax.barh([i + h / 2 for i in y], data["Medvedev"], height=h, label="Medvedev", color="#2E6FD8")
ax.barh([i - h / 2 for i in y], data["Tsitsipas"], height=h, label="Tsitsipas", color="#F2A541")

for i, (m, t) in enumerate(zip(data["Medvedev"], data["Tsitsipas"])):
    ax.text(m + 1, i + h / 2, f"{m:.0f}%", va="center", fontsize=10)
    ax.text(t + 1, i - h / 2, f"{t:.0f}%", va="center", fontsize=10)

ax.set_yticks(list(y))
ax.set_yticklabels(data["stat"])
ax.invert_yaxis()
ax.set_xlim(0, 100)
ax.set_xlabel("%")
ax.set_title("Medvedev 6-4 7-5 Tsitsipas · the gap was the 1st serve", loc="left", fontsize=12)
ax.legend(frameon=False, loc="lower right")
for side in ("top", "right"):
    ax.spines[side].set_visible(False)

fig.tight_layout()
out = Path(__file__).with_name("serve_comparison.png")
fig.savefig(out, dpi=150)
print(f"Chart saved to {out}")
