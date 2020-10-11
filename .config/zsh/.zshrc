# generic zsh to use if no zshrc exists



# oh-my-zsh
export ZSH=$HOME/.oh-my-zsh
ZSH_THEME="agnoster"

# custom prompt
[ ! -f "$ZSH/custom/themes/agnoster.zsh-theme" ] && http  --follow --output "$ZSH/custom/themes/agnoster.zsh-theme" https://gist.github.com/tyjak/9f9569d9fc118c88ad3a758fc2b26502/raw/agnoster.zsh-theme

plugins=(git taskwarrior sudo httpie fzf z python virtualenv virtualenvwrapper pip pep8)

#env
export LC_ALL=fr_FR.UTF-8
export EDITOR=vim
export HISTCONTROL=ignorespace
[ -f /usr/bin/fd ] && export FZF_DEFAULT_COMMAND='fd --type f'


source /etc/profile.d/vte.sh
source $ZSH/oh-my-zsh.sh

eval "$(dircolors ~/.config/color/dircolors.256dark)"

alias v='vim "$(fzf)"'
