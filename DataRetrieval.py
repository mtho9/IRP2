from pytrends.request import TrendReq
import pandas as pd
import time

pytrends = TrendReq(hl='en-US', tz=360)

def fetch_trends_data(query_file, start_date, end_date, output_file):
    """
    Fetch Google Trends data for the given time period and save it to a CSV file.
    """
    queries_df = pd.read_csv(query_file)
    queries = queries_df['Query'].tolist()

    all_data_list = []

    for query in queries:
        print(f"Fetching data for: {query}")
        pytrends.build_payload([query], timeframe=f'{start_date} {end_date}', geo='')

        time.sleep(30)  # adjust based on what works, usually 5-10 secs work

        try:
            data = pytrends.interest_over_time()

            if not data.empty:
                data['Month'] = data.index.to_period('M')
                data_monthly = data[['Month', query]].reset_index(drop=True)
                all_data_list.append(data_monthly)
            else:
                print(f"No data found for {query} in the specified timeframe.")

        except Exception as e:
            print(f"Error fetching data for {query}: {str(e)}")

    if all_data_list:
        all_data = pd.concat(all_data_list, axis=1, join='outer')
        all_data = all_data.loc[:, ~all_data.columns.duplicated()]
        all_data.to_csv(output_file, index=False)
        print(f"Data successfully fetched and saved to '{output_file}'.")
    else:
        print("No data was retrieved for any of the queries.")