[[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources
[[ "`cat /sys/class/drm/card0-HDMI-A-1/status`" = "connected" ]] && sh ~/.screenlayout/dualscreen.sh
[[ "`cat /sys/class/drm/card0-HDMI-A-1/status`" = "disconnected" ]] && sh ~/.screenlayout/laptop.sh
[[ -f /usr/bin/feh ]] && sh ~/.fehbg &
exec i3
