-- [[ Configure nvim-cmp ]]
-- See `:help cmp`
return {
	-- Autocompletion
	"hrsh7th/nvim-cmp",
	lazy = true,
	-- event = { "BufReadPre", "BufNewFile", "VeryLazy" }, -- to disable, comment this out
	event = "InsertEnter",
	dependencies = {
		"L3MON4D3/LuaSnip", -- snippet engine
		"saadparwaiz1/cmp_luasnip", -- for autocompletion
		"onsails/lspkind.nvim", -- vs-code like pictograms
		"rafamadriz/friendly-snippets", -- useful snippets

		"hrsh7th/cmp-nvim-lsp", -- for autocompletion
		"hrsh7th/cmp-buffer", -- source for text in buffer
		"hrsh7th/cmp-path", -- source for file system paths
		"hrsh7th/cmp-cmdline", -- For cmdline suggestions
	},
	config = function()
		local cmp = require("cmp")
		local luasnip = require("luasnip")
		local lspkind = require("lspkind")

		-- loads vscode style snippets from installed plugins (e.g. friendly-snippets)
		require("luasnip.loaders.from_vscode").lazy_load()

		cmp.setup({
			enabled = true,
			completion = {
				completeopt = "menu,menuone,preview,noselect,noinsert",
			},
			-- preselect = cmp.PreselectMode.None,
			snippet = { -- configure how nvim-cmp interacts with snippet engine
				expand = function(args)
					luasnip.lsp_expand(args.body)
				end,
			},

			mapping = cmp.mapping.preset.insert({
				["<C-p>"] = cmp.mapping.select_prev_item(), -- previous suggestion
				["<C-n>"] = cmp.mapping.select_next_item(), -- next suggestion
				["<C-Space>"] = cmp.mapping.complete(), -- show completion suggestions
				["<C-e>"] = cmp.mapping.abort(), -- close completion window
				["<C-y>"] = cmp.mapping.confirm({ select = true }),
			}),
			-- sources for autocompletion
			sources = cmp.config.sources({
				{ name = "nvim_lsp" },
				{ name = "luasnip" }, -- snippets
				{ name = "codeium" },
				{ name = "buffer" }, -- text within current buffer
				{ name = "path" }, -- file system paths
			}),
			window = {
				documentation = cmp.config.window.bordered(),
				completion = cmp.config.window.bordered(),
				-- documentation = {
				--   border = { "╭", "─", "╮", "│", "╯", "─", "╰", "│" },
				--   winhighlight = "NormalFloat:NormalFloat,FloatBorder:FloatBorder",
				-- },
			},
			-- configure lspkind for vs-code like pictograms in completion menu
			formatting = {
				format = lspkind.cmp_format({
					mode = "symbol_text",
					maxwidth = 80,
					ellipsis_char = "...",
					symbol_map = { Codeium = "" },
				}),
			},
		})
		-- `/` cmdline setup.
		cmp.setup.cmdline({ "/", "?" }, {
			mapping = cmp.mapping.preset.cmdline(),
			sources = {
				{ name = "buffer" },
			},
		})
		-- `:` cmdline setup.
		cmp.setup.cmdline(":", {
			mapping = cmp.mapping.preset.cmdline(),
			sources = cmp.config.sources({
				{ name = "path" },
			}, {
				{
					name = "cmdline",
					option = {
						ignore_cmds = { "Man", "!" },
					},
				},
			}),
		})
	end,
}
