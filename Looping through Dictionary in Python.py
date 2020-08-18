#lOOPING THROUGH DICTIONARY:
fav_languages={
    "Atish":"Python",
    "Aman":"HTML",
    "Anand":"C",
    "Gauarav":"JavaScript"
}

#Looping through all Key-Value Pairs:
for names,languages in fav_languages.items():
    print(names +" = "+languages)
    
print() #Blank Line
    
#Looping through only keys:
for names in fav_languages.keys():
    print(names)

print() #Blank Line

#Looping through only rows:
for languages in fav_languages.values():
    print(languages)

print() #Blank Line   
    
#Looping through all the keys in order:
for names in sorted(fav_languages.keys()):
    print(names)

print() #Blank Line

#Looping through all the values in order:
for languages in sorted(fav_languages.values()):
    print(languages)
