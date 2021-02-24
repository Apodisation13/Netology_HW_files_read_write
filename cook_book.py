with open("recipes.txt", encoding="utf-8") as f:
    a = f.readlines()
    cook_book = {}
    i = 0
    while i < len(a):
        ingredients = []
        ingredients_dict = {}
        number = int(a[i + 1])
        # print(i, number)
        for j in range(number):
            ingredients_dict["ingredient_name"] = a[i+2].split('|')[0].strip()
            ingredients_dict["quantity"] = int(a[i+2].split('|')[1])
            ingredients_dict["measure"] = a[i+2].split('|')[2].strip()
            # print(ingredients_dict)
            ingredients.append(ingredients_dict)
            ingredients_dict = {}
            # print(ingredients)
            i += 1
        cook_book[a[i - number].strip()] = ingredients
        # print(cook_book)
        i += 3

if __name__ == "__main__":
    print(cook_book)
