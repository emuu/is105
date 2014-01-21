#Her defineres variablen my_name
my_name = 'Zed A. Shaw'
#Her defineres variablen my_age
my_age = 35 # not a lie
#Her defineres variablen my_height
my_height = 74 # inches
#osv, osv.. 
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

#her henter han variablen my_name, og legger den inn i % i teksten
print "Let's talk about %s." % my_name
#her henter han variablen my_height
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
#her legger han sammen age, height, weight + height + weight
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

