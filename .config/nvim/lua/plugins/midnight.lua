return {
	"dasupradyumna/midnight.nvim",
	lazy = false,
	priority = 1000,
	config = function()
		require("midnight").setup({
			HighlightGroup = {
				fg = ForegroundColor, -- :h guifg
				bg = BackgroundColor, -- :h guibg
				sp = SpecialColor, -- :h guisp
				style = RenderStyle, -- :h attr-list
			},
		})
		-- Lua
		vim.cmd.colorscheme("midnight")
	end,
}
