subor=open('spokojnost.txt','r',encoding='utf-8')
spokojny=[]
nespokojny=[]
poc=0
for riadok in subor:
    poc+=1
    riadok=riadok.strip()
    riadok=riadok.split(' ')
    if riadok[1]=='áno':
        riadok=riadok[0].split(':')
        spokojny.append(int(riadok[0]))
    else:
        riadok=riadok[0].split(':')
        nespokojny.append(int(riadok[0]))
pocet_s=max(spokojny)
pocet_n=min(nespokojny)
percento=len(spokojny)/poc*100
percenton=len(nespokojny)/poc*100
print('Percento spokojnosti',percento)
print('Percento nespokojnosti',percenton)
print('Celkovy pocet vyjadreni je', poc)
print('Najviac spokojnich je o ',pocet_s,' hodine')
print('Najmenej spokojnich je o ',pocet_n,' hodine')
