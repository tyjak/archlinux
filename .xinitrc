[[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources
#[[ "`cat /sys/class/drm/card0-HDMI-A-1/status`" = "connected" ]] && sh ~/.screenlayout/dualscreen.sh
#[[ "`cat /sys/class/drm/card0-HDMI-A-1/status`" = "disconnected" ]] && sh ~/.screenlayout/laptop.sh
[[ -f /usr/local/bin/hotplug_monitor.sh ]] && sh /usr/local/bin/hotplug_monitor.sh
dunst &
syndaemon -t -k -i 2 &
exec i3
