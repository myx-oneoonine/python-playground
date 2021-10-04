def umbrella():
    return "1"


def stand():
    pass


def routing(rain: bool):
    if rain:
        umbrella()
    else:
        stand()

