import unittest

from mockito import spy2, verify

from unittesting.spy import rain
from unittesting.spy.rain import routing


class TestRain(unittest.TestCase):
    def test_routing(self):
        spy2(rain.umbrella)
        routing(rain=True)
        verify(rain, 1).umbrella()
        verify(rain, 0).stand()
