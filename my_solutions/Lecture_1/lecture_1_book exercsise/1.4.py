import sys 
meters = float(sys.argv[1])

def length_conversion(meters):
    inches = round((meters*100)/2.54,2)
    foots = inches/12
    yards  =  foots/3
    miles = yards/1760

    print(f"{meters} meters is {inches} inches, {foots} foots, {yards} yards and {miles} miles")
    

length_conversion(meters)
