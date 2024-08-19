
# rep grep

## Live grep args picker for telescope.nvim


[ripgrep](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md ":)")

## search with type
$ rg 'fn run' -g '*.rs'
Instead of writing out the glob every time, you can use ripgrep's support for file types:

用 telescope 可以直接 "print" -tpy 来查询python的脚本包含 print


$ rg 'fn run' --type rust
or, more succinctly,

$ rg 'fn run' -trust
The way the --type flag functions is simple. It acts as a name that is assigned to one or more globs that match the relevant files. This lets you write a single type that might encompass a broad range of file extensions. For example, if you wanted to search C files, you'd have to check both C source files and C header files:

$ rg 'int main' -g '*.{c,h}'
or you could just use the C file type:

$ rg 'int main' -tc
Just as you can write blacklist globs, you can blacklist file types too:

$ rg clap --type-not rust
or, more succinctly,

$ rg clap -Trust

