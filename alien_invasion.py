import sys
import pygame

class AlienInvasion:
    "Classe geral para gerenciar ativos e coportamento do jogo"
    def __init__(self):
        'Ininializa o jogo e crie recursos do jogo'
        pygame.init()
        self.clock=pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        #Deine a cor do background
        self.bg_color=(230,230,230)

    def run_game(self):
        "Inicia o loop principal do jogo"
        while True:
            "Observa os eventos do teclado e mouse"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Redesenha a tela durante cada passagem pelo loop
            self.screen.fill(self.bg_color)
            #Deixa a tela desenhada mais recente visivel
            pygame.display.flip()
            self.clock.tick(60)



if __name__ == '__main__':
    'Cria uma instância do jogo e execute o jogo'
    ai = AlienInvasion()
    ai.run_game