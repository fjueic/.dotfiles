function cmp()
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
				vim.snippet.expand(args.body)
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
			{ name = "buffer" }, -- text within current buffer
			{ name = "path" }, -- file system paths
		}, {
			name = "buffer",
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
end

function lsp()
	local lsps = {
		"bashls", -- Bash
		"clangd", -- C/C++
		"pyright", -- Python
		"lua_ls", -- Lua
		"html", -- HTML
		"htmx", -- HTMX
		"emmet_language_server", -- HTML
		"cssls", -- CSS
		"tailwindcss", -- Tailwind CSS
		"ts_ls", -- Javascript, TypeScript
		"eslint", -- React/NextJS/Svelte
		"marksman", -- Markdown lsp
		"sqlls", -- SQL
		"svelte", -- Svelte
		"denols",
		"angularls", -- angularls
		"pylsp",
	}

	require("mason").setup()

	require("mason-lspconfig").setup({
		-- list of servers for mason to install
		ensure_installed = lsps, -- auto-install configured servers (with lspconfig)
		automatic_installation = true, -- not the same as ensure_installed
	})
	local lspconfig = require("lspconfig")
	local map = vim.keymap.set
	function on_attach(client, bufnr)
		local function opts(desc)
			return { buffer = bufnr, desc = desc }
		end
		map("n", "gD", vim.lsp.buf.declaration, opts("Lsp Go to declaration"))
		map("n", "gd", vim.lsp.buf.definition, opts("Lsp Go to definition"))
		map("n", "K", vim.lsp.buf.hover, opts("Lsp hover information"))
		map("n", "gi", vim.lsp.buf.implementation, opts("Lsp Go to implementation"))
		map("n", "<leader>sh", vim.lsp.buf.signature_help, opts("Lsp Show signature help"))
		map("n", "<leader>wa", vim.lsp.buf.add_workspace_folder, opts("Lsp Add workspace folder"))
		map("n", "<leader>wr", vim.lsp.buf.remove_workspace_folder, opts("Lsp Remove workspace folder"))

		map("n", "<leader>wl", function()
			print(vim.inspect(vim.lsp.buf.list_workspace_folders()))
		end, opts("Lsp List workspace folders"))

		map("n", "<leader>D", vim.lsp.buf.type_definition, opts("Lsp Go to type definition"))

		map("n", "<leader>rn", vim.lsp.buf.rename, opts("Lsp Rename"))

		map({ "n", "v" }, "<leader>ca", vim.lsp.buf.code_action, opts("Lsp Code action"))
		map("n", "gr", vim.lsp.buf.references, opts("Lsp Show references"))
	end

	function on_init(client, _) end

	local capabilities = vim.lsp.protocol.make_client_capabilities()
	capabilities.textDocument.completion.completionItem = {
		documentationFormat = { "markdown", "plaintext" },
		snippetSupport = true,
		preselectSupport = true,
		insertReplaceSupport = true,
		labelDetailsSupport = true,
		deprecatedSupport = true,
		commitCharactersSupport = true,
		tagSupport = { valueSet = { 1 } },
		resolveSupport = {
			properties = {
				"documentation",
				"detail",
				"additionalTextEdits",
			},
		},
	}

	for _, lsp in ipairs(lsps) do
		lspconfig[lsp].setup({
			on_attach = on_attach,
			on_init = on_init,
			capabilities = capabilities,
			flags = {
				debounce_text_changes = 150,
			},
		})
	end
	----------------linting code--------------------
	---
	vim.diagnostic.config({
		virtual_text = true,
		signs = true, -- Show E/W in the sign column
		underline = true, -- Underline errors/warnings
		update_in_insert = false, -- Avoid diagnostics updating while typing
		float = {
			border = "rounded", -- Use a rounded border for floating diagnostics
			source = "always", -- Show the source of the diagnostics (e.g., ESLint, Pyright)
		},
	})

	vim.o.updatetime = 300 -- Speed up diagnostics display

	-- Keymap to show floating diagnostics (e.g., press <leader>d)
	vim.keymap.set("n", "<leader>d", function()
		vim.diagnostic.open_float(nil, { focusable = true })
	end, { desc = "Show diagnostics in floating window" })
	-------------------------------------------------------
end

return {

	"neovim/nvim-lspconfig",
	dependencies = {
		"williamboman/mason.nvim",
		"williamboman/mason-lspconfig.nvim",
		"hrsh7th/cmp-nvim-lsp",
		"hrsh7th/cmp-buffer",
		"hrsh7th/cmp-path",
		"hrsh7th/cmp-cmdline",
		"hrsh7th/nvim-cmp",
		"L3MON4D3/LuaSnip",
		"saadparwaiz1/cmp_luasnip",
		"j-hui/fidget.nvim",
		"rafamadriz/friendly-snippets",
		"onsails/lspkind.nvim",
	},

	config = function()
		cmp()
		lsp()
	end,
}
