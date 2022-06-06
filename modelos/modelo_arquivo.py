class ModeloArquivo:

    def __init__(self):
        self.header_arquivo = None
        self.lotes = []
        self.trailer_arquivo = None


class ModeloLote:

    def __init__(self):
        self.header_lote = None
        self.detalhes = []
        self.trailer_lote = None


class ModeloHeaderArquivo:

    def __init__(self, linha):
        self.codigo_banco = linha[0:3]
        self.lote_servico = linha[3:7]
        self.tipo_registro = linha[7]
        self.uso_exclusivo_nexxera = linha[8:17]
        self.inscricao_empresa = linha[17]
        self.numero_inscricao_empresa = linha[18:32]
        self.convenio_banco = linha[32:52]
        self.agencia_mantenedora_conta = linha[52:57]
        self.verificador_agencia = linha[57]
        self.conta_corrente = linha[58:70]
        self.verificador_conta = linha[70]
        self.verificador_agencia_conta = linha[71]
        self.nome_empresa = linha[72:102]
        self.nome_banco = linha[102:132]
        self.nome_van = linha[132:142]
        self.remessa_retorno = linha[142]
        self.data_geracao_arquivo = linha[143:151]
        self.hora_geracao_arquivo = linha[151:157]
        self.sequencial_arquivo = linha[157:164]
        self.versao_layout = linha[164:167]
        self.densidade_gravacao = linha[167:172]
        self.uso_reserva_banco = linha[172:191]
        self.uso_reserva_empresa = linha[191:211]
        self.uso_exclusivo_nexxera_final = linha[211:240]


class ModeloHeaderLote:

    def __init__(self, linha):
        self.codigo_banco_compensacao = linha[0:3]
        self.lote_servico = linha[3:7]
        self.registro = linha[7]
        self.operadora = linha[8]
        self.servico = linha[9:11]
        self.forma_lancamento = linha[11:13]
        self.versao_layout_lote = linha[13:16]
        self.uso_exclusivo_nexxera = linha[16]
        self.tipo_inscricao_empresa = linha[17]
        self.numero_inscricao_empresa = linha[18:32]
        self.convenio_banco = linha[32:52]
        self.agencia_mantenedora_conta = linha[52:57]
        self.verificador_agencia = linha[57]
        self.conta_corrente = linha[58:70]
        self.verificador_conta = linha[70]
        self.verificador_agencia_conta = linha[71]
        self.nome_empresa = linha[72:102]
        self.mensagem = linha[102:142]
        self.rua_avenida = linha[142:172]
        self.numero_local = linha[172:177]
        self.casa_apartamento = linha[177:192]
        self.cidade = linha[192:212]
        self.codigo_postal = linha[212:217]
        self.complemento_codigo_postal = linha[217:220]
        self.sigla_estado = linha[220:222]
        self.uso_exclusivo_nexxera_final = linha[222:230]
        self.ocorrencias_retorno = linha[230:240]


class ModeloDetalhe:

    def __init__(self, linha):
        self.codigo_banco_compensacao = linha[0:3]
        self.lote_servico = linha[3:7]
        self.registro = linha[7]
        self.registro_lote = linha[8:13]
        self.registro_detalhe = linha[13]
        self.movimento = linha[14]
        self.instrucao_movimento = linha[15:17]
        self.camara_centralizadora = linha[17:20]
        self.banco_favorecido = linha[20:23]
        self.mantenadora_conta = linha[23:28]
        self.verificador_agencia = linha[28]
        self.conta_corrente = linha[29:41]
        self.verificador_conta = linha[41]
        self.verificador_agencia_conta = linha[42]
        self.nome_favorecido = linha[43:73]
        self.documento_empresa = linha[73:93]
        self.data_pagamento = linha[93:101]
        self.tipo_moeda = linha[101:104]
        self.quantidade_moeda = linha[104:119]
        self.valor_pagamento = linha[120:134]
        self.documento_banco = linha[134:154]
        self.data_efetivacao_pagamento = linha[154:162]
        self.valor_efetivacao_pagamento = linha[162:177]
        self.outras_informacoes = linha[177:217]
        self.tipo_servico = linha[217:219]
        self.finalidade = linha[219:224]
        self.lancamento_extrato_conta = linha[224:229]
        self.aviso_favorecido = linha[229]
        self.ocorrencias_retorno = linha[230:240]


class ModeloTrailerLote:

    def __init__(self, linha):
        self.banco_compesacao = linha[0:3]
        self.lote_serviso = linha[3:7]
        self.registro = linha[7]
        self.uso_exclusivo_nexxera = linha[8:17]
        self.quantidade_registros = linha[17:23]
        self.somatoria_valores = linha[23:41]
        self.somatoria_moedas = linha[41:59]
        self.aviso_debito = linha[59:65]
        self.uso_exclusivo_nexxera_final = linha[65:230]
        self.ocorrencias_retorno = linha[230:240]


class ModeloTrailerArquivo:

    def __init__(self, linha):
        self.banco_compesacao = linha[0:3]
        self.lote_serviso = linha[3:7]
        self.registro = linha[7]
        self.uso_exclusivo_nexxera = linha[8:17]
        self.quantidade_lotes_arquivo = linha[17:23]
        self.quantidade_registros_arquivo = linha[23:29]
        self.quantidade_contas = linha[29:35]
        self.uso_exclusivo_nexxera_final = linha[35:240]
