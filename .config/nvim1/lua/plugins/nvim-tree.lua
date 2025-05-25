return {
	"nvim-tree/nvim-tree.lua",
	version = "*",
	lazy = false,
	dependencies = {
		"nvim-tree/nvim-web-devicons",
	},
	config = function()
		require("nvim-tree").setup({
			disable_netrw = false,
			hijack_netrw = false,
			update_focused_file = {
				enable = true,
				update_cwd = false,
				ignore_list = {},
			},
			git = {
				enable =true,
				ignore = false,
				timeout = 500,
			},
			renderer = {
				indent_markers = {
					enable = true,
				},
			},
			view = {
				width = 30,
				side = "right",
			},
		})
		vim.api.nvim_set_keymap("n", "<leader>e", ":NvimTreeToggle<CR>", { noremap = true, silent = true })
	end,
}
