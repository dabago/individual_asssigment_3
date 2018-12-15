
#%%% Exercise 1

class Product:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality

carrot = Product("carrot", 3)
potatoe = Product("potatoe",10)
ham = Product("ham",4)
cheese = Product("cheese", 6)

potato = Product("potato", 10)    
potato1 = Product("potato", 100)    
potato2 = Product("potato", .5)    
  

cheese = Product("cheese", 10)
cheese1 = Product("cheese", 100)    
cheese2 = Product("cheese", .5)    

pasta = Product("pasta", 4)
pasta1 = Product("pasta1", 20)
pasta2 = Product("pasta1", 5)


def recalculate_quality(product):
    if product.name == "potatoe":
        product.quality = product.quality - 0.5
    elif product.name == "potato":
        product.quality = product.quality - 0.5
    elif product.name == "cheese":
        product.quality = product.quality - 2
    else:
        if product.quality < 5:
            product.quality -= 3
