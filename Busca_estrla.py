# =============================================================================
# ESTRUTURAS DE DADOS: O MAPA DA ROMÊNIA (RUSSELL & NORVIG)
# =============================================================================

# Grafo representando as conexões reais entre as cidades e o custo das estradas
mapa_romenia = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

# Heurística h(n): Distância estimada em linha reta de cada cidade até Bucharest
heuristica_bucareste = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
    'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
    'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
    'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}

# =============================================================================
# ALGORITMO DE BUSCA A* (A-ESTRELA)
# =============================================================================

def busca_a_estrela(inicio, objetivo, grafo, heuristica):
    # A fronteira armazena tuplas completas: (valor_f, custo_g, cidade_atual, caminho_ate_aqui)
    # Inicialização: f(n) = g(n) + h(n) -> f(n) = 0 + heuristica[inicio]
    fronteira = [(heuristica[inicio], 0, inicio, [inicio])]
    
    # Conjunto para registrar nós já expandidos (garante a otimalidade e evita loops)
    visitados = set()
    
    print(f"--- Iniciando Busca A* de {inicio} para {objetivo} ---")
    
    while fronteira:
        # ORDENAÇÃO ÓTIMA: Ordena com base no f(n) = g(n) + h(n) (posição x[0])
        fronteira.sort(key=lambda x: x[0])
        
        # Remove o nó com o menor custo total estimado f(n)
        f_atual, g_atual, cidade_atual, caminho = fronteira.pop(0)
        
        print(f"Expandindo: {cidade_atual:15} | g(n) = {g_atual:3} | h(n) = {(f_atual - g_atual):3} -> f(n) = {f_atual}")
        
        # Teste de Objetivo: Feito apenas no momento da expansão para garantir o menor custo
        if cidade_atual == objetivo:
            return caminho, g_atual
            
        if cidade_atual not in visitados:
            visitados.add(cidade_atual)
            
            # Explora as cidades vizinhas na estrutura do grafo
            for vizinho, custo_estrada in grafo.get(cidade_atual, []):
                if vizinho not in visitados:
                    # g(n) do vizinho = g acumulado até agora + custo real da nova estrada
                    novo_g = g_atual + custo_estrada
                    # f(n) do vizinho = novo g(n) + heurística h(n) do vizinho
                    novo_f = novo_g + heuristica[vizinho]
                    
                    novo_caminho = caminho + [vizinho]
                    
                    # Insere na fronteira priorizando o custo global projetado
                    fronteira.append((novo_f, novo_g, vizinho, novo_caminho))
                    
    return None, float('inf')

# =============================================================================
# EXECUÇÃO DO TESTE
# =============================================================================

if _name_ == '_main_':
    caminho_final, custo_total = busca_a_estrela('Arad', 'Bucharest', mapa_romenia, heuristica_bucareste)
    
    print("\n--- RESULTADO DA BUSCA A* ---")
    if caminho_final:
        print("Caminho Ótimo Encontrado: ", " -> ".join(caminho_final))
        print(f"Custo Real Total da Viagem: {custo_total} km")
    else:
        print("Não foi possível encontrar um caminho até o objetivo.")
    