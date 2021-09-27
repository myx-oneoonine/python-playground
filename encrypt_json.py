PAYLOAD = {
    "num": 12345,
    "bool": True,
    "name": "myx",
    "age": "100",
    "list_str": ["ss", "ss"],
    "list_obj": [
        {
            "attr1": "a",
            "attr2": "b"
        }
    ],
    "obj": {
        "num": 12345,
        "bool": True,
        "name": "myx",
        "obj": {
            "attr1": "a",
            "attr2": "b"
        },
        "list_obj": [
            {
                "attr1": "a",
                "attr2": "b"
            },
            {
                "attr1": "a",
                "attr2": "b"
            },
            {
                "attr1": "a",
                "attr2": "b"
            }
        ],
    }
}


def encrypt_json(json: dict, modifier) -> dict:
    result: dict = {}

    for k, v in list(json.items()):
        if type(v) is dict:
            result[k] = encrypt_json(v, modifier)
        elif type(v) is list:
            result[k] = [(modifier(i) if type(i) is not dict else encrypt_json(i, modifier)) for i in v]
        else:
            result[k] = modifier(v)
    return result


if __name__ == '__main__':
    print("xxx", type(lambda s: str(s) + "!!"))
    print(encrypt_json(PAYLOAD, lambda s: str(s) + "!!"))
