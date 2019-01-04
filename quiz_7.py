# Defines two classes, Point() and Disk().
# The latter has an "area" attribute and three methods:
# - change_radius(r)
# - intersects(disk), that returns True or False depending on whether
#   the disk provided as argument intersects the disk object.
# - absorb(disk), that returns a new disk object that represents the smallest
#   disk that contains both the disk provided as argument and the disk object.
#
# Written by Xiaowei Zhu Z5102903 and Eric Martin for COMP9021


from math import pi, hypot
# pi is the same as pair
# hypot is the function sqrt(x^2 + y^2)

from math import sqrt


# build a Class
class Point:
    # __init__ is the default method to set Point(x,y)
    # self represent the Point() it's self
    # x=0,y=0 define the ininital value
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    # __repr__ represent the display of the value it's self
    def __repr__(self):
        # format print
        return f'Point({self.x:.2f}, {self.y:.2f})'


# build a Class
class Disk:
    
    # *, means we need to designate the name of every values in this class
    # centre = Point(), in this Class we call another Class
    def __init__(self, *, centre = Point(), radius = 0):
        self.centre = centre
        self.radius = radius
        
        # we can put the sub/lower attritude in the __init__ function
        # so we can use Disk().area to invoke this value
        self.area = pi*((self.radius)**2)
    
    # show the Class it's self, this a default format
    def __repr__(self):
        return f'Disk({self.centre}, {self.radius:.2f})'
    
    
    # if i use this format, the only way to get the value of area
    # is Disk().area()
    #    def area(self):
    #
    #        self.area = pi*(self.radius)**2
    #        return self.area
    #
    # judge is these two circle intersecting
    # (self,DK) self is default value, DK add another value in the ()
    # Instance: disk_4.intersects(disk_1)
    def intersects(self,DK):
        
        if ((self.centre.x) - (DK.centre.x))**2 +\
            ((self.centre.y) - (DK.centre.y))**2 <=\
                ((self.radius) + (DK.radius))**2:
                    
                    return True


# get the absorbed circle
# (self,DK),  Instance: disk_5.absorb(disk_6)
def absorb(self,DK):
    
    x_1, y_1 = self.centre.x, self.centre.y
        #y_1 = self.centre.y
        
        x_2, y_2 = DK.centre.x, DK.centre.y
        #y_2 = DK.centre.y
        
        r_1, r_2 = self.radius, DK.radius
        #r_2 = DK.radius
        
        if x_2 > x_1:
            gap_x = (x_2 - x_1)
    else:
        gap_x = (x_1 - x_2)
        if y_2 > y_1:
            gap_y = (y_2 - y_1)
    else:
        gap_y = (y_1 - y_2)
        
        #print(gap_x,gap_y)
        gap_p = (hypot(gap_x,gap_y))
        #print(gap_p)
        r_3 = (r_1 + r_2 + gap_p)/2
        #print(r_3)
        
        # judge the situation that one circle contain another circle
        # so the circle will be one of these two circles(bigger one)
        if gap_p + min(r_1,r_2) <= max(r_1,r_2):
            if r_1 == max(r_1,r_2):
                x_a,y_b = x_1,y_1
            else:
                x_a,y_b = x_2,y_2
            
            # return the Class value
            # we can define and designate the value of the output of this class
            return Disk(centre = Point(x_a,y_b),radius = max(r_1,r_2))

        else:
            
            gap_1 = (r_3 - r_2)
            
            a = x_2 - (gap_1/gap_p)*(x_2 - x_1)
            
            b = y_2 - (gap_1/gap_p)*(y_2 - y_1)
            
            return Disk(centre = Point(a,b),radius = r_3)

                
                
                # change the value of radius
                # disk_1.change_radius(2) in this situation we don,t need *
                def change_radius(self, r = None):

                    if r != None:
self.radius = r
    # ***** here we need to assign the value to self.area again
    # ***** because if we don't assign the value it will invoke the initial 0 ,WHY?????
    
    self.area = pi * self.radius**2





