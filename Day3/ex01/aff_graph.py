from load_csv import load
import matplotlib.pyplot as plt
import seaborn as sns
from sys import argv
import pandas as pd

def main():
    """Loads a csv file specified in argv[1] (default life_expectancy.csv)
then displays the informations for France in a seaborn lineplot graph
    """
    path = "life_expectancy_years.csv" if len(argv) <= 2 else argv[1]
    dataset = load(path)
    if not dataset.empty:
        try:
            france_data = dataset[dataset['country'] == 'France']
            france_long = france_data.melt(
                id_vars='country',
                var_name='Year',
                value_name='Life Expectancy'
            )
            france_long['Year'] = pd.to_numeric(france_long['Year'])
            plt.rcParams['toolbar'] = 'None'
            plot = sns.relplot(
                data=france_long,
                kind="line",
                x="Year",
                y="Life Expectancy",
                hue="country",
                legend=False,
                height=6,
                aspect=1.5
            )

            plot.set(
                title="France Life expectancy Projections",
                xlabel="Year",
                ylabel="Life expectancy",
                yticks=range(30, 101, 10),
                xticks=range(1800, 2100, 40)
            )

            plot.set_xticklabels(rotation=45)
            plot.tight_layout()
            plt.show()

        except Exception as e:
            print(f"{Exception.__name__}: {e}")


if __name__ == "__main__":
    main()
