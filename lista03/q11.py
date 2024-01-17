def traduzir_plus2(comando):
    traducoes = {
        "jqlg": "Hoje",
        "xqw": "vou",
        "rtqitcoct": "programar",
    }

    for palavra, traducao in traducoes.items():
        comando = comando.replace(palavra, traducao)

    return comando


comando = "rtkpv(" + "jvvru://ujqtvwtn.cv/eDIPX" + ")"

comando_traduzido = traduzir_plus2(comando)

print(comando_traduzido)