import argparse

def read_user_cli_args():

    parser = argparse.ArgumentParser(
        prog="sitechecker", description="Teste a disponibilidade de uma URL"
    )

    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="Insira um ou mais URLs"
    )
    parser.add_argument(
        "-c",
        "--csv",
        metavar="csv",
        nargs="+",
        type=str,
        default=[],
        help="Insira um arquivo csv com URLs"
    )
    parser.add_argument(
        "-w",
        "--reg_check",
        metavar="reg_check",
        nargs="+",
        type=int,
        default=[],
        help="Insira um tempo para checagem períodica"
    )
    return parser.parse_args()

def display_check_result(result, url, error=""):
    print(f'Os status da "{url}" é:', end =" ")
    if result:
        print('"Online!👍"')
        return 1
    else:
        print(f'"Offline?" 👎 \n  Erro: "{error}"')
        return 0