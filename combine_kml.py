import re

kml1 = '<kml xmlns="http://www.opengis.net/kml/2.2"><Document><Placemark><name>'
kml1 += 'displayMode=default</name><description>Hello, World!</description>'
kml1 += '<Style><BalloonStyle><displayMode>default</displayMode></BalloonStyle>'
kml1 += '</Style><Point><coordinates>-122.001,37.000</coordinates></Point>'
kml1 += '</Placemark><Placemark><name>displayMode=hide</name><description>'
kml1 += 'Hello, World!</description><Style><BalloonStyle><displayMode>hide</displayMode>'
kml1 += '</BalloonStyle></Style><Point><coordinates>-122.001,37.001</coordinates>'
kml1 += '</Point></Placemark></Document></kml>'

kml3 = '<kml xmlns="http://www.opengis.net/kml/2.2"><Document><Placemark><name>'
kml3 += 'BOOMIN</name></Placemark>'
kml3 += '<Poop>poooooooooooooooooooooooooooooooooooooooooop</Poop>'
kml3 += '</Document></kml>'

kml2 = '<kml xmlns="http://www.opengis.net/kml/2.2"><Document><Placemark>'
kml2 += '<name>displayMode=default</name><description>Hello, World!</description><Style>'
kml2 += '<BalloonStyle><displayMode>default</displayMode></BalloonStyle></Style>'
kml2 += '<Point><coordinates>-122.001,37.000</coordinates></Point></Placemark><Placemark>'
kml2 += '<name>displayMode=hide</name><description>Hello, World!</description>'
kml2 += '<Style><BalloonStyle><displayMode>hide</displayMode></BalloonStyle></Style><Point>'
kml2 += '<coordinates>-122.001,37.001</coordinates></Point></Placemark></Document></kml>'

def combine_kml(*arg):
    print "Combining ", len(arg), " kml files."
    base_kml_string = arg[0]
    insertion_point = base_kml_string.find('<Document>') + 10

    for kml_string in arg:
        replaced_string = strip_kml_designation(kml_string)
        base_kml_string = base_kml_string[:insertion_point] + replaced_string + base_kml_string[insertion_point:]

    print base_kml_string 
    return base_kml_string

def strip_kml_designation(kml):
    replaced = re.sub('<kml [\w=":/.!*^$#@?)(\-%&+]*><Document>', '', kml)
    replaced = re.sub('<\/Document>', '', replaced)
    replaced = re.sub('<\/kml>', '', replaced)
    return replaced 

combine_kml(kml1, kml2, kml3)
