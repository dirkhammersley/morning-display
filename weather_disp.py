import urllib2
import json
import scrollphathd as sphd
import time
import schedule
from rl_status import get_rl_status

def update_all():
    sphd.clear()
    sphd.show()
    f = urllib2.urlopen('http://api.wunderground.com/api/70975714a4d5236a/geolookup/conditions/q/MA/Boston.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    rs = get_rl_status()
    location = parsed_json['location']['city']
    w_est = parsed_json['current_observation']['weather']
    temp_f = parsed_json['current_observation']['temp_f']
    msg = "@%sUTC, %s, %sF, Red Line is %s.   " % (time.strftime("%H:%M"), w_est, temp_f, rs)
    f.close()
    sphd.write_string(msg, brightness=0.1)
    sphd.show()

update_all()

schedule.every().hour.do(update_all)

while True:
        sphd.show()
        sphd.scroll(1)
        schedule.run_pending()
        time.sleep(0.05)
