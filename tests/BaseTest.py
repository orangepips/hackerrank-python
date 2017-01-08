import abc
import unittest
import os
import sys
from StringIO import StringIO


class BaseTest(unittest.TestCase):
    def execute(self, case):
        fname_input = self.fname + '.input' + str(case) + '.txt'
        fname_output = self.fname + '.output' + str(case) + '.txt'

        input = open(fname_input).read()
        sys.stdin = StringIO()
        sys.stdin.write(input)
        sys.stdin.seek(0)

        output = open(fname_output).read()
        sys.stdout = StringIO()

        self.call_main()

        self.assertEqual(output, sys.stdout.getvalue().rstrip())

    @abc.abstractmethod
    def call_main(self):
        return

if __name__ == '__main__':
    unittest.main()