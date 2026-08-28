class Foodfix:
    def __init__(self, category, texture, flavour, burnt):
        self.category = category
        self.texture = texture
        self.flavour = flavour
        self.burnt = burnt

#Class for fix and criteria to be filled out in the forms
dishes = []
dishes.append(Foodfix('Soup', 'True', 'True', 'True'))
dishes.append(Foodfix('Sauces', 'True', 'True', 'True'))
dishes.append(Foodfix('Meats', 'True', 'True', 'True'))
dishes.append(Foodfix('Grains', 'True', 'True', 'True'))
dishes.append(Foodfix('Baked Goods', 'True', 'True', 'True'))