class Sofa:
    sofas_in_shop = 0

    def __init__(self, brand="", length=0, width=0, height=0,
                 colour="",
                 material="", price=0):
        self.brand = brand
        self.length = length
        self.height = height
        self.width = width
        self.colour = colour
        self.material = material
        self.price = price
        Sofa.sofas_in_shop += 1

    def __del__(self):
        pass

    def __str__(self):
        return "Sofa '" + self.brand + "'" \
               + ", Length - " + str(self.length)+" mm" \
               + ", Width- " + str(self.width)+" mm" \
               + ", Height - '" + str(self.height)+"mm" \
               + ", Colour - " + self.colour \
               + ", Material - " + self.material \
               + ", Price - " + str(self.price) + " UAN"

    @staticmethod
    def get_sofas_in_shop():
        return Sofa.sofas_in_shop


def main():
    sofa1 = Sofa("Bravisimo", 2150, 1000, 1000, "gray", "Chenille", 6667)
    sofa2 = Sofa("Acvador", length=2400, width=1000, height=800, price=11200)
    sofa3 = Sofa("Visanty", price=8800)
    print("There are", Sofa.get_sofas_in_shop(), "sofas in shop")
    print(sofa1)
    print(sofa2)
    print(sofa3)


main()
