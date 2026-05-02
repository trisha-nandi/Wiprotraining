#create a tuple with the names of 3 different cities you,d like to visit.print the tuple

city=("kolkata","goa","varanasi")
print(city)

#access and print the first and last elements of the tuple
print(city[0])
print(city[-1])

#create another tuple with 2 more cities.concatenate both tuples and print the result
more_city=("bengaluru","jaipur")
all_city = city + more_city
print ("Concatenated tuple:",all_city)

#try changing one element of the tuple
try:
    city[0] = "mumbai"
except TypeError as e:
    print("Error(Tuples are immutable)")

#unpack the elements of the tuple into sepate veriables
c1,c2,c3 = city
print("unpack cities: ", c1,c2,c3)

#