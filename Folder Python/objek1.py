class Triangle:
    def __init__(self,points):
        self.sides = 3
        self.points = list(points)
        if len(self.points) != 3:
            raise ValueError ("Wrong number points")
        
    def sides (self):
        return 3
    
    def __str__(self):
        return "I'm a triangle"
    
class Square:
    def __init__(self,points):
        self.sides = 4
        self.points = list(points)
        if len(self.points) != 4:
            raise ValueError ("Wrong number points")
        
    def side (self):
        return 4
    
    def __str__(self):
        return "I'm so Square"
        
                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                    