from datetime import timedelta


def date_range(_start, _end):
    for n in range((_end - _start).days + 1):
        yield _start + timedelta(n)
