# Busca A* (A-Star Search) - Solução Ótima para o Mapa da Romênia

Este repositório contém a implementação do algoritmo de **Busca $A^*$**, utilizando o cenário clássico do problema do Mapa da Romênia baseado no livro *Inteligência Artificial: Uma Abordagem Moderna* (Russell & Norvig).

---

## Para que serve a Busca A*?

A Busca A* é um dos algoritmos de busca informada mais populares e eficientes da computação. Ela serve para encontrar o **caminho mais curto possível (solução ótima)** entre um ponto inicial e um objetivo dentro de um grafo ou mapa.

Diferente da Busca Gulosa — que é "apressada" e escolhe caminhos baseando-se apenas no que parece mais perto no momento —, o $A^*$ é um algoritmo equilibrado e inteligente. Ele toma decisões avaliando tanto o **passado** (o custo real do caminho que ele já percorreu) quanto o **futuro** (a estimativa de quanto falta para chegar ao destino).

Para alcançar essa eficiência perfeita, sua função de avaliação matemática é definida como:
$$f(n) = g(n) + h(n)$$

* **$g(n)$:** O custo real do caminho percorrido do início até o nó atual (distância real em km das estradas).
* **$h(n)$:** A **heurística**, que representa a distância estimada em linha reta do nó atual até o objetivo final (**Bucharest**).



Ao somar esses dois valores, o $A^*$ garante que não vai entrar em estradas longas e sinuosas que pareciam boas apenas "em linha reta".

---

## Explicação Detalhada do Código

O código no arquivo `busca_a_estrela.py` está estruturado de forma organizada em três blocos principais:

### 1. Modelagem do Ambiente (Estruturas de Dados)
O programa prepara os dados geográficos da simulação:
* `mapa_romenia`: Um dicionário que representa as estradas do mundo real. Cada cidade mapeia suas vizinhas junto com a distância exata em quilômetros ($g(n)$).
* `heuristica_bucareste`: Um dicionário contendo as distâncias em linha reta até Bucharest ($h(n)$), simulando os dados obtidos por um GPS ou satélite.

### 2. A Função Principal `busca_a_estrela`
A função processa a lógica inteligente de navegação recebendo as cidades de `inicio` e `objetivo`, o `grafo` e a `heuristica`.

* **A Fronteira Avançada:** É iniciada como uma lista contendo a cidade de origem organizada em uma tupla estruturada:
    ```python
    fronteira = [(heuristica[inicio], 0, inicio, [inicio])]
    # Estrutura: (valor_f, custo_g, cidade_atual, caminho_ate_aqui)
    ```
* **A Ordenação Ótima:** Dentro do laço principal `while`, a fronteira é ordenada constantemente:
    ```python
    fronteira.sort(key=lambda x: x[0])
    ```
    Como a posição `x[0]` agora armazena o valor total de $f(n)$ (e não apenas o $h(n)$), o método `.pop(0)` sempre retira o nó que oferece a **menor projeção de custo global**.
* **Evitando Loops e Redundâncias:** O conjunto `visitados = set()` registra as cidades cuja melhor rota já foi totalmente processada, bloqueando re-explorações desnecessárias.
* **Cálculo da Equação $f = g + h$:** Ao analisar os caminhos vizinhos, o código executa o cálculo matemático chave:
    ```python
    novo_g = g_atual + custo_estrada
    novo_f = novo_g + heuristica[vizinho]
    ```
    Isso calcula o custo real acumulado até o vizinho (`novo_g`) e soma com a distância projetada em linha reta (`heuristica[vizinho]`), adicionando o resultado atualizado na fronteira.

### 3. Bloco de Execução (`if __name__ == '__main__':`)
É a porta de entrada que executa o teste prático ligando **Arad** a **Bucharest** e exibe os passos do algoritmo e o resultado final de forma limpa no terminal.

---

## O Sucesso da Solução Ótima

Diferente da Busca Gulosa (que falhou ao escolher o caminho de 450 km por Fagaras), a Busca $A^*$ analisa os custos globais com paciência e encontra o **caminho perfeito**:

`Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest`

* **Custo Real Total:** **418 km**

O código prova na prática que, ao equilibrar o custo real das decisões passadas ($g$) com a intuição heurística do futuro ($h$), o $A^*$ alcança a completude e a otimalidade no planejamento de trajetos.
