[[ -L ~/.Xresources ]] && xrdb -merge ~/.Xresources
[[ -L ~/.Xmodmap ]] && xmodmap ~/.Xmodmap
#[[ "`cat /sys/class/drm/card0-HDMI-A-1/status`" = "connected" ]] && sh ~/.screenlayout/dualscreen.sh
#[[ "`cat /sys/class/drm/card0-HDMI-A-1/status`" = "disconnected" ]] && sh ~/.screenlayout/laptop.sh
#[[ -f /usr/local/bin/hotplug_monitor.sh ]] && sh /usr/local/bin/hotplug_monitor.sh
export EDITOR=/usr/bin/vim
export PATH=~/share/bin/i3:~/share/bin:/usr/bin:/usr/local/bin:$PATH
export PATH=~/.gem/ruby/2.1.0/bin/:$PATH
export PYTHONPATH=/usr/lib/python3.3/site-packages
export BROWSER=/usr/bin/vimb
export TERMINAL=/usr/bin/termite
export OFFICE_IP=178.208.10.121
export DMENUHEIGHT=24
export WINIT_X11_SCALE_FACTOR=1.0
export TTRSS_SERVER=alarmpi
export NEWS=~/share/documents/feeds
export HOME_ADDR="#get the value via a file"
#export http_proxy=192.168.0.20:8118
#export http_proxy=127.0.0.1:8118
#export no_proxy=127.0.0.1,localhost,.jemepropose.com,.twitter.com,.jobintree.com,.adsnovo.com,.admintree.com,.reddit.com
[[ -f /usr/bin/fd ]] && export FZF_DEFAULT_COMMAND='/usr/bin/fd --type f'
#TOFIX no personal settings here, see how to move to some files to be shared via syncthing

#systemctl --user import-environment
#systemctl --user start graphical-session.target
autocutsel -fork &
autocutsel -selection PRIMARY -fork &

#dunst &
syndaemon -t -k -i 2 &
eval $(ssh-agent)
unclutter &
#stty -ixon
#xbindkeys -> pb commande non trouvé (voir journalctl -xn)
#clipmenud &
#redshift &
#udiskie &
#mpd ~/.config/mpd/mpd.conf
exec i3
