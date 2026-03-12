# Entendendo a Interpolação de Cores em um Triângulo com OpenGL

Este documento explica como o código Python (utilizando `glfw` e `PyOpenGL`) desenha um triângulo na tela preenchendo-o ponto a ponto e criando um gradiente de cores suave entre seus três vértices.

---

## 1. A Matemática do Preenchimento (Coordenadas Baricêntricas)

Em vez de usar coordenadas cartesianas tradicionais (X e Y) para pintar o triângulo, o código utiliza um conceito chamado **Coordenadas Baricêntricas**.

A função `pointBeta` é o coração dessa lógica. Ela recebe os três vértices do triângulo ($p_1, p_2, p_3$) e dois valores de controle ($\alpha$ e $\beta$, variando de 0 a 1). A fórmula calcula a posição de qualquer ponto interno multiplicando a posição de cada vértice pelo seu respectivo "peso" (influência):

$$P = w_1 \cdot p_1 + w_2 \cdot p_2 + w_3 \cdot p_3$$

No código, os pesos ($w$) foram definidos da seguinte forma:

- **Peso do Ponto 1 ($w_1$):** $\beta \cdot (1 - \alpha)$
- **Peso do Ponto 2 ($w_2$):** $\beta \cdot \alpha$
- **Peso do Ponto 3 ($w_3$):** $1 - \beta$

A soma desses três pesos sempre resulta em 1. Se um peso for 1 e os outros 0, o ponto desenhado cai exatamente em cima de um vértice. Se os três pesos forem equilibrados, o ponto é desenhado no meio do triângulo.

## 2. O Loop de Renderização e as Cores (`render`)

Como a atividade exige o uso de `GL_POINTS` (desenhar o triângulo pontinho por pontinho, em vez de usar o preenchimento automático de `GL_TRIANGLES`), precisamos criar uma malha densa de pontos.

- **Loops Aninhados:** Usamos dois blocos de repetição `for` (baseados em uma quantidade definida de `passos`) para gerar diversas combinações fracionadas de $\alpha$ e $\beta$. Isso varre toda a área 2D do triângulo.
- **Interpolação de Cores:** O grande truque aqui é usar os **mesmos pesos** calculados para a posição geométrica para definir a intensidade das cores RGB (Red, Green, Blue).
  - Nível de Vermelho ($R$) = $w_1$
  - Nível de Verde ($G$) = $w_2$
  - Nível de Azul ($B$) = $w_3$

A instrução `glColor3f(peso_p1, peso_p2, peso_p3)` aplica essa mistura exata para cada ponto desenhado. Quanto mais perto o ponto estiver do vértice $p_1$, mais vermelho ele será, gerando o gradiente visualmente perfeito.

## 3. Estrutura Base e Gerenciamento de Janela (`main` e `init`)

O restante do código lida com a infraestrutura do sistema operacional e do OpenGL:

- **`glfw.init()` e `glfw.create_window()`:** Inicializam a biblioteca e abrem a janela onde o desenho vai aparecer.
- **`glfw.make_context_current()`:** Informa ao OpenGL que os comandos de desenho a seguir devem ser aplicados a esta janela específica.
- **`glClear(GL_COLOR_BUFFER_BIT)`:** Limpa a tela a cada frame (quadro) para que os desenhos de frames anteriores não se sobreponham, criando um rastro borrado.
- **`glfw.poll_events()` e `glfw.swap_buffers()`:** Mantêm a janela "viva" (respondendo a comandos como clicar no X para fechar) e atualizam a imagem na tela de forma fluida.
