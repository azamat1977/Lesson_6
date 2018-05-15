class Transport:

    def __init__ (self, title, height, weight, length, speed, distance):
        self.title = title
        self.height = height
        self.weight = weight
        self.length = length
        self.speed = speed
        self.distance = distance

    def forward(self, x):

        self.distance = self.speed * x
        return self.distance

    def get_square(self):
        return self.height * self.length * self.weight


class Bus(Transport):
    def any (self, x):
        super(Bus, self).forward(x)
        return self.distance

transport = Transport('Any transport', 10 ,15 , 24, 100, 0)
bus = Bus('Endouver', 500, 1000, 30000, 500, 0)

#print(transport.distance)
#print(bus.distance)

transport.forward(10)
bus.any(10)

print(transport.distance)
print(bus.distance)

#print(transport.get_square())
#print(bus.get_square())