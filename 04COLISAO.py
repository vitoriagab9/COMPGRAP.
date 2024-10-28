import game 

PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)

LARGURAJANELA = 500 
ALTURAJANELA = 400

def mover(figura, dim_janela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dim_janela[0]
    borda_inferior = dim_janela[1]

    if figura['objRect'].top < borda_superior or figura['objRect'].bottom > borda_inferior:
        figura['vel'][1] = -figura['vel'][1]

    if figura['objRect'].left < borda_esquerda or figura['objRect'].right > borda_direita:
        figura['vel'][0] = -figura['vel'][0]

    figura['objRect'].x += figura['vel'][0]
    figura['objRect'].y += figura['vel'][1]

pygame.init()

relogio = pygame.time.Clock()

janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption("Colisão")

b1 = {'objRect': pygame.Rect(375, 80, 40, 40), 'cor': VERMELHO, 'vel': [0, 1]}
b2 = {'objRect': pygame.Rect(175, 200, 40, 40), 'cor': VERDE, 'vel': [0, -3]}
b3 = {'objRect': pygame.Rect(275, 150, 40, 40), 'cor': AMARELO, 'vel': [0, -1]}
b4 = {'objRect': pygame.Rect(75, 150, 40, 40), 'cor': AZUL, 'vel': [0, 4]}
blocos = [b1, b2, b3, b4]

bola = {'objRect': pygame.Rect(255, 255, 255, 128), 'cor': BRANCO, 'vel': [3, 3]}
deve_continuar = True

while deve_continuar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False

    janela.fill(PRETO)

    for bloco in blocos:
        mover(bloco, (LARGURAJANELA, ALTURAJANELA))
        pygame.draw.rect(janela, bloco['cor'], bloco['objRect'])

    mudarCor = bola['objRect'].colliderect(bloco['objRect'])
    if mudarCor:
        bola['cor'] = bloco['cor']

    mover(bola, (LARGURAJANELA, ALTURAJANELA))
    pygame.draw.ellipse(janela, bola['cor'], bola['objRect'])

    pygame.display.update()

    relogio.tick(40)

    pygame.quit()
