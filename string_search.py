text = """
Python — це потужна мова програмування, яка використовується в аналізі даних, 
машинному навчанні та веб-розробці. Python має простий синтаксис і велику спільноту. 
Багато студентів обирають Python для навчальних і комерційних проєктів. 
Алгоритми пошуку в рядку є важливою частиною програмування.
"""
import re
import hashlib
import time


class StringSearch:

    def init(self, text):
        self.text = text

    # ---------------------------
    # 1. НАЇВНИЙ АЛГОРИТМ
    # ---------------------------
    def naive_search(self, pattern):
        res = []
        n, m = len(self.text), len(pattern)

        for i in range(n - m + 1):
            if self.text[i:i+m] == pattern:
                res.append(i)

        return res


    # ---------------------------
    # 2. КМП (Кнут–Морріс–Пратт)
    # ---------------------------
    def kmp(self, pattern):

        def build_lps(p):
            lps = [0] * len(p)
            j = 0

            for i in range(1, len(p)):
                while j > 0 and p[i] != p[j]:
                    j = lps[j - 1]
                if p[i] == p[j]:
                    j += 1
                    lps[i] = j
            return lps

        lps = build_lps(pattern)
        res = []

        i = j = 0
        n, m = len(self.text), len(pattern)

        while i < n:
            if self.text[i] == pattern[j]:
                i += 1
                j += 1

                if j == m:
                    res.append(i - j)
                    j = lps[j - 1]
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return res


    # ---------------------------
    # 3. РАБІН–КАРП (хешування)
    # ---------------------------
    def rabin_karp(self, pattern):
        res = []
        n, m = len(self.text), len(pattern)

        if m > n:
            return []

        pattern_hash = hashlib.md5(pattern.encode()).hexdigest()

        for i in range(n - m + 1):
            window = self.text[i:i+m]
            if hashlib.md5(window.encode()).hexdigest() == pattern_hash:
                res.append(i)

        return res


    # ---------------------------
    # 4. REGEX ПОШУК
    # ---------------------------
    def regex_search(self, pattern):
        return [(m.start(), m.group()) for m in re.finditer(pattern, self.text)]


    # ---------------------------
    # 5. ШВИДКОДІЯ (ДЛЯ БАЛІВ)
    # ---------------------------
    def benchmark(self, pattern):
        methods = {
            "Naive": self.naive_search,
            "KMP": self.kmp,
            "Rabin-Karp": self.rabin_karp
        }

        results = {}

        for name, method in methods.items():
            start = time.time()
            method(pattern)
            end = time.time()
            results[name] = round(end - start, 6)

        return results

    text = """
    Python — це потужна мова програмування, яка використовується в аналізі даних, 
    машинному навчанні та веб-розробці. Python має простий синтаксис і велику спільноту. 
    Багато студентів обирають Python для навчальних і комерційних проєктів. 
    Алгоритми пошуку в рядку є важливою частиною програмування.
    """

    search = StringSearch(text)

    pattern = "Python"

    print(" Шукаємо:", pattern)

    print("\nNaive:", search.naive_search(pattern))
    print("KMP:", search.kmp(pattern))
    print("Rabin-Karp:", search.rabin_karp(pattern))
    print("Regex:", search.regex_search(r"Python"))

    print("\n ШВИДКОДІЯ:")
    print(search.benchmark(pattern))