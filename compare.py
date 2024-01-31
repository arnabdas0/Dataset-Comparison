import pandas as pd
from ydata_profiling import ProfileReport, compare

Dataset_df = pd.read_csv("ourDataset.csv")
Dataset_report = ProfileReport(Dataset_df, title="Our Dataset")

train_df = pd.read_csv("collectedDataset.csv")
train_report = ProfileReport(train_df, title="Collected Dataset")


comparison_report = compare([Dataset_report, train_report])

# Obtain merged statistics
statistics = comparison_report.get_description()

# Save report to file
comparison_report.to_file("index.html")
