from sitechecker.checker import _site_check
from sitechecker.cli import read_user_cli_args

def main():
    user_args = read_user_cli_args()
    flag = False
    for args in vars(user_args).values():
         if args:
             flag = True
    if flag:
        _site_check(user_args.urls, user_args.csv, user_args.reg_check)
    else:
        print("Nenhum parâmetro foi passado")

if __name__ == "__main__":
    main()