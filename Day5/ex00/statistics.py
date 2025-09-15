from typing import Any


def ft_statistics(*args: Any, **kwargs) -> None:
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
            return int(x) if x == int(x) else x

        def mean() -> int | float:
            return sum(data) / n

        def median() -> int | float:
            mid = n // 2
            if n % 2:
                return data[mid]
            return (data[mid - 1] + data[mid]) / 2

        def quartile() -> list[float]:
            def get_q(p: float):
                idx = (n - 1) * p
                low = int(idx)
                up = min(low + 1, n - 1)
                return data[low] + (idx - low) * (data[up] - data[low])
            return [get_q(0.25), get_q(0.75)]

        def variance() -> float:
            m = mean()
            return sum((x - m) ** 2 for x in data) / n

        def std() -> float:
            return variance() ** 0.5

        funcs = {
            "mean": mean,
            "median": median,
            "quartile": quartile,
            "var": variance,
            "std": std
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
