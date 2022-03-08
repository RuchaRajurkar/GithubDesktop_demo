# Create a class “Room” which will hold the “height”, “width” and “breadth” of the room in three
# fields(variables). This class also has a method “volume()” to calculate the volume of this room.

class Room:
    def __init__(self,height,width,breadth):
        self.h=height
        self.w=width
        self.b=breadth
    def volume(self):
        self.v=self.h*self.b*self.w
        print("Volume of Room is",self.v)

r1=Room(1,2,3)
r1.volume()
r2=Room(4,5,6)
r2.volume()