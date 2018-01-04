# coding: utf8

import sys

sys.path.append('../')

import unittest
from to_php_post_arr.convert import recursive_urlencode


class TestConvert(unittest.TestCase):
    def test_list(self):
        a = [1, 2]
        self.assertEquals(recursive_urlencode(a), '0=1&1=2')

    def test_tuple(self):
        a2 = (1, '2')
        self.assertEquals(recursive_urlencode(a2), '0=1&1=2')

    def test_dict(self):
        b = {'a': 11, 'b': 'foo'}
        self.assertEquals(recursive_urlencode(b), 'a=11&b=foo')

    def test_list_in_dict(self):
        c = {'a': 11, 'b': [1, 2]}
        self.assertEquals(recursive_urlencode(c), 'a=11&b[0]=1&b[1]=2')

    def test_dict_in_list(self):
        d = [1, {'a': 11, 'b': 22}]
        self.assertEquals(recursive_urlencode(d), '0=1&1[a]=11&1[b]=22')

    def test_nested_dict_list(self):
        e = {'a': 11, 'b': [1, {'c': 123}, [3, 'foo']]}
        self.assertEquals(recursive_urlencode(e), 'a=11&b[0]=1&b[1][c]=123&b[2][0]=3&b[2][1]=foo')
    
    def test_utf8(self):
        f = ['测试中文']
        self.assertEquals(recursive_urlencode(f), '0=%E6%B5%8B%E8%AF%95%E4%B8%AD%E6%96%87')


if __name__ == '__main__':
    unittest.main()
