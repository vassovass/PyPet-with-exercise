print 'Welcome to Pypet!'

cat = {
    'name': "Krench",
    'age': 6,
    'weight': 40,
    'hungry': True,
    'energylevel': 30,
    'photo': '(=^o.-^=)__',
}


def feed(pet):
    if pet['hungry'] == True:
        pet['hungry'] = False
        pet['weight'] = pet['weight'] + 10
        pet['energylevel'] = pet['energylevel'] + 4
        print 'You have FED your pet'
    else:
        print 'The Pypet is not hungry!'

def walk(pet):
    if pet['energylevel'] > 30:
        pet['hungry'] = True
        pet['weight'] = pet['weight'] - 4
        pet['energylevel'] = pet['energylevel'] - 6
        print 'You have WALKED your pet';
    else:
        print 'The Pypet is too tired!'

print cat
walk(cat)
print cat
feed(cat)
print cat
walk(cat)
print cat
walk(cat)
print cat
walk(cat)
print cat
feed(cat)
print cat
feed(cat)
print cat
walk(cat)
print cat
