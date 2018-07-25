# -*- coding: utf-8 -*-

import subprocess
import os.path
#import netifaces

from i3pystatus import Status
from i3pystatus.weather import weathercom

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
        )

#status.register("alsa",
#        format="\U0001D160  {volume}",
#        color_muted="#FF0000",
#        on_leftclick="pavucontrol"
#        )

# Show battery
if os.path.isfile("/sys/class/power_supply/BAT0/uevent"):
    status.register("battery",
            format="{remaining} {status}",
            alert=True,
            alert_percentage= 10,
            status={"DPL":"\uf212",
                    "CHR":"\uf211",
                    "DIS":"\uf215",
                    "FULL":"\uf213"}
            )

# Show network
net_interfaces = "wlp2s0b1"
status.register("network",
	interface=net_interfaces,
        format_up="\uf1eb {network_graph_recv} {bytes_recv}KB/s {essid} {quality}%",
        dynamic_color = True,
        graph_style = 'braille-fill',
        graph_width = 20
	)

status.register("syncthing")

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

#Show backlight
if os.path.isfile("/sys/class/backlight/acpi_video0/brightness"):
    status.register("backlight",
	format="\uf185 {percentage}%",
        backlight="intel_backlight")

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
status.register("load")

# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register("disk",
    path="/",
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

	hints={'markup': 'pango'},
	backend=weathercom.Weathercom(
	    location_code='FRXX0007:1:FR',
	    units='metric',
	),
)


status.register("bitcoin",
        currency="EUR",
        colorize=True,
        symbol="\uF15A")

#status.register("pomodoro",
#        sound="~/share/sounds/196106__aiwha__ding.wav",
#        format="\uE001 {current_pomodoro}/{total_pomodoro} {time}")

status.run()
