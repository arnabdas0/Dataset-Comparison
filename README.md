## Dataset Comparison Website for "Support Vector Machine Model for Identification and Classification of Various Transmission Line Faults"

This repository houses the code and resources for a web application comparing two datasets used in our research paper titled "Support Vector Machine Model for Identification and Classification of Various Transmission Line Faults." This website utilizes the powerful `ydata-profiling` library to generate a comprehensive side-by-side comparison report, highlighting key differences and similarities between the datasets.

### Purpose

This web application serves two main purposes:

1. **Compare and visualize data statistics:** Visually analyze and compare the statistical properties of our custom dataset and the corresponding dataset downloaded from Kaggle. This comparison helps assess the validity and representativeness of our custom data in relation to the publicly available data.
2. **Inform research methodology:** The generated comparison report provides valuable insights into the data distribution, missing values, outliers, and other key characteristics, guiding our research methodology choices and model training strategies.

### Technologies

* **Backend:** Python, pandas
* **Data Analysis:** `ydata-profiling` library
* **Frontend:** HTML

### Features

* Side-by-side comparison report for two datasets
* Comprehensive data statistics including descriptive measures, distributions, correlations, and missing values
* Interactive visualizations for each data statistic
* Downloadable HTML report for detailed inspection

### Getting Started

1. **Clone the repository:**

```
git clone https://github.com/arnabdas0/Dataset-Comparison.git
```

2. **Install dependencies:**

```
pip install pandas ydata-profiling
```
3. **Edit dataset names:**

   * Open `compare.py` in a text editor.
   * Modify the following lines with the actual file names of your datasets:

     ```
     Dataset_df = pd.read_csv("ourDataset.csv")
     train_df = pd.read_csv("collectedDataset.csv")
     ```

4. **Ensure dataset files are in the same folder:**

   * Place the two dataset files you want to compare in the same directory as `compare.py`.

5. **Run the code:**

   ```bash
   python compare.py
   ```

6. **View the comparison report:**

   * The code will generate an `index.html` file containing the comprehensive comparison report.
   * Open this file in your web browser to view the results.

### Contribution

Feel free to fork this repository and contribute by:

* Adding further visualizations or statistical analyses
* Enhancing the user interface and interactivity
* Implementing functionalities for comparing more than two datasets

### Disclaimer

This is a small project to support our research and is not intended for production use. It is provided as-is without warranty or guarantees.

### Related Resources

* Our research paper: [Publication in process]
* `ydata-profiling` library: [https://github.com/ydataai/ydata-profiling](https://github.com/ydataai/ydata-profiling)

By providing this readme.md, you ensure users understand the purpose and functionality of your website, how to run it, and how to contribute if they wish. Remember to replace the placeholder information with your specific details and links.

Feel free to adjust this template further to meet your specific needs and add any additional information you deem valuable for users.


