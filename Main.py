from DataRetrieval import fetch_trends_data
import DataAnalysis
import Classification

def main():
    file_path = "all_trends_data.xlsx"  # Replace with your Excel file path
    output_path = "prepared_SVM_dataset.csv"  # Desired output CSV file path

    df = DataAnalysis.load_and_prepare_data(file_path)

    monthly_means = DataAnalysis.calculate_monthly_means(df)

    dataset = DataAnalysis.prepare_dataset_for_svm(monthly_means, labels=None)

    DataAnalysis.save_dataset_to_csv(dataset, output_path)

if __name__ == "__main__":
    main()
