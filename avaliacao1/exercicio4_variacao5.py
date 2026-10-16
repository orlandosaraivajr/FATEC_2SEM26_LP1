# Variação 5 - Tuplas, listas, dicionários e conjuntos
#
# Faça um programa para cadastrar os imóveis de um loteamento. Para cada imóvel,
# leia a inscrição imobiliária, o bairro e o valor venal. O cadastro termina
# quando for digitada a inscrição "FIM".
#
# Regras:
#   - as faixas do IPTU (exercício 4) ficam em uma TUPLA de tuplas;
#   - cada imóvel é um DICIONÁRIO com as chaves "inscricao", "bairro",
#     "valor" e "iptu", e todos os imóveis ficam em uma LISTA;
#   - use um CONJUNTO para impedir inscrições repetidas
#     (se repetir, avise e ignore o imóvel);
#   - use um CONJUNTO para obter os bairros distintos cadastrados.
#
# Ao final, exiba:
#   a) a lista de imóveis com seus IPTUs;
#   b) os bairros cadastrados, em ordem alfabética;
#   c) o total de IPTU por bairro (use um dicionário bairro -> total);
#   d) o bairro com maior arrecadação.

FAIXAS = (
    (100000.00, 0.0, 0.00),
    (250000.00, 0.005, 500.00),
    (500000.00, 0.01, 1750.00),
    (1000000.00, 0.015, 4250.00),
    (float("inf"), 0.02, 9250.00),
)

imoveis = []
inscricoes = set()

inscricao = input("Inscrição imobiliária (FIM para encerrar): ").strip()
while inscricao.upper() != "FIM":
    if inscricao in inscricoes:
        print("Inscrição já cadastrada. Imóvel ignorado.")
    else:
        bairro = input("Bairro: ").strip()
        valor_venal = float(input("Valor venal: R$ "))
        for limite, aliquota, parcela in FAIXAS:
            if valor_venal <= limite:
                break
        imovel = {
            "inscricao": inscricao,
            "bairro": bairro,
            "valor": valor_venal,
            "iptu": round(valor_venal * aliquota - parcela, 2),
        }
        imoveis.append(imovel)
        inscricoes.add(inscricao)
    inscricao = input("Inscrição imobiliária (FIM para encerrar): ").strip()

if len(imoveis) == 0:
    print("Nenhum imóvel cadastrado.")
else:
    print("\nImóveis cadastrados:")
    for imovel in imoveis:
        print(imovel["inscricao"] + " | " + imovel["bairro"] +
              " | valor R$ " + str(imovel["valor"]) + " | IPTU R$ " + str(imovel["iptu"]))

    bairros = set()
    for imovel in imoveis:
        bairros.add(imovel["bairro"])
    print("\nBairros cadastrados: " + ", ".join(sorted(bairros)))

    total_por_bairro = {}
    for imovel in imoveis:
        bairro = imovel["bairro"]
        total_por_bairro[bairro] = total_por_bairro.get(bairro, 0) + imovel["iptu"]

    print("\nTotal de IPTU por bairro:")
    for bairro in sorted(total_por_bairro):
        print(bairro + ": R$ " + str(round(total_por_bairro[bairro], 2)))

    maior = max(total_por_bairro, key=total_por_bairro.get)
    print("\nBairro com maior arrecadação: " + maior +
          " (R$ " + str(round(total_por_bairro[maior], 2)) + ")")
