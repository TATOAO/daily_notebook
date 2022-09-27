

# 使用packer

``` lua
local packer = require("packer")
packer.startup({
  function(use)
    -- Packer 可以管理自己本身
    use 'wbthomason/packer.nvim'
    -- 你的插件列表...
  end,
  config = {
    -- 并发数限制
    max_jobs = 16,
    -- 自定义源
    git = {
      -- default_url_format = "https://hub.fastgit.xyz/%s",
      -- default_url_format = "https://mirror.ghproxy.com/https://github.com/%s",
      -- default_url_format = "https://gitcode.net/mirrors/%s",
      -- default_url_format = "https://gitclone.com/github.com/%s",
    },

    -- 可以定义display形式为 弹窗
    display = {
        open_fn = function()
            return require("packer.util").float({ border = "single" })
        end,
    },

  },
})

```


## packer 命令

:PackerCompile： 每次改变插件配置时，必须运行此命令或 PackerSync, 重新生成编译的加载文件
:PackerClean ： 清除所有不用的插件
:PackerInstall ： 清除，然后安装缺失的插件
:PackerUpdate ： 清除，然后更新并安装插件
:PackerSync : 执行 PackerUpdate 后，再执行 PackerCompile
:PackerLoad : 立刻加载 opt 插件


## 路径管理

Packer 会将插件默认安装在 标准数据目录/site/pack/packer/start 中，完整目录也就是~/.local/share/nvim/site/pack/packer/start 目录下。



