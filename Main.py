import DataRetrieval
import DataAnalysis

def main():
    file_path = "all_trends_data_nonseasonal.xlsx"
    output_path = "prepared_SVM_dataset_nonseass.csv"

    df = DataAnalysis.load_and_prepare_data(file_path)

    monthly_means = DataAnalysis.calculate_monthly_means(df)

    dataset = DataAnalysis.prepare_dataset_for_svm(monthly_means, labels=None)

    DataAnalysis.save_dataset_to_csv(dataset, output_path)

if __name__ == "__main__":
    # main()
    # DataRetrieval.fetch_trends_data("queries_non_seasonal.csv", "2004-01-01", "2024-01-01", "trends_non_seasonal.csv")
    DataAnalysis.calculate_summer_winter_ratio("prepared_SVM_dataset.csv", "sum_win_ratio.csv")
