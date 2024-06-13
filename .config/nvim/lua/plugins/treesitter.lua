return {
	-- Highlight, edit, and navigate code
	"nvim-treesitter/nvim-treesitter",
	lazy = true,
	-- event = { "BufReadPre", "BufNewFile" },
	event = "VeryLazy",
	build = ":TSUpdate",
	dependencies = {
		{
			"windwp/nvim-ts-autotag",
			event = { "BufReadPre", "BufNewFile" },
		},
	},
	config = function()
		vim.filetype.add({
			pattern = { [".*/hypr/.*%.conf"] = "hyprlang" },
		})
		require("nvim-treesitter.configs").setup({
			-- Add languages to be installed here that you want installed for treesitter
			ensure_installed = {
				"c",
				"cpp",
				"go",
				"lua",
				"python",
				"bash",
				"html",
				"hyprlang",
				"css",
				"javascript",
				"typescript",
				"tsx",
				"json",
				"vim",
				"vimdoc",
				"yaml",
				"markdown",
				"markdown_inline",
				"gitignore",
			},

			-- Autoinstall languages that are not installed. Defaults to false (but you can change for yourself!)
			sync_install = false,
			auto_install = true,
			autopairs = { enable = true },
			rainbow = { enable = true },
			autotag = { enable = true },
			indent = { enable = true },
			highlight = {
				enable = true,
				additional_vim_regex_highlighting = false,
			},
			incremental_selection = {
				enable = true,
				keymaps = {
					init_selection = "<c-space>",
					node_incremental = "<c-space>",
					scope_incremental = "<c-s>",
					node_decremental = "<M-space>",
				},
			},
		})
	end,
}
