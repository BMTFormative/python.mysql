class Point:
    
    def __init__(self,x, y):
        #self.__x = x
        #self.__y = y
        self.mov(x,y)
    
    def get_x(self): return self.__x 
    def set_x(self,x):
        assert(x>=0), "x must be positive"
        self.__x = x
    def del_x(self): del self.__x   
    x = property(get_x,set_x,del_x)
    def get_y(self): return self.__y 
    def set_y(self,y):
        assert(y>=0), "x must be positive"
        self.__y = y  
    def del_y(self): del self.__y      
    y = property(get_y,set_y,del_y)     
    def mov(self,x, y):
          self.set_x(x)
          self.set_y(y)
          
    def display(self):
        print("(%d,%d)" % (self.__x, self.__y))
        
    def __str__(self):
        return("[%d,%d]" % (self.__x, self.__y))
    def __del__(self):
        print("the point is deleted")
