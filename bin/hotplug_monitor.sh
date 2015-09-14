#!/usr/bin/bash

export DISPLAY=:0.0
export XAUTHORITY=/home/david/.Xauthority
#OUTPUTSCREEN=HDMI1
OUTPUTSCREEN=DP2

function connect(){
echo $DISPLAY
    #xrandr --output HDMI1 --right-of eDP1 --preferred --primary --output eDP1 --preferred 
    xrandr --output $OUTPUTSCREEN --auto --preferred --primary --output eDP1 --off
    #if grep -q open /proc/acpi/button/lid/LID0/state
    #then
    #    xrandr --output eDP1 --auto --left-of $OUTPUTSCREEN 
    #else
    #    xrandr --output eDP1 --off
    #fi
    [[ -f /usr/bin/feh ]] && sh ~/.fehbg &
}
  
function disconnect(){
    #xrandr --output HDMI1 --off 
    xrandr --output $OUTPUTSCREEN --off --output eDP1 --auto
    [[ -f /usr/bin/feh ]] && sh ~/.fehbg &
}
     
xrandr | grep "$OUTPUTSCREEN connected" &> /dev/null && connect || disconnect
