# Atividade de Interpolação de triângulo com pontos

---

## 1. A Matemática do Preenchimento (Coordenadas Baricêntricas)

Basicamente o que diferencia o meu código é que diferente da maioria dos outros que usaram while e eu fiz um for, bem como eu fiz funções ao invés de passar todos os valores sempre criando duas funções.

```python
def point(alfa: float, p1: tuple[float, float], p2: tuple[float, float], p3: tuple[float, float]):
    x = alfa * p2[0] + (1 - alfa) * p1[0]
    y = alfa * p2[1] + (1 - alfa) * p1[1]
    return (x, y)

def pointBeta(alfa: float, beta: float, p1: tuple[float, float], p2: tuple[float, float], p3: tuple[float, float]):
    x = (beta * alfa * p2[0]) + (beta * (1 - alfa) * p1[0]) + ((1 - beta) * p3[0])
    y = (beta * alfa * p2[1]) + (beta * (1 - alfa) * p1[1]) + ((1 - beta) * p3[1])
    return (x, y)
```

A função `point` é uma parte da lógica, que no GeoGebra visto faz o colorimento da linha entre um ponto e outro, inutilizado no código.

Já função `pointBeta` é o coração dessa lógica. Ela recebe os três vértices do triângulo ($p_1, p_2, p_3$) e dois valores de controle ($alpha$ e $beta$, variando de 0 a 1):

$$P = w_1 \cdot p_1 + w_2 \cdot p_2 + w_3 \cdot p_3$$

Os pesos do W foram definidos da seguinte forma:

- **Peso do Ponto 1 ($w_1$):** $beta \cdot (1 - alpha)$
- **Peso do Ponto 2 ($w_2$):** $beta \cdot alpha$
- **Peso do Ponto 3 ($w_3$):** $1 - beta$

## 2. O Loop de Renderização e as Cores (`render`)

- **Interpolação de Cores:** Eu uso os mesmos passos calculados para a posição geométrica para definir a intensidade das cores RGB (Red, Green, Blue).
  - Nível de Vermelho = $w_1$
  - Nível de Verde = $w_2$
  - Nível de Azul) = $w_3$

A instrução `glColor3f(peso_p1, peso_p2, peso_p3)` aplica essa mistura exata para cada ponto desenhado. Quanto mais perto o ponto estiver do vértice $p_1$, mais vermelho ele será, gerando o gradiente visualmente perfeito.

## 3. Estrutura Base e Gerenciamento de Janela (`main` e `init`)

O restante do código é o que foi feito em sala de aula e basicamente lida com a infraestrutura do sistema operacional e do OpenGL:

- **`glfw.init()` e `glfw.create_window()`:** Inicializam a biblioteca e abrem a janela onde o desenho vai aparecer.
- **`glfw.make_context_current()`:** Informa ao OpenGL que os comandos de desenho a seguir devem ser aplicados a esta janela específica.
- **`glClear(GL_COLOR_BUFFER_BIT)`:** Limpa a tela a cada frame (quadro) para que os desenhos de frames anteriores não se sobreponham, criando um rastro borrado.
- **`glfw.poll_events()` e `glfw.swap_buffers()`:** Mantêm a janela "viva" (respondendo a comandos como clicar no X para fechar) e atualizam a imagem na tela de forma fluida.
