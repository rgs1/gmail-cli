# -*- coding: utf-8 -*-

""" util test cases """

import unittest

from gmail_cli.util import (
    b64_url_decode
)


class UtilTestCase(unittest.TestCase):
    """ test util """

    def setUp(self):
        """
        nothing for now
        """
        pass

    def test_b64_url_decode(self):
        self.assertEqual(b64_url_decode('aGVsbG8'), 'hello')
