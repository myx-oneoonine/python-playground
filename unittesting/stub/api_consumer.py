from unittesting.stub import third_party_api


def routing():
    print(third_party_api.banana_api())
    print(third_party_api.papaya_api("Myx"))
