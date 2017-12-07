#To do:
    #Animacoes
    #Devolver sistema de vidas
    #Ensinar controles 

#Redes:
    #transformar esse codigo em servidor udp
    #cada jogador eh um cliente
    #os clientes e o servidor ficam mandando a lista com os inimigos um para o outro
    #os clientes tem que passar, alem da lista atualizada de inimigos, a posicao da nave de cada um
    #o servidor repassa para que a posicao do outro jogador seja atualizada na tela



import pygame
import random
 
# Definicao cores
BLACK = [0, 0, 0]
WHITE = [200, 200, 200]
ORANGE = [100, 50,0]
GREEN = [0, 80, 0]
RED = [80, 20, 20]
RED2 = [255, 0, 0]
BLUE = [0, 0, 255]
PURPLE = [255, 0, 255]
YELLOW = [255, 255, 0]

clock = pygame.time.Clock()

#musicas
pygame.mixer.init()



#definicoes hud

#fontes
pygame.font.init()
my_font= pygame.font.Font("./font/8bit.ttf", 13)
end_font = pygame.font.Font("./font/8bit.ttf", 40)



#pontuacao
score = 0
score_pos = [600, 50]
score_txt = my_font.render("Pontos: ", 1, (255, 255, 255))
score_txt2 = end_font.render("Pontos: ", 1, (255, 255, 255))

#vidas do jogador
life = 5
life_pos = [600 , 150]
life_txt = my_font.render("Vidas: ", 1, (255, 255, 255))

#powerups
pu_pos = [600, 350]
pu_txt = my_font.render("Power Ups: ", 1, (255, 255, 255))

#level
level_pos = [600, 250]
level_txt = my_font.render("Fase: ", 1, (255, 255, 255))
 
#Classes

#Inimigos 
class Enemy1(pygame.sprite.Sprite):
    #Classe das naves inimigas
    def __init__(self, color):
        #Transformar em sprite para fazer as colisoes
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.image.load("./images/inimigo1.png")
        
 
        self.rect = self.image.get_rect()
    
    def update(self):
        #Inimigos descerem
        self.rect.y += 2

class Enemy2(pygame.sprite.Sprite):
    #Classe das naves inimigas
    def __init__(self, color):
        #Transformar em sprite para fazer as colisoes
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.image.load("./images/inimigo2.png")
 
        self.rect = self.image.get_rect()
    
    def update(self):
        #Inimigos descerem
        self.rect.y += 3

class Enemy3(pygame.sprite.Sprite):
    #Classe das naves inimigas
    def __init__(self, color):
        #Transformar em sprite para fazer as colisoes
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.image.load("./images/inimigo3.png")
 
        self.rect = self.image.get_rect()
    
    def update(self):
        #Inimigos descerem
        self.rect.y += 4

class Enemy4(pygame.sprite.Sprite):
    #Classe das naves inimigas
    def __init__(self, color):
        #Transformar em sprite para fazer as colisoes
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.image.load("./images/inimigo4.png")
 
        self.rect = self.image.get_rect()
    
    def update(self):
        #Inimigos descerem
        self.rect.y += 4        
 
#Jogador 
class Player(pygame.sprite.Sprite):
    #Classe do jogador 
    def __init__(self):
        #Transformar em sprite para fazer as colisoes
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.image.load("./images/player.png")
 
        self.rect = self.image.get_rect()
 
    def update(self):
        #Mover a posicao do jogador
        self.rect.x = x_coord
        self.rect.y = y_coord
 
#Tiros jogador 
class Fire1(pygame.sprite.Sprite):
    #Classe dos tiros do jogador
    def __init__(self):
        #Transformar em sprite para fazer as colisoes
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(PURPLE)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        #Tiro subir
        self.rect.y -= 3

class Fire2(pygame.sprite.Sprite):
    #Classe dos tiros do jogador
    def __init__(self):
        #Transformar em sprite para fazer as colisoes
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(PURPLE)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        #Tiro subir
        self.rect.y -= 4

class Fire3(pygame.sprite.Sprite):
    #Classe dos tiros do jogador
    def __init__(self):
        #Transformar em sprite para fazer as colisoes
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(PURPLE)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        #Tiro subir
        self.rect.y -= 5

#Tiros inimigos
class E_Fire1(pygame.sprite.Sprite):
    #Classe dos tiros do jogador
    def __init__(self):
        #Transformar em sprite para fazer as colisoes
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.image.load("./images/efire.png")
 
        self.rect = self.image.get_rect()
 
    def update(self):
        #Tiro descer
        self.rect.y += 3

class E_Fire2(pygame.sprite.Sprite):
    #Classe dos tiros do jogador
    def __init__(self):
        #Transformar em sprite para fazer as colisoes
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.image.load("./images/efire.png")
 
        self.rect = self.image.get_rect()
 
    def update(self):
        #Tiro descer
        self.rect.y += 4

class E_Fire3(pygame.sprite.Sprite):
    #Classe dos tiros do jogador
    def __init__(self):
        #Transformar em sprite para fazer as colisoes
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.image.load("./images/efire.png")
 
        self.rect = self.image.get_rect()
 
    def update(self):
        #Tiro descer
        self.rect.y += 5

#Classes Chefes
class Boss1(pygame.sprite.Sprite):
    #Classe das naves inimigas
    def __init__(self, color):
        #Transformar em sprite para fazer as colisoes
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.image.load("./images/boss11.png")
        
 
        self.rect = self.image.get_rect()

    def update(self):
        #Mover a posicao do jogador
        self.rect.x = chefe1Pos[0]
        self.rect.y = chefe1Pos[1]

class Boss2(pygame.sprite.Sprite):
    #Classe das naves inimigas
    def __init__(self, color):
        #Transformar em sprite para fazer as colisoes
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.image.load("./images/boss22.png")
 
        self.rect = self.image.get_rect()

    def update(self):
        #Mover a posicao do jogador
        self.rect.x = chefe2Pos[0]
        self.rect.y = chefe2Pos[1]

class Boss3(pygame.sprite.Sprite):
    #Classe das naves inimigas
    def __init__(self, color):
        #Transformar em sprite para fazer as colisoes
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.image.load("./images/boss33.png")
        
 
        self.rect = self.image.get_rect()

    def update(self):
        #Mover a posicao do jogador
        self.rect.x = chefe3Pos[0]
        self.rect.y = chefe3Pos[1]

class Boss4(pygame.sprite.Sprite):
    #Classe das naves inimigas
    def __init__(self, color):
        #Transformar em sprite para fazer as colisoes
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.image.load("./images/boss44.png")
        
 
        self.rect = self.image.get_rect()

    def update(self):
        #Mover a posicao do jogador
        self.rect.x = chefe4Pos[0]
        self.rect.y = chefe4Pos[1]

class BossFinal(pygame.sprite.Sprite):
    #Classe das naves inimigas
    def __init__(self, color):
        #Transformar em sprite para fazer as colisoes
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.image.load("./images/garrosh.png")
 
        self.rect = self.image.get_rect()

    def update(self):
        #Mover a posicao do jogador
        self.rect.x = chefeFinalPos[0]
        self.rect.y = chefeFinalPos[1]



#Movimento dos Chefes
def movBoss1():
    global chefe1Estado, chefe1Contador, chefe1Pos, chefe1Destino
    if chefe1Estado == 'parado':
        chefe1Contador -= 1
        if chefe1Contador <= 0:
            chefe1Contador = 50
            chefe1Estado = 'movendo'
            chefe1Destino = [random.randrange(100, 330, 2), random.randrange(100, 400, 2)]
    if chefe1Estado == 'movendo':
        dX = chefe1Destino[0] - chefe1Pos[0]
        dY = chefe1Destino[1] - chefe1Pos[1]
        vX = -2
        vY = -2
        if (dX > 0):
            vX = 2
        elif (dX == 0):
            vX = 0
            
        if (dY > 0):
            vY = 2
        elif (dY == 0):
            vY = 0
            
        chefe1Pos[0] += vX
        chefe1Pos[1] += vY
        if chefe1Pos[0] == chefe1Destino[0] and chefe1Pos[1] == chefe1Destino[1]:
            chefe1Estado = 'parado' 

def movBoss2():
    global chefe2Estado, chefe2Contador, chefe2Pos, chefe2Destino
    if chefe2Estado == 'parado':
        chefe2Contador -= 1
        if chefe2Contador <= 0:
            chefe2Contador = 50
            chefe2Estado = 'movendo'
            chefe2Destino = [random.randrange(100, 320, 4), random.randrange(100, 400, 4)]
    if chefe2Estado == 'movendo':
        dX = chefe2Destino[0] - chefe2Pos[0]
        dY = chefe2Destino[1] - chefe2Pos[1]
        vX = -4
        vY = -4
        if (dX > 0):
            vX = 4
        elif (dX == 0):
            vX = 0
            
        if (dY > 0):
            vY = 4
        elif (dY == 0):
            vY = 0
            
        chefe2Pos[0] += vX
        chefe2Pos[1] += vY
        if chefe2Pos[0] == chefe2Destino[0] and chefe2Pos[1] == chefe2Destino[1]:
            chefe2Estado = 'parado' 

def movBoss3():
    global chefe3Estado, chefe3Contador, chefe3Pos, chefe3Destino
    if chefe3Estado == 'parado':
        chefe3Contador -= 1
        if chefe3Contador <= 0:
            chefe3Contador = 30
            chefe3Estado = 'movendo'
            chefe3Destino = [random.randrange(100, 320, 4), random.randrange(100, 400, 4)]
    if chefe3Estado == 'movendo':
        dX = chefe3Destino[0] - chefe3Pos[0]
        dY = chefe3Destino[1] - chefe3Pos[1]
        vX = -4
        vY = -4
        if (dX > 0):
            vX = 4
        elif (dX == 0):
            vX = 0
            
        if (dY > 0):
            vY = 4
        elif (dY == 0):
            vY = 0
            
        chefe3Pos[0] += vX
        chefe3Pos[1] += vY
        if chefe3Pos[0] == chefe3Destino[0] and chefe3Pos[1] == chefe3Destino[1]:
            chefe3Estado = 'parado' 

def movBoss4():
    global chefe4Estado, chefe4Contador, chefe4Pos, chefe4Destino
    if chefe4Estado == 'parado':
        chefe4Contador -= 1
        if chefe4Contador <= 0:
            chefe4Contador = 20
            chefe4Estado = 'movendo'
            chefe4Destino = [random.randrange(100, 320, 4), random.randrange(100, 400, 4)]
    if chefe4Estado == 'movendo':
        dX = chefe4Destino[0] - chefe4Pos[0]
        dY = chefe4Destino[1] - chefe4Pos[1]
        vX = -4
        vY = -4
        if (dX > 0):
            vX = 4
        elif (dX == 0):
            vX = 0
            
        if (dY > 0):
            vY = 4
        elif (dY == 0):
            vY = 0
            
        chefe4Pos[0] += vX
        chefe4Pos[1] += vY
        if chefe4Pos[0] == chefe4Destino[0] and chefe4Pos[1] == chefe4Destino[1]:
            chefe4Estado = 'parado' 

def movBossFinal():
    global chefeFinalEstado, chefeFinalContador, chefeFinalPos, chefeFinalDestino
    if chefeFinalEstado == 'parado':
        chefeFinalContador -= 1
        if chefeFinalContador <= 0:
            chefeFinalContador = 20
            chefeFinalEstado = 'movendo'
            chefeFinalDestino = [random.randrange(0, 320, 4), random.randrange(100, 320, 4)]
    if chefeFinalEstado == 'movendo':
        dX = chefeFinalDestino[0] - chefeFinalPos[0]
        dY = chefeFinalDestino[1] - chefeFinalPos[1]
        vX = -4
        vY = -4
        if (dX > 0):
            vX = 4
        elif (dX == 0):
            vX = 0
            
        if (dY > 0):
            vY = 4
        elif (dY == 0):
            vY = 0
            
        chefeFinalPos[0] += vX
        chefeFinalPos[1] += vY
        if chefeFinalPos[0] == chefeFinalDestino[0] and chefeFinalPos[1] == chefeFinalDestino[1]:
            chefeFinalEstado = 'parado' 


#Criar a tela do jogo
 
#Inicializar o Pygame
pygame.init()
 
#Tamanho da tela
screen_width = 700
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Em Busca da Joia da Eternidade")


#Menu Inicial 

menu = True

pygame.mixer.music.load("./sounds/SME.mp3")
pygame.mixer.music.play(-1)

hit = pygame.mixer.Sound('./sounds/hith.wav')
point = pygame.mixer.Sound('./sounds/point.wav')

menu_img =  pygame.image.load("./images/menu.png")
screen.fill(BLACK)
screen.blit(menu_img, (0,0))
pygame.display.flip()

while menu:
    for event in pygame.event.get():
        #Verificar se o jogador fechou a janela
        if event.type == pygame.QUIT:
            exit()
        #Verificar as teclas de controle do jogador
        elif event.type == pygame.KEYDOWN:
            #Ajustar a velocidade do jogador de acordo com a tecla pressionada
            if event.key == pygame.K_RETURN:
                menu = False


#historia
invasao_img =  pygame.image.load("./images/invasao.png")
screen.fill(BLACK)
screen.blit(invasao_img, (0,0))
pygame.display.flip()
pygame.time.wait(7000)
hospital_img =  pygame.image.load("./images/hospital.png")
screen.fill(BLACK)
screen.blit(hospital_img, (0,0))
pygame.display.flip()
pygame.time.wait(7000)
aluguel_img =  pygame.image.load("./images/aluguel.png")
screen.fill(BLACK)
screen.blit(aluguel_img, (0,0))
pygame.display.flip()
pygame.time.wait(7000)

#instrucoes para o jogador
inst = True
while inst:
    for event in pygame.event.get():
        #Verificar se o jogador fechou a janela
        if event.type == pygame.QUIT:
            exit()
        #Verificar as teclas de controle do jogador
        elif event.type == pygame.KEYDOWN:
            #Ajustar a velocidade do jogador de acordo com a tecla pressionada
            if event.key == pygame.K_RETURN:
                inst = False
    inst_img =  pygame.image.load("./images/instructions.png")
    screen.fill(BLACK)
    screen.blit(inst_img, (0,0))
    pygame.display.flip()
    clock.tick(60)

#Cria um array para as estrelas e planetas
starArr = []
planetArr = []
 
#Loop para criar uma posicao aleatoria x,y para a estrela e o planeta
for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 600)
    starArr.append([x, y])
for i in range(15):
    x = random.randrange(0, 400)
    y = random.randrange(0, 600)
    planetArr.append([x, y])
 
#Listas de controle de sprites
#Lista com todas as sprites do jogo
all_sprites_list = pygame.sprite.Group()
 
#Lista dos inimigos 
enemy_list = pygame.sprite.Group()
 
#Lista dos tiros do jogador
fire_list = pygame.sprite.Group()
fire_list2 = pygame.sprite.Group()

#Lista dos tiros inimigos
e_fire_list = pygame.sprite.Group() 
e_fire_list2 = pygame.sprite.Group()
e_fire_list3 = pygame.sprite.Group()
e_fire_list4 = pygame.sprite.Group()

#Lista do player porque funcionou, nao me pergunte como
player_list = pygame.sprite.Group() 


#Velocidade do jogador (pixels/frame)
x_speed = 0
y_speed = 0
 
#Posicao inicial do jogador
x_coord = 150
y_coord = 530

 
#Criar a nave do jogador
player = Player()
all_sprites_list.add(player)
player_list.add(player)
 
#teste se o jogador fechou a janela
done = False
 

pygame.mixer.music.load("./sounds/BOOM.mp3")
pygame.mixer.music.play(-1)

#Criar os inimigos
 
for i in range(50):
    #Inimigo
    enemy = Enemy1(BLUE)
 
    #Colocar o inimigo em uma posicao aleatoria acima da tela
    enemy.rect.x = random.randrange(0, 400)
    enemy.rect.y = random.randrange(-8000,0)
 
    #Adicionar o inimigo nas listas de sprites
    enemy_list.add(enemy)
    all_sprites_list.add(enemy)

#Loop fase 1
while not done:
    if life == 0: 
    
      done = True
    for event in pygame.event.get():
        #Verificar se o jogador fechou a janela
        if event.type == pygame.QUIT:
            exit()
            
        #Verificar as teclas de controle do jogador
        elif event.type == pygame.KEYDOWN:
            #Ajustar a velocidade do jogador de acordo com a tecla pressionada
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
            #Atirar quando o jogador pressiona espaco
            elif event.key == pygame.K_SPACE:
                fire = Fire2()
                #Colocar o tiro no mesmo lugar que o jogador
                fire.rect.x = (player.rect.x) + 22
                fire.rect.y = player.rect.y
                #Adicionar o tiro nas listas
                all_sprites_list.add(fire)
                fire_list.add(fire)
                effect = pygame.mixer.Sound('teste_nave2.wav')
                effect.play()  
 
        #Verificar se o jogador soltou a tecla
        elif event.type == pygame.KEYUP:
            #Se o jogador soltou as teclas de direcao, zerar a velocidade (nao queremos velocidades infinitas coff coff)
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
 
    if not enemy_list:
        done = True

    #Logica do jogo

    
    #Mover a nave do jogador de acordo com a velocidade 
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    #Delimitar o espaco para o jogador se mover
    if x_coord > 390:
        x_coord = 390

    if y_coord > 542:
        y_coord = 542

    if x_coord < 0:
        x_coord = 0

    if y_coord < 0:
        y_coord =0
 
    #Atualizar a lista com todos os sprites
    all_sprites_list.update()
 
    #Mecanicas de tiro
    for fire in fire_list:
 
        #Verificar se acertou um inimigo
        enemy_hit_list = pygame.sprite.spritecollide(fire, enemy_list, True)
 
        #Quando atingir o inimigo, eliminar o tiro e adicionar na pontuacao (score)
        for enemy in enemy_hit_list:
            point.play()
            fire_list.remove(fire)
            all_sprites_list.remove(fire)

            score += 1
            
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if fire.rect.y < -10:
            fire_list.remove(fire)
            all_sprites_list.remove(fire)
 
    #Mesmo esquema do tiro, mas agora para ver se o jogador bateu num inimigo 
    #IMPLEMENTAR MORTE!!!!
    for enemy in enemy_list:
        i=random.randrange(500)
        if i == 1: 
            if enemy.rect.y>0:
                efire = E_Fire1()
                #Colocar o tiro no mesmo lugar que o inimigo
                efire.rect.x = enemy.rect.x + 21
                efire.rect.y = enemy.rect.y + 48
                #Adicionar o tiro nas listas
                all_sprites_list.add(efire)
                e_fire_list.add(efire) 
 
        #Verificar colisao do jogador com o inimigo
        enemy_hit_list = pygame.sprite.spritecollide(player, enemy_list, True)
 
        #Quando houver colisao, tirar o inimigo e tirar da pontuacao
        #TROCAR PARA VIDA!!!
        for enemy in enemy_hit_list:
            hit.play()
            enemy_list.remove(enemy)
            all_sprites_list.remove(enemy)
            life -= 1
            
            
 
        #Eliminar os inimigos quando saem da tela (ELES DESCEM! PORTANTO, O Y DEVE SER POSITIVO E MAIOR QUE 600)
        if enemy.rect.y > 615:
            enemy_list.remove(enemy)
            all_sprites_list.remove(enemy)
            #tirar uma vida se passarem
            #life -=1
            

    for efire in e_fire_list:
 
        #Verificar se acertou o jogador
        player_hit_list = pygame.sprite.spritecollide(efire, player_list, False)
 
        #Quando atingir o jogador, eliminar o tiro e perder vida
        for player in player_hit_list:
            
            hit.play()
            e_fire_list.remove(efire)
            all_sprites_list.remove(efire)
            
            life -= 1
            
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if efire.rect.y > 610:
            e_fire_list.remove(efire)
            all_sprites_list.remove(efire)

   

    #Desenhar a tela
 
    #Limpar a tela
    screen.fill(BLACK)
    
    #Printar o HUD

    #pontos
    score_surf = my_font.render((str(score)), 1, (255, 255, 255))
    screen.blit(score_surf, score_pos)
    screen.blit(score_txt, (450, 50))
    #vidas
    life_surf = my_font.render((str(life)), 1, (255, 255, 255))
    screen.blit(life_surf, life_pos)
    screen.blit(life_txt, (450, 150))
    #fases
    level_surf = my_font.render("1", 1, (255, 255, 255))
    screen.blit(level_surf, level_pos)
    screen.blit(level_txt, (450, 250))
    #power ups
    pu_surf = my_font.render(" -- ", 1, (255, 255, 255))
    screen.blit(pu_surf, pu_pos)
    screen.blit(pu_txt, (450, 350))


    # Processar cada estrela do array
    for i in range(len(starArr)):
 
        # Desenhar a estrela
        pygame.draw.circle(screen, WHITE, starArr[i], 2)
 
        # Mover a estrela para baixo 1 pixel
        starArr[i][1] += 1
 
        # Se ela tiver saido da tela
        if starArr[i][1] > 600:
            # Manda de volta um pouco acima da tela
            y = random.randrange(-50, -10)
            starArr[i][1] = y
            # E coloca em outra posicao aleatoria
            x = random.randrange(0, 400)
            starArr[i][0] = x
    # Mesma coisa para os planetas
    for i in range(0,5):
 
        pygame.draw.circle(screen, GREEN, planetArr[i], 22)
 
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x

    for i in range(6,10):
 
        pygame.draw.circle(screen, ORANGE, planetArr[i], 15)
 
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x
    for i in range(11,15):
        pygame.draw.circle(screen, RED, planetArr[i], 8)
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x

 
    #Desenhar todos os sprites
    all_sprites_list.draw(screen)
 
    #Jogar tudo na tela
    pygame.display.flip()
 
    #Limitar a 20 fps (nao queremos um jogo mais impossivel do que ja esta)
    clock.tick(60)

pygame.mixer.music.stop()

done = False

#Variaveis dos Chefes
chefe1Pos = [100, -150]
chefe1Destino = [300, 500]
chefe1Estado = 'parado'
chefe1Contador = 50


if life > 0:
    pygame.mixer.music.load("./sounds/NT.mp3")
    pygame.mixer.music.play(-1)

#Criar o boss
enemy = Boss1(YELLOW)
#Vidas do boss
vidab1 = 10
  
#Colocar o boss acima da tela
enemy.rect.x = chefe1Pos[0]
enemy.rect.y = chefe1Pos[1]
     
#Adicionar o inimigo nas listas de sprites
enemy_list.add(enemy)
all_sprites_list.add(enemy)

#loop boss 1
while not done:
    if life == 0: 
        done = True
    for event in pygame.event.get():
        #Verificar se o jogador fechou a janela
        if event.type == pygame.QUIT:
            exit()
            
        #Verificar as teclas de controle do jogador
        elif event.type == pygame.KEYDOWN:
            #Ajustar a velocidade do jogador de acordo com a tecla pressionada
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
            #Atirar quando o jogador pressiona espaco
            elif event.key == pygame.K_SPACE:
                fire = Fire2()
                #Colocar o tiro no mesmo lugar que o jogador
                fire.rect.x = (player.rect.x) + 22
                fire.rect.y = player.rect.y
                effect = pygame.mixer.Sound('teste_nave2.wav')
                effect.play()
                #Adicionar o tiro nas listas
                all_sprites_list.add(fire)
                fire_list.add(fire)
              
 
        #Verificar se o jogador soltou a tecla
        elif event.type == pygame.KEYUP:
            #Se o jogador soltou as teclas de direcao, zerar a velocidade (nao queremos velocidades infinitas coff coff)
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
 
    if not enemy_list:
        done = True

    #Logica do jogo

    #Mover o Boss
    movBoss1()


    
    #Mover a nave do jogador de acordo com a velocidade 
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    #Delimitar o espaco para o jogador se mover
    if x_coord > 390:
        x_coord = 390

    if y_coord > 542:
        y_coord = 542

    if x_coord < 0:
        x_coord = 0

    if y_coord < 0:
        y_coord =0
 
    
 
    #Mecanicas de tiro
    for fire in fire_list:
 
        #Verificar se acertou um inimigo
        enemy_hit_list = pygame.sprite.spritecollide(fire, enemy_list, False)

        #verificar se ja tirou todas as vidas necessarias do inimigo antes de mata-lo
        if vidab1 < 1:
            enemy_hit_list = pygame.sprite.spritecollide(fire, enemy_list, True)            
 
        #Quando atingir o inimigo, eliminar o tiro e adicionar na pontuacao (score)
        for enemy in enemy_hit_list:
            fire_list.remove(fire)
            all_sprites_list.remove(fire)
            enemy_hit_list.remove(enemy)
            point.play()
            score += 1
            vidab1 -= 1
            
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if fire.rect.y < -10:
            fire_list.remove(fire)
            all_sprites_list.remove(fire)
 
    #Mesmo esquema do tiro, mas agora para ver se o jogador bateu num inimigo 
    #IMPLEMENTAR MORTE!!!!
    for enemy in enemy_list:
        i=random.randrange(100)
        if i == 1: 
            if enemy.rect.y>0:
                efire2 = E_Fire1()
                efire = E_Fire1()
                #Colocar os tiros nas laterais do inimigo
                efire.rect.x = enemy.rect.x +25
                efire.rect.y = enemy.rect.y + 85
                efire2.rect.x = enemy.rect.x + 75
                efire2.rect.y = enemy.rect.y + 85
                #Adicionar os tiros nas listas
                all_sprites_list.add(efire)
                e_fire_list.add(efire) 
                all_sprites_list.add(efire2)
                e_fire_list2.add(efire2) 
                effect = pygame.mixer.Sound('tiroboss1.wav')
                effect.play()  
 
        #Verificar colisao do jogador com o inimigo
        enemy_hit_list = pygame.sprite.spritecollide(player, enemy_list, False)
 
        #Quando houver colisao, tirar vida do jogador
        for enemy in enemy_hit_list:
            x_coord = 150
            y_coord = 530
            hit.play()
            life -= 1
            
 


    for efire in e_fire_list:
 
        #Verificar se acertou o jogador
        player_hit_list = pygame.sprite.spritecollide(efire, player_list, False)
 
        #Quando atingir o jogador, eliminar o tiro e perder vida
        for player in player_hit_list:
            e_fire_list.remove(efire)
            all_sprites_list.remove(efire)
            hit.play()
            life -= 1
            
            player_hit_list.remove(player)
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if efire.rect.y > 610:
            e_fire_list.remove(efire)
            all_sprites_list.remove(efire)

    for efire2 in e_fire_list2:
 
        #Verificar se acertou o jogador
        player_hit_list = pygame.sprite.spritecollide(efire2, player_list, False)
 
        #Quando atingir o jogador, eliminar o tiro e perder vida
        for player in player_hit_list:
            e_fire_list2.remove(efire2)
            all_sprites_list.remove(efire2)
            hit.play()
            life -= 1
            
            player_hit_list.remove(player)
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if efire2.rect.y > 610:
            e_fire_list2.remove(efire)
            all_sprites_list.remove(efire)
   

    #Desenhar a tela

    #Atualizar a lista com todos os sprites
    all_sprites_list.update()
 
    #Limpar a tela
    screen.fill(BLACK)

    #Printar o HUD

    #pontos
    score_surf = my_font.render((str(score)), 1, (255, 255, 255))
    screen.blit(score_surf, score_pos)
    screen.blit(score_txt, (450, 50))
    #vidas
    life_surf = my_font.render((str(life)), 1, (255, 255, 255))
    screen.blit(life_surf, life_pos)
    screen.blit(life_txt, (450, 150))
    #fases
    level_surf = my_font.render("1 - Chefe", 1, (255, 255, 255))
    screen.blit(level_surf, (550, 250))
    screen.blit(level_txt, (450, 250))
    #power ups
    pu_surf = my_font.render(" -- ", 1, (255, 255, 255))
    screen.blit(pu_surf, pu_pos)
    screen.blit(pu_txt, (450, 350))

    # Processar cada estrela do array
    for i in range(len(starArr)):
 
        # Desenhar a estrela
        pygame.draw.circle(screen, WHITE, starArr[i], 2)
 
        # Mover a estrela para baixo 1 pixel
        starArr[i][1] += 1
 
        # Se ela tiver saido da tela
        if starArr[i][1] > 600:
            # Manda de volta um pouco acima da tela
            y = random.randrange(-50, -10)
            starArr[i][1] = y
            # E coloca em outra posicao aleatoria
            x = random.randrange(0, 400)
            starArr[i][0] = x
    # Mesma coisa para os planetas
    for i in range(0,5):
 
        pygame.draw.circle(screen, GREEN, planetArr[i], 22)
 
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x

    for i in range(6,10):
 
        pygame.draw.circle(screen, ORANGE, planetArr[i], 15)
 
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x
    for i in range(11,15):
        pygame.draw.circle(screen, RED, planetArr[i], 8)
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x

 
    #Desenhar todos os sprites
    all_sprites_list.draw(screen)
 
    #Jogar tudo na tela
    pygame.display.flip()
 
    #Limitar a 20 fps (nao queremos um jogo mais impossivel do que ja esta)
    clock.tick(60)

pygame.mixer.music.stop()

done = False

if life > 0:
    life += 1
    


#tiros inimigos sao mais rapidos


if life > 0:
    pygame.mixer.music.load("./sounds/DOPE.mp3")
    pygame.mixer.music.play(-1)

#mais inimigos
for i in range(80):
    #Inimigo
    enemy = Enemy2(BLUE)
 
    #Colocar o inimigo em uma posicao aleatoria acima da tela
    enemy.rect.x = random.randrange(0, 400)
    enemy.rect.y = random.randrange(-8000,0)
 
    #Adicionar o inimigo nas listas de sprites
    enemy_list.add(enemy)
    all_sprites_list.add(enemy)

#Loop fase 2
while not done:
    if life == 0: 
        
        done = True
    for event in pygame.event.get():
        #Verificar se o jogador fechou a janela
        if event.type == pygame.QUIT:
            exit()
            done = True
        #Verificar as teclas de controle do jogador
        elif event.type == pygame.KEYDOWN:
            #Ajustar a velocidade do jogador de acordo com a tecla pressionada
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
            #Atirar quando o jogador pressiona espaco
            elif event.key == pygame.K_SPACE:
                fire = Fire2()
                #Colocar o tiro no mesmo lugar que o jogador
                fire.rect.x = (player.rect.x) + 22
                fire.rect.y = player.rect.y
                #Adicionar o tiro nas listas
                all_sprites_list.add(fire)
                fire_list.add(fire)
                effect = pygame.mixer.Sound('teste_nave2.wav')
                effect.play()    
            
 
        #Verificar se o jogador soltou a tecla
        elif event.type == pygame.KEYUP:
            #Se o jogador soltou as teclas de direcao, zerar a velocidade (nao queremos velocidades infinitas coff coff)
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
 
    if not enemy_list:
        done = True

    #Logica do jogo

    
    #Mover a nave do jogador de acordo com a velocidade 
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    #Delimitar o espaco para o jogador se mover
    if x_coord > 390:
        x_coord = 390

    if y_coord > 542:
        y_coord = 542

    if x_coord < 0:
        x_coord = 0

    if y_coord < 0:
        y_coord =0
 
    #Atualizar a lista com todos os sprites
    all_sprites_list.update()
 
    #Mecanicas de tiro
    for fire in fire_list:
 
        #Verificar se acertou um inimigo
        enemy_hit_list = pygame.sprite.spritecollide(fire, enemy_list, True)
 
        #Quando atingir o inimigo, eliminar o tiro e adicionar na pontuacao (score)
        for enemy in enemy_hit_list:
            fire_list.remove(fire)
            all_sprites_list.remove(fire)
            point.play()
            score += 1
            
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if fire.rect.y < -10:
            fire_list.remove(fire)
            all_sprites_list.remove(fire)
 
    #Mesmo esquema do tiro, mas agora para ver se o jogador bateu num inimigo 
    #IMPLEMENTAR MORTE!!!!
    for enemy in enemy_list:
        i=random.randrange(500)
        if i == 1: 
            if enemy.rect.y>0:
                efire = E_Fire2()
                #Colocar o tiro no mesmo lugar que o inimigo
                efire.rect.x = enemy.rect.x + 21
                efire.rect.y = enemy.rect.y + 48
                #Adicionar o tiro nas listas
                all_sprites_list.add(efire)
                e_fire_list.add(efire) 
 
        #Verificar colisao do jogador com o inimigo
        enemy_hit_list = pygame.sprite.spritecollide(player, enemy_list, True)
 
        #Quando houver colisao, tirar o inimigo e tirar da pontuacao
        #TROCAR PARA VIDA!!!
        for enemy in enemy_hit_list:
            enemy_list.remove(enemy)
            all_sprites_list.remove(enemy)
            hit.play()
            life -= 1
            
 
        #Eliminar os inimigos quando saem da tela (ELES DESCEM! PORTANTO, O Y DEVE SER POSITIVO E MAIOR QUE 600)
        if enemy.rect.y > 615:
            enemy_list.remove(enemy)
            all_sprites_list.remove(enemy)
            #tirar uma vida se passarem
            #life -=1
            

    for efire in e_fire_list:
 
        #Verificar se acertou o jogador
        player_hit_list = pygame.sprite.spritecollide(efire, player_list, False)
 
        #Quando atingir o inimigo, eliminar o tiro e adicionar na pontuacao (score)
        for player in player_hit_list:
            e_fire_list.remove(efire)
            all_sprites_list.remove(efire)
            hit.play()
            life -= 1
            
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if efire.rect.y > 610:
            e_fire_list.remove(efire)
            all_sprites_list.remove(efire)


    #Desenhar a tela
 
    #Limpar a tela
    screen.fill(BLACK)

    #Printar o HUD

    #pontos
    score_surf = my_font.render((str(score)), 1, (255, 255, 255))
    screen.blit(score_surf, score_pos)
    screen.blit(score_txt, (450, 50))
    #vidas
    life_surf = my_font.render((str(life)), 1, (255, 255, 255))
    screen.blit(life_surf, life_pos)
    screen.blit(life_txt, (450, 150))
    #fases
    level_surf = my_font.render("2", 1, (255, 255, 255))
    screen.blit(level_surf, level_pos)
    screen.blit(level_txt, (450, 250))
    #power ups
    pu_surf = my_font.render(" + velocidade tiro ", 1, (255, 255, 255))
    screen.blit(pu_surf, (450,380))
    screen.blit(pu_txt, (450, 350))

    # Processar cada estrela do array
    for i in range(len(starArr)):
 
        # Desenhar a estrela
        pygame.draw.circle(screen, WHITE, starArr[i], 2)
 
        # Mover a estrela para baixo 1 pixel
        starArr[i][1] += 1
 
        # Se ela tiver saido da tela
        if starArr[i][1] > 600:
            # Manda de volta um pouco acima da tela
            y = random.randrange(-50, -10)
            starArr[i][1] = y
            # E coloca em outra posicao aleatoria
            x = random.randrange(0, 400)
            starArr[i][0] = x
    # Mesma coisa para os planetas
    for i in range(0,5):
 
        pygame.draw.circle(screen, GREEN, planetArr[i], 22)
 
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x

    for i in range(6,10):
 
        pygame.draw.circle(screen, ORANGE, planetArr[i], 15)
 
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x
    for i in range(11,15):
        pygame.draw.circle(screen, RED, planetArr[i], 8)
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x

 
    #Desenhar todos os sprites
    all_sprites_list.draw(screen)
 
    #Jogar tudo na tela
    pygame.display.flip()
 
    #Limitar a 20 fps (nao queremos um jogo mais impossivel do que ja esta)
    clock.tick(60)

pygame.mixer.music.stop()
done = False

#Variaveis dos Chefes
chefe2Pos = [100, -100]
chefe2Destino = [300, 500]
chefe2Estado = 'parado'
chefe2Contador = 50


if life > 0:
    pygame.mixer.music.load("./sounds/DNA.mp3")
    pygame.mixer.music.play(-1)

#Criar o boss
enemy = Boss2(YELLOW)
#Vidas do boss
vidab2 = 15
  
#Colocar o inimigo em uma posicao aleatoria acima da tela
#inimigoPos[0]=random.randrange(0, 400)
#inimigoPos[1]=random.randrange(-100, 0)
enemy.rect.x = chefe2Pos[0]
enemy.rect.y = chefe2Pos[1]
     
#Adicionar o inimigo nas listas de sprites
enemy_list.add(enemy)
all_sprites_list.add(enemy)

#loop boss 2
while not done:
    if life == 0: 
        
        done = True
    for event in pygame.event.get():
        #Verificar se o jogador fechou a janela
        if event.type == pygame.QUIT:
            exit()
            done = True
        #Verificar as teclas de controle do jogador
        elif event.type == pygame.KEYDOWN:
            #Ajustar a velocidade do jogador de acordo com a tecla pressionada
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
            #Atirar quando o jogador pressiona espaco
            elif event.key == pygame.K_SPACE:
                #tiro mais rapido
                fire = Fire2()
                #Colocar o tiro no mesmo lugar que o jogador
                fire.rect.x = (player.rect.x) + 22
                fire.rect.y = player.rect.y
                #Adicionar o tiro nas listas
                all_sprites_list.add(fire)
                fire_list.add(fire)  
                effect = pygame.mixer.Sound('teste_nave2.wav')
                effect.play()  
            
 
        #Verificar se o jogador soltou a tecla
        elif event.type == pygame.KEYUP:
            #Se o jogador soltou as teclas de direcao, zerar a velocidade (nao queremos velocidades infinitas coff coff)
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
 
    if not enemy_list:
        done = True

    #Logica do jogo

    #Mover o Boss
    movBoss2()


    
    #Mover a nave do jogador de acordo com a velocidade 
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    #Delimitar o espaco para o jogador se mover
    if x_coord > 390:
        x_coord = 390

    if y_coord > 542:
        y_coord = 542

    if x_coord < 0:
        x_coord = 0

    if y_coord < 0:
        y_coord =0
 
    
 
    #Mecanicas de tiro
    for fire in fire_list:
 
        #Verificar se acertou um inimigo
        enemy_hit_list = pygame.sprite.spritecollide(fire, enemy_list, False)

        #verificar se ja tirou todas as vidas necessarias do inimigo antes de mata-lo
        if vidab2 < 1:
            enemy_hit_list = pygame.sprite.spritecollide(fire, enemy_list, True)            
 
        #Quando atingir o inimigo, eliminar o tiro e adicionar na pontuacao (score)
        for enemy in enemy_hit_list:
            fire_list.remove(fire)
            all_sprites_list.remove(fire)
            enemy_hit_list.remove(enemy)
            point.play()
            score += 1
            vidab2 -= 1
            
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if fire.rect.y < -10:
            fire_list.remove(fire)
            all_sprites_list.remove(fire)
 
    #Mesmo esquema do tiro, mas agora para ver se o jogador bateu num inimigo 
    #IMPLEMENTAR MORTE!!!!
    for enemy in enemy_list:
        i=random.randrange(100)
        if i == 1: 
            if enemy.rect.y>0:
                efire2 = E_Fire1()
                efire = E_Fire1()
                #Colocar os tiros nos lugares certos
                efire.rect.x = enemy.rect.x +25
                efire.rect.y = enemy.rect.y + 85
                efire2.rect.x = enemy.rect.x + 75
                efire2.rect.y = enemy.rect.y + 85
                #Adicionar os tiros nas listas
                all_sprites_list.add(efire)
                e_fire_list.add(efire) 
                all_sprites_list.add(efire2)
                e_fire_list2.add(efire2) 
                effect = pygame.mixer.Sound('tiroboss1.wav')
                effect.play()  
 
        #Verificar colisao do jogador com o inimigo
        enemy_hit_list = pygame.sprite.spritecollide(player, enemy_list, False)
 
        #Quando houver colisao, tirar vida do jogador
        for enemy in enemy_hit_list:
            hit.play()
            x_coord = 150
            y_coord = 530
            life -= 1
            
 


    for efire in e_fire_list:
 
        #Verificar se acertou o jogador
        player_hit_list = pygame.sprite.spritecollide(efire, player_list, False)
 
        #Quando atingir o jogador, eliminar o tiro e perder vida
        for player in player_hit_list:
            e_fire_list.remove(efire)
            all_sprites_list.remove(efire)
            hit.play()
            life -= 1
            
            player_hit_list.remove(player)
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if efire.rect.y > 610:
            e_fire_list.remove(efire)
            all_sprites_list.remove(efire)

    for efire2 in e_fire_list2:
 
        #Verificar se acertou o jogador
        player_hit_list = pygame.sprite.spritecollide(efire2, player_list, False)
 
        #Quando atingir o jogador, eliminar o tiro e perder vida
        for player in player_hit_list:
            e_fire_list2.remove(efire2)
            all_sprites_list.remove(efire2)
            hit.play()
            life -= 1
            
            player_hit_list.remove(player)
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if efire2.rect.y > 610:
            e_fire_list2.remove(efire2)
            all_sprites_list.remove(efire2)
   

    #Desenhar a tela

    #Atualizar a lista com todos os sprites
    all_sprites_list.update()
 
    #Limpar a tela
    screen.fill(BLACK)

    #Printar o HUD

    #pontos
    score_surf = my_font.render((str(score)), 1, (255, 255, 255))
    screen.blit(score_surf, score_pos)
    screen.blit(score_txt, (450, 50))
    #vidas
    life_surf = my_font.render((str(life)), 1, (255, 255, 255))
    screen.blit(life_surf, life_pos)
    screen.blit(life_txt, (450, 150))
    #fases
    level_surf = my_font.render("2 - Chefe", 1, (255, 255, 255))
    screen.blit(level_surf, (550, 250))
    screen.blit(level_txt, (450, 250))
    #power ups
    pu_surf = my_font.render(" + velocidade tiro ", 1, (255, 255, 255))
    screen.blit(pu_surf, (450,380))
    screen.blit(pu_txt, (450, 350))

    # Processar cada estrela do array
    for i in range(len(starArr)):
 
        # Desenhar a estrela
        pygame.draw.circle(screen, WHITE, starArr[i], 2)
 
        # Mover a estrela para baixo 1 pixel
        starArr[i][1] += 1
 
        # Se ela tiver saido da tela
        if starArr[i][1] > 600:
            # Manda de volta um pouco acima da tela
            y = random.randrange(-50, -10)
            starArr[i][1] = y
            # E coloca em outra posicao aleatoria
            x = random.randrange(0, 400)
            starArr[i][0] = x
    # Mesma coisa para os planetas
    for i in range(0,5):
 
        pygame.draw.circle(screen, GREEN, planetArr[i], 22)
 
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x

    for i in range(6,10):
 
        pygame.draw.circle(screen, ORANGE, planetArr[i], 15)
 
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x
    for i in range(11,15):
        pygame.draw.circle(screen, RED, planetArr[i], 8)
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x

 
    #Desenhar todos os sprites
    all_sprites_list.draw(screen)
 
    #Jogar tudo na tela
    pygame.display.flip()
 
    #Limitar a 20 fps (nao queremos um jogo mais impossivel do que ja esta)
    clock.tick(60)

pygame.mixer.music.stop()
done = False
if life > 0:
    life += 1
    


if life > 0:
    pygame.mixer.music.load("./sounds/RUN.mp3")
    pygame.mixer.music.play(-1)

#inimigos sao mais rapidos

#mais inimigos
for i in range(100):
    #Inimigo
    enemy = Enemy3(BLUE)
 
    #Colocar o inimigo em uma posicao aleatoria acima da tela
    enemy.rect.x = random.randrange(0, 400)
    enemy.rect.y = random.randrange(-8000,0)
 
    #Adicionar o inimigo nas listas de sprites
    enemy_list.add(enemy)
    all_sprites_list.add(enemy)

#Loop fase 3
while not done:
    if life == 0: 
        
        done = True
    for event in pygame.event.get():
        #Verificar se o jogador fechou a janela
        if event.type == pygame.QUIT:
            exit()
            done = True
        #Verificar as teclas de controle do jogador
        elif event.type == pygame.KEYDOWN:
            #Ajustar a velocidade do jogador de acordo com a tecla pressionada
            if event.key == pygame.K_LEFT:
                x_speed = -5
            elif event.key == pygame.K_RIGHT:
                x_speed = 5
            elif event.key == pygame.K_UP:
                y_speed = -5
            elif event.key == pygame.K_DOWN:
                y_speed = 5
            #Atirar quando o jogador pressiona espaco
            elif event.key == pygame.K_SPACE:
                fire = Fire3()
                #Colocar o tiro no mesmo lugar que o jogador
                fire.rect.x = (player.rect.x) + 22
                fire.rect.y = player.rect.y
                #Adicionar o tiro nas listas
                all_sprites_list.add(fire)
                fire_list.add(fire) 
                effect = pygame.mixer.Sound('teste_nave2.wav')
                effect.play()   

            
 
        #Verificar se o jogador soltou a tecla
        elif event.type == pygame.KEYUP:
            #Se o jogador soltou as teclas de direcao, zerar a velocidade (nao queremos velocidades infinitas coff coff)
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
 
    if not enemy_list:
        done = True

    #Logica do jogo

    
    #Mover a nave do jogador de acordo com a velocidade 
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    #Delimitar o espaco para o jogador se mover
    if x_coord > 390:
        x_coord = 390

    if y_coord > 542:
        y_coord = 542

    if x_coord < 0:
        x_coord = 0

    if y_coord < 0:
        y_coord =0
 
    #Atualizar a lista com todos os sprites
    all_sprites_list.update()
 
    #Mecanicas de tiro
    for fire in fire_list:
 
        #Verificar se acertou um inimigo
        enemy_hit_list = pygame.sprite.spritecollide(fire, enemy_list, True)
 
        #Quando atingir o inimigo, eliminar o tiro e adicionar na pontuacao (score)
        for enemy in enemy_hit_list:
            fire_list.remove(fire)
            all_sprites_list.remove(fire)
            point.play()
            score += 1
            
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if fire.rect.y < -10:
            fire_list.remove(fire)
            all_sprites_list.remove(fire)
 
    #Mesmo esquema do tiro, mas agora para ver se o jogador bateu num inimigo 
    #IMPLEMENTAR MORTE!!!!
    for enemy in enemy_list:
        i=random.randrange(500)
        if i == 1: 
            if enemy.rect.y>0:
                efire = E_Fire3()
                #Colocar o tiro no mesmo lugar que o inimigo
                efire.rect.x = enemy.rect.x + 21
                efire.rect.y = enemy.rect.y + 48
                #Adicionar o tiro nas listas
                all_sprites_list.add(efire)
                e_fire_list.add(efire) 
 
        #Verificar colisao do jogador com o inimigo
        enemy_hit_list = pygame.sprite.spritecollide(player, enemy_list, True)
 
        #Quando houver colisao, tirar o inimigo e tirar da pontuacao
        #TROCAR PARA VIDA!!!
        for enemy in enemy_hit_list:
            enemy_list.remove(enemy)
            all_sprites_list.remove(enemy)
            hit.play()
            life -= 1
            
 
        #Eliminar os inimigos quando saem da tela (ELES DESCEM! PORTANTO, O Y DEVE SER POSITIVO E MAIOR QUE 600)
        if enemy.rect.y > 615:
            enemy_list.remove(enemy)
            all_sprites_list.remove(enemy)
            #tirar uma vida se passarem
            #life -=1
            

    for efire in e_fire_list:
 
        #Verificar se acertou o jogador
        player_hit_list = pygame.sprite.spritecollide(efire, player_list, False)
 
        #Quando atingir o inimigo, eliminar o tiro e adicionar na pontuacao (score)
        for player in player_hit_list:
            e_fire_list.remove(efire)
            all_sprites_list.remove(efire)
            hit.play()
            life -= 1
            
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if efire.rect.y > 610:
            e_fire_list.remove(efire)
            all_sprites_list.remove(efire)

    #Desenhar a tela
 
    #Limpar a tela
    screen.fill(BLACK)

    #Printar o HUD

    #pontos
    score_surf = my_font.render((str(score)), 1, (255, 255, 255))
    screen.blit(score_surf, score_pos)
    screen.blit(score_txt, (450, 50))
    #vidas
    life_surf = my_font.render((str(life)), 1, (255, 255, 255))
    screen.blit(life_surf, life_pos)
    screen.blit(life_txt, (450, 150))
    #fases
    level_surf = my_font.render("3", 1, (255, 255, 255))
    screen.blit(level_surf, level_pos)
    screen.blit(level_txt, (450, 250))
    #power ups
    pu_surf = my_font.render(" ++ velocidade tiro ", 1, (255, 255, 255))
    pu_surf2 = my_font.render(" + velocidade nave ", 1, (255, 255, 255))
    screen.blit(pu_surf, (450,380))
    screen.blit(pu_surf2, (450,410))
    screen.blit(pu_txt, (450, 350))

    # Processar cada estrela do array
    for i in range(len(starArr)):
 
        # Desenhar a estrela
        pygame.draw.circle(screen, WHITE, starArr[i], 2)
 
        # Mover a estrela para baixo 1 pixel
        starArr[i][1] += 1
 
        # Se ela tiver saido da tela
        if starArr[i][1] > 600:
            # Manda de volta um pouco acima da tela
            y = random.randrange(-50, -10)
            starArr[i][1] = y
            # E coloca em outra posicao aleatoria
            x = random.randrange(0, 400)
            starArr[i][0] = x
    # Mesma coisa para os planetas
    for i in range(0,5):
 
        pygame.draw.circle(screen, GREEN, planetArr[i], 22)
 
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x

    for i in range(6,10):
 
        pygame.draw.circle(screen, ORANGE, planetArr[i], 15)
 
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x
    for i in range(11,15):
        pygame.draw.circle(screen, RED, planetArr[i], 8)
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x

 
    #Desenhar todos os sprites
    all_sprites_list.draw(screen)
 
    #Jogar tudo na tela
    pygame.display.flip()
 
    #Limitar a 20 fps (nao queremos um jogo mais impossivel do que ja esta)
    clock.tick(60)

pygame.mixer.music.stop()
done = False

#Variaveis dos Chefes
chefe3Pos = [100, -100]
chefe3Destino = [300, 500]
chefe3Estado = 'parado'
chefe3Contador = 30


if life > 0:
    pygame.mixer.music.load("./sounds/INU.mp3")
    pygame.mixer.music.play(-1)

#Criar o boss
enemy = Boss3(YELLOW)
#vidas do boss
vidab3=10
  
#Colocar o inimigo em uma posicao aleatoria acima da tela
#inimigoPos[0]=random.randrange(0, 400)
#inimigoPos[1]=random.randrange(-100, 0)
enemy.rect.x = chefe3Pos[0]
enemy.rect.y = chefe3Pos[1]
     
#Adicionar o inimigo nas listas de sprites
enemy_list.add(enemy)
all_sprites_list.add(enemy)

#loop boss 3
while not done:
    if life == 0: 
        
        done = True
    for event in pygame.event.get():
        #Verificar se o jogador fechou a janela
        if event.type == pygame.QUIT:
            exit()
            done = True
        #Verificar as teclas de controle do jogador
        elif event.type == pygame.KEYDOWN:
            #Ajustar a velocidade do jogador de acordo com a tecla pressionada
            if event.key == pygame.K_LEFT:
                x_speed = -5
            elif event.key == pygame.K_RIGHT:
                x_speed = 5
            elif event.key == pygame.K_UP:
                y_speed = -5
            elif event.key == pygame.K_DOWN:
                y_speed = 5
            #Atirar quando o jogador pressiona espaco
            elif event.key == pygame.K_SPACE:
                fire = Fire3()
                #Colocar o tiro no mesmo lugar que o jogador
                fire.rect.x = (player.rect.x) + 22
                fire.rect.y = player.rect.y
                #Adicionar o tiro nas listas
                all_sprites_list.add(fire)
                fire_list.add(fire)  
                effect = pygame.mixer.Sound('teste_nave2.wav')
                effect.play()  
            
 
        #Verificar se o jogador soltou a tecla
        elif event.type == pygame.KEYUP:
            #Se o jogador soltou as teclas de direcao, zerar a velocidade (nao queremos velocidades infinitas coff coff)
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
 
    if not enemy_list:
        done = True

    #Logica do jogo

    #Mover o Boss
    movBoss3()


    
    #Mover a nave do jogador de acordo com a velocidade 
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    #Delimitar o espaco para o jogador se mover
    if x_coord > 390:
        x_coord = 390

    if y_coord > 542:
        y_coord = 542

    if x_coord < 0:
        x_coord = 0

    if y_coord < 0:
        y_coord =0
 
    
 
    #Mecanicas de tiro
    for fire in fire_list:
 
         #Verificar se acertou um inimigo
        enemy_hit_list = pygame.sprite.spritecollide(fire, enemy_list, False)

        #verificar se ja tirou todas as vidas necessarias do inimigo antes de mata-lo
        if vidab3 < 1:
            enemy_hit_list = pygame.sprite.spritecollide(fire, enemy_list, True)            
 
        #Quando atingir o inimigo, eliminar o tiro e adicionar na pontuacao (score)
        for enemy in enemy_hit_list:
            fire_list.remove(fire)
            all_sprites_list.remove(fire)
            enemy_hit_list.remove(enemy)
            point.play()
            score += 1
            vidab3 -= 1
             
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if fire.rect.y < -10:
            fire_list.remove(fire)
            all_sprites_list.remove(fire)
 
    #Mesmo esquema do tiro, mas agora para ver se o jogador bateu num inimigo 
    #IMPLEMENTAR MORTE!!!!
    for enemy in enemy_list:
        i=random.randrange(50)
        if i == 1: 
            if enemy.rect.y>0:
                efire = E_Fire2()
                efire2 = E_Fire2()
                efire3 = E_Fire2()
                #Colocar os tiros nas laterais do inimigo
                efire.rect.x = enemy.rect.x +25
                efire.rect.y = enemy.rect.y + 85
                efire2.rect.x = enemy.rect.x + 75
                efire2.rect.y = enemy.rect.y + 85
                efire3.rect.x = enemy.rect.x + 50
                efire3.rect.y = enemy.rect.y + 70
                #Adicionar os tiros nas listas
                all_sprites_list.add(efire)
                e_fire_list.add(efire) 
                all_sprites_list.add(efire2)
                e_fire_list2.add(efire2)
                all_sprites_list.add(efire3)
                e_fire_list3.add(efire3) 
                effect = pygame.mixer.Sound('tiroboss1.wav')
                effect.play()  
 
        #Verificar colisao do jogador com o inimigo
        enemy_hit_list = pygame.sprite.spritecollide(player, enemy_list, False)
 
        #Quando houver colisao, tirar uma vida do jogador
        for enemy in enemy_hit_list:
            x_coord = 150
            y_coord = 530
            hit.play()
            life -= 1
            
 


    for efire in e_fire_list:
 
        #Verificar se acertou o jogador
        player_hit_list = pygame.sprite.spritecollide(efire, player_list, False)
 
        #Quando atingir o jogador, eliminar o tiro e perder vida
        for player in player_hit_list:
            e_fire_list.remove(efire)
            all_sprites_list.remove(efire)
            hit.play()
            life -= 1
            
            player_hit_list.remove(player)
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if efire.rect.y > 610:
            e_fire_list.remove(efire)
            all_sprites_list.remove(efire)

    for efire2 in e_fire_list2:
 
        #Verificar se acertou o jogador
        player_hit_list = pygame.sprite.spritecollide(efire2, player_list, False)
 
        #Quando atingir o jogador, eliminar o tiro e perder vida
        for player in player_hit_list:
            e_fire_list2.remove(efire2)
            all_sprites_list.remove(efire2)
            hit.play()
            life -= 1
            
            player_hit_list.remove(player)
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if efire2.rect.y > 610:
            e_fire_list2.remove(efire2)
            all_sprites_list.remove(efire2)
   

    for efire3 in e_fire_list3:
 
        #Verificar se acertou o jogador
        player_hit_list = pygame.sprite.spritecollide(efire3, player_list, False)
 
        #Quando atingir o jogador, eliminar o tiro e perder vida
        for player in player_hit_list:
            e_fire_list3.remove(efire3)
            all_sprites_list.remove(efire3)
            hit.play()
            life -= 1
            
            player_hit_list.remove(player)
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if efire3.rect.y > 610:
            e_fire_list3.remove(efire3)
            all_sprites_list.remove(efire3)

    #Desenhar a tela

    #Atualizar a lista com todos os sprites
    all_sprites_list.update()
 
    #Limpar a tela
    screen.fill(BLACK)

    #Printar o HUD

    #pontos
    score_surf = my_font.render((str(score)), 1, (255, 255, 255))
    screen.blit(score_surf, score_pos)
    screen.blit(score_txt, (450, 50))
    #vidas
    life_surf = my_font.render((str(life)), 1, (255, 255, 255))
    screen.blit(life_surf, life_pos)
    screen.blit(life_txt, (450, 150))
    #fases
    level_surf = my_font.render("3 - Chefe", 1, (255, 255, 255))
    screen.blit(level_surf, (550, 250))
    screen.blit(level_txt, (450, 250))
    #power ups
    pu_surf = my_font.render(" ++ velocidade tiro ", 1, (255, 255, 255))
    pu_surf2 = my_font.render(" + velocidade nave ", 1, (255, 255, 255))
    screen.blit(pu_surf, (450,380))
    screen.blit(pu_surf2, (450,410))
    screen.blit(pu_txt, (450, 350))

    # Processar cada estrela do array
    for i in range(len(starArr)):
 
        # Desenhar a estrela
        pygame.draw.circle(screen, WHITE, starArr[i], 2)
 
        # Mover a estrela para baixo 1 pixel
        starArr[i][1] += 1
 
        # Se ela tiver saido da tela
        if starArr[i][1] > 600:
            # Manda de volta um pouco acima da tela
            y = random.randrange(-50, -10)
            starArr[i][1] = y
            # E coloca em outra posicao aleatoria
            x = random.randrange(0, 400)
            starArr[i][0] = x
    # Mesma coisa para os planetas
    for i in range(0,5):
 
        pygame.draw.circle(screen, GREEN, planetArr[i], 22)
 
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x

    for i in range(6,10):
 
        pygame.draw.circle(screen, ORANGE, planetArr[i], 15)
 
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x
    for i in range(11,15):
        pygame.draw.circle(screen, RED, planetArr[i], 8)
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x

 
    #Desenhar todos os sprites
    all_sprites_list.draw(screen)
 
    #Jogar tudo na tela
    pygame.display.flip()
 
    #Limitar a 20 fps (nao queremos um jogo mais impossivel do que ja esta)
    clock.tick(60)

pygame.mixer.music.stop()

done = False
if life > 0:
    life += 1
    


#tiros inimigos sao mais rapidos




if life > 0:
    pygame.mixer.music.load("./sounds/BST.mp3")
    pygame.mixer.music.play(-1)

#mais inimigos
for i in range(120):
    #Inimigo
    enemy = Enemy4(BLUE)
 
    #Colocar o inimigo em uma posicao aleatoria acima da tela
    enemy.rect.x = random.randrange(0, 400)
    enemy.rect.y = random.randrange(-8000,0)
 
    #Adicionar o inimigo nas listas de sprites
    enemy_list.add(enemy)
    all_sprites_list.add(enemy)

#Loop fase 4
while not done:
    if life == 0: 
        
        done = True
    for event in pygame.event.get():
        #Verificar se o jogador fechou a janela
        if event.type == pygame.QUIT:
            exit()
            
        #Verificar as teclas de controle do jogador
        elif event.type == pygame.KEYDOWN:
            #Ajustar a velocidade do jogador de acordo com a tecla pressionada
            if event.key == pygame.K_LEFT:
                x_speed = -6
            elif event.key == pygame.K_RIGHT:
                x_speed = 6
            elif event.key == pygame.K_UP:
                y_speed = -6
            elif event.key == pygame.K_DOWN:
                y_speed = 6
            #Atirar quando o jogador pressiona espaco
            elif event.key == pygame.K_SPACE:
                fire = Fire3()
                #Colocar o tiro no mesmo lugar que o jogador
                fire.rect.x = (player.rect.x) + 22
                fire.rect.y = player.rect.y
                #Adicionar o tiro nas listas
                all_sprites_list.add(fire)
                fire_list.add(fire) 
                effect = pygame.mixer.Sound('teste_nave2.wav')
                effect.play()   
            
 
        #Verificar se o jogador soltou a tecla
        elif event.type == pygame.KEYUP:
            #Se o jogador soltou as teclas de direcao, zerar a velocidade (nao queremos velocidades infinitas coff coff)
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
 
    if not enemy_list:
        done = True

    #Logica do jogo

    
    #Mover a nave do jogador de acordo com a velocidade 
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    #Delimitar o espaco para o jogador se mover
    if x_coord > 390:
        x_coord = 390

    if y_coord > 542:
        y_coord = 542

    if x_coord < 0:
        x_coord = 0

    if y_coord < 0:
        y_coord =0
 
    #Atualizar a lista com todos os sprites
    all_sprites_list.update()
 
    #Mecanicas de tiro
    for fire in fire_list:
 
        #Verificar se acertou um inimigo
        enemy_hit_list = pygame.sprite.spritecollide(fire, enemy_list, True)
 
        #Quando atingir o inimigo, eliminar o tiro e adicionar na pontuacao (score)
        for enemy in enemy_hit_list:
            fire_list.remove(fire)
            all_sprites_list.remove(fire)
            point.play()
            score += 1
            
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if fire.rect.y < -10:
            fire_list.remove(fire)
            all_sprites_list.remove(fire)
 
    #Mesmo esquema do tiro, mas agora para ver se o jogador bateu num inimigo 
    #IMPLEMENTAR MORTE!!!!
    for enemy in enemy_list:
        i=random.randrange(500)
        if i == 1: 
            if enemy.rect.y>0:
                efire = E_Fire3()
                #Colocar o tiro no mesmo lugar que o inimigo
                efire.rect.x = enemy.rect.x + 21
                efire.rect.y = enemy.rect.y + 48
                #Adicionar o tiro nas listas
                all_sprites_list.add(efire)
                e_fire_list.add(efire) 
 
        #Verificar colisao do jogador com o inimigo
        enemy_hit_list = pygame.sprite.spritecollide(player, enemy_list, True)
 
        #Quando houver colisao, tirar o inimigo e tirar da pontuacao
        #TROCAR PARA VIDA!!!
        for enemy in enemy_hit_list:
            enemy_list.remove(enemy)
            all_sprites_list.remove(enemy)
            hit.play()
            life -= 1
            
 
        #Eliminar os inimigos quando saem da tela (ELES DESCEM! PORTANTO, O Y DEVE SER POSITIVO E MAIOR QUE 600)
        if enemy.rect.y > 615:
            enemy_list.remove(enemy)
            all_sprites_list.remove(enemy)
            #tirar uma vida se passarem
            #life -=1
            

    for efire in e_fire_list:
 
        #Verificar se acertou o jogador
        player_hit_list = pygame.sprite.spritecollide(efire, player_list, False)
 
        #Quando atingir o inimigo, eliminar o tiro e adicionar na pontuacao (score)
        for player in player_hit_list:
            e_fire_list.remove(efire)
            all_sprites_list.remove(efire)
            hit.play()
            life -= 1
            
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if efire.rect.y > 610:
            e_fire_list.remove(efire)
            all_sprites_list.remove(efire)


    #Desenhar a tela
 
    #Limpar a tela
    screen.fill(BLACK)

        #Printar o HUD

    #pontos
    score_surf = my_font.render((str(score)), 1, (255, 255, 255))
    screen.blit(score_surf, score_pos)
    screen.blit(score_txt, (450, 50))
    #vidas
    life_surf = my_font.render((str(life)), 1, (255, 255, 255))
    screen.blit(life_surf, life_pos)
    screen.blit(life_txt, (450, 150))
    #fases
    level_surf = my_font.render((str(4)), 1, (255, 255, 255))
    screen.blit(level_surf, level_pos)
    screen.blit(level_txt, (450, 250))
    #power ups
    pu_surf = my_font.render(" ++ velocidade tiro ", 1, (255, 255, 255))
    pu_surf2 = my_font.render(" ++ velocidade nave ", 1, (255, 255, 255))
    screen.blit(pu_surf, (450,380))
    screen.blit(pu_surf2, (450,410))
    screen.blit(pu_txt, (450, 350))

    # Processar cada estrela do array
    for i in range(len(starArr)):
 
        # Desenhar a estrela
        pygame.draw.circle(screen, WHITE, starArr[i], 2)
 
        # Mover a estrela para baixo 1 pixel
        starArr[i][1] += 1
 
        # Se ela tiver saido da tela
        if starArr[i][1] > 600:
            # Manda de volta um pouco acima da tela
            y = random.randrange(-50, -10)
            starArr[i][1] = y
            # E coloca em outra posicao aleatoria
            x = random.randrange(0, 400)
            starArr[i][0] = x
    # Mesma coisa para os planetas
    for i in range(0,5):
 
        pygame.draw.circle(screen, GREEN, planetArr[i], 22)
 
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x

    for i in range(6,10):
 
        pygame.draw.circle(screen, ORANGE, planetArr[i], 15)
 
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x
    for i in range(11,15):
        pygame.draw.circle(screen, RED, planetArr[i], 8)
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x

 
    #Desenhar todos os sprites
    all_sprites_list.draw(screen)
 
    #Jogar tudo na tela
    pygame.display.flip()
 
    #Limitar a 20 fps (nao queremos um jogo mais impossivel do que ja esta)
    clock.tick(60)

pygame.mixer.music.stop()
done = False

#Variaveis dos Chefes
chefe4Pos = [100, -100]
chefe4Destino = [300, 500]
chefe4Estado = 'parado'
chefe4Contador = 20


if life > 0:
    pygame.mixer.music.load("./sounds/ASIF.mp3")
    pygame.mixer.music.play(-1)

#Criar o boss
enemy = Boss4(YELLOW)
#vidas do boss
vidab4 = 15
  
#Colocar o inimigo em uma posicao aleatoria acima da tela
#inimigoPos[0]=random.randrange(0, 400)
#inimigoPos[1]=random.randrange(-100, 0)
enemy.rect.x = chefe4Pos[0]
enemy.rect.y = chefe4Pos[1]
     
#Adicionar o inimigo nas listas de sprites
enemy_list.add(enemy)
all_sprites_list.add(enemy)

#loop boss 4
while not done:
    if life == 0: 
        
        done = True
    for event in pygame.event.get():
        #Verificar se o jogador fechou a janela
        if event.type == pygame.QUIT:
            exit()
            done = True
        #Verificar as teclas de controle do jogador
        elif event.type == pygame.KEYDOWN:
            #Ajustar a velocidade do jogador de acordo com a tecla pressionada
            if event.key == pygame.K_LEFT:
                x_speed = -6
            elif event.key == pygame.K_RIGHT:
                x_speed = 6
            elif event.key == pygame.K_UP:
                y_speed = -6
            elif event.key == pygame.K_DOWN:
                y_speed = 6
            
            #Atirar quando o jogador pressiona espaco
            elif event.key == pygame.K_SPACE:
                fire = Fire3()
                #Colocar o tiro no mesmo lugar que o jogador
                fire.rect.x = (player.rect.x) + 22
                fire.rect.y = player.rect.y
                #Adicionar o tiro nas listas
                all_sprites_list.add(fire)
                fire_list.add(fire)
                effect = pygame.mixer.Sound('teste_nave2.wav')
                effect.play()   
            
 
        #Verificar se o jogador soltou a tecla
        elif event.type == pygame.KEYUP:
            #Se o jogador soltou as teclas de direcao, zerar a velocidade (nao queremos velocidades infinitas coff coff)
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
 
    if not enemy_list:
        done = True

    #Logica do jogo

    #Mover o Boss
    movBoss4()


    
    #Mover a nave do jogador de acordo com a velocidade 
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    #Delimitar o espaco para o jogador se mover
    if x_coord > 390:
        x_coord = 390

    if y_coord > 542:
        y_coord = 542

    if x_coord < 0:
        x_coord = 0

    if y_coord < 0:
        y_coord =0
 
    
 
    #Mecanicas de tiro
    for fire in fire_list:
 
         #Verificar se acertou um inimigo
        enemy_hit_list = pygame.sprite.spritecollide(fire, enemy_list, False)

        #verificar se ja tirou todas as vidas necessarias do inimigo antes de mata-lo
        if vidab4 < 1:
            enemy_hit_list = pygame.sprite.spritecollide(fire, enemy_list, True)            
 
        #Quando atingir o inimigo, eliminar o tiro e adicionar na pontuacao (score)
        for enemy in enemy_hit_list:
            fire_list.remove(fire)
            all_sprites_list.remove(fire)
            enemy_hit_list.remove(enemy)
            point.play()
            score += 1
            vidab4 -= 1
            
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if fire.rect.y < -10:
            fire_list.remove(fire)
            all_sprites_list.remove(fire)
 
    #Mesmo esquema do tiro, mas agora para ver se o jogador bateu num inimigo 
    #IMPLEMENTAR MORTE!!!!
    for enemy in enemy_list:
        i=random.randrange(50)
        if i == 1: 
            if enemy.rect.y>0:
                efire = E_Fire3()
                efire2 = E_Fire3()
                efire3 = E_Fire3()
                #Colocar os tiros nas laterais do inimigo
                efire.rect.x = enemy.rect.x +25
                efire.rect.y = enemy.rect.y + 85
                efire2.rect.x = enemy.rect.x + 75
                efire2.rect.y = enemy.rect.y + 85
                efire3.rect.x = enemy.rect.x + 50
                efire3.rect.y = enemy.rect.y + 70
                #Adicionar os tiros nas listas
                all_sprites_list.add(efire)
                e_fire_list.add(efire) 
                all_sprites_list.add(efire2)
                e_fire_list2.add(efire2)
                all_sprites_list.add(efire3)
                e_fire_list3.add(efire3)
                effect = pygame.mixer.Sound('tiroboss1.wav')
                effect.play()  
 
        #Verificar colisao do jogador com o inimigo
        enemy_hit_list = pygame.sprite.spritecollide(player, enemy_list, False)
 
        #Quando houver colisao, tirar vida do jogador
        for enemy in enemy_hit_list:
            x_coord = 150
            y_coord = 530
            hit.play()
            
            life -= 1
            
 


    for efire in e_fire_list:
 
        #Verificar se acertou o jogador
        player_hit_list = pygame.sprite.spritecollide(efire, player_list, False)
 
        #Quando atingir o jogador, eliminar o tiro e perder vida
        for player in player_hit_list:
            e_fire_list.remove(efire)
            all_sprites_list.remove(efire)
            hit.play()
            life -= 1
            
            player_hit_list.remove(player)
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if efire.rect.y > 610:
            e_fire_list.remove(efire)
            all_sprites_list.remove(efire)

    for efire2 in e_fire_list2:
 
        #Verificar se acertou o jogador
        player_hit_list = pygame.sprite.spritecollide(efire2, player_list, False)
 
        #Quando atingir o jogador, eliminar o tiro e perder vida
        for player in player_hit_list:
            e_fire_list2.remove(efire2)
            all_sprites_list.remove(efire2)
            hit.play()
            life -= 1
            
            player_hit_list.remove(player)
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if efire2.rect.y > 610:
            e_fire_list2.remove(efire2)
            all_sprites_list.remove(efire2)
   

    for efire3 in e_fire_list3:
 
        #Verificar se acertou o jogador
        player_hit_list = pygame.sprite.spritecollide(efire3, player_list, False)
 
        #Quando atingir o jogador, eliminar o tiro e perder vida
        for player in player_hit_list:
            e_fire_list3.remove(efire3)
            all_sprites_list.remove(efire3)
            hit.play()
            life -= 1
            
            player_hit_list.remove(player)
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if efire3.rect.y > 610:
            e_fire_list3.remove(efire3)
            all_sprites_list.remove(efire3)

    #Desenhar a tela

    #Atualizar a lista com todos os sprites
    all_sprites_list.update()
 
    #Limpar a tela
    screen.fill(BLACK)

        #Printar o HUD

    #pontos
    score_surf = my_font.render((str(score)), 1, (255, 255, 255))
    screen.blit(score_surf, score_pos)
    screen.blit(score_txt, (450, 50))
    #vidas
    life_surf = my_font.render((str(life)), 1, (255, 255, 255))
    screen.blit(life_surf, life_pos)
    screen.blit(life_txt, (450, 150))
    #fases
    level_surf = my_font.render("4 - Chefe", 1, (255, 255, 255))
    screen.blit(level_surf, (550, 250))
    screen.blit(level_txt, (450, 250))
    #power ups
    pu_surf = my_font.render(" ++ velocidade tiro ", 1, (255, 255, 255))
    pu_surf2 = my_font.render(" ++ velocidade nave ", 1, (255, 255, 255))
    screen.blit(pu_surf, (450,380))
    screen.blit(pu_surf2, (450,410))
    screen.blit(pu_txt, (450, 350))

    # Processar cada estrela do array
    for i in range(len(starArr)):
 
        # Desenhar a estrela
        pygame.draw.circle(screen, WHITE, starArr[i], 2)
 
        # Mover a estrela para baixo 1 pixel
        starArr[i][1] += 1
 
        # Se ela tiver saido da tela
        if starArr[i][1] > 600:
            # Manda de volta um pouco acima da tela
            y = random.randrange(-50, -10)
            starArr[i][1] = y
            # E coloca em outra posicao aleatoria
            x = random.randrange(0, 400)
            starArr[i][0] = x
    # Mesma coisa para os planetas
    for i in range(0,5):
 
        pygame.draw.circle(screen, GREEN, planetArr[i], 22)
 
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x

    for i in range(6,10):
 
        pygame.draw.circle(screen, ORANGE, planetArr[i], 15)
 
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x
    for i in range(11,15):
        pygame.draw.circle(screen, RED, planetArr[i], 8)
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x

 
    #Desenhar todos os sprites
    all_sprites_list.draw(screen)
 
    #Jogar tudo na tela
    pygame.display.flip()
 
    #Limitar a 20 fps (nao queremos um jogo mais impossivel do que ja esta)
    clock.tick(60)

pygame.mixer.music.stop()
done = False
if life > 0:    
    life += 1
    

#Variaveis dos Chefes
chefeFinalPos = [100, -100]
chefeFinalDestino = [300, 500]
chefeFinalEstado = 'parado'
chefeFinalContador = 50


if life > 0:
    pygame.mixer.music.load("./sounds/FIRE.mp3")
    pygame.mixer.music.play(-1)

#Criar o boss
enemy = BossFinal(YELLOW)
#vidas do boss
vidabfinal = 30
  
#Colocar o inimigo em uma posicao aleatoria acima da tela
#inimigoPos[0]=random.randrange(0, 400)
#inimigoPos[1]=random.randrange(-100, 0)
enemy.rect.x = chefeFinalPos[0]
enemy.rect.y = chefeFinalPos[1]
     
#Adicionar o inimigo nas listas de sprites
enemy_list.add(enemy)
all_sprites_list.add(enemy)

#loop boss final
while not done:
    if life == 0: 
        
        done = True
    for event in pygame.event.get():
        #Verificar se o jogador fechou a janela
        if event.type == pygame.QUIT:
            exit()
            done = True
        #Verificar as teclas de controle do jogador
        elif event.type == pygame.KEYDOWN:
            #Ajustar a velocidade do jogador de acordo com a tecla pressionada
            if event.key == pygame.K_LEFT:
                x_speed = -6
            elif event.key == pygame.K_RIGHT:
                x_speed = 6
            elif event.key == pygame.K_UP:
                y_speed = -6
            elif event.key == pygame.K_DOWN:
                y_speed = 6
            #Atirar quando o jogador pressiona espaco
            elif event.key == pygame.K_SPACE:
                fire = Fire3()
                fire2 = Fire3()
                #Colocar o tiro no mesmo lugar que o jogador
                fire.rect.x = (player.rect.x) + 15
                fire.rect.y = player.rect.y
                fire2.rect.x = (player.rect.x) + 30
                fire2.rect.y = player.rect.y
                #Adicionar o tiro nas listas
                all_sprites_list.add(fire)
                fire_list.add(fire)
                all_sprites_list.add(fire2)
                fire_list2.add(fire2) 
                effect = pygame.mixer.Sound('teste_nave2.wav')
                effect.play()  
            
 
        #Verificar se o jogador soltou a tecla
        elif event.type == pygame.KEYUP:
            #Se o jogador soltou as teclas de direcao, zerar a velocidade (nao queremos velocidades infinitas coff coff)
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
 
    if not enemy_list:
        done = True

    #Logica do jogo

    #Mover o Boss
    movBossFinal()


    
    #Mover a nave do jogador de acordo com a velocidade 
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    #Delimitar o espaco para o jogador se mover
    if x_coord > 390:
        x_coord = 390

    if y_coord > 542:
        y_coord = 542

    if x_coord < 0:
        x_coord = 0

    if y_coord < 0:
        y_coord =0
 
    
 
    #Mecanicas de tiro
    for fire in fire_list:
 
         #Verificar se acertou um inimigo
        enemy_hit_list = pygame.sprite.spritecollide(fire, enemy_list, False)

        #verificar se ja tirou todas as vidas necessarias do inimigo antes de mata-lo
        if vidabfinal < 1:
            enemy_hit_list = pygame.sprite.spritecollide(fire, enemy_list, True)            
 
        #Quando atingir o inimigo, eliminar o tiro e adicionar na pontuacao (score)
        for enemy in enemy_hit_list:
            fire_list.remove(fire)
            all_sprites_list.remove(fire)
            enemy_hit_list.remove(enemy)
            point.play()
            score += 1
            vidabfinal -= 1
            
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if fire.rect.y < -10:
            fire_list.remove(fire)
            all_sprites_list.remove(fire)

    for fire2 in fire_list2:
 
         #Verificar se acertou um inimigo
        enemy_hit_list = pygame.sprite.spritecollide(fire2, enemy_list, False)

        #verificar se ja tirou todas as vidas necessarias do inimigo antes de mata-lo
        if vidabfinal < 1:
            enemy_hit_list = pygame.sprite.spritecollide(fire2, enemy_list, True)            
 
        #Quando atingir o inimigo, eliminar o tiro e adicionar na pontuacao (score)
        for enemy in enemy_hit_list:
            fire_list2.remove(fire2)
            all_sprites_list.remove(fire2)
            enemy_hit_list.remove(enemy)
            point.play()
            score += 1
            vidabfinal -= 1
            
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if fire2.rect.y < -10:
            fire_list2.remove(fire2)
            all_sprites_list.remove(fire2)
 
    #Mesmo esquema do tiro, mas agora para ver se o jogador bateu num inimigo 
    #IMPLEMENTAR MORTE!!!!
    for enemy in enemy_list:
        i=random.randrange(50)
        if i == 1: 
            if enemy.rect.y>0:
                efire = E_Fire3()
                efire2 = E_Fire3()
                efire3 = E_Fire3()
                efire4 = E_Fire3()
                #Colocar os tiros nas laterais do inimigo
                efire.rect.x = enemy.rect.x 
                efire.rect.y = enemy.rect.y + 130
                efire2.rect.x = enemy.rect.x + 25
                efire2.rect.y = enemy.rect.y + 150
                efire3.rect.x = enemy.rect.x + 75
                efire3.rect.y = enemy.rect.y + 150
                efire4.rect.x = enemy.rect.x + 100
                efire4.rect.y = enemy.rect.y + 130
                #Adicionar os tiros nas listas
                all_sprites_list.add(efire)
                e_fire_list.add(efire) 
                all_sprites_list.add(efire2)
                e_fire_list2.add(efire2)
                all_sprites_list.add(efire3)
                e_fire_list3.add(efire3) 
                all_sprites_list.add(efire4)
                e_fire_list4.add(efire4) 
                effect = pygame.mixer.Sound('tiroboss1.wav')
                effect.play()  
 
        #Verificar colisao do jogador com o inimigo
        enemy_hit_list = pygame.sprite.spritecollide(player, enemy_list, False)
 
        #Quando houver colisao, tirar vida do jogador
        for enemy in enemy_hit_list:
            x_coord = 150
            y_coord = 530
            hit.play()
            life -= 1
            
 


    for efire in e_fire_list:
 
        #Verificar se acertou o jogador
        player_hit_list = pygame.sprite.spritecollide(efire, player_list, False)
 
        #Quando atingir o jogador, eliminar o tiro e perder vida
        for player in player_hit_list:
            e_fire_list.remove(efire)
            all_sprites_list.remove(efire)
            hit.play()
            life -= 1
            
            player_hit_list.remove(player)
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if efire.rect.y > 610:
            e_fire_list.remove(efire)
            all_sprites_list.remove(efire)

    for efire2 in e_fire_list2:
 
        #Verificar se acertou o jogador
        player_hit_list = pygame.sprite.spritecollide(efire2, player_list, False)
 
        #Quando atingir o jogador, eliminar o tiro e perder vida
        for player in player_hit_list:
            e_fire_list2.remove(efire2)
            all_sprites_list.remove(efire2)
            hit.play()
            life -= 1
            
            player_hit_list.remove(player)
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if efire2.rect.y > 610:
            e_fire_list2.remove(efire2)
            all_sprites_list.remove(efire2)
   

    for efire3 in e_fire_list3:
 
        #Verificar se acertou o jogador
        player_hit_list = pygame.sprite.spritecollide(efire3, player_list, False)
 
        #Quando atingir o jogador, eliminar o tiro e perder vida
        for player in player_hit_list:
            e_fire_list3.remove(efire3)
            all_sprites_list.remove(efire3)
            hit.play()
            life -= 1
            
            player_hit_list.remove(player)
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if efire3.rect.y > 610:
            e_fire_list3.remove(efire3)
            all_sprites_list.remove(efire3)

    for efire4 in e_fire_list4:
 
        #Verificar se acertou o jogador
        player_hit_list = pygame.sprite.spritecollide(efire4, player_list, False)
 
        #Quando atingir o jogador, eliminar o tiro e perder vida
        for player in player_hit_list:
            e_fire_list4.remove(efire4)
            all_sprites_list.remove(efire4)
            hit.play()
            life -= 1
            
            player_hit_list.remove(player)
 
        #Eliminar o tiro quando sai da tela (nao queremos comer toda a nossa ram coff coff)
        if efire4.rect.y > 610:
            e_fire_list4.remove(efire4)
            all_sprites_list.remove(efire4)

    #Desenhar a tela

    #Atualizar a lista com todos os sprites
    all_sprites_list.update()
 
    #Limpar a tela
    screen.fill(BLACK)

        #Printar o HUD

    #pontos
    score_surf = my_font.render((str(score)), 1, (255, 255, 255))
    screen.blit(score_surf, score_pos)
    screen.blit(score_txt, (450, 50))
    #vidas
    life_surf = my_font.render((str(life)), 1, (255, 255, 255))
    screen.blit(life_surf, life_pos)
    screen.blit(life_txt, (450, 150))
    #fases
    level_surf = my_font.render("Final!", 1, (255, 255, 255))
    screen.blit(level_surf, level_pos)
    screen.blit(level_txt, (450, 250))
    #power ups
    pu_surf = my_font.render(" ++ velocidade tiro ", 1, (255, 255, 255))
    pu_surf2 = my_font.render(" ++ velocidade nave ", 1, (255, 255, 255))
    pu_surf3 = my_font.render(" Tiro duplo ", 1, (255, 255, 255))
    screen.blit(pu_surf, (450,380))
    screen.blit(pu_surf2, (450,410))
    screen.blit(pu_surf3, (450,440))
    screen.blit(pu_txt, (450, 350))

    # Processar cada estrela do array
    for i in range(len(starArr)):
 
        # Desenhar a estrela
        pygame.draw.circle(screen, WHITE, starArr[i], 2)
 
        # Mover a estrela para baixo 1 pixel
        starArr[i][1] += 1
 
        # Se ela tiver saido da tela
        if starArr[i][1] > 600:
            # Manda de volta um pouco acima da tela
            y = random.randrange(-50, -10)
            starArr[i][1] = y
            # E coloca em outra posicao aleatoria
            x = random.randrange(0, 400)
            starArr[i][0] = x
    # Mesma coisa para os planetas
    for i in range(0,5):
 
        pygame.draw.circle(screen, GREEN, planetArr[i], 22)
 
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x

    for i in range(6,10):
 
        pygame.draw.circle(screen, ORANGE, planetArr[i], 15)
 
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x
    for i in range(11,15):
        pygame.draw.circle(screen, RED, planetArr[i], 8)
        planetArr[i][1] += 1
 
        if planetArr[i][1] > 600:
            y = random.randrange(-50, -10)
            planetArr[i][1] = y
            x = random.randrange(0, 400)
            planetArr[i][0] = x

 
    #Desenhar todos os sprites
    all_sprites_list.draw(screen)
 
    #Jogar tudo na tela
    pygame.display.flip()
 
    #Limitar a 20 fps (nao queremos um jogo mais impossivel do que ja esta)
    clock.tick(60)




if life <= 0:
    gameover = pygame.mixer.Sound('./sounds/gameover.wav')
    gameover.play() 
    
    gameover_img =  pygame.image.load("./images/gameover.png")
    screen.fill(BLACK)
    screen.blit(gameover_img, (0,0))
    pygame.display.flip()

    pygame.time.wait(2000)

else:
    victory = pygame.mixer.Sound('./sounds/LP.wav')
    victory.play(1)
    joia_img =  pygame.image.load("./images/joia.png")
    screen.fill(BLACK)
    screen.blit(joia_img, (0,0))
    pygame.display.flip()
    pygame.time.wait(3000) 
    illidanj_img =  pygame.image.load("./images/illidanj.png")
    screen.fill(BLACK)
    screen.blit(illidanj_img, (0,0))
    pygame.display.flip()
    pygame.time.wait(3000)
    final_img =  pygame.image.load("./images/final.png")
    screen.fill(BLACK)
    screen.blit(final_img, (0,0))
    pygame.display.flip()
    pygame.time.wait(3000)
    
    victory_img =  pygame.image.load("./images/victory.png")
    screen.fill(BLACK)
    screen.blit(victory_img, (0,0))
    pygame.display.flip()

    pygame.time.wait(3000)

screen.fill(BLACK)
score_surf = end_font.render((str(score)), 1, (255, 255, 255))
screen.blit(score_surf, (300, 350))
screen.blit(score_txt2, (200, 250))
pygame.display.flip()

pygame.time.wait(3000)


#Fechar nosso joguinho 
exit()