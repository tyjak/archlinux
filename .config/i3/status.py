# -*- coding: utf-8 -*-

import subprocess
import os.path
#import netifaces

from i3pystatus import Status
from i3pystatus.weather import weathercom
from i3pystatus.updates import yay, pacman

location = {"AUBERVILLIERS":"FRXX0007:1:FR", "MEUZAC":"FRXX1548:1:FR"}
city = os.getenv('CITY','AUBERVILLIERS')

#status = Status(standalone=True, logfile='i3pystatus.log')
status = Status(standalone=True)


#show a dot
status.register("anybar")

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
            on_leftclick="[ $( ps -eo cmd | grep -c '[t]ermite --title scratchpad_cal' ) -eq 2 ] && termite --title scratchpad_cal -e 'pal -m' || i3-msg [title=scratchpad_cal] scratchpad show;")

# Show sound
status.register("pulseaudio",
        format="\U0001D160  {volume}",
        color_muted="#FF0000",
        on_leftclick="apptoggle pavucontrol"
        )

#status.register("alsa",
#        format="\U0001D160  {volume}",
#        color_muted="#FF0000",
#        on_leftclick="pavucontrol"
#        )

# Show battery
if os.path.isfile("/sys/class/power_supply/BAT0/uevent"):
    status.register("battery",
            format = "[{remaining} ]{status}{glyph}",
            alert = True,
            alert_percentage = 8,
            full_color = "#00FF00",
            charging_color = "#b58900",
            critical_color = "#FF0000",
            glyphs = ["\uf244","\uf243","\uf242","\uf241","\uf240"],
            status = {"DPL":"\uf12a",
                    "CHR":"\uf0e7",
                    "DIS":"",
                    "FULL":""}
            )

# Show count updates available
status.register("updates",
        backends = [yay.Yay(), pacman.Pacman()],
        format = "\uf187 {count}",
        format_working = "\uf94f",
        on_rightclick = 'popup -d -s medium -f -e "yay -Syu && echo \"Done.\""',
        color = "#FF0000",
        color_working = "#FF8800"
        )

# Show network
net_interfaces = "wlp2s0b1"
status.register("network",
	interface=net_interfaces,
        format_up="\uf09e {network_graph_recv}",
        dynamic_color = True,
        graph_style = 'braille-fill',
        on_rightclick = 'popup -e "sudo wifi-menu"',
        on_leftclick = 'popup -e "watch -n 0.2 iwconfig"',
        graph_width = 20
	)


status.register("syncthing",
                format_up="\uf311",
                format_down="\uf311",
                on_leftclick="vimb http://127.0.0.1:8080")

status.register("runwatch",
        path="/var/run/ppp0.pid",
        name="VPN adsnovo",
        format_up="{name}",
        format_down="",
        )

status.register("runwatch",
        path="/run/openvpn@adsnovo.pid",
        name="VPN adsnovo",
        format_up="{name}",
        format_down="",
        )

status.register("openvpn",
        vpn_name = 'creamy',
        use_new_service_name = 'true'
        )

status.register("openvpn",
        vpn_name = 'pe',
        use_new_service_name = 'true'
        )


#Show backlight
#if os.path.isfile("/sys/class/backlight/acpi_video0/brightness"):
#    status.register("backlight",
#	format="\uf09e {percentage}%",
#        backlight="intel_backlight")

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
status.register("load",
        on_leftclick="popup -e gotop"
        )

# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register("disk",
    path="/",
    on_leftclick="popup -S -s medium -e ncdu /var",
    #format="{used}/{total}G [{avail}G]",)
    format="{avail}G",)

status.register("disk",
    path="/home",
    on_leftclick="popup -S -s medium -e ncdu",
    #format="{used}/{total}G [{avail}G]",)
    format="{avail}G",)

# Show weather => need ttf-weather-icons
color_icon_values={
	'Cloudy': ('<span font="Weather Icons 10">\uf013</span>', '#f8f8ff'),
	'Fog': ('<span font="Weather Icons 10">\uf014</span>', '#949494'),
	'Thunderstorm': ('<span font="Weather Icons 10">\uf016</span>', '#cbd2c0'),
	'Fair': ('<span font="Weather Icons 10">\uf00c</span>', '#ffcc00'),
	'Rainy': ('<span font="Weather Icons 10">\uf019</span>', '#cbd2c0'),
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
        #format="{current_temp} {current_wind} {humidity}%",
	format='{current_temp}{temp_unit}[ {icon}][ Max: {high_temp}{temp_unit}][ Min: {low_temp}{temp_unit}][ {wind_speed}{wind_unit} {wind_direction}][{pressure_trend}]',
        on_leftclick="popup -e wego",

	hints={'markup': 'pango'},
	backend=weathercom.Weathercom(
	    location_code='FRXX0007:1:FR',
	    units='metric',
	),
)


status.register("bitcoin",
        currency="EUR",
        colorize=True,
        on_rightclick=['open_something', 'https://cryptowat.ch/markets/kraken/btc/eur/15m'],
        symbol="\uF15A")

#status.register("pomodoro",
#        sound="~/share/sounds/196106__aiwha__ding.wav",
#        format="\uE001 {current_pomodoro}/{total_pomodoro} {time}")

status.run()
