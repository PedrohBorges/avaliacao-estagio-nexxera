from modelos.modelo_arquivo import (
    ModeloArquivo, ModeloLote, ModeloHeaderArquivo, ModeloHeaderLote, ModeloDetalhe, ModeloTrailerLote,
    ModeloTrailerArquivo
)


def construir_modelo_arquivo(nome_arquivo):
    arquivos = []
    with open(nome_arquivo, 'r') as arquivo_entrada:
        linhas = arquivo_entrada.readlines()
        for linha in linhas:
            if linha[7] == '0':
                arquivo = ModeloArquivo()
                arquivo.header_arquivo = ModeloHeaderArquivo(linha)
                arquivos.append(arquivo)
            elif linha[7] == '1':
                lote = ModeloLote()
                arquivo.lotes.append(lote)
                lote.header_lote = ModeloHeaderLote(linha)
            elif linha[7] == '3':
                detalhe = ModeloDetalhe(linha)
                lote.detalhes.append(detalhe)
            elif linha[7] == '5':
                lote.trailer_lote = ModeloTrailerLote(linha)
            elif linha[7] == '9':
                arquivo.trailer_arquivo = ModeloTrailerArquivo(linha)
    return arquivos

