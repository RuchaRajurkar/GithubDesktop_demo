# Create a class that captures planets. Each planet has a name, a distance from the sun, and its gravity relative
# to Earth’s gravity. For distance and gravity, use the type double which captures real numbers. Make objects for
# Earth and your favorite non-earth planet.

class Planets:
    def __init__(self,name,d,g):
        self.name=name
        self.distance=d
        self.gravity=g
    def show(self):
        print("Planet Name:",self.name)
        print("A distance from the Sun:", self.distance)
        print("Gravity Relative to Earth's Gravity:", self.gravity)

print("Planet Detail".center(50,"*"))
p1=Planets("Earth",3200,20)
p1.show()
print("************************************************")
p2=Planets("Jupiter",2100,25)
p2.show()

