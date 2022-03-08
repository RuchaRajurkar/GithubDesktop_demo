# Write a class “Box” that with three member-variables “height”, “width” and “breadth”. Write
# suitable constructors to initialize them. Add functions like “getVolume” and “getArea” that will
# return volume and surface area respectively. Create object of boxes and then print their volume
# and surface area
class Box:
      def __init__(self,height,width,breadth):
          self.h=height
          self.w=width
          self.b=breadth
      def getvolume(self):
          self.volume=(self.h*self.w*self.b)
          return self.volume
      def getArea(self):
          self.surfaceArea=(2*(self.b*self.w)+2*(self.b*self.h)+2*(self.h*self.w))
          return self.surfaceArea

b1=Box(2,3,4)
print("Volume of Box",b1.getvolume())
print("Surface of Box",b1.getArea())
