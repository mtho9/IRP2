# Google Trends Data Analysis: Seasonal and Non-Seasonal Trend Classification

This project analyzes Google Trends data for seasonal and non-seasonal trends, with a focus on how trends have evolved before and after the pandemic. The goal is to understand seasonality, autocorrelation patterns, and prepare the data for classification using Support Vector Machines (SVM).


## Project Structure

- **Main.py**: The main script that runs the analysis workflow. It calls functions to fetch data, perform analysis, and combine datasets.
- **DataRetrieval.py**: Fetch Google Trends data for specified queries and time periods.
- **DataAnalysis.py**: Perform seasonal decomposition, autocorrelation analysis, and calculate the summer-winter ratio for trend classification.
- **Classification.py**: Build an SVM model to classify trends as seasonal or non-seasonal based on various features.

## Data Files
- **all_trends_data.xlsx**: Contains seasonal query search volume data from 01/01/2004 to 01/01/2024.
- **all_trends_data_nonseasonal.xlsx**: Contains non-periodic query search volume data from 01/01/2004 to 01/01/2024.
- **prepared_SVM_dataset.csv**: Prepared dataset for SVM classification containing features such as monthly means, mean seasonality, ACF at lag 12, and summer-winter ratio.


## Requirements

- Python 3.x
- Libraries:
  - `pandas`
  - `pytrends`
  - `statsmodels`
  - `scikit-learn`
  - `matplotlib`

You can install the necessary libraries using `pip`:

```bash
pip install pandas pytrends statsmodels scikit-learn matplotlib
