import sys

from asyncore import read
from sitechecker.checker import site_is_online
from sitechecker.cli import display_check_result, read_user_cli_args
from sitechecker.ler_csv import ler_csv

def main():
    user_args = read_user_cli_args()
    urls = user_args.urls
    csv = user_args.csv
    if not urls and not csv:
        print("Faltou URL ou csv")
        sys.exit(1)
    if urls:
        _site_check(urls)
    if csv:
        _site_check(ler_csv(user_args.csv[0]))

def _site_check(urls):
    for url in urls:
        error = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)

if __name__ == "__main__":
    main()