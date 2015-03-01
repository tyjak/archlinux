[[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources
dunst &
syndaemon -t -k -i 2 &
exec i3
