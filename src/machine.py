# 6 a 7, agua boaaa 
# 2 a 5, ruim 
# 8 a 10 ruim tambem

class IA:
    def __init__(self, ph):
        self.ph = ph
        self.RANGE_MIN = 6.0
        self.RANGE_MAX = 7.0
        self.status = ''
    
    def classificador(self):
        if(self.ph <= self.RANGE_MAX and self.ph >= self.RANGE_MIN):
            self.status = 'Bom'
        else:
            self.status = 'Ruim'

    def definidor(self):
        if(self.ph < self.RANGE_MIN):
            self.status += ' - acida'
        elif(self.ph > self.RANGE_MAX):
            self.status += ' - alcalina'