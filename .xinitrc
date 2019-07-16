[[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources
[[ -f /usr/bin/feh ]] && sh ~/.fehbg &

export TERMINAL=termite
export EDITOR=/usr/bin/vim
export PATH=~/share/bin/i3:~/share/bin:/usr/bin:/usr/local/bin:$PATH
export BROWSER=/usr/bin/vimb
export PRINTER=Brother_HL_2030_series
export CITY=AUBERVILLIERS
#export http_proxy=127.0.0.1:8118
#export no_proxy=127.0.0.1,localhost,.jemepropose.com,.twitter.com,.jobintree.com,.adsnovo.com,.admintree.com,.reddit.com
#source ~/share/etc/proxy.pe

xss-lock -- /usr/bin/i3lock -c 002B36 &
dunst &
syndaemon -t -k -i 2 &
unclutter &
stty -ixon
setxkbmap -layout fr
xbindkeys
xmodmap ~/.Xmodmap
#redshift &
#mpd ~/.config/mpd/mpd.conf
udiskie &
mkfifo /tmp/mplayer
exec i3
