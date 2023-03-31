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
