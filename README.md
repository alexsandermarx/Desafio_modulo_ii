<h1 align="center"> Verificador de Disponibilidade de Sites </h1>

![Imagem programa LightHouse 2023.4](https://github.com/alexsandermarx/Desafio_modulo_ii/blob/main/capa%20lh%202023.png)

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

Este projeto é resultado da atividade prática do módulo II - Fundamentos de Programação, do Programa LightHouse 2023-4, ofertado pela Indicium. O projeto possui como base, um código disponibilizado pelo programa. A ferramenta contida neste projeto possui o objetivo de testar a disponibilidade de sites passados via parâmetro ou arquivos .csv.

# :hammer: Funcionalidades do projeto

- `Funcionalidade 1`: A entrada de sites pode ser feita diretamente na linha de comandos
- `Funcionalidade 2`: A entrada de sites pode ser feita por um arquivo .csv (essa função possui limitações, descritas adiante)
- `Funcionalidade 3`: A ferramenta executa periodicamente, similar ao comando ping, e gera um relatório ao final da execução

# 📁 Acesso ao projeto

A ferrameta pode ser executada diretamente pelo terminal da máquila local.

# 🛠️ Abrir e rodar o projeto

Para inicializar a ferramenta, é necessário criar um ambiente virtual. Para isso, execute os seguintes comandos >

```
cd meuprojeto/
python3 -m venv venv
source venv/bin/activate
```
Se você estiver utilizando o Windows, o comando deverá ser o seguinte >

```
PS> python3 -m venv venv
PS> venv\Scripts\activate
(venv) PS>
```
Ao final, a estrutura resultante será similar a esta >
```
README.md
requirements.txt
sitechecker/
├── checker.py
├── cli.py
├── ler_csv.py
├── __init__.py
├── __main__.py
```

É possível executar o projeto, a partir de comandos como:
```
python3 -m sitechecker -u site_de_exemplo.com
```
Em que o parâmetro -u especifica um ou mais sites como parâmetro para serem checados.

```
python3 -m sitechecker -c arquivos.csv
```
Em que o parâmetro -c especifica um ou mais arquivos como parâmetro para serem checados.

```
python3 -m sitechecker -w 2
```
Em que o parâmetro -w especifica o tempo entre cada checagem

Ou mesmo qualquer combinação dos comandos anteriores

# TODO

- [ ] Adicionar paralelismo na checkagem de sites e leitura do teclado
- [ ] Melhorar a função que lê os arquivos .csv (por exemplo, possibilitando outros limitadores, exclusão de cabeçalhos, etc)
- [ ] Verificar não somente o site host
- [ ] Criar um script em Bash que permite rodar esse verificador a partir de uma periodicidade pré-definida (por exemplo, a cada 24 horas). Ver CRON.
- [ ] Correção de bugs (como mensagem de 'Arquivo .csv inextente', mesmo ao carregar o arquivo)
- [ ] Adicionar verificação de valores inválidos para o parâmetro -w

# Credits

Exemplo baseado em:
https://realpython.com/site-connectivity-checker-python/
