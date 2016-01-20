[[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources
#[[ "`cat /sys/class/drm/card0-HDMI-A-1/status`" = "connected" ]] && sh ~/.screenlayout/dualscreen.sh
#[[ "`cat /sys/class/drm/card0-HDMI-A-1/status`" = "disconnected" ]] && sh ~/.screenlayout/laptop.sh
[[ -f /usr/local/bin/hotplug_monitor.sh ]] && sh /usr/local/bin/hotplug_monitor.sh
[[ -f ~/.Xmodmap ]] && xmodmap ~/.Xmodmap

export EDITOR=/usr/bin/vim
export PATH=~/share/bin:/usr/bin:/usr/local/bin:$PATH
export PATH=~/.gem/ruby/2.1.0/bin/:$PATH
export PYTHONPATH=/usr/lib/python3.3/site-packages
export BROWSER=/usr/bin/vimb
export PRINTER=Brother_HL_2030_series
export http_proxy=127.0.0.1:8118
export no_proxy=127.0.0.1,localhost,www.jemepropose.com,twitter.com,local.jemepropose.com,local.jobintree.com,recette.jemepropose.com,recette.jobintree.com

dunst &
syndaemon -t -k -i 2 &
eval $(ssh-agent)
unclutter &
stty -ixon
exec i3
