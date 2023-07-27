import pandas as pd

def print_country_names(filename):
    try:
        # Load the dataset using pandas
        df = pd.read_csv(filename)

        # Check if the "country_full" column exists in the dataset
        if 'country_full' in df.columns:
            # Extract the values from the "country_full" column and print them
            country_names = df['country_full'].values
            for country in country_names:
                print(country)
        else:
            print("Error: 'country_full' column not found in the dataset.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    file_name = "fifa_ranking.csv"
    print_country_names(file_name)
