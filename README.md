# Projeto Final de COCADA

**Nome**: João Pedro Bianco

**DRE**: 120064499

**Email**: joaopmab@ic.ufrj.br

---
# Gerador de texto utilizando cadeias de Markov

### O que é uma cadeia de Markov?

Cadeia de Markov é um processo estoástico com estados discretos, onde o estado atual depende apenas do anterior para ser calculado. Ou seja, tendo um estado inicial, conseguimos gerar os próximos estados que desejamos.

Podemos representar cadeias de Markov de duas maneiras: por meio de matrizes, e por meio de grafos.

##### 1. Matrizes

Imaginando uma tabela de $n$ elementos por $n$ elementos. Onde cada elemento é um estado possível do que estamos analisando. Com isso, podemos formar uma matriz da seguinte maneira:

$$
M = \begin{bmatrix} 
  p_{1,1} & \dots  & p_{1,n} \\
  \vdots & \ddots & \vdots   \\
  p_{n,1} & \dots  & p_{n,n} 
  \end{bmatrix}
$$

Onde cada $p_{i,j}$ representa a probabilidade de transição do estado $i$ para o estado $j$. Além disso, tendo um vetor que representa o estado inicial $v_0$, podemos calcular $v_0 . M^t$ para calcular a probabilidade do estado $v_t$. No entanto, essa não é a maneira mais intuitiva de se visualizar o problema.

##### 2. Grafos

Também podemos representar cadeias de Markov por grafos. Onde cada nó do grafo é um estado e $p(i,j)$ é a probabilidade de transição do estado $i$ para o estado $j$. Perceba que no grafo é mais claro quais estados tem relações com quais. É por causa disso que vamos utilizar essa versão no nosso algoritmo.

No mesmo cenário, teriamos uma representação do tipo:

![graph](https://github.com/jpmab26/textgenerator/assets/118858926/c691958e-d494-4908-a323-fd14d0f8285f)

### Como podemos utiliza-la para construir um gerador de textos?

Como um texto é formado por uma sequência de palavras, podemos usar algum texto como base de dados para formar um grafo das palavras utilizadas. Com esse grafo, conseguimos gerar novos textos aleatórios. Basta começarmos de um nó (uma palavra) aleatório, e a partir daí calcularmos os proximos estados e irmos adicionando ao texto que será gerado.

Para entendermos melhor esse processo, vamos fazer um exemplo simples.

#### Exemplo simples

Vamos pegar alguns provérbios para a nossa base de dados:

> A pressa é a inimiga da perfeição.

> A voz do povo é a voz de Deus.


Agora vamos montar um grafo da nossa base de dados:


![graph2](https://github.com/jpmab26/textgenerator/assets/118858926/b0ec587d-ff53-40ef-b41d-2fc700a55c39)

Como podemos ver, temos a transição "é" para "a" e de "a" para "voz" ocorrendo duas vezes. Com isso, temos que incrementar o peso dessas respectivas transições para termos um modelo melhor.

O nosso algoritmo agora basicamente escolhe um nó aleatório e transita entre os próximo nós de acordo com os pesos pela quantidade de vezes que pedimos, formando um texto.

Aqui está alguns exemplos de provérbios criados pelo algoritmo com uma base de dados de 71 provérbios ([fonte](https://www.todamateria.com.br/proverbios-e-ditados/)):

Rodando `python3 generate.py proverbios.txt 10 5 10`, tivemos:

> Palavra basta para baixo todo santo ajuda pimenta nos olhos dos outros é o faça. 

> Vigário cor de cego é da caça com ferro será ferido. 

> Aparências enganam a voz do caçador todos os gatos. 

> Caça com porcos farelo come quem espera sempre alcança caiu? 

> Degenera nem tudo que eu digo mas não degenera nem tudo que é da perfeição à noite todos os levam!

> Deus cada um conto aumenta um? 

> Gongo cair no fogo dar uma de velho para. 

> Refresco pôr a voz! 

> Peneira não há mal que sempre dure nem bem? 

> Que fura a cavalo dado não faz milagre quem tem!

Para o algoritmo ter um funcionamento mais legal, não fixamos o tamanho total do texto gerado, colocamos um intervalo, e o tamanho do texto gerado será algo dentro desse intervalo. Além disso, o texto não pode terminar em 'o', 'a', 'os', 'as', 'que', 'e', 'qual', 'do', 'da', 'de', 'dos', 'das', 'nas', 'em', 'no', 'na', e 'ao'. Caso isso aconteça removemos a última palavra. Também fizemos a primeira letra do texto ser maiúscula, e todo texto terminar em ponto final, exclamação, ou interrogação --- sendo o peso deles 6, 3, 1, respectivamente.

##### Como usar o programa?

Rode `python3 generate.py <local_da_base_de_dados> <quantidade_de_textos> <tamanho_mínimo> <tamanho_máximo>`. Sendo `<quantidade_de_textos>`, `<tamanho_mínimo>`, `<tamanho_máximo>` opicionais, tendo valores padrão de 5, 5, e 20, respectivamente.

### Onde algoritmos parecidos são utilizados?

Um lugar em que isso pode ser implementado são nos algoritmos de sugestão de palavras quando se está escrevendo um texto. Pense nas sugestões que o seu celular dá enquanto você está digitando. Nele aparecem as 3 palavras com maiores probabilidades de transição dada a palavra anterior escrita. O gerador de texto implementado aqui pode ser reproduzido utilizando as suas palavras como base de dados, basta você sair clicando nas sugestões que aparecem.

<img src="https://github.com/jpmab26/textgenerator/assets/118858926/b35e727e-91d9-4051-963b-2275309b4b2b" width="350" height="auto" />

### Alguns textos gerados:

##### Utlizando músicas do Legião Urbana como base de dados

> Lixo comercial e quis se levantar ficou deitado e você vai ficar rico vamos ter nome de vocês somos o que tem que foi escondido é esse que país é tudo isso é esse yeah todas? 

> E decidiu trabalhar e mesmo mês que país é esse ah terceiro mundo todos os filhos da escuridão ficaremos acordados imaginando alguma solução pra que foi prometido ninguém eu não pertenço a nossa vez vamos! 

> Cocacola geração cocacola woah depois telefonaram e melhor não quis saber um dia sempre em paz na morte eu vou fugir de ser quando! 

> Quando vendermos todas as luzes acesas agora chegou nossa própria criação serão noites inteiras talvez por tudo isso é esse que nem feijão com tudo isso em vão ver suas crianças derrubando reis fazer comédia no vestibular e o eduardo meio tonto só pensava em qualquer! 

> Parar pra brasília e mesmo com tudo isso não é esse que país é fácil de caetano e cofres e mônica riu e viu que não pertenço a minha mãe mas o lixo comercial e do bandeira e cofres! 

> Um dia se é esse que país é que isso não quis saber um milhão quando vendermos todas as suas leis somos o brasil vai nos proteger será que nada vai nos proteger será que chega é! 

> Esquisita eu moro na escola escola não é absurdo são meus pais não entende seus pais não houvesse amanhã porque se ver suas crianças derrubando reis fazer comédia no cinema com vocês nos perderemos entre monstros da nossa própria criação serão noites inteiras? 

> Barra mais bonito é bem mais birita e mesmo mês que nem me entender dorme agora chegou nossa vez vamos fazer nosso egoísmo? 

> Amanhã porque o lixo em tanta casa que país é azul explica a menina tinha de areia você me abraça. 

> Viajar porque se for piada no cinema com meus filhos da cidade a mônica fizeram natação fotografia teatro artesanato e eduardo. 

##### Utlizando o livro dos três mosqueteiros como base de dados

> Continuou a ponta de dizer a portinhola e embora fôssemos todos os afasta para porthos e dos mosqueteiros diante de disse! 

> Contrastes entretanto as suas acomodações os quatro rapazes mas resmungando malditos gascões são oito anos a porta parecia querer aramis e como uma cadeira de sua eminência pode dizer palavra no patamar que sempre preocupada a morte disseme ele claro mas quero que estava visível satisfação. 

> Adversário palavra que há dúvida esses tesouros do louvre do ouro e o sr de todo o pobre criatura do criado que se ela escreveu para minha honra do duque de modo a questão d’artagnan ameaçada e notou que segura o deixar começou a porthos apertando a mas. 

> Você a verdade eu o que se juntar a espada e o outro a sra bonacieux diabo disse ela chamou a garganta e obediente godeau estalajadeiro dos seus soldados. 

> Fazer um pouco o carpinteiro da necessidade de cabrito assada e morto e eu não aparecessem o outro lugar à fonte e correram portanto a porta e não podendo ter. 

> Mas há sempre e diz mais raro que ketty e com uma febre no centro da sua sepultura d’artagnan já lhe pareceram dar uma faca embotouse “ah se tivesse de que o risco a segunda vez os viajantes que fosse porque porthos teve. 

> Que se o pó vermelho respondeulhe que vinham visitálo com a portsmouth devido à fisionomia cintilante de la rochelle e uma centena é um grande distância havia cinco anos apenas com o mudasse! 

> Ajoelhouse e os espanhóis não suspeita de cahusac gritando a agitação estava de circunvalação e três amigos que se ouvia o provérbio athos quando em cima de si mesmo tempo passava na vida. 

> Cima do jovem de fato de tréville entrou é mesmo tem alguma coisa o que dormir devido ao seu gabinete encontrou athos o qual vai a sentinela. 

> Mas eu estarei procure lembrarse em você o jovem que lorde de sorrir o que seu quarto destinado a prisão onde ficava apenas a uma tristeza geral como por fim de partir imediatamente!
