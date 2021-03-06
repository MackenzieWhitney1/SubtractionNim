import unittest
import PNLogic
import io
from contextlib import redirect_stdout


P_List = PNLogic.init(100)
P_Quick_List = PNLogic.quick_init(100)

# bugged. doesn't actually compare correctly
class TestQuickListIsSufficient(unittest.TestCase):
    def test_list_equal_100(self):
        p_list_repr = io.StringIO()
        with redirect_stdout(p_list_repr):
            PNLogic.repr_list(P_List)
        p_list_out = p_list_repr.getvalue()
        p_quick_list_repr = io.StringIO()
        with redirect_stdout(p_quick_list_repr):
            PNLogic.repr_list(P_Quick_List)
        p_quick_list_out = p_quick_list_repr.getvalue()
        self.assertEqual(p_list_out, p_quick_list_out)


class TestIsP(unittest.TestCase):
    def test_same_number_is_P(self):
        self.assertTrue((0, 0) in P_List)
        self.assertTrue((7, 7) in P_List)


class TestIsN(unittest.TestCase):
    def test_exactly_one_zero_is_N(self):
        self.assertTrue((0, 1) not in P_List)
        self.assertTrue((7, 1) not in P_List)


class TestOptimalPlay(unittest.TestCase):
    def test_main_case(self):
        f = io.StringIO()
        with redirect_stdout(f):
            PNLogic.show_optimal_play(P_List, (52, 15))
        out = f.getvalue()
        self.assertEqual(out,
                         """(52, 15) N
(22, 15) P
(7, 15) N
(7, 8) P
(7, 1) N
(1, 1) P
(1, 0) N
(0, 0) P
""")
