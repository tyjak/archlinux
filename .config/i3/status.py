# -*- coding: utf-8 -*-

import logging
import subprocess
import os.path
import re
import time
#import netifaces

from i3pystatus import Status
from i3pystatus.weather import weathercom
from i3pystatus.updates import yay, pacman

location = {"AUBERVILLIERS":"FRXX0007:1:FR", "MEUZAC":"FRXX1548:1:FR"}
city = os.getenv('CITY','AUBERVILLIERS')

#status = Status(standalone=True, logfile='i3pystatus.log')
status = Status(standalone=True)

green="#2aa198"
orange="#b58900"
red="#dc321F"
grey="#93a1a1"

#show a dot
status.register("anybar",
            hints = {"min_width": 12},
            on_leftclick="infonotif creamy up state"
        )

# covid19 R0
status.register("anybar",
            port=1837,
            hints = {"separator": False, "separator_block_width": 4},
            on_leftclick="infonotif R0 covid19"
        )


# FIXME: error "IndexError: list index out of range" when ping ok...
status.register(
    "ping",
    format="\uf0ec",
    interval=1,
    color="#00FF00",
    color_disabled="#949494",
    format_down="\uf0ec",
    host="1.1.1.1",
    hints={'separator':False, 'separator_block_width':10}
)


# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
            on_leftclick="pal-i3",
            hints = {"separator": False, "separator_block_width": 4}
            )


# Show sound
#status.register("pulseaudio",
#        format="\U0001D160  {volume}",
#        color_muted=red,
#        on_leftclick="apptoggle pavucontrol"
#        )

status.register("alsa",
        format="\U0001D160  {volume}",
        color_muted=red,
        on_leftclick="apptoggle pavucontrol"
        )

def gpodder_perc(text):
    lines = text.split("\n")[-2:]
    if(re.match('^ANS_', lines[0])):
        length = float(re.sub(r'^ANS_LENGTH=([0-9]+)',r'\1',list(filter(lambda v: re.match(r'^ANS_LENGTH=',v), lines))[0]))
        pos = float(re.sub(r'^ANS_TIME_POSITION=([0-9]+)',r'\1',list(filter(lambda v: re.match(r'^ANS_TIME_POSITION=',v), lines))[0]))
        time_format = ["%M:%S","%H:%M:%S"]
        last_time = length - pos 
        return 'podcast: -'+time.strftime(time_format[last_time>3600], time.gmtime(last_time))
    else:
        return ''

#gpodder data are get from mplayer fifo via ~/share/bin/playpodcast
status.register(
    "file",
    components={"podcast":(gpodder_perc,'gpodder.out')},
    base_path="/tmp",
    format="{podcast}"
)

# Show battery
if os.path.isfile("/sys/class/power_supply/BAT0/uevent"):
    status.register("battery",
            format = "[{remaining} ]{status}{glyph}",
            alert = True,
            alert_percentage = 12,
            full_color = green,
            charging_color = orange,
            critical_color = red,
            on_rightclick = 'popup -f "watch upower -i /org/freedesktop/UPower/devices/battery_BAT0"',
            glyphs = ["\uf244","\uf243","\uf242","\uf241","\uf240"],
            status = {"DPL":"\uf12a",
                    "CHR":"\uf0e7",
                    "DIS":"",
                    "FULL":""}
            )

# Show count updates available
status.register("updates",
        backends = [yay.Yay(False), pacman.Pacman()],
        format = "\uf323 {count}",
        format_working = "\uf323",
        on_rightclick = 'yay-i3',
        color = red,
        color_working = "#FF8800"
        )

# Show network
net_interfaces = "wlan0"
status.register("network",
	interface=net_interfaces,
        format_up="\uf1eb {network_graph_recv}",
        start_color=green,
        end_color=red,
        color_up=green,
        color_down=red,
        dynamic_color = True,
        graph_style = 'braille-fill',
        on_rightclick = 'popup -e "sudo wifi-menu"',
        on_leftclick = 'popup -e "watch -n 0.2 iwconfig"',
        graph_width = 20
	)


status.register("syncthing",
                format_up="\uf311",
                format_down="\uf311",
            color_up=green,
            color_down=red,
                on_leftclick="vimb http://127.0.0.1:8384")

status.register("shell",
                command="systemctl --user is-active ipfs.service",
                ignore_empty_stdout=False,
                format="\uf1b2",
                color=green,
                error_color=grey,
                interval=5,
                on_leftclick="~/share/bin/toggle-ipfs",
                on_rightclick="webapp http://127.0.0.1:5001/ipfs/bafybeianwe4vy7sprht5sm3hshvxjeqhwcmvbzq73u55sdhqngmohkjgs4/#/files ipfs")

status.register("openvpn",
        vpn_name = 'creamy',
        color_up=green,
        color_down=grey,
        status_up= "\uf00C",
        status_down= "",
        use_new_service_name = 'true'
        )

#status.register("openvpn",
#        vpn_name = 'kamatera',
#        color_up=green,
#        color_down=grey,
#        status_up= "\uF00C",
#        status_down= "",
#        use_new_service_name = 'true'
#        )

#status.register("openvpn",
#        vpn_name = 'pe',
#        use_new_service_name = 'true'
#        )
#

#Show backlight
if os.path.isfile("/sys/class/backlight/acpi_video0/brightness"):
    status.register("backlight",
    format="\u263c {percentage}%"
    )

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
status.register("load",
        on_leftclick="popup -s medium -e sudo gotop"
        )

status.register("mem",
        format = "{percent_used_mem}%",
        color = "#93a1a1",
        warn_percentage = 90,
        alert_percentage = 94,
        on_leftclick="popup -s medium -e sudo gotop"
        )

# Shows disk usage of /

# Format:
# 42/128G [86G]
#status.register("disk",
#    path="/home",
#    on_leftclick="popup -S -s medium -e 'ncdu /home --exclude=media'",
#    #format="{used}/{total}G [{avail}G]",)
#    format="{avail}G",)

status.register("disk",
    path="/",
    on_leftclick="ncdu-i3",
    #format="{used}/{total}G [{avail}G]",)
    format="{avail}G",)


# Show weather => need ttf-weather-icons
# See https://openweathermap.org/weather-conditions for text
# See https://erikflowers.github.io/weather-icons/ for icon
color_icon_values={
    'Cloudy': ('<span font="Weather Icons 10">\uf013</span>', '#f8f8ff'),
    'Fog': ('<span font="Weather Icons 10">\uf014</span>', '#949494'),
    'Thunderstorm': ('<span font="Weather Icons 10">\uf016</span>', '#cbd2c0'),
    'Fair': ('<span font="Weather Icons 10">\uf00c</span>', '#ffcc00'),
    'Rain': ('<span font="Weather Icons 10">\uf019</span>', '#cbd2c0'),
    'Rain Shower': ('<span font="Weather Icons 10">\uf01a</span>', '#cbd2c0'),
    'Rainy': ('<span font="Weather Icons 10">\uf0b5</span>', '#cbd2c0'),
    'Partly Cloudy': ('<span font="Weather Icons 10">\uf002</span>', '#f8f8ff'),
    'Snow': ('<span font="Weather Icons 10">\uf01b</span>', '#ffffff'),
    'default': ('', None),
    'Sunny': ('<span font="Weather Icons 10">\uf00d</span>', '#ffff00')
}

status.register("weather",
    #location_code="FRXX5264",
    interval=900,
    colorize=True,
    color_icons=color_icon_values,
    format="{icon} {current_temp}°C {wind_speed}kph",
    #format='{current_temp}{temp_unit}[ {icon}][ Max: {high_temp}{temp_unit}][ Min: {low_temp}{temp_unit}][ {wind_speed}{wind_unit} {wind_direction}][{pressure_trend}]',
    on_leftclick='wego-i3',
    hints={'markup': 'pango'},
    log_level=logging.DEBUG,
    backend=weathercom.Weathercom(
        location_code='FRXX0076:1:FR',
        units='metric',
        log_level=logging.DEBUG
    ),
)


status.register("bitcoin",
        currency="USD",
        colorize=True,
        color_up=green,
        color_down=red,
        on_leftclick='',
        on_doubleleftclick='coin',
        on_rightclick='binance',
        interval=30,
        )

#status.register("pomodoro",
#        sound="~/share/sounds/196106__aiwha__ding.wav",
#        format="\uE001 {current_pomodoro}/{total_pomodoro} {time}")

status.run()
