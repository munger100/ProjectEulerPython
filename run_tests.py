from poker import *
import unittest


class TestPoker(unittest.TestCase):
    def test_euler_winners(self):
        hand1, hand2 = ["5H", "5C", "6S", "7S", "KD"], ["2C", "3S", "8S", "8D", "TD"]
        self.assertEqual(do(hand1, hand2), 2, msg="%s    %s" % (hand1, hand2))

        hand1, hand2 = ["5D", "8C", "9S", "JS", "AC"], ["2C", "5C", "7D", "8S", "QH"]
        self.assertEqual(do(hand1, hand2), 1, msg="%s    %s" % (hand1, hand2))

        hand1, hand2 = ["2D", "9C", "AS", "AH", "AC"], ["3D", "6D", "7D", "TD", "QD"]
        self.assertEqual(do(hand1, hand2), 2, msg="%s    %s" % (hand1, hand2))

        hand1, hand2 = ["4D", "6S", "9H", "QH", "QC"], ["3D", "6D", "7H", "QD", "QS"]
        self.assertEqual(do(hand1, hand2), 1, msg="%s    %s" % (hand1, hand2))

        hand1, hand2 = ["2H", "2D", "4C", "4D", "4S"], ["3C", "3D", "3S", "9S", "9D"]
        self.assertEqual(do(hand1, hand2), 1, msg="%s    %s" % (hand1, hand2))

    def test_winners2(self):
        # two pair
        hand1, hand2 = ["5D", "5C", "7H", "7C", "AH"], ["5S", "5H", "9C", "3S", "9H"]
        self.assertEqual(do(hand1, hand2), 2, msg="%s    %s" % (hand1, hand2))

        # different fours
        hand1, hand2 = ["TD", "TH", "TC", "TS", "AS"], ["JS", "JD", "JH", "JC", "3C"]
        self.assertEqual(do(hand1, hand2), 2, msg="%s    %s" % (hand1, hand2))

    def test_hand_strings(self):
        dud = ["3H", "JS", "QC", "KH", "5H"]

        hs = ["3H", "JH", "QH", "KH", "5H"]
        self.assertTrue(is_flush(set_flags(hs)), msg=hs)
        self.assertFalse(is_flush(set_flags(dud)), msg=dud)

        hs = ["2H", "3S", "4D", "6C", "5D"]
        self.assertTrue(is_straight(remove_suits(set_flags(hs))), msg=hs)
        self.assertFalse(is_straight(remove_suits(set_flags(dud))), msg=dud)

        hs = ["4H", "4S", "4D", "4C", "5D"]
        self.assertTrue(is_four_of_a_kind(remove_suits(set_flags(hs))), msg=hs)
        self.assertFalse(is_four_of_a_kind(remove_suits(set_flags(dud))), msg=dud)

    def test_get_ranks(self):
        hs = "3H JS QH KH 5H".split(" ")
        self.assertEqual(evaluate(hs)[0], 1, msg=hs)

        hs = "3H JS QH 3H 5H".split(" ")
        self.assertEqual(evaluate(hs)[0], 2, msg=hs)

        hs = "KH QS QH KH 5H".split(" ")
        self.assertEqual(evaluate(hs)[0], 3, msg=hs)

        hs = "JH QS QH KH QH".split(" ")
        self.assertEqual(evaluate(hs)[0], 4, msg=hs)

        hs = "8H 9S JH QH TH".split(" ")
        self.assertEqual(evaluate(hs)[0], 5, msg=hs)

        hs = "KH QH TH KH 5H".split(" ")
        self.assertEqual(evaluate(hs)[0], 6, msg=hs)

        hs = "KS TS TH KD KH".split(" ")
        self.assertEqual(evaluate(hs)[0], 7, msg=hs)

        hs = "TD TS TC TH JH".split(" ")
        self.assertEqual(evaluate(hs)[0], 8, msg=hs)

        hs = "4D 5D 7D 6D 8D".split(" ")
        self.assertEqual(evaluate(hs)[0], 9, msg=hs)

        hs = "TS JS QS KS AS".split(" ")
        self.assertEqual(evaluate(hs), 10, msg=hs)

    def test_basics(self):
        hs = ["3H", "5H", "6D", "TS", "JD"]
        rk = [3, 5, 6, 10, 11]
        container = []
        for card, count in remove_suits(set_flags(hs)).items():  # Put all cards in hand into a container
            if count == 1:
                container.append(card)
        ranks = []
        for item in container:  # Get ranks of each card, to check for straight
            ranks.append(get_rank(item))
        ranks = sorted(ranks)
        self.assertEqual(ranks, rk)

        hs = ["3H", "3H", "KD", "KS", "KD"]
        matches = {"thr": 2, "k": 3}
        self.assertEqual(set_flags(hs).get("thr"), 2)
        self.assertEqual(set_flags(hs).get("k"), 3)

        hs = "3H 5H KD QS KD".split(" ")
        matches = {"03": 1, "05": 1, "13": 2, "12": 1}
        self.assertEqual(set_flags(hs).get("thr"), 1)
        self.assertEqual(set_flags(hs).get("fiv"), 1)
        self.assertEqual(set_flags(hs).get("k"), 2)
        self.assertEqual(set_flags(hs).get("q"), 1)

        hr = "4H 6C 7C KS KS".split(" ")
        self.assertEqual(give_highest(remove_suits(set_flags(hr))), 13)

        hr = "4S KS 4H KH KD".split(" ")
        self.assertEqual(give_highest(remove_suits(set_flags(hr))), 13)


if __name__ == "__main__":
    unittest.main()
