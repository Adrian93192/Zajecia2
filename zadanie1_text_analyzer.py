class TextAnalyzer:
    # Bazowa klasa do analizy tekstu

    def word_count(self, text):
        # Zwraca liczbę słów
        return len(text.split())

    def char_count(self, text):
        # Zwraca liczbę wszystkich znaków
        return len(text)

    def unique_words(self, text):
        # Zwraca liczbę unikalnych słów (ignoruje wielkość liter)
        words = text.lower().split()
        return len(set(words))


class AdvancedTextAnalyzer(TextAnalyzer):
    # Rozszerzona klasa z analizą sentymentu

    def sentiment_analysis(self, text):
        # Prosty system klasyfikacji sentymentu na podstawie słów kluczowych
        pozytywne = {"wspaniały", "świetny", "dobry", "cudowny", "fantastyczny"}
        negatywne = {"okropny", "zły", "tragiczny", "nieszczęsny", "kiepski"}

        text_lower = text.lower()

        if any(word in text_lower for word in pozytywne):
            return "Pozytywny"
        elif any(word in text_lower for word in negatywne):
            return "Negatywny"
        else:
            return "Neutralny"


# Przykład użycia:
# analyzer = AdvancedTextAnalyzer()
# print(analyzer.word_count("To był naprawdę wspaniały dzień!"))
# print(analyzer.char_count("To był naprawdę wspaniały dzień!"))
# print(analyzer.unique_words("To był naprawdę wspaniały dzień!"))
# print(analyzer.sentiment_analysis("To był naprawdę okropny dzień!"))
