return {
	"williamboman/mason-lspconfig.nvim",
	config = function()
		local mason_lspconfig = require("mason-lspconfig")
		local lsps = {
			"bashls", -- Bash
			"clangd", -- C/C++
			"gopls", -- Golang
			"pyright", -- Python
			"lua_ls", -- Lua
			"html", -- HTML
			"htmx", -- HTMX
			"emmet_language_server", -- HTML
			"cssls", -- CSS
			"tailwindcss", -- Tailwind CSS
			"tsserver", -- Javascript, TypeScript
			"eslint", -- React/NextJS/Svelte
			-- "biome", -- Json, and JS
			"marksman", -- Markdown lsp
			"sqlls", -- SQL
		}
		mason_lspconfig.setup({
			-- list of servers for mason to install
			ensure_installed = lsps, -- auto-install configured servers (with lspconfig)
			automatic_installation = true, -- not the same as ensure_installed
		})
	end,
}
