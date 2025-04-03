#IMPORTS
import numpy as np
import random
import matplotlib.pyplot as plt

# Tabela Hash Perfeita
def hashingPerfeitoProgram():
  def hashing_perfeito(chaves):
      hash_map = {1: 0, 10: 1, 20: 2, 30: 3, 40: 4}  # Mapeamento manual
      tabela = [None] * len(chaves)
      for chave in chaves:
          tabela[hash_map[chave]] = chave
      return tabela

  def plot_hash_table(tabela, titulo):
      indices = range(len(tabela))
      valores = [1 if chave is not None else 0 for chave in tabela]  # Binário: 1 se ocupado, 0 se vazio

      plt.figure(figsize=(10, 5))
      plt.bar(indices, valores, color='skyblue')
      plt.xlabel('Índice da Tabela Hash')
      plt.ylabel('Ocupação (1 = Chave Presente)')
      plt.title(titulo)
      plt.xticks(indices)
      plt.yticks([0, 1])
      plt.grid(axis='y', linestyle='--', alpha=0.7)

      # Adicionar rótulos das chaves
      for i, chave in enumerate(tabela):
          if chave is not None:
              plt.text(i, 0.5, str(chave), ha='center', va='center', fontweight='bold')

      plt.show()

  # Dados
  chaves = [1, 10, 20, 30, 40]
  tamanho_tabela = len(chaves)

  # Gerar tabelas
  tabela_perfeita = hashing_perfeito(chaves)

  # Plotar
  plot_hash_table(tabela_perfeita, "Tabela Hash Perfeita")

def hashingUniversalProgram():
  def is_prime(n):
      """Verifica se um número é primo."""
      if n <= 1:
          return False
      for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
              return False
      return True

  def next_prime(n):
      """Retorna o próximo primo após n."""
      while True:
          n += 1
          if is_prime(n):
              return n

  def universal_hash(k, a, b, p, m):
      """Função de hash universal para inteiros."""
      return ((a * k + b) % p) % m

  def generate_perfect_hash(chaves):
      """Gera uma função de hash perfeita para as chaves."""
      p = next_prime(max(chaves))  # Primo > maior chave
      m = len(chaves)  # Tamanho da tabela (pode ser ajustado)

      # Testa combinações de a e b até encontrar uma função sem colisões
      max_attempts = 1000
      for _ in range(max_attempts):
          a = random.randint(1, p-1)
          b = random.randint(0, p-1)
          hash_table = [None] * m
          collision = False

          for k in chaves:
              index = universal_hash(k, a, b, p, m)
              if hash_table[index] is not None:
                  collision = True
                  break
              hash_table[index] = k

          if not collision:
              print(f"Parâmetros encontrados: a={a}, b={b}, p={p}, m={m}")
              return hash_table, (a, b, p, m)

      raise ValueError("Não foi possível gerar um hash perfeito após várias tentativas.")

  def plot_hash_table(tabela, titulo):
      """Visualiza a tabela hash."""
      indices = range(len(tabela))
      ocupacao = [1 if chave is not None else 0 for chave in tabela]

      plt.figure(figsize=(10, 5))
      plt.bar(indices, ocupacao, color='lightgreen')
      plt.xlabel('Índice da Tabela Hash')
      plt.ylabel('Ocupação (1 = Chave Presente)')
      plt.title(titulo)
      plt.xticks(indices)
      plt.yticks([0, 1])
      plt.grid(axis='y', linestyle='--', alpha=0.7)

      for i, chave in enumerate(tabela):
          if chave is not None:
              plt.text(i, 0.5, str(chave), ha='center', va='center', fontweight='bold')

      plt.show()

  # Exemplo de uso
  chaves = [1, 10, 20, 30, 40, 99, 123]
  tabela_perfeita, params = generate_perfect_hash(chaves)
  print("Tabela hash perfeita:", tabela_perfeita)
  print("Parâmetros (a, b, p, m):", params)

  plot_hash_table(tabela_perfeita, "Tabela Hash Perfeita Universal (Implementação Manual)")

def hashingEncadeadoProgram():
  #Mostra o número de colisões por índice
  class No:
      """Nó para lista encadeada."""
      def __init__(self, chave, valor):
          self.chave = chave
          self.valor = valor
          self.proximo = None

  class TabelaHashEncadeamento:
      def __init__(self, tamanho):
          self.tamanho = tamanho
          self.tabela = [None] * tamanho  # Cada posição armazena a cabeça de uma lista encadeada

      def hash(self, chave):
          """Função de hash simples (resto da divisão)."""
          return chave % self.tamanho

      def inserir(self, chave, valor):
          """Insere um par chave-valor na tabela."""
          indice = self.hash(chave)
          no = No(chave, valor)

          if self.tabela[indice] is None:
              self.tabela[indice] = no  # Primeiro nó na lista
          else:
              # Adiciona no final da lista encadeada
              atual = self.tabela[indice]
              while atual.proximo is not None:
                  atual = atual.proximo
              atual.proximo = no

      def buscar(self, chave):
          """Busca um valor pela chave."""
          indice = self.hash(chave)
          atual = self.tabela[indice]

          while atual is not None:
              if atual.chave == chave:
                  return atual.valor
              atual = atual.proximo
          return None  # Chave não encontrada

      def visualizar(self):
          """Mostra a tabela hash com listas encadeadas."""
          for i in range(self.tamanho):
              print(f"[{i}]", end=" ")
              atual = self.tabela[i]
              while atual is not None:
                  print(f"→ ({atual.chave}: {atual.valor})", end=" ")
                  atual = atual.proximo
              print()

  # Exemplo de uso
  tabela = TabelaHashEncadeamento(tamanho=3) #Divide a chave por isso, e retorna o resto da divisão como índice
  tabela.inserir(10, "A")
  tabela.inserir(20, "B")
  tabela.inserir(15, "C")  # Colide com 20 (ambos têm hash 0)
  tabela.inserir(30, "D")

  #Testes
  #tabela.inserir(12345678900, "João")  # Hash = 3
  #tabela.inserir(98765432100, "Maria") # Hash = 3 → Colisão!


  print("Tabela Hash com Encadeamento:")
  tabela.visualizar()

  print("\nBusca:")
  print("chave=20 ->", tabela.buscar(20))  # Saída: "B"
  print("chave=15 ->", tabela.buscar(15))  # Saída: "C"
  #print("O cpf buscado é de -> "tabela.buscar(12345678900))

  import matplotlib.pyplot as plt

  def plot_encadeamento(tabela):
      fig, ax = plt.subplots(figsize=(10, 5))
      ax.set_title("Tabela Hash com Encadeamento")
      ax.set_xlabel("Índice")
      ax.set_ylabel("Número de Colisões")

      indices = range(tabela.tamanho)
      colisoes = [0] * tabela.tamanho

      for i in indices:
          atual = tabela.tabela[i]
          contador = 0
          while atual is not None:
              contador += 1
              atual = atual.proximo
          colisoes[i] = contador

      bars = ax.bar(indices, colisoes, color='skyblue')

      # Adiciona rótulos
      for bar in bars:
          height = bar.get_height()
          ax.text(bar.get_x() + bar.get_width()/2., height,
                  f'{int(height)}', ha='center', va='bottom')

      plt.xticks(indices)
      plt.grid(axis='y', linestyle='--', alpha=0.7)
      plt.show()

  plot_encadeamento(tabela)

def hashingSondagemProgram():
  class TabelaHashSondagemLinear:
      def __init__(self, tamanho):
          self.tamanho = tamanho
          self.tabela = [None] * tamanho  # None = vazio, "DELETADO" = removido

      def hash(self, chave):
          """Função de hash básica para inteiros."""
          return chave % self.tamanho

      def inserir(self, chave, valor):
          """Insere um par chave-valor usando sondagem linear."""
          indice = self.hash(chave)

          for i in range(self.tamanho):
              novo_indice = (indice + i) % self.tamanho  # Sondagem circular
              if self.tabela[novo_indice] is None or self.tabela[novo_indice] == "DELETADO":
                  self.tabela[novo_indice] = (chave, valor)
                  return
          raise Exception("Tabela hash cheia!")

      def buscar(self, chave):
          """Busca um valor pela chave."""
          indice = self.hash(chave)

          for i in range(self.tamanho):
              novo_indice = (indice + i) % self.tamanho
              entrada = self.tabela[novo_indice]

              if entrada is None:
                  return None  # Chave não encontrada
              elif entrada != "DELETADO" and entrada[0] == chave:
                  return entrada[1]  # Retorna o valor
          return None

      def remover(self, chave):
          """Remove uma chave da tabela (marca como 'DELETADO')."""
          indice = self.hash(chave)

          for i in range(self.tamanho):
              novo_indice = (indice + i) % self.tamanho
              entrada = self.tabela[novo_indice]

              if entrada is None:
                  return  # Chave não existe
              elif entrada != "DELETADO" and entrada[0] == chave:
                  self.tabela[novo_indice] = "DELETADO"
                  return

      def visualizar(self):
          """Mostra a tabela hash."""
          for i in range(self.tamanho):
              print(f"[{i}]", end=" ")
              if self.tabela[i] is None:
                  print("Vazio")
              elif self.tabela[i] == "DELETADO":
                  print("DELETADO")
              else:
                  print(f"{self.tabela[i][0]}: {self.tabela[i][1]}")

  def plot_tabela_hash(tabela):
      """Plotagem visual da tabela hash com sondagem linear."""
      indices = np.arange(tabela.tamanho)
      valores = []
      cores = []

      for entrada in tabela.tabela:
          if entrada is None:
              valores.append(0)  # Vazio
              cores.append('white')
          elif entrada == "DELETADO":
              valores.append(1)  # Removido
              cores.append('red')
          else:
              valores.append(2)  # Ocupado
              cores.append('lightgreen')

      fig, ax = plt.subplots(figsize=(10, 6))
      barras = ax.bar(indices, valores, color=cores, edgecolor='black')

      # Customização do gráfico
      ax.set_title("Tabela Hash com Sondagem Linear", pad=20)
      ax.set_xlabel("Índice da Tabela")
      ax.set_ylabel("Estado")
      ax.set_yticks([0, 1, 2])
      ax.set_yticklabels(["Vazio", "DELETADO", "Ocupado"])
      ax.set_xticks(indices)

      # Adiciona rótulos com chaves/valores
      for i, entrada in enumerate(tabela.tabela):
          if entrada not in [None, "DELETADO"]:
              ax.text(i, 1.5, f"{entrada[0]}: {entrada[1]}", ha='center', fontweight='bold')

      plt.grid(axis='y', linestyle='--', alpha=0.7)
      plt.show()

  # Exemplo de uso
  tabela = TabelaHashSondagemLinear(tamanho=7)
  tabela.inserir(10, "João")
  tabela.inserir(20, "Maria")
  tabela.inserir(15, "Carlos")  # Colide e usa sondagem
  tabela.remover(20)  # Remove Maria

  plot_tabela_hash(tabela)

def hashingDuploProgram():
  class TabelaHashDuploHash:
      def __init__(self, tamanho):
          self.tamanho = tamanho
          self.tabela = [None] * tamanho
          self.primo = self._encontrar_primo_menor(tamanho - 1)  # Primo < tamanho

      def _encontrar_primo_menor(self, n):
          """Encontra o maior número primo menor que n."""
          if n <= 1:
              return 2
          for num in range(n, 1, -1):
              if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
                  return num
          return 2

      def h1(self, chave):
          """Primeira função de hash."""
          return chave % self.tamanho

      def h2(self, chave):
          """Segunda função de hash (deve retornar um valor coprimo com self.tamanho)."""
          return self.primo - (chave % self.primo)

      def inserir(self, chave, valor):
          """Insere um par chave-valor usando duplo hash."""
          indice = self.h1(chave)
          passo = self.h2(chave)

          for i in range(self.tamanho):
              novo_indice = (indice + i * passo) % self.tamanho
              if self.tabela[novo_indice] is None or self.tabela[novo_indice] == "DELETADO":
                  self.tabela[novo_indice] = (chave, valor)
                  return
          raise Exception("Tabela cheia!")

      def buscar(self, chave):
          """Busca um valor pela chave."""
          indice = self.h1(chave)
          passo = self.h2(chave)

          for i in range(self.tamanho):
              novo_indice = (indice + i * passo) % self.tamanho
              entrada = self.tabela[novo_indice]

              if entrada is None:
                  return None  # Chave não encontrada
              elif entrada != "DELETADO" and entrada[0] == chave:
                  return entrada[1]  # Retorna o valor
          return None

      def remover(self, chave):
          """Remove uma chave da tabela (marca como 'DELETADO')."""
          indice = self.h1(chave)
          passo = self.h2(chave)

          for i in range(self.tamanho):
              novo_indice = (indice + i * passo) % self.tamanho
              entrada = self.tabela[novo_indice]

              if entrada is None:
                  return  # Chave não existe
              elif entrada != "DELETADO" and entrada[0] == chave:
                  self.tabela[novo_indice] = "DELETADO"
                  return

      def visualizar(self):
          """Mostra a tabela hash."""
          for i in range(self.tamanho):
              print(f"[{i}]", end=" ")
              if self.tabela[i] is None:
                  print("Vazio")
              elif self.tabela[i] == "DELETADO":
                  print("DELETADO")
              else:
                  print(f"{self.tabela[i][0]}: {self.tabela[i][1]}")
  def plot_tabela_hash(tabela):
    """Plotagem visual da tabela hash com duplo hash."""
    indices = np.arange(tabela.tamanho)
    estados = []
    cores = []

    for entrada in tabela.tabela:
        if entrada is None:
            estados.append(0)  # Vazio
            cores.append('white')
        elif entrada == "DELETADO":
            estados.append(1)  # Removido
            cores.append('red')
        else:
            estados.append(2)  # Ocupado
            cores.append('lightgreen')

    fig, ax = plt.subplots(figsize=(12, 6))
    barras = ax.bar(indices, estados, color=cores, edgecolor='black', width=0.8)

    # Customização
    ax.set_title("Tabela Hash com Duplo Hash", pad=20, fontsize=14)
    ax.set_xlabel("Índice da Tabela", fontsize=12)
    ax.set_ylabel("Estado", fontsize=12)
    ax.set_yticks([0, 1, 2])
    ax.set_yticklabels(["Vazio", "DELETADO", "Ocupado"])
    ax.set_xticks(indices)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Adiciona rótulos com chaves/valores
    for i, entrada in enumerate(tabela.tabela):
        if entrada not in [None, "DELETADO"]:
            ax.text(i, 1.5, f"{entrada[0]}: {entrada[1]}",
                   ha='center', fontweight='bold', fontsize=10)

    # Destaque para colisões resolvidas
    for i in range(1, tabela.tamanho):
        if tabela.tabela[i] not in [None, "DELETADO"]:
            h1 = tabela.h1(tabela.tabela[i][0])
            if h1 != i:  # Se houve sondagem
                ax.text(i, 2.2, "⚡", ha='center', fontsize=14, color='orange')

    plt.tight_layout()
    plt.show()

  # Exemplo de uso
  tabela = TabelaHashDuploHash(tamanho=7)
  tabela.inserir(10, "João")
  tabela.inserir(20, "Maria")
  tabela.inserir(15, "Carlos")  # Colisão resolvida com duplo hash
  tabela.remover(20)

  plot_tabela_hash(tabela)

  print("=== Tabela Hash com Duplo Hash ===")
  tabela.visualizar()

  print("\nBusca:")
  print("chave=15 ->", tabela.buscar(15))  # Saída: "Carlos"

  print("\nRemovendo chave=20...")
  tabela.remover(20)
  tabela.visualizar()

#hashingPerfeitoProgram()
#hashingUniversalProgram()
#hashingEncadeadoProgram()
#hashingSondagemProgram()
#hashingDuploProgram()
