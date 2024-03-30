colunas = dict().fromkeys(['Estado da conta corrente existente', 'Duração em meses', 'Histórico de credito', 'Propósito', 'Valor do crédito', 'conta poupança/títulos', 'Emprego atual desde', 'Taxa de parcelamento em porcentagem da renda disponível', 'Estado civil e sexo', 'Outros devedores / fiadores', 'Residência atual desde', 'Propriedade', 'Idade em anos', 'Outros planos de parcelamento', 'Moradia', 'Número de créditos existentes neste banco', 'Emprego', 'Número de pessoas obrigadas a fornecer sustento', 'telefone', 'Trabalhador estrangeiro'])


need_replace = {
    'Estado da conta corrente existente' : {
        "A11" : "... <    0 DM",
        "A12" : "0 <= ... <  200 DM",
        "A13" : "... >= 200 DM",
        "A14" : "Conta não verificad",
    },
    'Histórico de credito' : {
        "A30" : "Nenhum crédito tomado/todos os créditos pagos devidamente.",
        "A31": "todos os créditos deste banco pagos devidamente",
        "A32": "créditos existentes pagos devidamente até agora",
        "A33": "atraso no pagamento no passado",
        "A34": "conta crítica / outros créditos existentes (não deste banco)"
    },
    'Propósito' : {
            "A40": "carro (novo)",
            "A41": "carro (usado)",
            "A42": "móveis/equipamentos",
            "A43": "rádio/televisão",
            "A44": "eletrodomésticos",
            "A45": "reparos",
            "A46": "educação",
            "A47": "(férias - não existe?)",
            "A48": "reciclagem",
            "A49": "negócio",
            "A410": "outros"
    },
    'conta poupança/títulos' :  {
            "A61": "... < 100 DM",
            "A62": "100 <= ... < 500 DM",
            "A63": "500 <= ... < 1000 DM",
            "A64": "... >= 1000 DM",
            "A65": "desconhecido / sem conta poupança"
    },
    'Emprego atual desde' : {
            "A71": "desempregado",
            "A72": "... < 1 ano",
            "A73": "1 <= ... < 4 anos",
            "A74": "4 <= ... < 7 anos",
            "A75": "... >= 7 anos"
    },
    'Estado civil e sexo' : {
            "A91": "masculino: divorciado/separado",
            "A92": "feminino: divorciado/separado/casado",
            "A93": "masculino: solteiro",
            "A94": "masculino: casado/viúvo",
            "A95": "feminino: solteiro"
    },
    'Outros devedores / fiadores' : {
          "A101": "nenhum",
          "A102": "co-requerente",
          "A103": "fiador"  
    },
    'Propriedade' : {
            "A121": "imóvel",
            "A122": "se não imóvel : acordo de poupança de associação de construção / seguro de vida",
            "A123": "se não imóvel ou acorde de poupança : carro ou outro, não no atributo 6",
            "A124": "desconhecido / sem propriedade"
    },
    'Outros planos de parcelamento' : {
            "A141": "banco",
            "A142": "lojas",
            "A143": "nenhum"
    },
    'Moradia' : {
            "A151": "aluguel",
            "A152": "próprio",
            "A153": "libre"
    },
    'Emprego' : {
        "A171": "desempregado/não qualificado - não residente",
        "A172": "não qualificado - residente",
        "A173": "empregado qualificado/funcionário público",
        "A174": "gestão/trabalhador autônomo/funcionário altamente qualificado/funcionário"
    },
    'telefone' : {
           "A191": "nenhum",
            "A192": "sim, registrado em nome do cliente" 
    },
    'Trabalhador estrangeiro' : {
            "A201": "sim",
            "A202": "não"
    }    
}

for key in colunas.keys():
    if key in need_replace.keys() :
        pass