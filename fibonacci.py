import matplotlib.pyplot as plt
import math

# --- Função Fibonacci com Memoização ---
fib_memo = {0: 0, 1: 1}
def fibonacci(n):
    if n < 0:
        return 0
    if n not in fib_memo:
        fib_memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return fib_memo[n]

# --- Função para Calcular a Largura da Subárvore ---
def calculate_subtree_width(n, depth, max_depth):
    if n <= 1 or depth >= max_depth:
        return 1
    return calculate_subtree_width(n-1, depth+1, max_depth) + calculate_subtree_width(n-2, depth+1, max_depth)

# --- Função para Desenhar a Árvore ---
def draw_fibonacci_tree(n, x, y, depth, width, vertical_spacing, max_depth, scale_factor=1.0):
    fib_val = fibonacci(n)

    # Condição de parada para nós não relevantes
    if fib_val <= 0 and n != 1:
        return

    # --- Desenho do Nó Atual ---
    base_font_size = 14
    font_size = max(base_font_size - depth * 0.8, 8) * scale_factor
    node_size = 0.15 * scale_factor

    plt.text(x, y, str(fib_val),
             ha='center', va='center',
             fontsize=font_size,
             color='black',
             fontweight='bold',
             zorder=2,
             bbox=dict(facecolor='lightgreen',
                      edgecolor='black',
                      boxstyle='circle',
                      pad=node_size))

    # --- Condição de Parada da Recursão ---
    if n > 1 and depth < max_depth:
        new_y = y - vertical_spacing * scale_factor

        # Calcula as larguras das subárvores
        left_width = calculate_subtree_width(n-1, depth+1, max_depth)
        right_width = calculate_subtree_width(n-2, depth+1, max_depth)
        total_width = left_width + right_width

        # Calcula posições baseadas nas larguras das subárvores
        left_offset = (right_width / total_width) * width
        right_offset = (left_width / total_width) * width

        new_x_left = x - left_offset/2
        new_x_right = x + right_offset/2

        # --- Filho Esquerdo (F(n-1)) ---
        fib_left = fibonacci(n - 1)
        if fib_left > 0 or (n - 1) == 1:
            plt.plot([x, new_x_left], [y, new_y], 'k-', lw=1.2*scale_factor, zorder=1)
            draw_fibonacci_tree(n - 1, new_x_left, new_y, depth + 1,
                              left_width, vertical_spacing, max_depth, scale_factor)

        # --- Filho Direito (F(n-2)) ---
        fib_right = fibonacci(n - 2)
        if fib_right > 0 or (n - 2) == 1:
            plt.plot([x, new_x_right], [y, new_y], 'k-', lw=1.2*scale_factor, zorder=1)
            draw_fibonacci_tree(n - 2, new_x_right, new_y, depth + 1,
                              right_width, vertical_spacing, max_depth, scale_factor)

# --- Configurações ---
n_inicial = 10
max_depth = 7
vertical_spacing = 2.0  # Aumentado para melhor espaçamento
scale_factor = 1.5      # Fator de escala para aumentar nós e texto

# Calcula a largura total necessária
total_width = calculate_subtree_width(n_inicial, 0, max_depth)

# Ajusta o tamanho da figura com base na largura total e profundidade
fig_width = total_width * 0.7 * scale_factor
fig_height = max_depth * 1.5 * scale_factor

plt.figure(figsize=(fig_width, fig_height))
plt.axis('off')
plt.gca().invert_yaxis()  # Faz a árvore crescer para baixo

# Limpa o cache
fib_memo = {0: 0, 1: 1}

# Desenha a árvore
draw_fibonacci_tree(n_inicial, 0, 0, 0, total_width, vertical_spacing, max_depth, scale_factor)

plt.title(f"Árvore de Fibonacci para F({n_inicial}) - Versão Final", pad=20, fontsize=14*scale_factor)
plt.gca().set_aspect('equal')
plt.tight_layout()
plt.show()
