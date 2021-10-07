from unittest import TestCase
from mockito import when2, unstub, ANY

from unittesting.stub import third_party_api, api_consumer


class TestStub(TestCase):
    def test_stub(self):
        when2(third_party_api.banana_api).thenReturn("stub banana")
        when2(third_party_api.papaya_api, ANY).thenAnswer(lambda s: f"HELLO {s}")

        api_consumer.routing()
        unstub()
        print("----unstub function----")
        api_consumer.routing()
