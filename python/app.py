import pygame  # Comando "pip install pygame" no Prompt de Comando
import math  # Comando "pip install python-math" no Prompt de Comando
pygame.init()  # Inicia o módulo PYGAME

# Define o nome da janela e sua LARGURA e ALTURA em pixels
WIDTH, HEIGHT = 1550, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ÓRBITAS PLANETÁRIAS")

# Define as cores dos planetas, utilizando o padrão RGB
AMARELO = (255, 255, 0)
BRANCO = (255, 255, 255)
CINZA_CLARO = (200, 200, 200)
CINZA_ESCURO = (80, 78, 80)
AZUL = (0, 0, 255)
VERMELHO = (188, 38, 50)
FONTE = pygame.font.SysFont("comicsans", 16)


class Planetas(pygame.sprite.Sprite):
    # Unidade Atronômica - Distância da Terra ao Sol (Padrão de distância utilizado ~ 149.6 milhões de km, em metros)
    UA = 149.6e6 * 1000
    G = 6.67428e-11  # Constante Gravitacional
    ESCALA = 200 / UA  # 1 UA = 100 PIXELS
    TEMPO = 3600*24  # O Tempo de Órbita É ALTERADO AQUI (1 Dia = 1 Segundo)

    # Função, da classe Planetas, que será utilizada para definir os valores de x, y, raio, cor e massa (nessa ordem)
    def __init__(self, x, y, raio, cor, massa):
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = cor
        self.massa = massa
        self.orbita = []
        self.sol = False
        self.distancia_sol = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):  # Exibe os planetas (círculos) baseados na distância ao centro da tela (Sol)
        x = self.x * self.ESCALA + WIDTH / 2
        y = self.y * self.ESCALA + HEIGHT / 2

        if len(self.orbita) > 2:  # Atualiza as coordenadas de X e Y e exibe pontos sucessivos nessas coordenadas, formando uma linha (rastro)
            pontos_atualizados = []
            for ponto in self.orbita:
                x, y = ponto
                x = x * self.ESCALA + WIDTH / 2
                y = y * self.ESCALA + HEIGHT / 2
                pontos_atualizados.append((x, y))

            pygame.draw.lines(win, self.cor, False, pontos_atualizados, 2)

        # Armazenando o círculo no objeto
        self.drawed = pygame.draw.circle(win, self.cor, (x, y), self.raio)

        # Escreve a distância (em "km") de cada planeta até o sol
        if not self.sol:
            valor_distancia = FONTE.render(
                f"{round(self.distancia_sol/1000, 1)}km", 1, BRANCO)
            win.blit(valor_distancia, (x - valor_distancia.get_width() /
                     2, y - valor_distancia.get_height()/2))

    def atracao(self, outro):  # Definimos a distância entre um objeto1 e um objeto2 e aplicamos ao Teorema de Pitágoras (h^2 = x^2 + y^2)
        outro_x, outro_y = outro.x, outro.y
        distancia_x = outro_x - self.x
        distancia_y = outro_y - self.y
        distancia = math.sqrt(distancia_x ** 2 + distancia_y ** 2)

        if outro.sol:  # Se esse objeto for o próprio Sol, não precisamos fazer esse cáculo
            self.distancia_sol = distancia

        # Calculamos a Força Gravitacional com "F = (G*M*m)/r^2" , usando a distância descoberta acima
        forca = self.G * self.massa * outro.massa / distancia**2
        # Dividimos a Força em Força no Eixo_X e Força no Eixo_Y para exibir o movimento em tela
        teta = math.atan2(distancia_y, distancia_x)
        # Cosseno de Theta = Ângulo Adjascente / Hipotenusa (Força)
        forca_x = math.cos(teta) * forca
        # Seno de Theta = Ângulo Oposto / Hipotenusa (Força)
        forca_y = math.sin(teta) * forca
        return forca_x, forca_y

    def posicao(self, planets):  # Definimos a posição dos planetas em tela
        fx_total = fy_total = 0

        for planeta in planets:
            if self == planeta:
                continue

            fx, fy = self.atracao(planeta)
            fx_total += fx
            fy_total += fy

        # Isolamos e encontramos a velocidade dos planetas através da fórmula "Força Total = Massa / Aceleração" para os Eixos Y e X
        self.x_vel += fx_total / self.massa * self.TEMPO
        self.y_vel += fy_total / self.massa * self.TEMPO

        # Definimos a mudança de posição (movimento) dos planetas através da velocidade, calculada acima, e o Tempo já definido
        self.x += self.x_vel * self.TEMPO
        self.y += self.y_vel * self.TEMPO
        # Definimos que a Órbita é a posição "atualizada" de X e de Y
        self.orbita.append((self.x, self.y))


def main():  # Strings de Planetas e seus parâmetros (Dist. até o sol (x, y); Raio; Cor; Massa) // Suas velocidades inicias no Eixo Y

    ligado = True
    clock = pygame.time.Clock()

    sol = Planetas(0, 0, 30, AMARELO, 1.98892 * 10**30)
    sol.sol = True

    terra = Planetas(-1 * Planetas.UA, 0, 16, AZUL, 5.9742 * 10**24)
    terra.y_vel = 29.783 * 1000

    marte = Planetas(-1.524 * Planetas.UA, 0, 12, VERMELHO, 6.39 * 10**23)
    marte.y_vel = 24.077 * 1000

    mercurio = Planetas(0.387 * Planetas.UA, 0, 8, CINZA_ESCURO, 3.30 * 10**24)
    mercurio.y_vel = -47.4 * 1000

    venus = Planetas(0.723 * Planetas.UA, 0, 14, CINZA_CLARO, 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000

    planets = [sol, terra, marte, mercurio, venus]

    while ligado:  # Taxa de atualização da tela, evento para fechar o programa e exibir os planetas na tela
        clock.tick(60)
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ligado = False

            # Checando se o evento foi o clique no botão
            if event.type == pygame.MOUSEBUTTONUP:
                for planeta in planets:
                    
                    # Checando se o círculo foi colidido, caso der 1 foi. 
                    click = planeta.drawed.collidepoint(pygame.mouse.get_pos())
                    if click == 1:
                        print('clickado')

        for planeta in planets:
            planeta.posicao(planets)
            planeta.draw(WIN)

        # Atualiza a tela, fazendo com que os planetas mudem de posição (baseado nos cálculos acima), gerando movimento
        pygame.display.update()

    pygame.quit()


main()
