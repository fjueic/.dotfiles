return {
    "neovim/nvim-lspconfig",
    config = function()
        local lsps = {
            "bashls",       -- Bash
            "clangd",       -- C/C++
            "pyright",      -- Python
            "lua_ls",       -- Lua
            "html",         -- HTML
            "htmx",         -- HTMX
            "emmet_language_server", -- HTML
            "cssls",        -- CSS
            "tailwindcss",  -- Tailwind CSS
            "tsserver",     -- Javascript, TypeScript
            "eslint",       -- React/NextJS/Svelte
            "marksman",     -- Markdown lsp
            "sqlls",        -- SQL
        }
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
    end,
}
