import csv

def ler_csv(arq_csv):
    lista_urls = []
    try:
        with open (arq_csv, "r") as urls:
            url_csv = csv.reader(urls, delimiter=",")
            for i, linha in enumerate(url_csv):
                lista_urls.append(str(linha[0]))
    except:
        print("Arquivo .csv inexistente")
    return lista_urls