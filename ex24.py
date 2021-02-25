print("Let's practice everthing")
print("You\'d need to know \'bout escapes with \\ that do \n new lines and \t tabs.")

poem= """
\t the lovely world
with logic so firmly planted
can not discern \n the needs of love
nor comprehend passion from intuition
and requires an explnation
\n \t where there is none.
"""
print("_____________")
print(poem)
print("_____________")

five=10-2+3-6
print(f"This shold be five: {five}")

def secret_formula(started):
    jelly_beans= started*500
    jars=jelly_beans/1000
    crates=jars/100
    return jelly_beans,jars,crates

start_point=10000
beans,jars, crates= secret_formula(start_point)

print(f"With a starting point of: {start_point}")
print(f" we have {beans} beans, {jars} jars ,{crates} crates ")
start_point= start_point/10

print("We can also do that this way")
formula= secret_formula(start_point)
print("We'd have {} beans,{} jars ,{} crates.".format(* formula))
