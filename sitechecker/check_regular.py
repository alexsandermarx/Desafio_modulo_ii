from time import sleep
import sys
from sitechecker.ler_csv import ler_csv
from sitechecker.checker import _site_check

def check_regular(urls, csv, user_args, time = -1):
    if time != -1:
        if not urls and not csv:
            print("Faltou URL ou csv")
            sys.exit(1)
        if urls:
            _site_check(urls)
        if csv:
            _site_check(ler_csv(user_args.csv[0]))
