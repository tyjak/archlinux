[[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources

# var settings
export PRINTER=Brother_HL_2030_series
export BROWSER=/usr/bin/vimb
export PATH=/usr/bin:/usr/local/bin:$PATH

setxkbmap -layout fr
dunst &
exec i3
