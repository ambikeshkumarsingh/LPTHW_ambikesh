people=30
cars=40
buses=15

if cars > people:
    print("We should take the cars")
elif cars < people:
    print("We shouldn't take cars")
else:
    print("We don't know")

if (buses > cars):
    print("That's too many trucks")
elif buses < cars :
    print(" May be we can take the trucks")
else:
    print(" We still can't decide")
if people > buses :
    print("Alright, let's just take the buses")
else:
    print("Fine, let's stay at home then..")
