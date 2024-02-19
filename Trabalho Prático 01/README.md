
# BIM Pathfinding



## Descrição do Projeto


Este projeto implementa uma solução para identificar a viabilidade de deslocamento de um equipamento em um ambiente de projeto BIM (Building Information Modeling). A implementação utiliza uma aplicação de visualização de imagens com a capacidade de analisar uma imagem bitmap 2D. A abordagem adotada baseia-se na teoria dos grafos, onde cada pixel na imagem representa um nó, e arestas são estabelecidas entre pixels vizinhos.

O propósito principal da aplicação é encontrar um caminho apropriado a partir de um pixel vermelho, indicando a posição atual do equipamento, até uma área verde que representa a zona de manutenção desejada. A aplicação permite aos usuários fazer o upload de uma imagem bitmap, visualizá-la na interface e, em seguida, utilizar o algoritmo de Busca em Largura (BFS) para caminhos para identificar e exibir a sequência de passos necessários para o deslocamento.
## Tecnologias Utilizadas

- Python 3
- Tkinter
- Pillow (PIL)
- Numpy

## Estrutura do Código

- `main.py`: Contém o código principal para interação com o usuário.
- `graph.py`: Implementação da estrutura de grafo, algoritmo de busca em largura e manipulação de imagem.
- `load_image.py`: Função para carregar uma imagem.
- `draw_path.py`: Função para desenhar o caminho encontrado na imagem.


## Contribuidores

Este projeto foi concebido e desenvolvido pelos seguintes contribuidores:

- [Alexssander Fernandes Cândido](https://github.com/JuBinLuB)
- [Gabriel Henrique](https://github.com/gabrielhs33)
