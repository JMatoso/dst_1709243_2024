# Modelo de IA para Reconhecer Escritas à Mão Personalizadas

- 1. Descrição do Trabalho
- 2. Implementação do Trabalho
   - 2.1. Criação do Conjunto de Dados MNIST
   - 2.2. Implementação do Modelo de Inteligência Artificial
- 3. Funcionamento do Trabalho
   - 3.1. Criação do MNIST Dataset
   - 3.2. Treinamento do Modelo
- 4. Conclusão
- Bibliografia

## 1. Descrição do Trabalho

Este projeto consiste em criar um conjunto de dados MNIST contendo dígitos de 0 a 9 escritos à mão, seguido pela implementação de um modelo de inteligência artificial básico para reconhecer esses números.

## 2. Implementação do Trabalho

### 2.1. Criação do Conjunto de Dados MNIST

Isso envolve a criação de uma imagem de dígitos escritos à mão de 0 a 9 numa matriz de 10x10. Essa imagem é dividida e cada imagem gerada é então processada, sendo possível redimensioná-las para 35x35 e depois são convertidas em (.csv) um formato que pode ser usado para treinar o modelo de aprendizado de máquina

### 2.2. Implementação do Modelo de Inteligência Artificial

Uma vez que o conjunto de dados esteja pronto, um modelo de aprendizado de máquina é implementado para reconhecer os dígitos escritos à mão. O modelo é treinado no conjunto de dados MNIST e, em seguida, testado para verificar sua precisão.

## 3. Funcionamento do Trabalho

### 3.1. Criação do MNIST Dataset

Para compor o conjunto de dados do MNIST, uma matriz de 10x10 foi criada em uma folha de papel, na qual os números de 0 a 9 foram escritos à mão em suas respetivas células. Posteriormente, uma fotografia da folha foi tirada e adicionada ao projeto, servindo como parte do conjunto de dados MNIST personalizado.

![MNIST](https://github.com/JMatoso/dst_1709243_2024/blob/main/project-images/mnist.jpg?raw=true){width=100px}

O primeiro passo será a divisão da imagem, o segundo será o redimensionamento das imagens para 35x35 em blocos separando os números.

``` bash
dataset-builder
│
└── datasets
│   └── builds
│   └── images
│
└── output
│   └── final
│   └── text
│
├── _init_.py 
├── data_builder.py 
├── file_reader.py 
├── image_resizer.py 
├── image_splitter.py 
└── picture_to_numbers_converter.py 
```

O terceiro passo envolverá a conversão das imagens divididas em formato .csv, preparando-as para a construção do nosso conjunto de dados.

``` py
if __name__ == "__main__":
    split("mnist.jpg", 10, 10)
    read_files()
    load_ai(build())
```
O script foi alterado para executar todos os passos necessários para construir o dataset, eliminando a necessidade de intervenção manual.

![SplittedImages](https://github.com/JMatoso/dst_1709243_2024/blob/main/project-images/splitted-images.png?raw=true)

A conversão das imagens divididas para o formato .csv foi realizada para facilitar o processamento e a manipulação dos dados durante a construção do conjunto de dados. O formato .csv é amplamente utilizado para armazenar dados tabulares, o que o torna conveniente para representar imagens pixel a pixel. Isso permite que as informações das imagens sejam organizadas em linhas e colunas, tornando mais fácil o acesso aos dados durante a fase de pré-processamento e treinamento dos modelos de inteligência artificial.

```
O primeiro passo é adicionar a imagem do conjunto de dados MNIST na pasta images.
```

![ConvertedImages](https://github.com/JMatoso/dst_1709243_2024/blob/main/project-images/converted-images-csv.png?raw=true)

```
A seguir, alterar o método split, passando o nome da imagem e o formato. O método load_ai() será chamado no final da construção
```

``` bash
dataset-builder
│
└── datasets
│   └── builds
│       └── final_<ticks>_<filename>.<file.format>
```

```
E por fim o nosso dataset é criado.
```

![FinalDataset](https://github.com/JMatoso/dst_1709243_2024/blob/main/project-images/final-dataset.png?raw=true)

### 3.2. Treinamento do Modelo

Quando o __init__.py no simple-ai é chamado, ele executa todos os passos necessários para treinar o nosso modelo, excluindo a necessidade de intervenção manual.

``` bash
simple-ai
│
└── datasets
│
├── _init_.py 
├── dataset_preparer.py 
├── dataset-splitter.py 
├── model_evaluator.py 
├── model_trainer.py 
└── predictor.py 
```

``` py
file_name = sys.argv[1]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing required argument: file_name")
        sys.exit(1)
    
    prepare_dataset(file_name)
    split_dataset()
    train_model()
    evaluate_model()
    predict()
```

O conjunto de dados é separado em conjuntos de treinamento e teste para avaliar a capacidade do modelo. A separação do conjunto de dados em treinamento e teste é uma prática fundamental para garantir a validade e a generalização dos modelos de aprendizado de máquina.

``` py
def load_ai(file_name):
    print(f"\nLoading AI with file '{file_name}'...")
    ai_path = os.path.abspath("./simple-ai/__init__.py")

    if not os.path.isfile(ai_path):
        print("File not found:", ai_path)
        return

    subprocess.run(["python", ai_path, file_name])
```

```
load_ai(), é responsável por executar o treinamento do nosso modelo, é chamado tão logo termine a construção do dataset.
```

<code>prepared_dataset</code>

```
Gerado durante a preparação do dataset.
```

<code>prepared_dataset_test</code> e <code>prepared_dataset_train</code>

```
Gerados durante a separação do dataset.
```

```
Model Predictor gerado durante o treinamento do modelo.
```

O <code>model_predictor</code> é um objeto que pode ser usado para fazer previsões em novos
dados após o treinamento ter sido concluído.

A seguir o código avalia o modelo de aprendizado de máquina carregando um conjunto
de dados de teste, carregando um modelo treinado, fazendo previsões sobre os dados de
teste usando o modelo carregado e calculando a precisão das previsões. A precisão é
calculada comparando as previsões do modelo com as verdadeiras classes dos dados de
teste.

Por fim a nossa IA está pronta para prever. Ela carrega um modelo previamente treinado
solicita ao usuário que insira os valores necessários para a previsão, converte esses valores
em uma lista, com base nessa lista faz previsões usando o modelo carregado. Finalmente,
ele exibe o número previsto.

## 4. Conclusão

Neste projeto, desenvolvi um MNIST Dataset. Inicialmente, criamos uma matriz 10x
contendo dígitos de 0 a 9, os quais foram escritos à mão em uma folha de papel e
posteriormente capturados em uma imagem. Essa imagem serviu como a base do nosso
conjunto de dados personalizado.

Em uma etapa subsequente, dividimos o conjunto de dados em conjuntos de treinamento
e teste, uma prática fundamental para treinar e avaliar nossos modelos de forma eficaz. Por
meio desse processo, capacitamos o nosso modelo para reconhecer e prever dígitos com
base nos dados fornecidos pelo usuário.

Esse procedimento não apenas nos permitiu criar um modelo robusto, mas também nos
possibilitará realizar melhorias contínuas à medida que refinarmos e ajustarmos o nosso
conjunto de dados e algoritmos de aprendizado de máquina.

## Bibliografia

```
[1] Paulo Vieira, Leitura- 4 - C-Building_a_MNIST_dataset_rev-2.pdf
[2] Paulo Vieira, Leitura- 4 - B-Datasets_AED.pdf
```

