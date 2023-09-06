from unittest import TestCase, main
from main import *
import os


class ProgramTest(TestCase):

    def test_test_for_test(self):
        test_path = 'text.txt'
        test_content = 'test 70053 test'
        save_result(test_path)
        with open(test_path, 'r', encoding='utf-8') as file:
            from_file = file.read()
        self.assertEqual(from_file, test_content)


if __name__ == '__main__':
    main()
