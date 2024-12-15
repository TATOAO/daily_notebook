# 中文输入法退出 normal mode 自动切换英文


 install im-select

 https://github.com/daipeihust/im-select#installation

 vscode setting.json

"vim.autoSwitchInputMethod.enable": true,
"vim.autoSwitchInputMethod.defaultIM": "com.apple.keylayout.US",
"vim.autoSwitchInputMethod.obtainIMCmd": "/usr/local/bin/im-select",
"vim.autoSwitchInputMethod.switchIMCmd": "/usr/local/bin/im-select {im}"

作者：Daniel
链接：https://www.zhihu.com/question/303850876/answer/540324790
来源：知乎


# vscode vim 模式无法用右键复制问题

"vim.useSystemClipboard": true

https://stackoverflow.com/questions/58306002/vs-code-vim-extension-copy-and-paste
