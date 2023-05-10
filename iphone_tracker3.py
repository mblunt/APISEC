from pyicloud import PyiCloudService
import time
import geopy.distance

api = PyiCloudService('michaelbblunt@icloud.com', 'password')

#Query for the 2FA code
if api.requires_2fa:
    print("Two-factor authentication required.")
    code = input("Enter the code you received of one of your approved devices: ")
    result = api.validate_2fa_code(code)
    print("Code validation result: %s" % result)

#If code is wrong, exit with error
    if not result:
        print("Failed to verify security code")
        sys.exit(1)

#Request trust if trust not established
    if not api.is_trusted_session:
        print("Session is not trusted. Requesting trust...")
        result = api.trust_session()
        print("Session trust result %s" % result)

#Warn about trust not being established
        if not result:
            print("Failed to request trust. You will likely be prompted for the code again in the coming weeks")

#2StepAuth
elif api.requires_2sa:
    import click
    print("Two-step authentication required. Your trusted devices are:")

#SMS to device
    devices = api.trusted_devices
    for i, device in enumerate(devices):
        print("  %s: %s" % (i, device.get('deviceName',
            "SMS to %s" % device.get('phoneNumber'))))

#What Device to send to
    device = click.prompt('Which device would you like to use?', default=0)
    device = devices[device]
    if not api.send_verification_code(device):
        print("Failed to send verification code")
        sys.exit(1)

#Enter Code from sms
    code = click.prompt('Please enter validation code')
    if not api.validate_verification_code(device, code):
        print("Failed to verify verification code")
        sys.exit(1)


'''
Data Collection and Processing Phase:
DAD IPHONE
'''

print(api.devices)

dad_dict = api.devices["EbbR5VR6yCpAPFXxaZPDcWfEvI3Gng3Qxpja9041/6uuzxhWQvCsc871F/SMl1G6TnJLEgcQbVkyUNS6EoaB1C9qZTPnncDC"].location()
print(dad_dict)

#Accuracy Verification
last_ping = ( ((int(time.time()))*1000) - (int(dad_dict["timeStamp"])) )

if last_ping > 30000: #30 second window
    print("DAD: " + str(last_ping) + " milliseconds since last ping, refresh needed")
elif last_ping <= 30000: #30 second window
    print("DAD: " + str(last_ping) + ", Time is good")
    
if dad_dict["isOld"] != bool(False):
    print("DAD: Location Data is old")
    
if dad_dict["isInaccurate"] != bool(False):
    print("DAD: Location Data is inaccurate")
    
#Lat/Long Cords
dad_lat = dad_dict["latitude"]
dad_long = dad_dict["longitude"]
dad_coords = (dad_lat, dad_long)

'''
MOM IPHONE
'''

mom_dict = api.devices["EbbR5VR6yCqsS0qMMiqlvDXigFflP8EU34m6+qF/+bauzxhWQvCsc0b4H3z5v4pnJ5Q7K2HDExwyUNS6EoaB1C9qZTPnncDC"].location()

#Accuracy Verification
last_ping = ( ((int(time.time()))*1000) - (int(mom_dict["timeStamp"])) )

if last_ping > 30000: #30 second window
    print("MOM: " + str(last_ping) + " milliseconds since last ping, refresh needed")
elif last_ping <= 30000: #30 second window
    print("MOM: " + str(last_ping) + ", Time is good")

if mom_dict["isOld"] != bool(False):
    print("MOM: Location Data is old")
    
if mom_dict["isInaccurate"] != bool(False):
    print("MOM: Location Data is inaccurate")
    
#Lat/Long Cords
mom_lat = mom_dict["latitude"]
mom_long = mom_dict["longitude"]
mom_coords = (mom_lat, mom_long)
  
'''
MICHAEL IPHONE
'''
me_dict = api.devices["dYgDxjNDw6CGu8GVaN/hEE7WJmEP6e4bi7mxiFvihSk="].location()

#Accuracy Verification
last_ping = ( ((int(time.time()))*1000) - (int(me_dict["timeStamp"])) )

if last_ping > 30000: #30 second window
    print("ME: " + str(last_ping) + " milliseconds since last ping, refresh needed")
elif last_ping <= 30000: #30 second window
    print("ME: " + str(last_ping) + ", Time is good")

if me_dict["isOld"] != bool(False):
    print("ME: Location Data is old")
    
if me_dict["isInaccurate"] != bool(False):
    print("ME: Location Data is inaccurate")
    
#Lat/Long Cords
me_lat = me_dict["latitude"]
me_long = me_dict["longitude"]
me_coords = (me_lat, me_long)

'''
MARISA IPHONE
'''
mar_dict = api.devices["EbbR5VR6yCoaXoZlU0Jm3JEr0gGsYNM73gDblanixsOuzxhWQvCsc0MnWuScMa9preUOaeOUE44G+KZb2T+4xi7naZIuzVUZ"].location()

#Accuracy Verification
last_ping = ( ((int(time.time()))*1000) - (int(mar_dict["timeStamp"])) )

if last_ping > 30000: #30 second window
    print("MARISA: " + str(last_ping) + " milliseconds since last ping, refresh needed")
elif last_ping <= 30000: #30 second window
    print("MARISA: " + str(last_ping) + ", Time is good")

if mar_dict["isOld"] != bool(False):
    print("MARISA: Location Data is old")
    
if mar_dict["isInaccurate"] != bool(False):
    print("MARISA: Location Data is inaccurate")
    
#Lat/Long Cords
mar_lat = mar_dict["latitude"]
mar_long = mar_dict["longitude"]
mar_coords = (mar_lat, mar_long)  
  
'''
DISTANCE CHECKER
'''
dad_miles = []
dad_miles.append(int(geopy.distance.distance(me_coords, dad_coords).miles))
mom_miles = []
mom_miles.append(int(geopy.distance.distance(me_coords, mom_coords).miles))
mar_miles = []
mar_miles.append(int(geopy.distance.distance(me_coords, mar_coords).miles))

print("Miles from Dad: " + str(geopy.distance.distance(me_coords, dad_coords).miles))
print("Miles from Mom: " + str(geopy.distance.distance(me_coords, mom_coords).miles))
print("Miles from Marisa: " + str(geopy.distance.distance(me_coords, mar_coords).miles))



'''
DEV PLAN

Get location of phones
distance from phones calculated using lat long coords
alert when within radius of 10 miles or movement
'''
