# -*- coding: utf-8 -*-

import subprocess
import os.path

from i3pystatus import Status

status = Status(standalone=True)

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock")

# Show sound
#status.register("alsa")

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
status.register("network",
	interface="wlp2s0",
        format_up="{network_graph}{kbs}KB/s {essid} {quality}%",
        dynamic_color = True,
        graph_style = 'braille-fill',
        graph_width = 20
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

# Show weather
status.register("weather",
        location_code="FRXX5264",
        colorize=True,
        format="{current_temp} {current_wind} {humidity}%",
        )


status.register("bitcoin",
        currency="EUR",
        symbol="\uF15A")

status.run()
