from random import randint, choice
from util import Util
from Cromossomo import Cromossomo

class AG:
    @staticmethod
    def gerar_populacao(populacao, tamanho_populacao, estado_final):
        for _ in range(tamanho_populacao):
            populacao.append(Cromossomo(Util.gerar_palavra(len(estado_final)), estado_final))

    @staticmethod
    def ordenar(populacao):
        populacao.sort(reverse=True)

    @staticmethod
    def exibir(populacao):
        for cromossomo in populacao:
            print(f"Valor: {cromossomo.valor}, Aptidão: {cromossomo.aptidao}")

    @staticmethod
    def selecionar_por_torneio(populacao, nova_populacao, taxa_selecao):
        qtd_selecionados = taxa_selecao * len(populacao) // 100
        nova_populacao.append(populacao[0])  # elitismo
        i = 1
        while i <= qtd_selecionados:
            c1 = choice(populacao)
            c2 = choice(populacao)
            c3 = choice(populacao)
            torneio = sorted([c1, c2, c3], key=lambda x: x.aptidao, reverse=True)
            selecionado = torneio[0]
            if selecionado not in nova_populacao:
                nova_populacao.append(selecionado)
                i += 1

    @staticmethod
    def selecionar_por_roleta(populacao, nova_populacao, taxa_selecao):
        aptidao_total = sum(cromossomo.aptidao for cromossomo in populacao)
        for cromossomo in populacao:
            cromossomo.porcentagem_aptidao = cromossomo.aptidao * 100 / aptidao_total if aptidao_total > 0 else 1

        sorteio = [cromossomo for cromossomo in populacao for _ in range(int(cromossomo.porcentagem_aptidao))]
        qtd_selecionados = taxa_selecao * len(populacao) // 100
        nova_populacao.append(populacao[0])  # elitismo
        for _ in range(1, qtd_selecionados + 1):
            selecionado = choice(sorteio)
            nova_populacao.append(selecionado)
            sorteio.remove(selecionado)

    @staticmethod
    def reproduzir(populacao, nova_populacao, taxa_reproducao, estado_final):
        qtd_reproduzidos = taxa_reproducao * len(populacao) // 100
        i = 0
        while i < qtd_reproduzidos:
            pai = choice(populacao)
            mae = choice(populacao)
            s_pai = pai.valor
            s_mae = mae.valor
            s_filho1 = s_pai[:len(s_pai) // 2] + s_mae[len(s_mae) // 2:]
            s_filho2 = s_mae[:len(s_mae) // 2] + s_pai[len(s_pai) // 2:]
            nova_populacao.append(Cromossomo(s_filho1, estado_final))
            nova_populacao.append(Cromossomo(s_filho2, estado_final))
            i += 2

        while len(nova_populacao) > len(populacao):
            nova_populacao.pop()

    @staticmethod
    def mutar(populacao, estado_final):
        qtd_mutantes = randint(0, len(populacao) // 5)
        for _ in range(qtd_mutantes):
            posicao_mutante = randint(0, len(populacao) - 1)
            mutante = populacao[posicao_mutante]
            print(f"vai mutar {mutante.valor}  {mutante.aptidao}")
            valor_mutado = mutante.valor
            caracter_mutante = mutante.valor[randint(0, len(mutante.valor) - 1)]
            caracter_sorteado = choice(Util.letras)
            valor_mutado = valor_mutado.replace(caracter_mutante, caracter_sorteado)
            mutante = Cromossomo(valor_mutado, estado_final)
            populacao[posicao_mutante] = mutante

