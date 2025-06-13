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

##### **Trabalho de Simmons (1973): Quadros de Caso**
Uma das primeiras abordagens para criar relacionamentos padronizados foi a de Simmons, que focou na estrutura de casos dos verbos. A ideia, baseada em trabalhos anteriores do linguista Charles Fillmore, é que os verbos definem "quadros de caso" (`case frames`), e os elos da rede representam os papéis que os substantivos desempenham na ação.

- **Relacionamentos de Caso:** Incluem papéis como `agente` (quem faz a ação), `objeto` (o que sofre a ação), `instrumento` (o que é usado para a ação), `localização` e `tempo`.
- **Funcionamento:** Ao analisar uma frase como "Sarah consertou a cadeira com cola", o sistema identifica o verbo ("consertou") e ativa seu quadro de caso. Em seguida, preenche os papéis: Sarah é o `agente`, cadeira é o `objeto` e cola é o `instrumento`.
  
![Exemplo de quadro de caso (Figura 7.5)](https://github.com/niad-ufla/niad/blob/main/IA/Imagens/simmons_sarah.png)

Essa abordagem incorpora a estrutura profunda da linguagem diretamente no formalismo da rede, permitindo que o sistema compreenda as relações semânticas de forma independente da sentença exata que foi usada.

##### **Teoria da Dependência Conceitual (Roger Schank)**
Talvez a tentativa mais ambiciosa de modelar a semântica da linguagem natural tenha sido a Teoria da Dependência Conceitual de Roger Schank. O objetivo era criar um conjunto completo de "primitivas" para representar o significado de qualquer frase de forma inequívoca.

- **Componentes Primitivos:** A teoria propõe que todo significado é construído a partir de quatro tipos de conceitos:
    - **ATOs:** Ações primitivas.
    - **PFs:** Objetos (do inglês, _Picture Producers_).
    - **AAs:** Modificadores de ações.
    - **AFs:** Modificadores de objetos.

- **Ações Primitivas (ATOs):** Schank postulou que todas as ações humanas podem ser decompostas em um ou mais elementos desse pequeno conjunto de cerca de 12 ações básicas, como:
    - `ATRANS`: Transferir um relacionamento abstrato (ex: dar).
    - `PTRANS`: Transferir a localização física de um objeto (ex: ir).
    - `PROPEL`: Aplicar força a um objeto (ex: empurrar).
    - `INGERIR`: Ingerir um objeto (ex: comer).
    - `MTRANS`: Transferir informação mental (ex: contar).
    - `MBUILD`: Construir nova informação mental (ex: decidir).

- Por fim, pode ser adicionada ao conjunto de conceitualizações a informação de tempo e de modo verbais. Uma lista parcial deles está logo abaixo:
	- `p`: Passado.
	- `f`: Futuro.
	- `t`: Transição.
	- `ti`: Transição inicial.
	- `?`: Interrogativo.
	- `tf`: Transição final.
	- `c`: Condicional.
	- `/`: Negativo.
	- `nil`: Presente.
	- `delta?`: Atemporal.

- **Gramática Semântica:** A teoria define um conjunto de **regras de dependência conceitual** que funcionam como uma gramática para o significado, descrevendo como os conceitos se relacionam (ex: a relação entre agente e verbo, ou entre verbo e objeto).
  
![Exemplo de dependência conceitual (Figura 7.8)](https://github.com/niad-ufla/niad/blob/main/IA/Imagens/exemplos_dependencia_conceitual.png)

- **Benefícios e Forma Canônica:** O principal benefício buscado era a **forma canônica**. Isso significa que todas as sentenças com o mesmo significado (ex: "Maria deu um livro para João" e "João recebeu um livro de Maria") seriam reduzidas a um único e idêntico grafo de dependência conceitual. Isso simplificaria enormemente as tarefas de inferência e compreensão.

- **Críticas e Legado:** Apesar de sua influência, a teoria foi criticada por diversos motivos:
    1. **Custo Computacional:** Reduzir todas as sentenças a primitivas de baixo nível é um processo caro.
    2. **Viabilidade:** Críticos questionaram se a redução à forma canônica é computacionalmente viável para a complexidade da linguagem natural.
    3. **Limitação das Primitivas:** As primitivas podem ser simples demais para capturar conceitos mais sutis e abstratos (ex: a ambiguidade de um adjetivo como "alto").

Apesar das críticas, a Teoria da Dependência Conceitual foi extremamente influente, gerando pesquisas importantes em áreas como **roteiros (scripts)**, que descrevem sequências de eventos em contextos específicos, e **MOPs (Memory Organization Packets)**, que foram fundamentais para o desenvolvimento do **raciocínio baseado em casos**.

---

**OBS:** Esse conteúdo ainda está incompleto! No entanto, está aberto a contribuições de outros estudantes, e seguirei trabalhando nele durante nossos encontros.
