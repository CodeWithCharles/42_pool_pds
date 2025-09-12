from load_csv import load
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sys import argv


def main():
    """
    Load GNP and life expectancy data and plot their correlation for a given
year.

    This function loads two CSV files:
        - 'income_per_person_gdppercapita_ppp_inflation_adjusted.csv'
        - 'life_expectancy_years.csv'
    It extracts the data for the specified year (default is 1900 if no year is\
provided), cleans it by converting values to numeric and removing missing\
or invalid entries, and creates a scatter plot of life expectancy vs. GNP\
per capita for each country. The GNP axis is displayed on a logarithmic\
scale.

    Command-line usage:
        python script_name.py [year]

    Args:
        None (year can be passed as a command-line argument via sys.argv[1])

    Returns:
        None (displays a matplotlib scatter plot)
    """
    try:
        gnp_data = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )
        life_data = load("life_expectancy_years.csv")

        year = ('1900' if len(argv) <= 1 else argv[1])
        plt.rcParams['toolbar'] = 'None'
        plot_data = pd.DataFrame({
            'Country': gnp_data['country'],
            'GNP': gnp_data[year],
            'LifeExpectancy': life_data[year]
        })

        plot_data['GNP'] = pd.to_numeric(plot_data['GNP'], errors='coerce')
        plot_data['LifeExpectancy'] = pd.to_numeric(
            plot_data['LifeExpectancy'], errors='coerce'
        )
        plot_data = plot_data.dropna(subset=['GNP', 'LifeExpectancy'])
        plot_data = plot_data[plot_data['GNP'] > 0]

        plt.figure(figsize=(10, 6))
        ax = sns.scatterplot(
            data=plot_data,
            x='GNP',
            y='LifeExpectancy',
            hue='Country',
            legend=False
        )
        ax.set_xscale("log")
        ax.set_xticks([300, 1000, 10000])
        ax.set_xticklabels(['300', '1k', '10k'])
        ax.set_xlabel("Gross National Product (per capita)")
        ax.set_ylabel("Life Expectancy (Years)")
        ax.set_title(f"Life Expectancy vs. GNP per Capita (Year {year})")

        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"{Exception.__name__}: {e}")


if __name__ == "__main__":
    main()
