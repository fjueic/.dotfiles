return {
	"vimwiki/vimwiki",
	init = function()
		vim.g.vimwiki_list = {
			{
				path = "~/Obsidian/",
				syntax = "markdown",
				ext = ".md",
				vimwiki_global_ext = 0,
			},
		}
	end,
}
