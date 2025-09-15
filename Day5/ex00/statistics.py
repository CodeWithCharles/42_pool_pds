from typing import Any


def ft_statistics(*args: Any, **kwargs) -> None:
    """Compute and display statistical measures based on input arguments.

    Args:
        *args (Any): Positional arguments representing numerical values.
        **kwargs: Keyword arguments specifying which statistics to compute.
            Supported values:
                - "mean": Mean of the data
                - "median": Median of the data
                - "quartile": First and third quartiles of the data
                - "var": Variance of the data
                - "std": Standard deviation of the data

    Returns:
        None: Results are printed to stdout.
    """
    data = list(args)
    if data:
        try:
            data = [float(x) for x in data]
        except ValueError:
            print("ERROR: arguments must be numbers")
            return

        data.sort()
        n = len(data)

        def fmt(x):
            """Format numbers as int if possible, otherwise keep float.

            Args:
                x (float): Value to format.

            Returns:
                int | float: Integer if `x` has no decimal part,
                else the original float.
            """
            return int(x) if x == int(x) else x

        def mean() -> int | float:
            """Compute the arithmetic mean.

            Returns:
                int | float: Mean value of the dataset.
            """
            return sum(data) / n

        def median() -> int | float:
            """Compute the median.

            Returns:
                int | float: Median value of the dataset.
            """
            mid = n // 2
            if n % 2:
                return data[mid]
            return (data[mid - 1] + data[mid]) / 2

        def quartile() -> list[float]:
            """Compute the first (Q1) and third (Q3) quartiles.

            Returns:
                list[float]: A list containing Q1 and Q3.
            """

            def get_q(p: float):
                """Interpolate the quartile value for a given percentile.

                Args:
                    p (float): Percentile as a fraction (e.g., 0.25 for Q1).

                Returns:
                    float: Interpolated value at the given percentile.
                """
                idx = (n - 1) * p
                low = int(idx)
                up = min(low + 1, n - 1)
                return data[low] + (idx - low) * (data[up] - data[low])

            return [get_q(0.25), get_q(0.75)]

        def variance() -> float:
            """Compute the variance.

            Returns:
                float: Variance of the dataset.
            """
            m = mean()
            return sum((x - m) ** 2 for x in data) / n

        def std() -> float:
            """Compute the standard deviation.

            Returns:
                float: Standard deviation of the dataset.
            """
            return variance() ** 0.5

        funcs = {
            "mean": mean,
            "median": median,
            "quartile": quartile,
            "var": variance,
            "std": std,
        }

        for _, v in kwargs.items():
            if v in funcs:
                result = funcs[v]()
                if isinstance(result, list):
                    print(f"{v} : {result}")
                else:
                    print(f"{v} : {fmt(result)}")
    else:
        [print("ERROR") for _ in kwargs.items()]
