class parent():
    
    def __init__(self):
        print("This is the parent class")
        
    def menu(dish):
        if dish=="sandwich":
            print("You can add the following fillings")
            print("Letuce leaves | Cheese slice")
        elif dish=="custard":
            print("You can add the following ingredients")
            print("Fruits | Dry Fruits")
        else:
            print("Please enter a valid dish")
    
    def final_amount(dish, add_ons):
        if dish=="sandwich" and add_ons=="letuce leaves":
            print("Amount : 349 INR")
        elif dish=="burger" and add_ons=="cheese slice":
            print("Amount : 399 INR")
        elif dish=="custard"and add_ons=="Fruits":
            print("Amount : 369 INR")
        elif dish=="custard" and add_ons=="Dry Fruits":
            print("Amount : 359 INR")
            
class child1(parent):
    
    def __init__(self,dish):
        self.new_dish = dish
    def get_menu(self):
        parent.menu(self.new_dish)
        
class child2(parent):
    def __init__(self,dish,addons):
        self.new_dish = dish
        self.addons = addons
        
    def get_final_amount(self):
        parent.final_amount(self.new_dish,self.addons)
        
child1_object=child1("burger")
child1_object.get_menu()
child2_object=child2("burger","jalepeeno")
child2_object.get_final_amount()
        