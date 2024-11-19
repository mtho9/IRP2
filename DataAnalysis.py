import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose

import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose

def analyze_seasonality_acf(input_file, output_file):
    """
    Analyze seasonality and autocorrelation for the given trends data.
    Save the results to a CSV file.
    """
    df = pd.read_csv(input_file, index_col='Month', parse_dates=True, encoding='ISO-8859-1')

    df.index = pd.to_datetime(df.index, format='%Y-%m').to_period('M')

    # Create a full PeriodIndex that includes all months from 2004-01 to 2024-01
    full_index = pd.period_range(start='2004-01', end='2024-01', freq='M')

    # Reindex the DataFrame to include all months, filling missing months with NaN
    df = df.reindex(full_index)

    results = []

    for query in df.columns:
        print(f"Processing: {query}")
        data = df[query]

        # skipping queries with too many missing values
        if data.isnull().sum() / len(data) > 0.5:  # Skip if more than 50% NaN
            print(f"Skipping {query} due to too many missing values.")
            continue

        if (data <= 0).any():
            data = data.where(data > 0, 1e-6)

        # seasonal decomposition
        try:
            result = seasonal_decompose(data, model='multiplicative', extrapolate_trend='freq', period=12)
            seasonal_all = result.seasonal
            mean_seasonal_all = seasonal_all.mean()

            # autocorrelation function at lag 12
            acf_all = sm.tsa.acf(data, nlags=12)
            acf_lag_12 = acf_all[12]

            results.append({
                'Query': query,
                'Mean Seasonality': mean_seasonal_all,
                'ACF at Lag 12': acf_lag_12
            })
        except Exception as e:
            print(f"Error processing {query}: {e}")

    results_df = pd.DataFrame(results)
    results_df.to_csv(output_file, index=False)
    print(f"Results have been saved to '{output_file}'.")

def combine_data(pre_file, post_file, output_file):
    """
    Combine pre-pandemic and post-pandemic data into one CSV file.
    """
    pre_pandemic_data = pd.read_csv(pre_file)
    post_pandemic_data = pd.read_csv(post_file)

    pre_pandemic_data['Month'] = pd.to_datetime(pre_pandemic_data['Month']).dt.to_period('M')
    post_pandemic_data['Month'] = pd.to_datetime(post_pandemic_data['Month']).dt.to_period('M')

    combined_data = pd.concat([pre_pandemic_data, post_pandemic_data], axis=0, ignore_index=True)

    combined_data['Month'] = combined_data['Month'].dt.to_timestamp(freq='M')

    combined_data = combined_data.sort_values(by='Month')

    combined_data.to_csv(output_file, index=False)

    print(f"Data successfully combined and saved to '{output_file}'.")