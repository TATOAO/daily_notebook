


## echo useful info




command line in neovim:

:echo stdpath('config')
:echo stdpath('data')


## change stdpath


:h standard-path

The "base" (root) directories conform to the XDG Base Directory Specification.
https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html
The $XDG_CONFIG_HOME, $XDG_DATA_HOME, $XDG_RUNTIME_DIR, $XDG_STATE_HOME,
$XDG_CACHE_HOME, $XDG_CONFIG_DIRS and $XDG_DATA_DIRS environment variables
are used if defined, else default values (listed below) are used.


Throughout the help pages these defaults are used as placeholders, e.g.
"~/.config" is understood to mean "$XDG_CONFIG_HOME or ~/.config".

CONFIG DIRECTORY (DEFAULT) ~
                  *$XDG_CONFIG_HOME*            Nvim: stdpath("config")
    Unix:         ~/.config                   ~/.config/nvim
    Windows:      ~/AppData/Local             ~/AppData/Local/nvim

DATA DIRECTORY (DEFAULT) ~
                  *$XDG_DATA_HOME*              Nvim: stdpath("data")
    Unix:         ~/.local/share              ~/.local/share/nvim
    Windows:      ~/AppData/Local             ~/AppData/Local/nvim-data

RUN DIRECTORY (DEFAULT) ~
                  *$XDG_RUNTIME_DIR*            Nvim: stdpath("run")
    Unix:         /tmp/nvim.user/xxx          /tmp/nvim.user/xxx
    Windows:      $TMP/nvim.user/xxx          $TMP/nvim.user/xxx

STATE DIRECTORY (DEFAULT) ~
                  *$XDG_STATE_HOME*             Nvim: stdpath("state")
    Unix:         ~/.local/state              ~/.local/state/nvim
    Windows:      ~/AppData/Local             ~/AppData/Local/nvim-data

CACHE DIRECTORY (DEFAULT) ~
                  *$XDG_CACHE_HOME*             Nvim: stdpath("cache")
    Unix:         ~/.cache                    ~/.cache/nvim
    Windows:      ~/AppData/Local/Temp        ~/AppData/Local/Temp/nvim-data

LOG FILE (DEFAULT) ~
                  `$NVIM_LOG_FILE`              Nvim: stdpath("log")/log
    Unix:         ~/.local/state/nvim         ~/.local/state/nvim/log
    Windows:      ~/AppData/Local/nvim-data   ~/AppData/Local/nvim-data/log

Note that stdpath("log") is currently an alias for stdpath("state").





### usage


export XDG_CONFIG_HOME=$(realpath .)


To build the app image
export XDG_CONFIG_HOME="/AppDir/usr/share/config"
export XDG_DATA_HOME='/AppDir/usr/share/local/state'
export XDG_STATE_HOME='/AppDir/usr/share/local/share'


E121: Undefined variable: sjeifjew

/Users/tatoaoliang/.local/share/nvim
