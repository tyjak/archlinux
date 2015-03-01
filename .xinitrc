[[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources
setxkbmap -layout fr
dunst &
exec i3
