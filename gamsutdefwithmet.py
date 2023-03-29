tools = ['gunting','kertas','batu']


# header
def header():
    print ('-- Ini adalah permainan gamsut --')
    print ('''
    Gunting (0)
    Kertas (1)
    Batu (2)
    ''')

#player
def playerinput ():
    inputuser = int (input ('Apa piihan anda? '))
    player = tools[inputuser]
    print (f'\nPlayer memilih {player}')
    return player

# komputer
def komputerinput():
    import random
    computerinput = random.choice(tools)
    print (f'Computer memilih {computerinput}')
    return computerinput


#output
def output(player,computerinput):
    # player gunting
    if player == 'gunting' and computerinput == 'batu':
        player = 'lose'
        print ('Player kalah')
    elif player == 'gunting' and computerinput == 'kertas':
        player = 'win'
        print ('Player menang')
    elif player == 'gunting' and computerinput == 'gunting':
        player = 'draw'
        print ('Seri')  

    # player batu
    if player == 'batu' and computerinput == 'batu':
        player = 'draw'
        print ('Seri')
    elif player == 'batu' and computerinput == 'kertas':
        player = 'lose'
        print ('Player kalah')
    elif player == 'batu' and computerinput == 'gunting':
        player = 'win'
        print ('Player menang')  

    # player kertas
    if player == 'kertas' and computerinput == 'batu':
        player = 'win'
        print ('Player menang')
    elif player == 'kertas' and computerinput == 'kertas':
        player = 'draw'
        print ('Seri')
    elif player == 'kertas' and computerinput == 'gunting':
        player = 'lose'
        print ('Player kalah')  

class hitung :
    score = 0

    def __init__ (self,name,jumlah):
        self.name = name
        self.jumlah = jumlah
    
    def playermenang (self,player):
        self.jumlah = 0
        if player == 'Player menang':
            self.jumlah += 1
            print (f'{self.name} = {self.jumlah}')
        


#utama 
while True :
    header ()
    Pemain = hitung('pemain',0)
    PLAYER = playerinput()
    COMPUTER = komputerinput()
    HASIL = output (PLAYER,COMPUTER)
    Pemain.playermenang(HASIL)

    konfirmasi = input ('\nIngin bermain lagi? ')
    if konfirmasi == 'ya':
        pass
    else:
        break
print ('Terimakasih sudah bermain...')
