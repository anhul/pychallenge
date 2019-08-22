import unittest
import PythonChallenge1

class TestPychallenge1(unittest.TestCase):

    def setUp(self):
        self.test_sentence = "(bcambcb gl y pgefr uyw - 5+)!!!"
        self.expected_sentence = "(decoded in a right way - 5+)!!!"

    def test_letters(self):
        self.assertEqual(py_challenge_1("a"), "c")
        self.assertEqual(py_challenge_1("y"), "a")
        self.assertEqual(py_challenge_1("z"), "b")
        self.assertEqual(py_challenge_1("x"), "z")

    def test_other_symbols(self):
        self.assertEqual(py_challenge_1(" "), " ", "Non lower case letters \
                                                    must not be changed")
        self.assertEqual(py_challenge_1("."), ".")
        self.assertEqual(py_challenge_1("'"), "'")
        self.assertEqual(py_challenge_1("25"), "25")


    def test_sentence_decoding(self):
        self.assertEqual(py_challenge_1(self.test_sentence), self.expected_sentence)

if __name__ == '__main__':
    unittest.main()
