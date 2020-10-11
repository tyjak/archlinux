# generic zsh to use if no zshrc exists

# oh-my-zsh
ZSH_THEME="agnoster"
plugins=(git taskwarrior sudo httpie fzf z python virtualenv virtualenvwrapper pip pep8)

#env
export LC_ALL=fr_FR.UTF-8
export EDITOR=vim
export HISTCONTROL=ignorespace
[ -f /usr/bin/fd ] && export FZF_DEFAULT_COMMAND='fd --type f'


source /etc/profile.d/vte.sh
source $HOME/.oh-my-zsh.sh

eval "$(dircolors ~/.config/color/dircolors.256dark)"

alias v='vim "$(fzf)"'