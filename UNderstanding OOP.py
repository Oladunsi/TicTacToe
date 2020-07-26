class Cirle(object):
    
    pi = 3.14
    
    def __init__(self,radius=1):
        self.radius = radius

    def Area(self):
        return Cirle.pi * (self.radius**2)
        
    def _radius(self,rad):
        self.rad = rad
        self.radius = rad
        
    
    

circle = Cirle(radius = 40)    

print(circle)
    
