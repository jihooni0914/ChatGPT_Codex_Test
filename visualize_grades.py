import pandas as pd
import matplotlib.pyplot as plt
import argparse


def load_data(path: str) -> pd.DataFrame:
    """Load grade data from a CSV file."""
    df = pd.read_csv(path)
    return df


def plot_grade_distribution(df: pd.DataFrame, year: str):
    """Plot grade distributions for a specific year (2023 or 2024)."""
    subj50 = f"Subject50_{year}"
    subj70 = f"Subject70_{year}"
    comp50 = f"Comprehensive50_{year}"
    comp70 = f"Comprehensive70_{year}"

    cols = [subj50, subj70, comp50, comp70]

    # Remove rows where all values are NaN for the given year
    data = df.dropna(subset=cols, how='all')

    labels = data['School']
    values = data[cols]

    x = range(len(labels))
    width = 0.2

    plt.figure(figsize=(12, 6))
    plt.bar([i - 1.5 * width for i in x], values[subj50], width, label='Subject 50%')
    plt.bar([i - 0.5 * width for i in x], values[subj70], width, label='Subject 70%')
    plt.bar([i + 0.5 * width for i in x], values[comp50], width, label='Comprehensive 50%')
    plt.bar([i + 1.5 * width for i in x], values[comp70], width, label='Comprehensive 70%')

    plt.xticks(list(x), labels, rotation=45, ha='right')
    plt.ylabel('Grade Cutoff')
    plt.title(f'University Grade Cutoffs ({year})')
    plt.legend()
    plt.tight_layout()
    plt.show()


def main():
    parser = argparse.ArgumentParser(description="Visualize university grade cutoffs")
    parser.add_argument('--csv', default='grades.csv', help='Path to CSV file with grade data')
    parser.add_argument('--year', default='2024', choices=['2023', '2024'], help='Year to visualize')
    args = parser.parse_args()

    df = load_data(args.csv)
    plot_grade_distribution(df, args.year)


if __name__ == '__main__':
    main()
