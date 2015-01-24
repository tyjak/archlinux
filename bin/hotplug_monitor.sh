#! /usr/bin/bash

export DISPLAY=:0
export XAUTHORITY=/home/david/.Xauthority
#OUTPUTSCREEN=HDMI1
OUTPUTSCREEN=DP2

function connect(){
    #xrandr --output HDMI1 --right-of eDP1 --preferred --primary --output eDP1 --preferred 
    xrandr --output $OUTPUTSCREEN --auto --output eDP1 --off 
    [[ -f /usr/bin/feh ]] && sh ~/.fehbg &
}
  
function disconnect(){
    #xrandr --output HDMI1 --off 
    xrandr --output $OUTPUTSCREEN --off --output eDP1 --auto
    [[ -f /usr/bin/feh ]] && sh ~/.fehbg &
}
     
xrandr | grep "$OUTPUTSCREEN connected" &> /dev/null && connect || disconnect
