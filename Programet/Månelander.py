# -*- coding: ansi -*-
#Romskip prosjekt (med Autopilot og manuell styring)
#Dato      : Vår 2018
#Forfatter : Fredrik R. Johannessen og Eivind Strand Harboe

#------IMPORTER--------
"""Importerer alle moduler som trengs i programmet"""

from pylab import *
import pygame
from pygame.locals import *
from vm01 import *
from vm02 import *
from vm03 import *
pygame.init()


#----------------------------------------------

RØD=(255,0,0)
GRØNN=(0,255,0)
BLÅ=(0,0,255)
GUL=(255,255,0)
HVIT=(255,255,255)
SVART=(0,0,0)
SILVER=(192,192,192)

#----------------GRAFIKK OG KONSTANTER-------------------
"""Inneholder bildene som blir brukt av pygame og gravitasjonskonstanten"""

gm = 1.62
moon=pygame.image.load('144074-0.png') 
lander=pygame.image.load('pixel_moon_lander_by_aslansilva-d34xrwc.png') 
landerødelagt=pygame.image.load('pixel_moon_lander_by_aslansilva-d34xrwc-ødelagt.png')
flameMed=pygame.image.load('Untitled-1.png')    
flameMax=pygame.image.load('Untitled-2.png')
flameMin=pygame.image.load('Untitled-3.png')
swe=pygame.image.load('144074-0-swe.png')
rcs=pygame.image.load('Flamme.png')
rcs1=pygame.image.load('Flamme1.png')


#-------------------------------------------

#-----------------------ROMSKIP------------------------
"""Initierer data om romskip, definerer difflikningene som beskriver bevegelsen
og regner ut pos og fart til romskip etter gitt tid"""

def initromskip(y0,vy0, x0, vx0,ax0) : #Initsierer pos og fart til romskip
    global y, vy , x, vx, ax
    y = y0 ; vy = vy0 ; x=x0 ; vx=vx0; ax=ax0
#end initromskip
    
def f(t,y,vy) : #Definerer difflikning 1
    return vy

def g(t,y,vy) : #Definerer difflikning 2
    return S/mTotal-gm

def nyttromskip() : #Bruker Euler2 for å finne neste punkt og fart
    global t, y, vy, x, ax, vx
    t,y,vy = euler2nestepunkt(f,g,t,y,vy,dt)
    x, vx = xnestepunkt(x, vx, ax, dt)
#end nyttromskip

def getaks() : #Finner akselerasjonen ved hjelp av kraft, masse og Newtons 2.lov
    S = getS()
    m = getm()
    return S/m-gm
#end getaks

#-----------------------------------------------

#------------------------- MASSER ------------------
"""Definerer og oppdaterer massene til fuelen og romskipet, og finner total masse"""

def initmasser(fuel) : #Initsierer masser til fartøyet
    global mTom, mFuel, mTotal
    mTom = 7030
    mFuel = fuel
    mTotal = mTom + mFuel
#end initmasser

def nyemasser() : #Oppdaterer massene med fuelforbruket
    global mFuel, mTotal
    mFuel = mFuel -((fuelforbrukmax*Sprosent/100)+2)*dt #Finner mengden fuel utfra motorbrenningen
    mTotal = mTom + mFuel
#end nyemasser

def getm() : #Finner totalmasse
    return mTotal
#end getm

#--------------------------------------------------------

#------------------------ MOTOR ----------------------
"""Finner motorkraften til enhver tid, ut ifra hva ønsket motorkraft er"""  

def initmotor() : #Initsierer motorkraft, og bensinforbruk
    global Sprosent,Smax,fuelforbrukmax,S
    Smax = 45030
    Sprosent = 100
    fuelforbrukmax = 15
    S = Smax*Sprosent/100
#end initmotor

def getS() :
    return S
#end getS

def nymotor(Sønsket): #Regner ut motorkraft
    global mFuel,Sprosent,S
    if mFuel<=0: #Skyvekraften blir 0, siden tom for fuel
        S=0 ; mFuel=0 ; Sprosent=0 ; return
    if Sønsket==0: #Slår av motoren, hvis Sønsket er 0
        S=0 ; Sprosent=0 ; return
    økning=25*dt #prosentvis økning i motorkraft
    if Sønsket>Sprosent-1: #øker motorkraften
        Sprosent+=økning
    elif Sønsket<Sprosent+1: #reduserer motorkraft
        Sprosent-=økning
    if Sprosent>100: #Forhindrer at motorkraften går over 100%
        Sprosent=100
    elif Sprosent<10: #Forhindrer at motorkraften går under 10%. Vi kan ikke slå av og på motoren 
        Sprosent=10
    S=Smax*Sprosent/100
#end nymotor
    
def slutt(): 
    global x,y,vy
    if vy<-1: #Hvis landingen var raskere enn 1 m/s krasjer skipet
        krasj(vy,y,x)
        pygame.display.update()
    else: #alt annet, som vil si tregere enn 1 m/s så får brukeren en melding om vellyket landing
        landing(vy)
        pygame.display.update()
    for e in pygame.event.get():
        if e.type == QUIT:
            pygameSlutt()
        if e.type==pygame.KEYDOWN:
                if e.key==K_r:
                    mode='u'
                    

#---------------------------------------------------

#-------------- SKRIV OG TEGN -----------------------
"""Omhandler alt om skriving og tegning til pygame"""

def initinstrumenter() : #Initsierer Pygame 
    global flate
    flate=lagVindu(450,650,(22,22,38),"Månelander Simulering")
    pygame.display.update()
#end initinstrumenter

def visinstrumenter() : #Oppdaterer instrumentene
    ay = getaks()
    setFontsize(20)
    rektangel(0,0,250,648,False)
    s = "TID  : " + str(round(t)) + "s"
    skrivE(s,30,40)
    rektangel(25,70,150,100,False)
    s = "ALT  : " + str(round(y)) + "m"
    skrivE(s,30,80)
    s = "SPD  : " + str(round(vy, 1))
    skrivE(s,30,110)
    s = "AKS  : " + str(round(ay, 1))
    skrivE(s,30,140)
    
    rektangel(25,190,150,67,False)
    s = "FUEL  : " + str(round(mFuel))
    skrivE(s,30,200)
    s = "MOTOR  : " + str(round(Sprosent)) + "%"
    skrivE(s,30,230)
    
    rektangel(25,280,150,100,False)
    s = "AKS x  : " + str(round(ax))
    skrivE(s,30,290)
    s = "SPD x  : " + str(round(vx,4))
    skrivE(s,30,320)
    s = "POS x  : " + str(round(x))
    skrivE(s,30,350)
    
    rektangel(200,70, 20,310, False)
    rektangel(200,380, 20, - (310/100)*Sprosent, True)
    print (Sprosent)
    
    
#end visinstrumenter

def tegnromskip(xvindu,yvindu) : #Tegner romskip ved hjelp av importerte bilder
    flate.blit(lander,(xvindu-30,yvindu-64)) #Tegner romskipet 
    if Sprosent>80: #Hvis motorkraften er mer enn 80% brukes maxflame grafikken 
        flate.blit(flameMax,(xvindu-5,yvindu-19))
    elif Sprosent>40 and Sprosent<80: #Bruker medflame grafikken
        flate.blit(flameMed,(xvindu-3,yvindu-19))
    elif Sprosent>4 and Sprosent<40: #Bruker minflame grafikken
        flate.blit(flameMin,(xvindu-2,yvindu-19))
    if ax<0:
        flate.blit(rcs,(xvindu+17,yvindu-49))
    elif ax>0:
        flate.blit(rcs1,(xvindu-28,yvindu-47))
#end tegnromskip

def tegnrute(y,x) : #Tegner rektangele og månen/stjernehimmelen
    global xvindu, yvindu
    flate.blit(moon,(250,0)) #Tegner måneoverflaten og stjernehimmelen
    yvindu = 600-0.22*y
    xvindu = 350+x
    tegnromskip(xvindu,yvindu) #Kjører tegnromskip og tegner romskipet
#end tegnrute

#-------------------------------------------------

#--------------- AUTOPILOT -------------------
"""Styrer motorkraften automatisk slik at månelanderen lander
trygt hver gang"""

Sønsket = 100 #ønsker 100% motorkraft

def fartønsket(y) : #definerer ønsket fart etter høyde på romskipet
    if y>2000 : return -100
    elif y>1500 : return -80
    elif y>1000 : return -50
    elif y>500: return -40
    elif y>250: return -30
    elif y>150: return -17
    elif y>50: return -10
    elif y>25: return -7
    elif y>6: return -2
    else : return -0.5 
#end fartønsket

def autopilot(y,vy) : #Styrer motorkraften
    global Sønsket
    ønsketfart = fartønsket(y)
    #Bruker bare P i PID-regulator
    feilfart = vy-ønsketfart
    kp = 10
    Sønsket = -kp*feilfart+25
    if Sønsket>100 : Sønsket=100 #forhindrer at Sønsket kommer utenfor definisjonsområdet
    elif Sønsket<10 : Sønsket=10
#end autopilot

#------------------------------------

#--------KRASJ OG LANDING--------------
"""Skriver ulike beskjeder, basert på om månelanderen
krasjet eller landet"""

def krasj(vy,y,x): #Hvis landeren krasjer endres litt av det grafiske og dte skrives en ny beskjed
    global xvindu, yvindu
    fargegammel = getFarge()
    setFarge(BLÅ)
    s='Fysen, det ser ut som' 
    skrivE((s),15,470)
    s='svenskene har tuklet' 
    skrivE((s),15,490)
    s='med motoren din.' 
    skrivE((s),15,510)
    s='Hastigheten ved treff:' 
    skrivE((s),15,530)
    s=(str(round(vy,2)))+'m/s'
    skrivE(s,15,550)
    flate.blit(swe,(250,0))
    flate.blit(landerødelagt,(xvindu-38,yvindu-64))
    pygame.display.update()
    
    
#end krasj

def landing(vy): #Den lander, og det skrives en annen beskjed
    skrivE(('GRATULERER!'),15,470)    
    skrivE(('Månelanderen har landet'),15,490)
    skrivE(('med hastigheten: '),15,510)
    skrivE((str(round(vy,1))),186,510)
    skrivE(('m/s'),225,510)
#end landing

#---------------------------------------------
    
    
class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
    
#----------------- HOVEDPROGRAM -----------------------
"""Hovedprogrammet, her kjøres alle funskjonene vi ahr definert ovenfor"""

t = 0 ; dt = 0.02 #Definerer tiden og dt

initromskip(2500,randint(-140,-110), randint(-20,20),randint(-4,4),0) #Initsierer programmet
initmasser(1000)
initmotor()
initinstrumenter()

mode='u' #setter moden til vent

knapp=button(RØD, 200,200,200,200,'Knapp')

while mode == 'u' or 'a' or 'm' or't' : #Hovedløkke: Hovedprogrammet kjøres så lenge landeren er over overflaten

                    
    while mode=='a' and y>0: #Underløkke 2: Hvis vi ønsket auto og skipet er over bakken, kjøres programmet
        blankSkjerm() #Blanker skjermen
        nyttromskip() #Finner ny posisjon og fart
        nyemasser() #Finner de nye massene
        fartønsket(y) #Sjekker hva farten bør være
        autopilot(y,vy) #Kjører autopiloten som regner ut hva motorkraften bør være
        tegnrute(y,x) #Tegner rute, som ogsåå tegner bakgrunnen og alle deler av romskipet
        nymotor(Sønsket) #øker eller senker motorkraften
        visinstrumenter() #Tegner alle instrumenter
        pygame.display.update() 
        while y <= 0:
            knapp.draw(flate)
            for e in pygame.event.get(): 
                if e.type == QUIT :
                    pygameSlutt()
                if e.type==pygame.KEYDOWN:
                    if e.key==K_r:
                        print('pppppp')
                        setFarge(RØD)
                        blankSkjerm()
                        skrivE(('Trykk: A for autopilot/M for manuell'),50,300)
                        skrivE(('Ved manuell: '),153,320)
                        skrivE(('Bruk piltastene for å kontrollere'),65,340) #Spør om bruker vil ha autopilot eller manuell styring
                        initromskip(2500,randint(-140,-110), 0,0,0) #Initsierer programmet
                        initmasser(1000)
                        initmotor()
                        t=0
                        pygame.display.update()
                        dt = 0.02
                        for e in pygame.event.get() :
                            if e.type==pygame.KEYDOWN:
                                if e.key==K_a:
                                    mode='a'
                            if e.type==pygame.KEYDOWN:
                                if e.key==K_m:
                                    mode='m'
                            if e.type == QUIT :
                                pygameSlutt() 
            
                          
            slutt()
            
            
                        
        for e in pygame.event.get(): 
            if e.type == QUIT :
                pygameSlutt()
            if e.type==pygame.KEYDOWN:
                if e.key==K_r:
                    mode='u'
            if e.type==pygame.KEYDOWN:
                if e.key==K_1:
                    dt = 0.02
            if e.type==pygame.KEYDOWN:
                if e.key==K_2:
                    dt = 0.05
            if e.type==pygame.KEYDOWN:
                if e.key==K_3:
                    dt = 0.2
                           
    while mode=='m' and y>0: #Underløkke 3: Hvis vi ønsket manuell styring og skipet er over bakken, kjøres programmet
        if e.type==pygame.KEYDOWN: 
            if e.key==K_UP: #Når vi ønsker å øke motorkraft 
                Sønsket+=.5
            elif e.key==K_DOWN: #Når vi ønsker å senke motorkraft
                Sønsket-=.5
            if e.key==K_RIGHT: #Når vi ønsker å øke motorkraft 
                ax=2
                print(ax, vx)
            elif e.key==K_LEFT: #Når vi ønsker å senke motorkraft
                ax=-2
                print(ax, vx)
        blankSkjerm() #Programmet er helt likt som auto, bortsett fra at vi ikke kjører noen deler av autopiloten.
        nyttromskip()
        nyemasser()
        tegnrute(y,x)
        nymotor(Sønsket)
        visinstrumenter()
        pygame.display.update()
        ax=0
        while y <= 0:
            slutt()
            for e in pygame.event.get(): 
                if e.type == QUIT :
                    pygameSlutt()
                if e.type==pygame.KEYDOWN:
                    if e.key==K_r:
                        setFarge(RØD)
                        blankSkjerm()
                        skrivE(('Trykk: A for autopilot/M for manuell'),50,300)
                        skrivE(('Ved manuell: '),153,320)
                        skrivE(('Bruk piltastene for å kontrollere'),65,340) #Spør om bruker vil ha autopilot eller manuell styring
                        initromskip(2500,randint(-140,-110), 0,0,0) #Initsierer programmet
                        initmasser(1000)
                        initmotor()
                        t=0
                        pygame.display.update()
                        dt = 0.02
                        for e in pygame.event.get() :
                            if e.type==pygame.KEYDOWN:
                                if e.key==K_a:
                                    mode='a'
                            if e.type==pygame.KEYDOWN:
                                if e.key==K_m:
                                    mode='m'
                            if e.type == QUIT :
                                pygameSlutt() 
                        
        for e in pygame.event.get():
            
            if e.type==pygame.KEYDOWN:
                if e.key==K_1:
                    dt = 0.02
            if e.type==pygame.KEYDOWN:
                if e.key==K_2:
                    dt = 0.05
            if e.type==pygame.KEYDOWN:
                if e.key==K_3:
                    dt = 0.2
            if e.type == QUIT :
                pygameSlutt()
            if e.type==pygame.KEYDOWN:
                if e.key==K_r:
                    mode='u'
                    initromskip(2500,randint(-140,-110), 0,0,0) #Initsierer programmet
                    initmasser(1000)
                    initmotor()
                    initinstrumenter()
                    
            pos=pygame.mouse.get_pos()
            
            if e.type == QUIT :
                    pygameSlutt()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if knapp.isOver(pos):
                    print('pikk')
            if e.type == QUIT :
                pygameSlutt()

    while mode=='u': #Underløkke 1: Programmet venter på at bruker skal svare
        blankSkjerm()
        skrivE(('Trykk: A for autopilot/M for manuell'),50,300)
        skrivE(('Ved manuell: '),153,320)
        skrivE(('Bruk piltastene for å kontrollere'),65,340) #Spør om bruker vil ha autopilot eller manuell styring
        initromskip(2500,randint(-140,-110), 0,0,0) #Initsierer programmet
        initmasser(1000)
        initmotor()
        t=0
        knapp.draw(flate, False)
        for e in pygame.event.get():
            pos=pygame.mouse.get_pos()
            if e.type==pygame.KEYDOWN:
                if e.key==K_a:
                    mode='a'
            if e.type==pygame.KEYDOWN:
                if e.key==K_m:
                        mode='m'
                if e.type == QUIT :
                    pygameSlutt()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if knapp.isOver(pos):
                    print('pikk')
            if e.type == QUIT :
                pygameSlutt()
        pygame.display.update()
        dt = 0.02


    while mode == 't': #Landeren har landet, så en sluttmelding skrives og vinduet oppdateres konstant, slik at det kan lukkes
        print('while t')
        knapp.draw(flate)
        if vy<-1: #Hvis landingen var raskere enn 1 m/s krasjer skipet
            krasj(vy,y,x)
            pygame.display.update()
        else: #alt annet, som vil si tregere enn 1 m/s så får brukeren en melding om vellyket landing
            landing(vy)
            pygame.display.update()
        for e in pygame.event.get():
            if e.type == QUIT:
                pygameSlutt()
            
            pos=pygame.mouse.get_pos()
            
            if e.type == QUIT :
                    pygameSlutt()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if knapp.isOver(pos):
                    mode='u'
            if e.type == QUIT :
                pygameSlutt()
#end While
#-----------PROGRAM SLUTT---------------
        
        
        