import unittest

from implement_58 import Solution


class LengthOfLastWordTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_leetcode_examples(self):
        self.assertEqual(self.sol.lengthOfLastWord("Hello World"), 5)
        self.assertEqual(self.sol.lengthOfLastWord("   fly me   to   the moon  "), 4)
        self.assertEqual(self.sol.lengthOfLastWord("luffy is still joyboy"), 6)

    def test_single_word(self):
        self.assertEqual(self.sol.lengthOfLastWord("Hello"), 5)
        self.assertEqual(self.sol.lengthOfLastWord("a"), 1)

    def test_leading_and_trailing_spaces(self):
        self.assertEqual(self.sol.lengthOfLastWord("  Hello"), 5)
        self.assertEqual(self.sol.lengthOfLastWord("Hello  "), 5)
        self.assertEqual(self.sol.lengthOfLastWord("  Hello  "), 5)
        self.assertEqual(self.sol.lengthOfLastWord("   a"), 1)
        self.assertEqual(self.sol.lengthOfLastWord("a   "), 1)

    def test_multiple_spaces_between_words(self):
        self.assertEqual(self.sol.lengthOfLastWord("hi    there"), 5)
        self.assertEqual(self.sol.lengthOfLastWord("one  two   three"), 5)

    def test_last_word_shorter_than_previous(self):
        self.assertEqual(self.sol.lengthOfLastWord("abcdefghijklmnopqrstuvwxyz a"), 1)
        self.assertEqual(self.sol.lengthOfLastWord("day"), 3)

    def test_constraint_bounds(self):
        self.assertEqual(self.sol.lengthOfLastWord("a"), 1)
        self.assertEqual(self.sol.lengthOfLastWord("a" * 10000), 10000)
        self.assertEqual(self.sol.lengthOfLastWord(" " * 9999 + "b"), 1)
        self.assertEqual(self.sol.lengthOfLastWord("b" + " " * 9999), 1)


if __name__ == "__main__":
    unittest.main()
