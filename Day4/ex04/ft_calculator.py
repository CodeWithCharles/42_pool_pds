class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculates and prints the dot product of two matrices"""
        dot_product = 0.0
        for i in V1:
            dot_product += i * V2[V1.index(i)]
        print(f"Dot product is : {int(dot_product)}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Adds two matrices and prints the result"""
        result = []
        for i in V1:
            result.append(i + V2[V1.index(i)])
        print(f"Add Vector is : {[f'{x:.1f}' for x in result]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Substracts two matrices and prints the result"""
        result = []
        for i in V1:
            result.append(i - V2[V1.index(i)])
        print(f"Sous Vector is : {[f'{x:.1f}' for x in result]}")
