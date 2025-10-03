from ampel import Ampel
a1 = Ampel('rot')
a2 = Ampel('gruen')
print('Ampel 1:', a1.getLampen())
print('Ampel 2:', a2.getLampen())
print()
while a1.getZustand() != 'gelb':
    a1.schalten()
    a2.schalten()
    print('Ampel 1:', a1.getLampen())
    print('Ampel 2:', a2.getLampen())
    print()
