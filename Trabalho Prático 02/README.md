
# BIM Pathfinding 3D


## Descrição do Projeto

Este projeto, desenvolvido como parte do Trabalho Prático II da disciplina de Teoria dos Grafos (CSI466), tem como objetivo estender o Trabalho Prático I, aproximando-o do problema real de deslocamento de equipamentos em ambientes 3D. Este projeto consiste em uma aplicação de busca de caminhos em ambientes 3D, utilizando algoritmos de grafos. A principal finalidade é otimizar o deslocamento de equipamentos em projetos BIM (Building Information Modeling), levando em consideração múltiplas áreas de laydown, evitando obstáculos e possibilitando deslocamentos verticais entre diferentes andares.
## Objetivos do Projeto

1. **Leitura e Manipulação de Dados**: Desenvolver habilidades na leitura e manipulação de dados provenientes de imagens bitmap que representam projetos BIM.

2. **Reforço em Estruturas de Dados em Grafos**: Aplicar e reforçar conhecimentos em estruturas de dados relacionadas a grafos para modelar eficientemente as relações entre diferentes pontos no ambiente 3D.

3. **Aplicação Prática dos Conhecimentos**: Utilizar algoritmos de grafos para resolver problemas práticos relacionados ao deslocamento de equipamentos.
## Requisitos Adicionais do Trabalho

Além dos requisitos estabelecidos no Trabalho Prático I, o Trabalho Prático II incorpora as seguintes considerações:

- **Múltiplas Áreas de Laydown**: O programa deve calcular o melhor deslocamento do equipamento para qualquer uma das áreas de laydown disponíveis.

- **Evitar Obstáculos**: O deslocamento deve evitar passar próximo de objetos de colisão, promovendo maior segurança operacional. As conexões para nós mais próximos aos obstáculos devem ter um peso maior, favorecendo rotas alternativas.

- **Deslocamento 3D**: O algoritmo deve contemplar o deslocamento vertical, permitindo que o objeto se mova não apenas nas direções tradicionais, mas também para cima e para baixo entre diferentes andares.

- **Geometria do Objeto (Extra)**: O objeto a ser deslocado pode ocupar mais de um pixel na imagem, representando sua geometria real. Considerações especiais devem ser feitas para garantir que todo o corpo do objeto possa passar sem conflitos durante o deslocamento.
## Estrutura do Projeto

O projeto está organizado em diversos módulos para facilitar a manutenção e a compreensão do código. A estrutura do projeto é a seguinte:

- `main.py`: Arquivo principal para interação com o usuário e execução do programa.
- `interface.py`: Módulo contendo a classe ImageViewer responsável por criar a interface gráfica usando Tkinter.
- `graph.py`: Implementação da estrutura de grafo e algoritmos relacionados.
- `draw_path.py`: Função para desenhar o caminho na imagem.
- `load_image.py`: Função para carregar imagens utilizando a biblioteca Pillow.
- `colors.py`: Módulo contendo uma classe simples para representar cores.

## Tecnologias Utilizadas
- Linguagem: Python
- Biblioteca para Manipulação de Imagens: PIL (Pillow)
- Interface Gráfica: Tkinter
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
     <img src="https://github.com/JuBinLuB/Teoria-dos-Grafos/assets/110267649/6dc71e20-c90c-4d09-ae17-8bfa862f4ff9" alt="Imagem1" width="400">
   </div>

5. **Exibir Caminho Otimizado**:  
   Após o carregamento das imagens, clique no botão "Exibir Caminho" para calcular e apresentar o caminho otimizado para o deslocamento de equipamentos em ambientes 2D e 3D.

   <p align="center">
      <img src="https://github.com/JuBinLuB/Teoria-dos-Grafos/assets/110267649/681244c3-280a-44a5-9f6e-28d37a52c294" alt="Imagem1" width="200">
      <img src="https://github.com/JuBinLuB/Teoria-dos-Grafos/assets/110267649/dea3c122-aa5f-420a-aa0a-8351e3b58b1b" alt="Imagem2" width="200">
   </p>
## Melhorias Futuras

- **Geometria do Objeto**: O objeto a ser deslocado pode ocupar mais de um pixel na imagem, representando sua geometria real. Considerações especiais devem ser feitas para garantir que todo o corpo do objeto possa passar sem conflitos durante o deslocamento.

- **Melhor Visualização das Imagens**: A interface gráfica pode ser aprimorada para proporcionar uma melhor visualização das imagens. Isso inclui ajustes na escala e disposição das imagens para uma experiência mais intuitiva.

## Contribuidores

Agradecemos a todas as pessoas que contribuíram para este projeto. Este projeto foi concebido e desenvolvido pelos seguintes contribuidores:

- [Alexssander Fernandes Cândido](https://github.com/JuBinLuB)
- [Gabriel Henrique](https://github.com/gabrielhs33)



