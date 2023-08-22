import sys
import pygame

class AlienInvasion:
    "Classe geral para gerenciar ativos e coportamento do jogo"
    def __init__(self):
        'Ininializa o jogo e crie recursos do jogo'
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        "Inicia o loop principal do jogo"
        while True:
            "Observa os eventos do teclado e mouse"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Deixa a tela desenhada mais recente visivel
            pygame.display.flip()



if __name__ == '__main__':
    'Cria uma instância do jogo e execute o jogo'
    ai = AlienInvasion()
    ai.run_game