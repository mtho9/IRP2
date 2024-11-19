from DataRetrieval import fetch_trends_data
from DataAnalysis import analyze_seasonality_acf, combine_data

def main():
    # # Fetch trends data for all periods
    # fetch_trends_data('queries.csv', '2004-01-01', '2024-01-01', 'trends_data_monthly_2004_2024.csv')
    # fetch_trends_data('queries.csv', '2004-01-01', '2020-02-29', 'pre_pandemic_trends_data.csv')
    # fetch_trends_data('queries.csv', '2021-04-01', '2024-01-01', 'post_pandemic_trends_data.csv')

    # Perform analysis (Seasonality and ACF) on full data set
    # analyze_seasonality_acf('all_trends_data.xlsx', 'seasonality_acf_results.csv')

    # Combine pre-pandemic and post-pandemic data
    # combine_data('pre_pandemic_trends_data.csv', 'post_pandemic_trends_data.csv', 'combined_trends_data.csv')

    # Perform analysis on combined data set with no pandemic
    analyze_seasonality_acf('combined_trends_data.csv', 'seasonality_acf_results_without_pandemic.csv')

if __name__ == "__main__":
    main()
