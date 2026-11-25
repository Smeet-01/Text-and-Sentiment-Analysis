import sys
import types
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    import nltk.tokenize  # noqa: F401
except ImportError:
    nltk_mod = types.ModuleType("nltk")
    tok_mod = types.ModuleType("nltk.tokenize")
    tok_mod.wordpunct_tokenize = lambda text: text.split()
    tok_mod.sent_tokenize = lambda text, lang="english": [s.strip() for s in text.split(".") if s.strip()]

    class _StubSyllableTokenizer:
        def tokenize(self, word):
            return [ch for ch in word if ch in "aeiou"] or [word]

    tok_mod.SyllableTokenizer = _StubSyllableTokenizer
    nltk_mod.tokenize = tok_mod
    sys.modules["nltk"] = nltk_mod
    sys.modules["nltk.tokenize"] = tok_mod

from List_of_words import Words
from Metrics_for_Analysis import Metrics


class TestWords(unittest.TestCase):
    def test_extend_accepts_strings_and_lists(self):
        pos = Words.positive("extra")
        self.assertIn("extra", pos)
        neg = Words.negative("terrible", ["awful_custom"])
        self.assertIn("terrible", neg)
        self.assertIn("awful_custom", neg)

    def test_currencies_has_no_duplicate_rupee(self):
        cur = Words.currencies()
        self.assertEqual(cur.count("rupee"), 1)


class TestMetrics(unittest.TestCase):
    def test_empty_text_does_not_raise(self):
        m = Metrics("")
        self.assertEqual(m.avg_sentence_length, 0.0)
        self.assertEqual(m.text_complexity(), 0.0)
        self.assertEqual(m.Average_syllable_count(), 0.0)
        self.assertEqual(m.polarity_score(), 0.0)
        self.assertEqual(m.subjectivity_score(), 0.0)

    def test_gfi_preserves_float_precision(self):
        m = Metrics("Awesome brilliant")
        self.assertEqual(m.GFI(1.5), round(0.4 * (m.avg_sentence_length + 1.5), 4))


if __name__ == "__main__":
    unittest.main()
