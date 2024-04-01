def print_hms(sec):
    mins = sec//60
    hrs = mins//60
    minsTot = mins%60
    remainder = mins%60
    print(hrs, minsTot, remainder, sep=':')