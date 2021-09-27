import enum


class DayOfWeek(enum.Enum):
    SUN= "SUNAAAAA"
    MON= "MON"
    TUE= "TUE"
    WED= "WED"
    THU= "THU"
    FRI= "FRI"
    SAT= "SAT"


if __name__ == '__main__':
    day = DayOfWeek.SUN
    print(day.name)
    print(type(day.name))
    print(day.value)

    print(DayOfWeek['SUN'])
    if(day is DayOfWeek.SUN):
        print("sssss")
