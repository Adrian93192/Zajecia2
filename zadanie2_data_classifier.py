class NegativeValueError(Exception):
    # Własny wyjątek dla wartości ujemnych
    def __init__(self, value):
        super().__init__(f"Podana wartość ({value}) jest ujemna.")


class DataClassifier:
    # Klasa klasyfikująca wartości numeryczne

    def classify(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Wartość musi być liczbą (int lub float).")

        if value < 0:
            raise NegativeValueError(value)

        if value < 30:
            return "Niska wartość"
        elif value <= 70:
            return "Średnia wartość"
        else:
            return "Wysoka wartość"


# Przykład użycia:
# classifier = DataClassifier()
# try:
#     print(classifier.classify(50))     # Średnia wartość
#     print(classifier.classify(-10))    # NegativeValueError
#     print(classifier.classify("abc"))  # TypeError
# except Exception as e:
#     print(f"Błąd: {e}")
