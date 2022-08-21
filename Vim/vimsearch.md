# vim search 和 

这些不用 escape
 < > ' "

这些需要 escape

( / & ! . ^ * $ \ ?) 

https://stackoverflow.com/questions/3864467/whats-the-difference-between-vim-regex-and-normal-regex

Perl    Vim             vscode vim           Explanation
---------------------------
x?      x\=                                     Match 0 or 1 of x                                   
x+      x\+             x+                      Match 1 or more of x
(xyz)   \(xyz\)                                 Use brackets to group matches
x{n,m}  x\{n,m}                                 Match n to m of x
x*?     x\{-}                                   Match 0 or 1 of x, non-greedy
x+?     x\{-1,}                                 Match 1 or more of x, non-greedy
\b      \< \>                                   Word boundaries
$n      \n                                      Backreferences for previously grouped matches


------



### https://stackoverflow.com/questions/3101877/find-first-non-matching-line-in-vim

negative look behind 
@<!
