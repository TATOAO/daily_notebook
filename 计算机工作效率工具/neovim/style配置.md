
# highlight group 


比如说 colorcolumn 80 th


[Link](https://codeyarns.com/tech/2011-07-29-vim-set-color-of-colorcolumn.html#gsc.tab=0 ":)")

:highlight ColorColumn guibg=Black


[reddit](https://www.reddit.com/r/neovim/comments/xvb1wc/how_to_link_a_highlight_group_in_a_lua/ ":)")



```
vim.api.nvim_set_hl(0, 'Normal', { fg = "#ffffff", bg = "#333333" })
vim.api.nvim_set_hl(0, 'Comment', { fg = "#111111", bold = true })
vim.api.nvim_set_hl(0, 'Error', { fg = "#ffffff", undercurl = true })
vim.api.nvim_set_hl(0, 'Cursor', { reverse = true })


vim.api.nvim_set_hl(0, "your-group", { link = "another-group" })
```



vim.api.nvim_set_hl(0, 'ColorColumn', { fg = "#ffffff", undercurl = true })

失败了
