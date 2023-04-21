from http.client import HTTPConnection
from urllib.parse import urlparse
from sitechecker.cli import display_check_result
from sitechecker.ler_csv import ler_csv
from time import sleep
import os


def site_is_online(url, timeout=10):
    """Return True if the target URL is online.

    Raise an exception otherwise.
    """
    error = Exception("Deu ruim!")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request("HEAD", "/")
            return True
        except Exception as e:
            error = e
        finally:
            connection.close()
    raise error

def _site_check(urls, csv, reg_check):
    
    if reg_check == []:
        reg_check = 0
    else:
        reg_check = int(reg_check[0])

    for csv_i in range(len(csv)):
        lista_csv = ler_csv(csv[csv_i])
        for item_csv in lista_csv:
            urls.append(item_csv) 

    verificacoes = 0
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            for url in urls:
                error = ""
                try:
                    result = site_is_online(url)
                except Exception as e:
                    result = False
                    error = str(e)
                display_check_result(result, url, error)
            
            verificacoes += 1
            print("Quantidade de verificações: {}".format(verificacoes))

            print("Pressione 'Ctrl + C' para cancelar a execução")
            sleep(reg_check)
    except (KeyboardInterrupt):
        print("\n\nExecução finalizada\n\n")
        pass

