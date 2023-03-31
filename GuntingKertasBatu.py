tools = ['gunting','kertas','batu'] 

def header():
        print ('-- Ini adalah permainan gamsut --')
        print ('''
        Gunting (0)
        Kertas (1)
        Batu (2)
        ''')

class gamsut :
    def _init_(self,name):
        self.name = name
                
    def playerinput (self):
        inputuser = int (input (f'Apa pilihan {self.name} (angka)? '))
        if inputuser > 2 or inputuser < 0:
            print("Masukkan pilihan dengan benar!\n")
            return gamsut.playerinput()
        player = tools[inputuser]
        print (f'\n{self.name} memilih {player}')
        return player

    def komputerinput():
        import random
        computerinput = random.choice(tools)
        print (f'Computer memilih {computerinput}')
        return computerinput

    def output(self,player,computerinput):
        # player gunting
        if player == 'gunting' and computerinput == 'batu':
            print(f'{self.name} Kalah')
        elif player == 'gunting' and computerinput == 'kertas':
            print (f'{self.name} Menang')
        elif player == 'gunting' and computerinput == 'gunting':
            print ('Seri')  

        # player batu
        if player == 'batu' and computerinput == 'batu':
            print ('Seri')
        elif player == 'batu' and computerinput == 'kertas':
            print (f'{self.name} kalah')
        elif player == 'batu' and computerinput == 'gunting':
            print (f'{self.name} menang')  

        # player kertas
        if player == 'kertas' and computerinput == 'batu':
            print (f'{self.name} menang')
        elif player == 'kertas' and computerinput == 'kertas':
            print ('Seri')
        elif player == 'kertas' and computerinput == 'gunting':
            print (f'{self.name} kalah')  
        
player1 = gamsut(input('siapa ini yang bermain? '))
while True :
    header()
    PLAYER = gamsut.playerinput(player1)
    COMPUTER = gamsut.komputerinput()
    RESULT = gamsut.output(player1,PLAYER,COMPUTER)
    
    konfirmasi = input ('\nIngin bermain lagi (ya/tidak)? ')
    if konfirmasi == 'ya':
        pass
    else:
        break
print ('Terimakasih sudah bermain...')
