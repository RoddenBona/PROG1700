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