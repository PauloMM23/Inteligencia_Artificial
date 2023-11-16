from Cromossomo import Cromossomo
from util import Util
from AG import AG

tamanho_populacao = int(input("Tamanho da população: "))
estado_final = input("Palavra desejada: ")
taxa_selecao = int(input("Taxa de seleção (entre 20 a 40%): "))
taxa_reproducao = 100 - taxa_selecao
taxa_mutacao = int(input("Taxa de mutação (entre 5 a 10%): "))
qtd_geracoes = int(input("Quantidade de gerações: "))

populacao = []
nova_populacao = []

# 1a população que é 100% aleatória
AG.gerar_populacao(populacao, tamanho_populacao, estado_final)
AG.ordenar(populacao)
print("Geração 1")
AG.exibir(populacao)

# gerações
for i in range(1, qtd_geracoes):
    # selecionar
    AG.selecionar_por_torneio(populacao, nova_populacao, taxa_selecao)  # método que TENTA selecionar os mais aptos

    # cruzar
    AG.reproduzir(populacao, nova_populacao, taxa_reproducao, estado_final)  # método que cria novos indivíduos

    # mutacao
    # definir o momento da mutacao
    if i % (len(populacao) // taxa_mutacao) == 0:
        AG.mutar(nova_populacao, estado_final)  # estado_final é passado, pq indivíduos mutados devem ter suas aptidões recalculadas

    populacao.clear()
    populacao.extend(nova_populacao)
    nova_populacao.clear()
    AG.ordenar(populacao)

    print(f"\n\nGeração {i + 1}")
    AG.exibir(populacao)
