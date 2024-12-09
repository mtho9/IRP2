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


def load_and_prepare_data(file_path):

    df = pd.read_excel(file_path)

    # converting month column
    df['Month'] = pd.to_datetime(df['Month'])

    df['Month_Name'] = df['Month'].dt.month_name()

    df = df.drop(columns=['Month'])

    # need to rearrange col so Month_Name comes first
    cols = ['Month_Name'] + [col for col in df if col != 'Month_Name']
    df = df[cols]

    return df


def calculate_monthly_means(df):

    monthly_means = df.groupby('Month_Name').mean()

    # sort
    month_order = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    monthly_means = monthly_means.reindex(month_order)

    return monthly_means


def prepare_dataset_for_svm(monthly_means, labels=None):

    # transpose to make each query a row
    dataset = monthly_means.T
    dataset.columns = [
        "Jan_mean", "Feb_mean", "Mar_mean", "Apr_mean", "May_mean", "Jun_mean",
        "Jul_mean", "Aug_mean", "Sep_mean", "Oct_mean", "Nov_mean", "Dec_mean"
    ]

    dataset.reset_index(inplace=True)
    dataset.rename(columns={'index': 'Query'}, inplace=True)

    # label column for classifier
    if labels is not None:
        dataset['Label'] = labels
    else:
        dataset['Label'] = None  # leaving blank for manual labeling

    return dataset


def save_dataset_to_csv(dataset, output_path):
    dataset.to_csv(output_path, index=False)
    print(f"Dataset saved to {output_path}")