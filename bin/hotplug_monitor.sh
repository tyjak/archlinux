#! /usr/bin/bash

export DISPLAY=:0
export XAUTHORITY=/home/david/.Xauthority

function connect(){
    #xrandr --output HDMI1 --right-of eDP1 --preferred --primary --output eDP1 --preferred 
    xrandr --output HDMI1 --auto --output eDP1 --off 
    [[ -f /usr/bin/feh ]] && sh ~/.fehbg &
}
  
function disconnect(){
    #xrandr --output HDMI1 --off 
    xrandr --output HDMI1 --off --output eDP1 --auto
    [[ -f /usr/bin/feh ]] && sh ~/.fehbg &
}
     
xrandr | grep "HDMI1 connected" &> /dev/null && connect || disconnect
