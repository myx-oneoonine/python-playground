@property
def url_success():
    return "url here!!!!"

@url_success.getter
def url_success():
    pass

@url_success.setter
def url_success():
    pass

print(url_success())