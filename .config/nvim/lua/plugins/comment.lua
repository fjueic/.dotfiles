return {
	"numToStr/Comment.nvim",
	dependencies = { "JoosepAlviste/nvim-ts-context-commentstring" },
	lazy = true,
	event = "VeryLazy",

	config = function()
		vim.api.nvim_command("autocmd BufEnter *.conf silent set commentstring=#%s")
		require("Comment").setup({
			pre_hook = require("ts_context_commentstring.integrations.comment_nvim").create_pre_hook(),
			sticky = true,
			padding = true,
			toggler = {
				line = "<M-/>",
			},
			opleader = {
				line = "<M-/>",
			},
			mappings = {
				basic = true,
				extra = true,
			},
		})
	end,
}
