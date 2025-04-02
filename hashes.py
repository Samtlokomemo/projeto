def hashPerfeito():
  def hashing_perfeito(chaves, tamanho_tabela):
    tabela = [None] * tamanho_tabela
    for chave in chaves:
        indice = chave % tamanho_tabela
        tabela[indice] = chave
    return tabela
  
  chaves = [1, 10, 20, 30, 40]
  tamanho_tabela = len(chaves)
  tabela_hash = hashing_perfeito(chaves, tamanho_tabela)
  print(tabela_hash)
  
def hashUniversal():
  import random
  
  def funcao_hash_universal(a, b, p, tamanho_tabela):
      def hash_func(chave):
          return ((a * chave + b) % p) % tamanho_tabela
      return hash_func
  
  def hashing_universal(chaves, tamanho_tabela):
      p = 101  # Um número primo maior que o número de chaves
      a = random.randint(1, p - 1)
      b = random.randint(0, p - 1)
      hash_func = funcao_hash_universal(a, b, p, tamanho_tabela)
      tabela = [[] for _ in range(tamanho_tabela)]
      for chave in chaves:
          indice = hash_func(chave)
          tabela[indice].append(chave)
      return tabela
  
    chaves = [1, 10, 20, 30, 40, 50, 60]
    tamanho_tabela = 10
    tabela_hash = hashing_universal(chaves, tamanho_tabela)
    print(tabela_hash)
def hashEncadeado():
  def hashing_encadeamento(chaves, tamanho_tabela):
    tabela = [[] for _ in range(tamanho_tabela)]
    for chave in chaves:
        indice = chave % tamanho_tabela
        tabela[indice].append(chave)
    return tabela
    
def hashSondagem():
  def hashing_sondagem_linear(chaves, tamanho_tabela):
    tabela = [None] * tamanho_tabela
    for chave in chaves:
        indice = chave % tamanho_tabela
        while tabela[indice] is not None:
            indice = (indice + 1) % tamanho_tabela
        tabela[indice] = chave
    return tabela
def hashDupla():
  def hashing_dupla_hash(chaves, tamanho_tabela):
    tabela = [None] * tamanho_tabela
    for chave in chaves:
        indice1 = chave % tamanho_tabela
        indice2 = 1 + (chave % (tamanho_tabela - 1))
        indice = indice1
        i = 0
        while tabela[indice] is not None:
            indice = (indice1 + i * indice2) % tamanho_tabela
            i += 1
        tabela[indice] = chave
    return tabela

import matplotlib.pyplot as plt

def visualizar_tabela_hash(tabela_hash):
    plt.bar(range(len(tabela_hash)), [len(lista) if isinstance(lista, list) else 1 for lista in tabela_hash])
    plt.xlabel('Índice da Tabela Hash')
    plt.ylabel('Número de Chaves')
    plt.title('Distribuição de Chaves na Tabela Hash')
    plt.show()

chaves = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90]
tamanho_tabela = 10

tabela_perfeita = hashing_perfeito(chaves[:5], 5)
tabela_universal = hashing_universal(chaves, tamanho_tabela)
tabela_encadeamento = hashing_encadeamento(chaves, tamanho_tabela)
tabela_sondagem_linear = hashing_sondagem_linear(chaves, tamanho_tabela)
tabela_dupla_hash = hashing_dupla_hash(chaves, tamanho_tabela)

print("Hashing Perfeito:", tabela_perfeita)
print("Hashing Universal:", tabela_universal)
print("Hashing Encadeamento:", tabela_encadeamento)
print("Hashing Sondagem Linear:", tabela_sondagem_linear)
print("Hashing Dupla Hash:", tabela_dupla_hash)

visualizar_tabela_hash(tabela_dupla_hash) #Trocar a tabela aqui
