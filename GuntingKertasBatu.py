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
