local markdown_preview_debounce_time = 1000
local markdown_preview_debounce = nil
local markdown_preview = 0
local line_number = 0

function _G.toggle_markdown_preview()
	if markdown_preview == 1 then
		markdown_preview = 0
		print("Markdown preview disabled")
		vim.api.nvim_command("autocmd! markdown_preview")
	else
		markdown_preview = 1
		vim.api.nvim_command(
			"autocmd markdown_preview CursorMoved,CursorMovedI *.md silent lua scroll_to_markdown_to_view()"
		)
		vim.api.nvim_command(
			"autocmd markdown_preview TextChanged,TextChangedI *.md silent lua debounce(send_buffer_to_markdown_preview, "
				.. markdown_preview_debounce_time
				.. ")"
		)
		vim.api.nvim_command(
			"autocmd markdown_preview BufEnter *.md silent lua send_buffer_to_markdown_preview();scroll_to_markdown_to_view() "
		)
		print("Markdown preview enabled")
	end
end

function _G.send_buffer_to_markdown_preview()
	if markdown_preview == 0 then
		return
	end
	local text = vim.api.nvim_buf_get_lines(0, 0, -1, false)
	text = table.concat(text, "\n")
	local curl = require("plenary.curl")
	local url = "http://localhost:9876/markdown_update"
	local data = {
		text = text,
	}
	local headers = {
		["Content-Type"] = "application/json",
	}
	if
		pcall(function()
			curl.post(url, {
				headers = headers,
				body = vim.fn.json_encode(data),
				timeout = 1000,
			})
		end)
	then
		return
	else
		print("Failed to send buffer to markdown preview")
	end
end

function _G.debounce(func, time)
	if markdown_preview_debounce then
		vim.loop.timer_stop(markdown_preview_debounce)
		markdown_preview_debounce:close()
		markdown_preview_debounce = nil
	end
	markdown_preview_debounce = vim.loop.new_timer()
	vim.loop.timer_start(markdown_preview_debounce, time, 0, vim.schedule_wrap(func))
end

function _G.scroll_to_markdown_to_view()
	if markdown_preview == 0 or vim.fn.line(".") == line_number then
		return
	end
	line_number = vim.fn.line(".")
	local text = vim.api.nvim_buf_get_lines(0, 0, -1, false)
	text = table.concat(text, "\n")
	local curl = require("plenary.curl")
	local url = "http://localhost:9876/line_number_update"
	local data = {
		line_number = line_number,
	}

	local headers = {
		["Content-Type"] = "application/json",
	}

	if
		pcall(function()
			curl.post(url, {
				headers = headers,
				body = vim.fn.json_encode(data),
				timeout = 1000,
			})
		end)
	then
		return
	else
		print("Failed to send buffer to markdown preview")
	end
end

vim.keymap.set("n", "<leader>=", "<cmd>lua toggle_markdown_preview()<CR>")
vim.api.nvim_command("augroup markdown_preview")
