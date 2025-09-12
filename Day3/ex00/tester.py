from load_csv import load
from sys import argv
import webbrowser
import os


def main():
    """Loads a csv file specified in argv[1] (default life_expectancy.csv)
then saves it into a 'saved_dump.html' file and opens a webbrowser page
    """
    saved_filename = 'saved_dump.html'
    saved_path = f'file:///{os.getcwd()}/{saved_filename}'
    path = "life_expectancy_years.csv" if len(argv) <= 2 else argv[1]
    dataset = load(path)
    if not dataset.empty:
        try:
            f = open(saved_filename, 'w')
            f.write(dataset.to_html())
            f.close()
            webbrowser.open_new_tab(saved_path)

        except Exception as e:
            print(f"{Exception.__name__}: {e}")


if __name__ == "__main__":
    main()
