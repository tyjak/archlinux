# -*- coding: utf-8 -*-

import subprocess

from i3pystatus import Status

status = Status(standalone=True)

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock")

# Show sound
#status.register("alsa")

# Show battery
status.register("battery",
	format="{remaining} {status}")

# Show network
status.register("network",
	interface="wlp2s0",
        format_up="{network_graph}{kbs}KB/s {essid} {quality}%",
        dynamic_color = True,
        graph_style = 'braille-fill',
        graph_width = 20
	)
#Show backlight
status.register("backlight",
	format="\u263C {percentage}%",
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
        format="{current_temp} {current_wind} {humidity}%",)


status.register("bitcoin",
        currency="EUR")

status.run()
