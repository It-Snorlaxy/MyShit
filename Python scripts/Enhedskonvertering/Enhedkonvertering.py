a_units = {
'meter':{'base':'meter','factor':1},
'foot':{'base':'meter','factor':0.3048},
'au':{ 'base':'meter','factor':149597870691},
'decimeter':{'base':'meter','factor':0.1},
'centimeter':{'base':'meter','factor':0.01},
'millimeter':{'base':'meter','factor':0.001},
'kilometer':{'base':'meter','factor':1000},
'inches':{'base':'meter','factor':0.0254},
'yard':{'base':'meter','factor':1.09361},
'mile':{'base':'meter','factor':1.61},
'm2':{'base':'m2','factor':1},
'km2':{'base':'m2','factor':1000000},
'inch2':{'base':'m2','factor':0.00064516},
'foot2':{'base':'m2','factor':0.092903},
'yard2':{'base':'m2','factor':0.836127},
'mile2':{'base':'m2','factor':2589988.1},
'acre':{'base':'m2','factor':4046.86},
'hectare':{'base':'m2','factor':10000}
}





while True:

    source = None
    while source not in a_units.keys():
        print('\nEnheder keywords:\nmeter\nfoot\nau\ndecimeter\ncentimeter\nmillimeter\nkilometer\ninches\nyard\nmile\nm2\nkm2\ninch2\nfoot2\nyard2\nmile2\nacre\nhectare\n')
        source = input("Hvad vil du konvertere fra? \n")



    amount=input("Hvor meget vil du konvertere? ")
    while amount.isdecimal() == False:
        amount=input("Hvor meget vil du konvertere? ")
    target=input("Hvad vil du konvertere til? ")

    if a_units[source]['base']==a_units[target]['base']:
        source_to_target = float(amount) * a_units[source]['factor']
        base_to_target = source_to_target/a_units[target]['factor']
        print(base_to_target)
    else:
        print('De enheder passer ikke sammen')

    if input('vil du konvertere mere?  Y/N \n') == 'N':
        break
