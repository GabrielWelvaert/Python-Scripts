def cookie():

    # parse ingredient type
    ingredient = ""
    while(ingredient == ""):
        ingredient = str(input('Enter Ingredient to be weighed (must be: "butter", "sugar", "egg", or "flour"): \n'))
        if(ingredient.lower() not in ("butter", "sugar", "egg", "flour")):
            print("Invalid Ingredient entered")
            ingredient = ""

    # parse ingredient weight
    weight = 0.0
    while(weight == 0.0):
        failed = False
        try:
            extraText = ""
            if(ingredient == "egg"):
                extraText = " (cracked into bowl!)"
            weight = float(input(f"Enter weight of {ingredient + extraText} being used (grams): \n"))
        except ValueError:
            failed = True

        if(weight <= 0.0):
            failed = True

        if(failed):
            print("Invalid weight")
            weight = 0.0

    ratios = {"butter":143.51,"sugar":213.08,"egg":49.83,"vanilla":5.73,"baking soda":2.44,"salt":2.7,"flour":200}
    ratio = ratios[ingredient]/weight

    print(f'Here are your ingredient masses (grams) for the ultimate average cookie:')
    for x,y in ratios.items():
        y = round(y/(ratio),2)
        print(f'{x}: {y}')

if __name__ == '__main__':
    cookie()

