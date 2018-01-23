#--coding:utf-8--
name="Zed A. Shaw"
age=35 # not a lie
height=74 #inches
weight = 180 #lbs
eyes ='Blue'
teeth='white'
hair='Brown'
print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes,hair)
print "His teath are usually %s depending on the coffee." % teeth
#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age,height,weight,age+height+weight)

# convert inches to cms 1 inch=2.54 cm
print "Zed is %d cms tall." % (height*2.54)
# convert lbs to kg
print "Zed is %d kg heavy." % (weight*453.59/1000)