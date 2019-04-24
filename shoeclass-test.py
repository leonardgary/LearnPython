#--------------------------------------------------------------
# Create a Shoe object with the default contructor, some
# Accessor and Mutator methods
#--------------------------------------------------------------
class Shoes:
    def __init__(self):
        fstyle = "Walking"
        fcolor = "Red"
        fsize = "8.5"
 
    def Shoes(self, ffstyle, ffcolor, ffsize):
        self.__style = ffstyle
        self.__color = ffcolor
        self.__size = ffsize
#--------------------------------------------------------------
# Mutator methods
#--------------------------------------------------------------          
    def set_style(self, fstyle):
        self.__style = fstyle

    def set_color(self, fcolor):
        self.__color = fcolor

    def set_size(self, fsize):
        self.__size = fsize
#--------------------------------------------------------------
# Accessor methods...
#--------------------------------------------------------------
    def get_style(self):
        return self.__style

    def get_color(self):
        return self.__color

    def get_size(self):
        return self.__size

def main():
#--------------------------------------------------------------
# Create a Shoe object with the default contructor
# & Display it's default values...
#--------------------------------------------------------------
    fancyShoes = Shoes()
#--------------------------------------------------------------
# Create a call to set the color, style
# & sizes of the fancyShoes....
#--------------------------------------------------------------
    fstyle = input('Set the style of the Fancy Shoes[Dancing]: ')
    fancyShoes.set_style(fstyle)
    fcolor = input('Set the color of the Fancy Shoes[RED]: ')
    fancyShoes.set_color(fcolor)
    fsize = input('Set the size of the Fancy Shoes[9.5]: ')
    fancyShoes.set_size(fsize)
#--------------------------------------------------------------
# Display the style of the Fancy Shoe...
#--------------------------------------------------------------
    print('The style of the shoe is', fancyShoes.get_style())
#--------------------------------------------------------------
# Create a Shoe object and initialize its
# fields with default values
#--------------------------------------------------------------
    athleticShoes = Shoes("Running", "White", "8.5")
    fcolor = input('Set the color of the athletic Shoes[BLACK]: ')
    athleticShoes.set_color(fcolor)
    print('The color of the athletic shoe is', athleticShoes.get_color())
main() 

        
