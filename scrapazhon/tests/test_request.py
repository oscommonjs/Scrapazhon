import mock

import unittest

import scrapazhon

from unittest           import TestCase

from scrapazhon.request import Request

from nose.tools         import *

from mock               import patch

from mock import MagicMock

class RequestTest(unittest.TestCase):

    def setUp(self):
        self.patcher      = patch('urllib2.urlopen')
        self.urlopen_mock = self.patcher.start()
        self.urlopen_mock = self.patcher.start()
        self.code_mock    = self.patcher.start()

    def url_instance_variable_test(self):
        requestObject = Request("http://www.amazon.com/appstore")
        self.assertEqual(vars(requestObject), {'url': 'http://www.amazon.com/appstore'})

    @raises(Exception)
    def url_error_exception_test(self):
        requestObject = Request("htwwqtp://@@@@com/appstore")
        self.assertRaises(URLError, requestObject.getHtmlFromUrl())

    @raises(Exception)
    def http_error_exception_test(self):
        request = Request('http://www.amazon.com/holahellohalloczesc')
        self.assertRaises(HTTPError, requestObject.getHtmlFromUrl())

    def tearDown(self):
        self.patcher.stop()