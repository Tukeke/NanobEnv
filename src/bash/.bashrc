# Editor and deity
export DEITY=GOD
export EDITOR=vim

## Less important...
	export BROWSER="/usr/bin/mozilla"
	export MAIL="/var/spool/mail/xayon"

# This is for debian packaging
export DEBEMAIL="xayon@xayon.net"
export DEBFULLNAME="David Francos Cuartero (XayOn)"

# This is for debian live devel
export LH_INTERACTIVE="enabled"

# Set $HOME/.bin in path to make some home scripts work :)
export PATH=$PATH:$HOME/.bin/
export CDPATH=".:~:~/temp/:~/temp/GoogleCode/"

# Some other handy variables.
shopt -s cdable_vars
export CGIBIN=/usr/lib/cgi-bin

#History stuffs
export HISTCONTROL=$HISTCONTROL${HISTCONTROL+,}ignoredups
export HISTCONTROL=ignoreboth
shopt -s histappend

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "$debian_chroot" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi
export TERM="xterm-256color"

# I allways use a coloured prompt
PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '

# external alias file.
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    eval "`dircolors -b`"
    alias ls='ls --color=yes'
    alias dir='dir --color=yes'
    alias vdir='vdir --color=yes'

    alias grep='grep --color=yes'
    alias fgrep='fgrep --color=yes'
    alias egrep='egrep --color=yes'
fi

# some more ls aliases
alias ll='ls -l -v1'
alias la='ls -A'
alias l='ls -CF -v1'
