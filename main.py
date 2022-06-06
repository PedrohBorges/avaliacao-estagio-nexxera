from sys import argv
import logging

from construtores.construtor_html import construir_arquivo_html
from construtores.construtor_modelo_entrada import construir_modelo_arquivo

logging.basicConfig(level=logging.DEBUG)

logging.info(" INICIANDO PROCESSAMENTO ".center(50, '-'))

if len(argv) == 3:
    aplicacao, entrada, saida = argv

    logging.info("Construindo objeto do arquivo entrada")
    arquivos_entrada = construir_modelo_arquivo(entrada)

    logging.info("Construindo arquivo de saida html")
    html_saida = construir_arquivo_html(arquivos_entrada)

    logging.info("Escrevendo arquivo de saida html")
    with open(saida, "w") as relatorio:
        relatorio.write(html_saida)

else:
    logging.info("Execução incorreta! Verificar argumentos passados.")

logging.info(" PROCESSAMENTO FINALIZADO ".center(50, '-'))
