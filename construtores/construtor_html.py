from os.path import dirname, join

from jinja2 import FileSystemLoader, Environment


def construir_arquivo_html(arquivos_entrada):
    cabecalhos = []
    for arquivo_entrada in arquivos_entrada:
        header_arquivo = arquivo_entrada.header_arquivo
        header_lote = arquivo_entrada.lotes[0].header_lote
        cabecalho = {
            'nome_empresa': header_arquivo.nome_empresa,
            'numero_inscricao_empresa': header_arquivo.numero_inscricao_empresa,
            'nome_banco': header_arquivo.nome_banco,
            'nome_rua': header_lote.rua_avenida,
            'numero_local': header_lote.numero_local,
            'cidade': header_lote.cidade,
            'cep': _montar_cep(header_lote),
            'sigla_estado': header_lote.sigla_estado,
            'detalhes': []
            }
        cabecalhos.append(cabecalho)
        for lote in arquivo_entrada.lotes:
            for detalhe in lote.detalhes:
                detalhe_saida = {
                    'nome_favorecido': detalhe.nome_favorecido,
                    'data_pagamento': detalhe.data_pagamento,
                    'valor_pagamento': detalhe.valor_pagamento,
                    'numero_documento_empresa': detalhe.documento_empresa,
                    'forma_lancamento': header_lote.forma_lancamento
                }
                cabecalho['detalhes'].append(detalhe_saida)

    return _retonar_html(cabecalhos)


def _montar_cep(header_lote):
    cep = f'{header_lote.codigo_postal}-{header_lote.complemento_codigo_postal}'
    return cep


def _retonar_html(cabecalhos):
    diretorio_template = FileSystemLoader(join(dirname(__file__), "..", "templates"))
    ambiente = Environment(loader=diretorio_template)
    modelo_html = ambiente.get_template("modelo_relatorio.html")
    return modelo_html.render(cabecalhos=cabecalhos)
