class Alpha:
    normal = 1
    _lucky = 13
    __secret = 777

    def print_x(self):
        print(self.x)


if __name__ == '__main__':
    print(Alpha.normal)
    print(Alpha._lucky)
    # print(Alpha.__secret)
    print(Alpha.__dict__)
    print(Alpha._Alpha__secret)
    Alpha._Alpha__secret = 1234
    print(Alpha._Alpha__secret)
    Alpha.x = 2222
    print(Alpha.x)
    Alpha.print_x()