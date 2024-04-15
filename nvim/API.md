

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

