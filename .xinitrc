[[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources

export EDITOR=/usr/bin/vim
export PATH=~/share/bin:/usr/bin:/usr/local/bin:$PATH
export PATH=~/.gem/ruby/2.1.0/bin/:$PATH
export PYTHONPATH=/usr/lib/python3.3/site-packages
export BROWSER=/usr/bin/vimb
export PRINTER=Brother_HL_2030_series
export http_proxy=127.0.0.1:8118
export no_proxy=127.0.0.1,localhost,.jemepropose.com,.twitter.com,.jobintree.com,.adsnovo.com,.admintree.com,.reddit.com

setxkbmap -layout fr
dunst &
syndaemon -t -k -i 2 &
eval $(ssh-agent)
clipmenud &
unclutter &
stty -ixon
exec i3
