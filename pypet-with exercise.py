print 'Welcome to Pypet!'

cat = {
    'name': "Kitty",
    'age': 6,
    'weight': 40,
    'hungry': True,
    'energylevel': 30,
    'photo': '(=^o.-^=)__',
}

mouse = {
    'name': "Mousey",
    'age': 2,
    'weight': 2,
    'hungry': False,
    'energylevel': 34,
    'photo': '(=(00.00)=)_____',
}
pets = [cat, mouse]

def feed(pet):
    print ('FEED FEED FEED')
    if pet['hungry'] == True:
        pet['hungry'] = False
        pet['weight'] = pet['weight'] + 10
        pet['energylevel'] = pet['energylevel'] + 4
        print 'You have FED your pet'
    else:
        print 'The Pypet is not hungry!'

def walk(pet):
    print ('WALK WALK WALK')
    if pet['energylevel'] > 30:
        pet['hungry'] = True
        pet['weight'] = pet['weight'] - 4
        pet['energylevel'] = pet['energylevel'] - 6
        print 'You have WALKED your pet';
    else:
        print 'The Pypet is too tired!'


for pet in pets:
    print '------------------------------'
    print 'Hello ' + pet['name'] + '!'
    print 'Weight: ' + str(pet['weight'])
    print 'EL: ' + str(pet['energylevel'])
    print 'Hunger: ' + str(pet['hungry'])
    walk(pet)
    walk(pet)
    print 'Weight: ' + str(pet['weight'])
    print 'EL: ' + str(pet['energylevel'])
    print 'Hunger: ' + str(pet['hungry'])
    print '------------------------------'
    feed(pet)
    walk(pet)
    print 'Weight: ' + str(pet['weight'])
    print 'EL: ' + str(pet['energylevel'])
    print 'Hunger: ' + str(pet['hungry'])
    print '------------------------------'
