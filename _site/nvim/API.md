

# Neovim 重要api


```lua
local function start_job()
    -- Callbacks to handle job output and exit
    local on_stdout = function(job_id, data, event)
        if data then
            print("Output:", table.concat(data, "\n"))
        end
    end

    local on_exit = function(job_id, exit_code, event)
        print("Job", job_id, "exited with code", exit_code)
    end

    -- Setting up the jobstart options
    local opts = {
        on_stdout = on_stdout,
        on_exit = on_exit,
        stdout_buffered = true,
		stdin = true and "pipe"
    }

	local command = {
		"/Users/tatoaoliang/.local/share/nvim/mason/bin/sql-formatter",
		"--config",
		"/Users/tatoaoliang/.config/nvim/lua/plugin-config/sql_formatter_config.json"
	}
    -- The command to run
    -- local command = "cat"

    -- Start the job
    local status, job_id_or_err = pcall(vim.fn.jobstart, command, opts)

    if status then
        print("Job started successfully with ID:", job_id_or_err)
    else
        print("Failed to start job:", job_id_or_err)
    end

	local jid = job_id_or_err
	vim.api.nvim_chan_send(jid, "select shit from sdfsd.table")
	print(jid)
	print('eeeeee')
    vim.fn.chanclose(jid, "stdin")

	-- vim.fn.jobstop(jid)


end

-- Execute the function
start_job()


```
vim.api.nvim_chan_send(jid, "string")
vim.fn.chanclose(jid, "stdin")
vim.fn.jobstop(jid)




## buff 

vim.api.nvim_create_namespace('MaskNamespace' .. i)
vim.api.nvim_buf_clear_namespace(0, mask_ns_id_list[index], 0, -1)
vim.api.nvim_buf_add_highlight(0, mask_ns_id_list[index], highlight_group, start_line - 1, start_col - 1, end_col)

vim.schedule(function () xxxx)

local current_win = vim.api.nvim_get_current_win()
local current_pos = vim.api.nvim_win_get_cursor(current_win)
local start_line, start_col = unpack(vim.fn.getpos("'<"), 2, 3)
local end_line, end_col = unpack(vim.fn.getpos("'>"), 2, 3)
local lines = vim.fn.getline(start_line, end_line)

local attached = vim.api.nvim_buf_attach(buf, false, {
    on_lines = on_lines
})

