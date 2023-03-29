tools = ['gunting','kertas','batu']


# header
def header():
    print ('Ini adalah permainan gamsut')
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
        print ('Player kalah')
    elif player == 'gunting' and computerinput == 'kertas':
        print ('Player menang')
    elif player == 'gunting' and computerinput == 'gunting':
        print ('Seri')  

    # player batu
    if player == 'batu' and computerinput == 'batu':
        print ('Seri')
    elif player == 'batu' and computerinput == 'kertas':
        print ('Player kalah')
    elif player == 'batu' and computerinput == 'gunting':
        print ('Player menang')  

    # player kertas
    if player == 'kertas' and computerinput == 'batu':
        print ('Player menang')
    elif player == 'kertas' and computerinput == 'kertas':
        print ('Seri')
    elif player == 'kertas' and computerinput == 'gunting':
        print ('Player kalah')  


#utama 
while True :
    header ()
    PLAYER = playerinput()
    COMPUTER = komputerinput()
    HASIL = output (PLAYER,COMPUTER)
    
    konfirmasi = input ('Ingin bermain lagi? ')
    if konfirmasi == 'ya':
        pass
    else:
        break
print ('Terimakasih sudah bermain...')
