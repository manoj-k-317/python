#this file exists in main branch

info = {"mondstad":"barbatos",
        "liyue":"morax",
        "inazuma":"ei",
        "sumeru":"buer"}
info.update({"fontaine":"focalors"})

nations = info.keys()
elements = info.values()
items = info.items()
print(items)
for key, value in items:
    print(f"{key}:{value}")
 
