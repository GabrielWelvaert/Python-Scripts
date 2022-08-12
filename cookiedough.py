#cookie dough ratio when given a specific amount of butter, in grams:
def fromButter(butterweight):
    butter = 143.51
    d = {"sugar":213.08,"egg":49.83,"vanilla":5.73,"baking soda":2.44,"salt":2.7,"flour":200}
    newline = '\n'
    print(f'{newline}Here are your ingredient masses (grams) for the ultimate average cookie:{newline}(most scales cant accurately detect small changes ~<3 grams, use intuition when needed if you have a small batch){newline}{newline}butter: {butterweight}')
    for x,y in d.items():
        y = round(y/(butter/butterweight),2)
        print(f'{x}: {y}')
    print(newline)

butterweight = float(input("\nEnter weight of butter being used (grams): "))
fromButter(butterweight)

