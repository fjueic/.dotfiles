return {
	"stevearc/conform.nvim",
	config = function()
		local conform = require("conform")
		conform.setup({
			formatters_by_ft = {
				c = { "clang_format" },
				cpp = { "clang_format" },
				javascript = { "biome" },
				typescript = { "biome" },
				javascriptreact = { "prettierd", "prettier" },
				typescriptreact = { "prettierd", "prettier" },
				css = { "prettierd", "prettier" },
				html = { "prettierd", "prettier" },
				json = { "biome" },
				jsonc = { "prettierd", "prettier" },
				yaml = { "prettierd", "prettier" },
				markdown = { "prettierd", "prettier" },
				graphql = { "prettierd", "prettier" },
				lua = { "stylua" },
				python = { "isort", "black" },
				["_"] = { "trim_whitespace", "trim_newlines" },
				["*"] = { "codespell" },
			},
			formatters = {
				clang_format = {
					command= "clang-format",
					-- args = { "-style=llvm" },
				},
			},
		})

		vim.keymap.set({ "n", "v" }, "=", function()
			conform.format({
				lsp_fallback = true,
				async = false,
			})
		end, {
			desc = "Format file or visual selected",
		})
	end,
}
