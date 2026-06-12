# scripts/email_report.py

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

processed_dir = BASE_DIR / "data" / "processed"
reports_dir = BASE_DIR / "reports"

reports_dir.mkdir(exist_ok=True)

# Load available performance files
try:
    sharpe = pd.read_csv(processed_dir / "sharpe_ratios.csv")
    cagr = pd.read_csv(processed_dir / "cagr_results.csv")

    top_sharpe = sharpe.sort_values(
        by=sharpe.columns[-1],
        ascending=False
    ).iloc[0]

    bottom_sharpe = sharpe.sort_values(
        by=sharpe.columns[-1]
    ).iloc[0]

except Exception as e:
    print(f"Error loading files: {e}")
    exit()

html_content = f"""
<html>
<head>
<title>Weekly Mutual Fund Report</title>

<style>
body {{
    font-family: Arial;
    margin: 40px;
}}

h1 {{
    color: #0d6efd;
}}

.card {{
    border: 1px solid #ccc;
    padding: 15px;
    margin-bottom: 20px;
    border-radius: 8px;
}}

table {{
    border-collapse: collapse;
    width: 100%;
}}

th, td {{
    border: 1px solid #ddd;
    padding: 8px;
}}

th {{
    background-color: #f2f2f2;
}}
</style>
</head>

<body>

<h1>Weekly Mutual Fund Performance Summary</h1>

<p>
Generated automatically from project analytics outputs.
</p>

<div class="card">
<h2>Top Performing Fund (Sharpe Ratio)</h2>

<p>
<b>Fund:</b> {top_sharpe.iloc[0]}
</p>

<p>
<b>Sharpe Ratio:</b> {top_sharpe.iloc[-1]}
</p>
</div>

<div class="card">
<h2>Lowest Performing Fund (Sharpe Ratio)</h2>

<p>
<b>Fund:</b> {bottom_sharpe.iloc[0]}
</p>

<p>
<b>Sharpe Ratio:</b> {bottom_sharpe.iloc[-1]}
</p>
</div>

<h2>CAGR Summary</h2>

{cagr.head(10).to_html(index=False)}

</body>
</html>
"""

output_file = reports_dir / "weekly_report.html"

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Report generated: {output_file}")