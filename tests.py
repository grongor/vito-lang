#!venv/bin/python
# -*- coding: utf-8 -*-


import unittest
import tempfile
from subprocess import call, DEVNULL

__author__ = 'martin.voznik@heureka.cz'


class TestForbiddenWords(unittest.TestCase):

    def testWrongStrings(self):
        string = """
import random
čosi teď bude ['a', 'b', 'c']
Volám Čuprovi(random.choice(čosi))
        """
        self.assertEqual(1, _test_string(string))

        string = """
Budeme používat random
čosi teď bude ['a', 'b', 'c']
print(random.choice(čosi))
        """
        self.assertEqual(1, _test_string(string))

        string = """
Hele prostě tohle dělej dokuď do piče Je neni:
    pass
        """
        self.assertEqual(1, _test_string(string))

    def testCorrectStrings(self):
        string = """
Budeme používat random
čosi teď bude ['a', 'b', 'c']
Volám Čuprovi(random.choice(čosi))
        """
        self.assertEqual(0, _test_string(string))

        string = """
A to si piš kurva("hovno")
        """
        self.assertEqual(0, _test_string(string))


if __name__ == '__main__':
    unittest.main()


def _test_string(string):
    with tempfile.NamedTemporaryFile('w+b', 0, suffix='.nohy') as file:
        file.write(string.encode())

        return call(['chci', file.name], stdout=DEVNULL)
