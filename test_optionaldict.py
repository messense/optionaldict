# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import pickle
import unittest
try:
    import simplejson as json
except ImportError:
    import json

from optionaldict import optionaldict


class optionaldictTestCase(unittest.TestCase):

    def test_init_with_none(self):
        d = optionaldict(
            a=1,
            b=None
        )
        self.assertEqual(1, d['a'])
        self.assertTrue('b' not in d)

    def test_init_with_dict_contains_none(self):
        d1 = {
            'a': 1,
            'b': None
        }
        d = optionaldict(d1)
        self.assertEqual(1, d['a'])
        self.assertTrue('b' not in d)

    def test_setitem_with_none(self):
        d = optionaldict()
        d['a'] = 1
        d['b'] = None
        self.assertEqual(1, d['a'])
        self.assertTrue('b' not in d)

    def test_setdefault_with_none(self):
        d = optionaldict()
        a = d.setdefault('a', 1)
        b = d.setdefault('b', None)
        self.assertEqual(1, a)
        self.assertTrue(b is None)
        self.assertEqual(1, d['a'])
        self.assertTrue('b' not in d)

    def test_json_dumps(self):
        d = optionaldict(
            a=1,
            b=None
        )
        json.dumps(d)

    def test_pickle_dumps(self):
        d = optionaldict(
            a=1,
            b=None
        )
        pickle.dumps(d)

    def test_pickle_loads(self):
        d = optionaldict(
            a=1,
            b=None
        )
        s = pickle.dumps(d)
        pickle.loads(s)
