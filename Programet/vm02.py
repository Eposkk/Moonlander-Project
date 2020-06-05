""" Dokumentasjon av vm2
vm2=valler modul nr.2
Denne modulen har med pygame å gjøre.
Den inneholder farger, størrelse på skrift,
tykkelse på linjer og gjør det lettere å
tegne og skrive på vinduet eller flaten.
"""

import pygame, sys

"""Farger som konstanter"""
RØD=(255,0,0)
GRØNN=(0,255,0)
BLÅ=(0,0,255)
GUL=(255,255,0)
HVIT=(255,255,255)
SVART=(0,0,0)
SILVER=(192,192,192)

fontsize=20
farge=RØD
fargeBG=SILVER
tykkelse=2

def blankSkjerm():
    flate.fill(fargeBG)

def setFargeBG(farge):
    """Skifter farge på vindet/flaten """
    global fargeBG
    fargeBG=farge
    flate.fill(farge)

def lagVindu(lengde, høyde, fargevindu, vtekst):
    """Lager et vindu eller flate som vi kan
    skrive og tegne på """
    global flate, fargeBG
    flate=pygame.display.set_mode((lengde,høyde))
    flate.fill(fargevindu)
    fargeBG=fargevindu
    pygame.display.set_caption(vtekst)
    pygame.display.update()
    return flate

def setFontsize(fontsizen):
    """Setter størrelse på skrift """    
    global fontsize
    fontsize=fontsizen

def setFarge(f):
    """Setter fargen som skrives/tegnes med """
    global farge
    farge=f

def setTykkelse(tykkelsen):
    global tykkelse
    tykkelse=tykkelsen

def getFargeBG():
    """Finner nåværende bakgrunnsfarge """
    return fargeBG

def getFontsize():
    """Finner nåværende skriftstørrelse"""
    return getFontsize

def getFarge():
    """Finner nåværende bakgrunnsfarge """
    return farge

def getTykkelse():
    return tykkelse
    
def pygameSlutt():
    """Avslutter Pygame og programmet pent """
    pygame.quit()
    sys.exit()

def skriv(flate, s, fontsize, farge, fargeBG, x, y):
    """Med denne kan vi skrive litt tekst på flaten,
    der vi ønsker, med ønsket farge og størrelse"""
    fontObj=pygame.font.Font('freesansbold.ttf', fontsize)
    tekstFlateObj=fontObj.render(s,True,farge,fargeBG)
    tekstRectObj=tekstFlateObj.get_rect()
    tekstRectObj.left=x
    tekstRectObj.top=y
    flate.blit(tekstFlateObj, tekstRectObj)

def skrivE(s,x,y):
    """Kan skrive en tekst der vi ønsker.
    Fargen og størrelsen må være bestemt tidligere"""
    global flate, fontsize
    fontObj=pygame.font.Font('LEMONMILK-Regular.otf', 16)
    tekstFlateObj=fontObj.render(s,True,farge,fargeBG)
    tekstRectObj=tekstFlateObj.get_rect()
    tekstRectObj.left=x
    tekstRectObj.top=y
    flate.blit(tekstFlateObj, tekstRectObj)    

def getTegn(e):
    """Finner tegnet når vi kjenner
    tasten som er trykket ned """
    if e.key==pygame.K_1: return '1'
    elif e.key==pygame.K_2: return '2'
    elif e.key==pygame.K_3: return '3'
    elif e.key==pygame.K_4: return '4'
    elif e.key==pygame.K_5: return '5'
    elif e.key==pygame.K_6: return '6'
    elif e.key==pygame.K_7: return '7'
    elif e.key==pygame.K_8: return '8'
    elif e.key==pygame.K_9: return '9'
    elif e.key==pygame.K_0: return '0'
    elif e.key==pygame.K_q: return 'q'
    elif e.key==pygame.K_w: return 'w'
    elif e.key==pygame.K_e: return 'e'
    elif e.key==pygame.K_r: return 'r'
    elif e.key==pygame.K_t: return 't'
    elif e.key==pygame.K_y: return 'y'
    elif e.key==pygame.K_u: return 'u'
    elif e.key==pygame.K_i: return 'i'
    elif e.key==pygame.K_o: return 'o'
    elif e.key==pygame.K_p: return 'p'
    elif e.key==pygame.K_a: return 'a'
    elif e.key==pygame.K_s: return 's'
    elif e.key==pygame.K_d: return 'd'
    elif e.key==pygame.K_f: return 'f'
    elif e.key==pygame.K_g: return 'g'
    elif e.key==pygame.K_h: return 'h'
    elif e.key==pygame.K_j: return 'j'
    elif e.key==pygame.K_k: return 'k'
    elif e.key==pygame.K_l: return 'l'
    elif e.key==pygame.K_z: return 'z'
    elif e.key==pygame.K_x: return 'x'
    elif e.key==pygame.K_c: return 'c'
    elif e.key==pygame.K_v: return 'v'
    elif e.key==pygame.K_b: return 'b'
    elif e.key==pygame.K_n: return 'n'
    elif e.key==pygame.K_m: return 'm'
    elif e.key==59: return 'ø'
    elif e.key==39: return 'æ'
    elif e.key==91: return 'å'
    
def linjeFraTil(xStart,yStart,xSlutt,ySlutt):
    """Tegner linje fra start til slutt med
    gjeldende farge og tykkelse"""
    pygame.draw.line(flate,farge,(xStart,yStart),(xSlutt,ySlutt),tykkelse)

def rektangel(x,y,lengde,høyde,fyll):
    """Tegner rektangel med øverste venstre hjøre i
    punktet (x,y). Når parameteren "fyll"==False betyr
    vanlig rektangel, mens True betyr at rektangelet fylles"""
    if fyll==True:
        pygame.draw.rect(flate, farge, (x,y,lengde,høyde))
    else:
        pygame.draw.rect(flate,farge,(x,y,lengde,høyde), tykkelse)

def sirkel(xSenter,ySenter,radien,fyll):
    """Tegner sirkel. Hvis fyll==True så fylles sirkelen
    ellers så tegnes med gjeldende tykkelse"""
    xSenter=round(xSenter)
    ySenter=round(ySenter)
    radien=round(radien)
    if fyll==False:
        pygame.draw.circle(flate,farge,(xSenter,ySenter),radien, tykkelse)
    else:
        pygame.draw.circle(flate,farge,(xSenter,ySenter),radien)    
    
    

