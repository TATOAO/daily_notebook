
# echo 工具
:echo @%                |" directory/name of file
:echo expand('%:t')     |" name of file ('tail')
:echo expand('%:p')     |" full path
:echo expand('%:p:h')   |" directory containing file ('head')


vim 里面的特殊含义  % 当前文件
:!echo %
:!echo %:t
:!echo %:p
:!echo %:p:h

