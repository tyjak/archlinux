# -*- coding: utf-8 -*-

# import logging
import subprocess
import os.path
import re
import time

from i3pystatus import Status
from i3pystatus.updates import yay, pacman

location = {"AUBERVILLIERS": "FRXX0007:1:FR", "MEUZAC": "FRXX1548:1:FR"}
city = os.getenv("CITY", "AUBERVILLIERS")
hidpi_scale = os.getenv("HIDPI_SCALE", 1)

status = Status(standalone=True, logfile='i3pystatus.log')
# status = Status(standalone=True)

green="#2aa198"
orange="#d33682"
red="#dc321F"
grey="#93a1a1"

# show a dot
status.register(
    "anybar",
    hints={'separator': False, 'separator_block_width': 10},
    on_leftclick="infonotif 'creamy up state'"
)

# show meuzac status
status.register(
    "anybar",
    port=1837,
    hints={'separator': False, 'separator_block_width': 10},
    on_leftclick="infonotif Meuzac"
)

# FIXME: error "IndexError: list index out of range" when ping ok...
status.register(
    "ping",
    format="\uf0ec",
    interval=1,
    color=green,
    color_disabled=grey,
    format_down="\uf0ec",
    host="1.1.1.1",
    hints={'separator': False, 'separator_block_width': 10}
)

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register(
    "clock",
    on_leftclick="twcal-i3",
)

# Show sound
# status.register("pulseaudio",
#        format="\U0001D160  {volume}",
#        )

status.register(
    "alsa",
    format="{volume} \uf028",
    color_muted=red,
    on_leftclick="apptoggle pavucontrol",
)

status.register(
    "shell",
    command="headset_battery_level barba",
    on_leftclick="headset_quality_switch barba",  # mic or not mic
    ignore_empty_stdout=True,
    format="{output}"
   )


#def gpodder_perc(text):
#    lines = text.split("\n")[-2:]
#    if (re.match('^ANS_', lines[0])):
#        length = float(re.sub(r'^ANS_LENGTH=([0-9]+)', r'\1', list(filter(lambda v: re.match(r'^ANS_LENGTH=', v), lines))[0]))
#        pos = float(re.sub(r'^ANS_TIME_POSITION=([0-9]+)', r'\1', list(filter(lambda v: re.match(r'^ANS_TIME_POSITION=', v), lines))[0]))
#        time_format = ["%M:%S", "%H:%M:%S"]
#        last_time = length - pos 
#        return 'podcast: -'+time.strftime(time_format[last_time > 3600], time.gmtime(last_time))
#    else:
#        return ''


# gpodder data are get from mplayer fifo via ~/share/bin/playpodcast
#status.register(
#    "file",
#    components={"podcast": (gpodder_perc, 'gpodder.out')},
#    base_path="/tmp",
#    format="{podcast}"
#)

# Show battery
if os.path.isfile("/sys/class/power_supply/BAT0/uevent"):
    status.register(
        "battery",
        format="[{remaining} ]{status}{glyph}",
        alert=True,
        alert_percentage=8,
        full_color=green,
        charging_color=orange,
        critical_color=red,
        glyphs=["\uf244", "\uf243", "\uf242", "\uf241", "\uf240"],
        status={"DPL": "\uf12a", "CHR": "\uf0e7", "DIS": "", "FULL": ""},
    )

# Show count updates available
status.register(
    "updates",
    backends = [yay.Yay(False), pacman.Pacman()],
    format = "\uf323 {count}",
    format_working = "\uf323",
        on_rightclick = 'popup -d -s medium -f -e "yay -Syu && paccache -r -k 2 && ~/share/bin/yaycache-keep2 && echo \"Done.\""',
    color = red,
    color_working = orange
)


# Show network
#net_interfaces = "wlp4s0"
#status.register(
#    "network",
#    interface=net_interfaces,
#    format_up="\uf1eb {network_graph_recv} {bytes_recv}KB/s {essid} {quality}%",
#    dynamic_color=True,
#    graph_style="braille-fill",
#    on_rightclick = 'popup -e "sudo wifi-menu"',
#    on_leftclick = 'popup -e "watch -n 0.2 iwconfig"',
#    graph_width=20,
#)

status.register(
    "syncthing",
    color_up=green,
    color_down=red,
    format_up="\uf311",
    format_down="\uf311",
    on_leftclick="vimb http://127.0.0.1:8384",
)

#status.register("openvpn", vpn_name="peold", use_new_service_name="true")

status.register("openvpn", vpn_name="ft", use_new_service_name="true")

status.register("openvpn", vpn_name="creamy", use_new_service_name="true")

# Show backlight
if os.path.isfile("/sys/class/backlight/acpi_video0/brightness"):
    status.register(
        "backlight", format="\uf09e {percentage}%", backlight="intel_backlight"
    )

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
status.register("load", on_leftclick="popup -S -s medium -e sudo gotop")

# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register(
    "disk",
    path="/",
    on_leftclick="popup -S -s medium ncdu --exclude ~/pCloudDrive/",
    # format="{used}/{total}G [{avail}G]",)
    format="{avail}G",
)

# NOTE : noto-fonts and noto-fonts-emoji to work
status.register("shell",
                command="curl -Ls -f 'wttr.in/"+city+"?format=%c+%t+%w+%h'",
                ignore_empty_stdout=True,
                #format="\uf1b2",
                #color=green,
                #error_color=grey,
                interval=7200,
                on_leftclick='wego-i3')

# check fuel price
status.register("shell_ansi",
                command="price_check.sh prix-essence 'à Magnac'",
                format="{output}€",
                ignore_empty_stdout=True,
                #format="\uf1b2",
                #color=green,
                #error_color=grey,
                interval=7200)

## Show weather => need ttf-weather-icons
#color_icon_values = {
#    "Cloudy": ('<span font="Weather Icons 10">\uf013</span>', "#f8f8ff"),
#    "Fog": ('<span font="Weather Icons 10">\uf014</span>', "#949494"),
#    "Thunderstorm": ('<span font="Weather Icons 10">\uf016</span>', "#cbd2c0"),
#    "Fair": ('<span font="Weather Icons 10">\uf00c</span>', "#ffcc00"),
#    "Rainy": ('<span font="Weather Icons 10">\uf019</span>', "#cbd2c0"),
#    "Partly Cloudy": ('<span font="Weather Icons 10">\uf002</span>', "#f8f8ff"),
#    "Snow": ('<span font="Weather Icons 10">\uf01b</span>', "#ffffff"),
#    "default": ("", None),
#    "Sunny": ('<span font="Weather Icons 10">\uf00d</span>', "#ffff00"),
#}
#
#status.register(
#    "weather",
#    format="{current_temp}{temp_unit}[ {icon}]",
#    on_rightclick='HIDPI_SCALE=1.5 popup -s medium -f -e "~/share/bin/wego {}"'.format(city),
#    interval=900,
#    colorize=True,
#    color_icons=color_icon_values,
#    # format="{current_temp} {current_wind} {humidity}%",
#    # format='{current_temp}{temp_unit}[ {icon}][ Max: {high_temp}{temp_unit}][ Min: {low_temp}{temp_unit}][ {wind_speed}{wind_unit} {wind_direction}][{pressure_trend}]',
#    # log_level=logging.DEBUG,
#    hints={"markup": "pango"},
#    backend=weathercom.Weathercom(
#        location_code=location[city],
#        units="metric",
#        # log_level=logging.DEBUG,
#    ),
#)

# modem_icon = [
#     '',
#     '\uf8a3',
#     '\uf8a6',
#     '\uf8a9',
#     '\uf8ac'
# ]
#status.register(
#    "shell",
#    command="modem-signal-huewai",
#    on_leftclick="vimb http://192.168.8.1",
#    ignore_empty_stdout=True,
#    format="{output}"
#)

status.register(
    "taskwarrior",
    urgent_filter="context:work +DUE",
    format="{urgent}"
)

status.register("shell",
                command="curl -Ls -f 'ifconfig.me'",
                ignore_empty_stdout=True,
                # format="\uf1b2",
                # color=green,
                # error_color=grey,
                interval=300)


# status.register("shell",
#     command="watchprice https://certideal.com/iphone-12-mini/iphone-12-mini-128-go-bleu-6219 '//*[@id=\"product-state-switch\"]/div[2]/div/a/div/div/p[1]'",
#     on_leftclick="vimb https://certideal.com/iphone-12-mini/iphone-12-mini-128-go-bleu-6219",
#     ignore_empty_stdout=True,
#     format="{output}",
#     interval=3600
#        )

#status.register(
#    "pomodoro",
#    sound="~/share/sounds/196106__aiwha__ding.wav",
#    format="\uE001 {current_pomodoro}/{total_pomodoro} {time}",
#)


#status.register(
#    "bitcoin",
#    currency="USD",
#    colorize=True,
#    on_leftclick="",
#    on_doubleleftclick="coin",
#    on_rightclick="binance",
#    interval=30,
#)

# status.register("shell",
#        command="newsboat -u ~/share/documents/news-urls -x reload print-unread",
#        on_rightclick="news",
#        interval=3600,
#        )
#

status.run()
