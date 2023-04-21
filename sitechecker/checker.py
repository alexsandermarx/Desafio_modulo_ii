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
        reg_check = 1
    else:
        reg_check = int(reg_check[0])

    matriz_url = []

    for csv_i in range(len(csv)):
        lista_csv = ler_csv(csv[csv_i])
        for item_csv in lista_csv:
            matriz_url.append([item_csv,0,0])

    for url in urls:
        matriz_url.append([url,0,0])

    verificacoes = 0
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            for url in matriz_url:
                error = ""
                try:
                    result = site_is_online(url[0], reg_check)
                except Exception as e:
                    result = False
                    error = str(e)
                online = display_check_result(result, url[0], error)
                url[1] += online
                url[2] += 1
            
            verificacoes += 1
            print("Quantidade de verificações: {}".format(verificacoes))

            print("Pressione 'Ctrl + C' para cancelar a execução")
            sleep(reg_check)
    except (KeyboardInterrupt):
        print("\n\nExecução finalizada\n\n")
        arq_resultado = open("resultado.txt", "w")
        for url in matriz_url:
            arq_resultado.write("O site {} ficou online em {}%% das tentativas\n".format(url[0],(url[1]/url[2])*100))
        arq_resultado.close()
        pass

