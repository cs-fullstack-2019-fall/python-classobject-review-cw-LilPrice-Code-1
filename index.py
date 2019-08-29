def main():
    pro1()
    pro2()
# Problem 1:
#
# Create a Movie class with the following properties/attributes: movieName, rating, and yearReleased.
#
# Override the default str (to-String) method and implement the code that will print the value of all the properties/attributes of the Movie class
#
#
# Assign a value of your choosing for each property/attribute
#
# Print all properties to the console.
#

def pro1():
    class Movie:
        def __init__(self, movieName, rating,yearReleased):
            self.movie = movieName
            self.rating = rating
            self.year = yearReleased

        def __str__(self):
            mystr = (f"self.movie = {self.movie}\n"
                     f"self.rating = {self.rating}\n"
                     f"self.year = {self.year}")
            return mystr

    my1 = Movie("A Silent Voice", "9,7/10", "2018")
    # !! : create *two* instances 
    print(my1)
#
# Problem 2:
#
# Create a class Product that represents a product sold online.
#
# A Product has price, quantity and name properties/attributes.
#
# Override the default str (to-String) method and implement the code that will print the value of all the properties/attributes of the Product class
#
# In your main function create two instances of the Product class
#
# Assign a value of your choosing for each property/attribute
#
# Print all properties to the console.
def pro2():
    class Product:
        def __init__(self,price,quantity,name):
            self.price = price
            self.quan = quantity
            self.name = name

        def __str__(self):
            mystr = (f"self.price = {self.price}\n"
                     f"self.quan = {self.quan}\n"
                     f"self.name = {self.name}")
            return mystr
    p1 = Product(15, 3, 'apple')
    # !! : create *two* instances 
    print(p1)


main()