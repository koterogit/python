import location
import reminders
import datetime

currentLoc = location.get_location()
lat = currentLoc["latitude"]
lng = currentLoc["longitude"]

url ='comgooglemaps://?q='+str(lat)+','+str(lng)

r=reminders.Reminder()
r.title='parking_'+str(datetime.date.today()) 
r.notes=url
r.url="https:"
r.save()
