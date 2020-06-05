#vm03
#Forfatter: Eivnd Strand Harboe
#Dato : Thu Mar  1 10:30:48 2018

from pylab import *

def euler1(f,t0,x0,tSlutt,dt):
    #Eulers metode på en ODE med funksjon x(t)
    t=t0;x=x0 #Lokale Variabler initieseres
    tL=[t];xL=[x] #Initsierer listene
    while t<=tSlutt: 
        F=f(t,x) #Stigning i dette punktet
        x=x+F*dt #x-verdi til neste Punkt
        t=t+dt #neste Tidspunkt
        tL.append(t); xL.append(x) #Fornyer listene
    return(tL, xL) #Returnerer

def heun1(f,t0,x0,tSlutt,dt):
    #Heuns metode på en ODE med funksjon x(t)
    t=t0;x=x0 #Lokale Variabler initieseres
    tL=[t];xL=[x] #Initsierer listene
    while t<=tSlutt:
        F1=f(t,x) #Stigning i dette punkt
        F2=f(t+dt,x+F1*dt) # Stigning i neste punkt
        F=(F1+F2)/2 #Gjennomsnittsverdien for stigning mellom dette og neste punkt
        x=x+F*dt #x-verdi til neste Punkt
        t=t+dt #neste Tidspunkt
        tL.append(t); xL.append(x) #Fornyer listene
    return(tL, xL) #Returnerer

def euler2nestepunkt(f,g,t,x,y,dt):
    F=f(t,x,y);G=g(t,x,y)
    x=x+F*dt; y=y+G*dt; t=t+dt
    return (t,x,y)

def xnestepunkt(x,vx,ax,dt):
    vx=vx+ax*dt
    x=x+vx*dt+0.5*ax*dt**2
    return (x, vx)

def heun2nestepunkt(f,g,t,x,y,dt):
    F1=f(t,x,y);G1=g(t,x,y)
    F2=f(t+dt,x+F1*dt,y+G1*dt);G2=g(t+dt,x+F1*dt,y+G1*dt)
    F=(F1*F2)/2;G=(G1*G2)/2
    x=x+F*dt; y=y+G*dt; t=t+dt
    return (t,x,y)

def euler2(f,g,t0,x0,y0,tSlutt,dt):
    t=t0; x=x0; y=y0
    tL=[t]; xL=[x];yL=[y]
    while t<=tSlutt:
        F=f(t,x,y);G=g(t,x,y)
        x=x+F*dt; y=y+G*dt; t=t+dt
        tL.append(t);xL.append(x);yL.append(y)
    return(tL,xL,yL)

def heun2(f,g,t0,x0,y0,tSlutt,dt):
    t=t0; x=x0; y=y0
    tL=[t]; xL=[x];yL=[y]
    while t<=tSlutt:
        F1=f(t,x,y);G1=g(t,x,y)
        F2=f(t+dt,x+F1*dt,y+G1*dt)
        G2=g(t+dt,x+F1*dt,y+G1*dt)
        F=(F1+F2)/2;G=(G1+G2)/2
        x=x+F*dt; y=y+G*dt; t=t+dt
        tL.append(t);xL.append(x);yL.append(y)
    return(tL,xL,yL)

def euler3(f,g,h,t0,x0,y0,z0,tSlutt,dt):
    t=t0 ; x=x0 ; y=y0 ; z=z0
    tL=[t] ; xL=[x] ; yL=[y] ; zL=[z]
    while t<=tSlutt:
        F=f(t,x,y,z) ; G=g(t,x,y,z) ; H=h(t,x,y,z) 
        x=x+F*dt ; y=y+G*dt ; z=z+H*dt ; t=t+dt
        tL.append(t) ; xL.append(x) ; yL.append(y) ; zL.append(z)
    return(tL, xL, yL, zL)

def heun3(f,g,h,t0,x0,y0,z0,tSlutt,dt):
    t=t0; x=x0; y=y0; z=z0
    tL=[t]; xL=[x];yL=[y];zL=[z]
    while t<=tSlutt:
        F1=f(t,x,y,z);G1=g(t,x,y,z);H1=h(t,x,y,z)
        F2=f(t+dt,x+F1*dt,y+G1*dt,z+H1*dt)
        G2=g(t+dt,x+F1*dt,y+G1*dt,z+H1*dt)
        H2=h(t+dt,x+F1*dt,y+G1*dt,z+H1*dt)
        F=(F1+F2)/2;G=(G1+G2)/2;H=(H1+H2)/2
        x=x+F*dt; y=y+G*dt;z=z+H*dt; t=t+dt
        tL.append(t);xL.append(x);yL.append(y);zL.append(z)
    return(tL,xL,yL,zL)

def euler4(f,g,h,i,t0,x0,y0,z0,u0,tSlutt,dt):
    t=t0 ; x=x0 ; y=y0 ; z=z0 ; u=u0
    tL=[t] ; xL=[x] ; yL=[y] ; zL=[z] ; uL=[u]
    while t<=tSlutt:
        F=f(t,x,y,z,u) ; G=g(t,x,y,z,u) ; H=h(t,x,y,z,u) ; I=i(t,x,y,z,u)
        x=x+F*dt ; y=y+G*dt ; z=z+H*dt ; u=u+I*dt ; t=t+dt
        tL.append(t) ; xL.append(x) ; yL.append(y) ; zL.append(z) ; uL.append(u)
    return(tL, xL, yL, zL, uL)
#end euler4

def heun4(f,g,h,u,t0,x0,y0,z0,u0,tSlutt,dt):
    t=t0; x=x0; y=y0; z=z0;u=u0
    tL=[t]; xL=[x];yL=[y];zL=[z];uL=[u]
    while t<=tSlutt:
        F1=f(t,x,y,z,u);G1=g(t,x,y,z,u);H1=h(t,x,y,z,u);I1=i(t,x,y,z,u)
        F2=f(t+dt,x+F1*dt,y+G1*dt,z+H1*dt,u+I1*dt)
        G2=g(t+dt,x+F1*dt,y+G1*dt,z+H1*dt,u+I1*dt)
        H2=h(t+dt,x+F1*dt,y+G1*dt,z+H1*dt,u+I1*dt)
        I2=i(t+dt,x+F1*dt,y+G1*dt,z+H1*dt,u+I1*dt)
        F=(F1+F2)/2;G=(G1+G2)/2;H=(H1+H2)/2;I=(I1+I2)/2
        x=x+F*dt; y=y+G*dt;z=z+H*dt;u=u+I*dt;t=t+dt
        tL.append(t);xL.append(x);yL.append(y);zL.append(z);uL.append(u)
    return(tL,xL,yL,zL,uL)

def rk41(f,xStart,yStart,xSlutt,h):
    x=xStart;y=yStart
    xL=[x];yL=[y]
    while x<=xSlutt :
        F1=f(x,y)
        F2=f(x+h/2,y+h/2*F1)
        F3=f(x+h/2,y+F2*h/2)
        F4=f(x+h,y+h*F3)
        y=y+h/6*(F1+2*F2+2*F3+F4)
        x=x+h
        xL.append(x);yL.append(y)
    return xL,yL

def funksjonsverdi(x,xL,yL):
    """Returnerer funksjonsverdien y når argumentet x ligger mellom
    to x-verdier i listen xL. Vi regner at det er rett linje mellom 
    punktene"""
    sisteindeks=len(xL)-1
    if x<xL[0]:
        return "feil"
    elif x>xL[sisteindeks]:
        return "feil"
    else:
        i=0
        while x>xL[i]:
            i=i+1
            if i==0: return yL[0] #Nå er x mellom xL[i-1] og xL[i]
            k=(yL[i]-yL[i-1])/(xL[i]-xL[i-1])
        return round(k*x-k*xL[i]+yL[i],7)
#end funksjonsverdi
     
def skriv2lister(tL,xL,fra,kommentar):
    for i in range(0, len(tL)):
        if tL[i]>= fra:
            print(round(tL[i],4),(round(xL[i],4)))
    print(kommentar)

def skriv3lister(tL,xL,yL,fra,kommentar):
    for i in range(0, len(tL)):
        if tL[i]>= fra:
            print((round(tL[i],4)),(round(xL[i],4)),(round(yL[i],4)))
    print(kommentar)

def skriv4lister(tL,xL,yL,zL,fra,kommentar):
    for i in range(0, len(tL)):
        if tL[i]>= fra:
            print((round(tL[i],4)),(round(xL[i],4)),(round(yL[i],4)),(round(zL[i],4)))
    print(kommentar)

def skriv5lister(tL,xL,yL,zL,uL,fra,kommentar):
    for i in range(0, len(tL)):
        if tL[i]>= fra:
            print((round(tL[i],4)),(round(xL[i],4)),(round(yL[i],4)),(round(zL[i],4)),(round(uL[i],4)))
    print(kommentar)



            
