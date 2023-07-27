import pandas as pd

def load_dataset(file_path):
    try:
        dataset = pd.read_csv(file_path)
        return dataset
    except FileNotFoundError:
        print("Error: The file could not be found.")
        return None

def filter_teams_by_confederation(dataset, confederation):
    filtered_teams = dataset[dataset['confederation'].str.contains(confederation)]
    return filtered_teams

def main():
    file_path = "fifa_ranking.csv"
    confederation_to_filter = "UEFA"

    dataset = load_dataset(file_path)
    if dataset is not None:
        uefa_teams = filter_teams_by_confederation(dataset, confederation_to_filter)
        print("Soccer teams in UEFA confederation:")
        print(uefa_teams[['rank', 'country_full', 'confederation']])

if __name__ == "__main__":
    main()
