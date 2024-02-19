
# BIM Pathfinding

## Descrição do Projeto

Este projeto implementa uma solução para identificar a viabilidade de deslocamento de um equipamento em um ambiente de projeto BIM (Building Information Modeling). A implementação utiliza uma aplicação de visualização de imagens com a capacidade de analisar uma imagem bitmap 2D. A abordagem adotada baseia-se na teoria dos grafos, onde cada pixel na imagem representa um nó, e arestas são estabelecidas entre pixels vizinhos.

O propósito principal da aplicação é encontrar um caminho apropriado a partir de um pixel vermelho, indicando a posição atual do equipamento, até uma área verde que representa a zona de manutenção desejada. A aplicação permite aos usuários fazer o upload de uma imagem bitmap, visualizá-la na interface e, em seguida, utilizar o algoritmo de Busca em Largura (BFS) para caminhos para identificar e exibir a sequência de passos necessários para o deslocamento.

## Objetivos do Projeto

1. **Leitura e Manipulação de Dados**: Desenvolver habilidades na leitura e manipulação de dados provenientes de imagens bitmap que representam projetos BIM.

2. **Reforço em Estruturas de Dados em Grafos**: Aplicar e reforçar conhecimentos em estruturas de dados relacionadas a grafos para modelar eficientemente as relações entre diferentes pontos no ambiente 3D.

3. **Aplicação Prática dos Conhecimentos**: Utilizar algoritmos de grafos para resolver problemas práticos relacionados ao deslocamento de equipamentos.
## Estrutura do Código

- `main.py`: Contém o código principal para interação com o usuário.
- `graph.py`: Implementação da estrutura de grafo, algoritmo de busca em largura e manipulação de imagem.
- `load_image.py`: Função para carregar uma imagem.
- `draw_path.py`: Função para desenhar o caminho encontrado na imagem.
## Tecnologias Utilizadas

- Python 3
- Tkinter
- Pillow (PIL)
- Numpy
## Execução do Projeto

1. **Instalação de Dependências**:  
   Certifique-se de ter o Python 3 instalado em seu ambiente. Execute o seguinte comando no terminal para instalar as dependências necessárias:
   
   `pip install Pillow`

2. **Execução do Programa**:  
   Execute o programa principal usando o seguinte comando no terminal:
   
   `python main.py`.

3. **Carregar Imagens**:  
   No programa aberto, clique no botão "Carregar Imagens" para selecionar os arquivos bitmap (.bmp) que representam os diferentes andares do projeto. Os arquivos bitmap estão localizados na pasta `Datasets`.

   <div align="center">
     <img src="https://github.com/JuBinLuB/Teoria-dos-Grafos/assets/110267649/73b9b1ed-7619-4447-a87d-6ccdc82f1f2b" alt="Imagem1" width="400">
   </div>

4. **Exibir Caminho Otimizado**:  
   Após o carregamento das imagens, clique no botão "Exibir Caminho" para calcular e apresentar o caminho otimizado para o deslocamento de equipamentos em ambientes 2D e 3D.

   <p align="center">
      <img src="https://github.com/JuBinLuB/Teoria-dos-Grafos/assets/110267649/0881ab9c-2c6b-44b0-a2e7-1ba11cc6d8c6" alt="Imagem1" width="200">
      <img src="https://github.com/JuBinLuB/Teoria-dos-Grafos/assets/110267649/42b5aa28-1f15-4a9f-b909-66afb19f1a6d" alt="Imagem2" width="200">
   </p>

## Contribuidores

Este projeto foi concebido e desenvolvido pelos seguintes contribuidores:

- [Alexssander Fernandes Cândido](https://github.com/JuBinLuB)
- [Gabriel Henrique](https://github.com/gabrielhs33)
