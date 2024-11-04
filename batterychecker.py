import psutil
import os

battery = psutil.sensors_battery()

if battery is not None:
    if battery.percent == 100 and battery.power_plugged:
        print('your battery is 100%')
        desktop_path = os.path.join(os.path.expanduser('~'),"Desktop","BatteryReminder.txt")
        with open(desktop_path,'w') as file:
            file.write('your battery is 100%, remove charging pin.')

        try:
            os.startfile(desktop_path)
        except:
            print(f'Reminder saved at {desktop_path}')
