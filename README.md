# IRP2
# Google Trends Data Analysis

This project retrieves Google Trends data, performs seasonality and autocorrelation analysis, and combines pre-pandemic and post-pandemic data for trend analysis.

## Project Structure

- **Main.py**: The main script that runs the analysis workflow. It calls functions to fetch data, perform analysis, and combine datasets.
- **DataRetrieval.py**: Contains functions to fetch Google Trends data for specified queries and time periods.
- **DataAnalysis.py**: Contains functions to analyze seasonality and autocorrelation for the fetched data, as well as combine pre-pandemic and post-pandemic data.

## Requirements

- Python 3.x
- Libraries:
  - `pandas`
  - `pytrends`
  - `statsmodels`

You can install the necessary libraries using `pip`:

```bash
pip install pandas pytrends statsmodels
