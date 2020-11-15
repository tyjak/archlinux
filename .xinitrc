[[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources
[[ -f /usr/bin/feh ]] && sh ~/.fehbg &

export TERMINAL=termite
export EDITOR=/usr/bin/vim
export PATH=~/share/bin/i3:~/share/bin:/usr/bin:/usr/local/bin:$PATH
export BROWSER=/usr/bin/vimb
export PRINTER=Brother_HL_2030_series
export CITY=AUBERVILLIERS
export QT_AUTO_SCREEN_SCALE_FACTOR=1.5
export SMSFILE=~/share/documents/sms
#export http_proxy=127.0.0.1:8118
#export no_proxy=127.0.0.1,localhost,.jemepropose.com,.twitter.com,.jobintree.com,.adsnovo.com,.admintree.com,.reddit.com
#source ~/share/etc/proxy.pe
export FBFONT=/usr/share/kbd/consolefonts/ter-216n.psf.gz
export DMENUHEIGHT=36

xset -b & #disable beep
xss-lock -- /usr/bin/i3lock -c 002B36 &
dunst &
syndaemon -t -k -i 2 &
unclutter -idle 1 -jitter 2 -root &
stty -ixon
setxkbmap -layout fr
xbindkeys
xmodmap ~/.Xmodmap
#redshift &
#mpd ~/.config/mpd/mpd.conf
udiskie &
mkfifo /tmp/mplayer
touch /tmp/gpodder.out
exec i3
