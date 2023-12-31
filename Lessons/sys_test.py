planet = {
    'name': 'Earth',
    'moons': 1
}

print(planet)

print(planet.get('name'))

planet.update({
    'name': 'Jupiter',
    'moons': 79
})

print(planet)

planet['orbital period'] = 4333

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }

print(planet)

planet.pop('orbital period')

print(planet)

planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

print(planet)

print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')

print(planet)


# Enter code below
planet = { 
    'name': 'Mars',
    'moons': 2
}

#old print format
print(planet["name"], "has", planet["moons"], "moons")

# f string

name = "Rodden"
age = 7

print(f'{name} is {age + 13} years old')

myDic = {'favFood':'Pizza',
         'bestSport':'Hockey',
         'favMovie':'Jim Carreys Grinch',
         'favNumbers':(8,64,128),
         'favBands':['Marianas Trench','Tally Hall','Red Vox'],
         'favPlanets':{'name':'mars',
                        'moons':2}
         }

print(myDic['favBands'])
print(myDic['favMovie'])
print(myDic['favNumbers'])
print(myDic['favPlanets']['name'])
#test line