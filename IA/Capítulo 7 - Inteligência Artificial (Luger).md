# Tópicos principais
• Base de conhecimento
• Linguagens de representação

## Derivações
• Teorias associacionistas (exemplo: rede semântica com grafos)

## Definições
Abaixo, seguem definições dos termos mais importantes tratados nos tópicos acima.

### Base de conhecimento
É um mapeamento entre os objetos e as relações de um domínio de problema e entre os
objetos computacionais e as relações de um programa. Os resultados de inferências na base de conhecimento devem corresponder aos resultados de ações ou às observações no mundo.

### Linguagem de representação
Media os objetos, relações e inferências computacionais disponíveis para programadores. Geralmente, as linguagens para a representação de conheci­mento são mais restritas que o cálculo de predicados ou as linguagens de programação.

### Teorias associacionistas
As teorias associacionistas definem o significado de um objeto em termos de uma rede de associações com outros objetos. Para os associacionistas, quando os seres humanos percebem um objeto, essa percepção é mapeada primeiro em um conceito. Esse conceito é parte do nosso conhecimento completo do mundo e está conectado através de relacionamentos apropriados a outros conceitos.

Teorias associacionistas estão bastante ligadas às áreas da linguística e da psicologia. Muitos estudos que tentam entender a estrutura do raciocínio/entendimento humano partem dessas áreas, e a nossa área (IA) se aproveita bastante disso.

#### Rede semântica
Uma rede semântica representa o conhecimento como um grafo, com os nós que correspondem a fatos ou conceitos e os arcos como relações ou associações entre conceitos. Tanto os nós como os arcos são normalmente rotulados.

O termo “rede semântica” abrange uma família de representações baseadas cm grafos. Essas representações diferem, sobretudo, nos nomes que podem ser usados para os nós e arcos e nas inferências que podem vir dessas estruturas.

Um programa muito influente, que ilustra muitas das características das redes semânticas iniciais, foi escrito por Quillian no final dos anos 1960. Esse programa definia as palavras em inglês de forma semelhante aos dicionários: uma palavra é definida em termos de outras palavras e os componentes da definição são definidos da mes­ma forma.

Exemplo de rede semântica:

![Exemplo de rede semântica (Figura 7.1)](https://github.com/niad-ufla/niad/blob/main/IA/Imagens/rede_semantica.png)

##### Programa de Quillian (1967)

Em vez de definir as palavras formalmente em termos de axiomas básicos, cada definição simplesmente conduz a outras definições em uma forma desestruturada e, possivelmente, circular. Ao procurar por uma palavra, percorremos essa “rede” até que estejamos satisfeitos com o que compreendemos da palavra original. Cada nó na rede de Quillian corresponde a um conceito de palavra com elos associados a outros conceitos de
palavras que formaram a sua definição. A base de conhecimento era organizada em planos, onde cada plano era um grafo que definia uma única palavra.

Usando esse caminho de interseção, o programa era capaz de concluir:
chorar 2 é, entre outras coisas, fazer um som triste. Confortar 3 pode ser tornar 2 um pouco menos triste (Quillian, 1967).

Os números na resposta indicam que o programa realizou uma seleção entre diferentes significados das palavras.

![Fluxograma exemplificando o programa de Quillian (Figura 7.3)](https://github.com/niad-ufla/niad/blob/main/IA/Imagens/programa_quillian_1.png)

![Fluxograma exemplificando o programa de Quillian (Figura 7.4)](https://github.com/niad-ufla/niad/blob/main/IA/Imagens/programa_quillian_2.png)

Embora o trabalho inicial de Quillian tenha estabelecido a maioria das características significativas do formalis­mo das redes semânticas, como os arcos e os elos rotulados, a herança hierárquica e as inferências ao longo de elos associativos, ele se mostrou limitado em sua habilidade de tratar as complexidades de muitos domínios. Uma das principais razões para essa deficiência se encontra na pobreza dos relacionamentos (elos) que captavam os aspectos semânticos mais profundos do conhecimento. A maioria dos elos representava associações extremamente genéricas entre os nós e não fornecia uma base real para a estruturação dos relacionamentos semânticos.

#### Voltando a redes semânticas...
Muito do trabalho em representações por redes que se seguiu ao de Quillian se concentrou na definição de um conjunto mais rico de rótulos dos elos (relacionamentos) que pudesse modelar mais completamente a semântica da linguagem natural. Ao implementar os relacionamentos semânticos fundamentais da linguagem natural como parte do formalismo, em vez de ser parte do conhecimento do domínio acrescentado pelo construtor do sistema, as bases de conhecimento deixam de ser tão artesanais e alcançam maior generalidade.

---

**OBS:** Esse conteúdo ainda está incompleto! No entanto, está aberto a contribuições de outros estudantes, e seguirei trabalhando nele durante nossos encontros.
