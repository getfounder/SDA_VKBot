def split_dt(datetime):
    # type(datetime) >> str()

    date, time = datetime.split()

    year, month, day = date.split("-")
    hour, minute, sec = time.split(":")
    sec = sec.split(".")[0]

    return (day, month, year, hour, minute, sec)