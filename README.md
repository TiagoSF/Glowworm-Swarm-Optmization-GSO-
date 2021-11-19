# Glowworm-Swarm-Optmization-GSO-and-Particle-Swarm-Optimization-PSO

### PSO

O PSO foi proposto por Eberhart e Kennedy em 1995, posteriormente foi aplicado em milhares de artigos científicos e a problemas diversos, demonstrando ser uma ferramenta eficaz.
PSO é uma meta-heurística de inteligência de enxame inspirada no comportamento de grupo de animais, por exemplo bandos de pássaros ou cardumes de peixes. Da mesma forma que os algoritmos genéticos (AG), é um método baseado em população, ou seja, representa o estado do algoritmo por uma população, que é modificado iterativamente até que um critério de terminação seja satisfeito. 
Cada partícula mantém um registro de suas coordenadas no espaço que estão associadas à melhor solução (fitness) que ela alcançou até agora. Esse valor é chamado de melhor da partícula (particle best). Outro valor “melhor” também é rastreado, a versão global do otimizador de enxame de partículas rastreia o melhor global (global best) e sua localização, obtido até agora por qualquer partícula na população.
O conceito de Otimização de Enxame de Partículas (PSO) consiste em, a cada passo de tempo, mudar a velocidade (aceleração) de cada partícula em direção a sua particle best e global best. A aceleração é descrita por números aleatórios, sendo gerados para aceleração em direção à particle best e global best.


### GSO

O GSO faz parte da família de algoritmos baseados em inteligência de enxame, e foi introduzido por Kaipa N. Krishnanand e D. Ghose em 2005, para o cálculo simultâneo de múltiplos ótimos de funções multimodais .
Os agentes em GSO são Vagalumes (Glowworm) que carregam uma quantidade de luminescência chamada luciferina (Luciferin) junto com eles.
No GSO, um enxame é iniciado aleatoriamente no espaço de solução. Cada Vagalume representa uma solução de função objetivo no espaço de busca e carrega uma certa quantidade de luciferin junto com ele. O nível de luciferin está associado à aptidão da posição atual do agente (fitness). O indivíduo mais brilhante significa uma posição melhor, ou seja, uma solução melhor.
Usando um mecanismo probabilístico, cada agente só pode ser atraído por um vizinho cuja intensidade de luciferina é maior do que a sua dentro o domínio de decisão local e então se move em direção a ele.
Um Vagalume que considera outro Vagalume, como seu vizinho, se este estiver no raio de vizinhança, e o nível de luciferin seja maior do que o seu próprio.
O GSO ainda é bastante utilizado para análise de cluster, e uma ferramenta importante para análise exploratória de dados, assim como para resolver problemas de planejamento de trajetória.
