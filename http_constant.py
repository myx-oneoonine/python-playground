from http import HTTPStatus

print(HTTPStatus(HTTPStatus.BAD_REQUEST).value)
print(HTTPStatus(HTTPStatus.BAD_REQUEST).phrase)
print(HTTPStatus(HTTPStatus.BAD_REQUEST).description)

print(HTTPStatus(HTTPStatus.OK).name)