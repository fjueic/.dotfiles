vim.g.mapleader = " "
vim.keymap.set("n", "<leader>pv", vim.cmd.Ex) --explorer

vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv") -- move code blocks
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv")

vim.keymap.set("n", "J", "mzJ`z") -- join next line with a space without changing cursor position
vim.keymap.set("n", "<C-d>", "<C-d>zz") -- half page jump down
vim.keymap.set("n", "<C-u>", "<C-u>zz") -- up
vim.keymap.set("n", "n", "nzzzv") -- when searching keep the cursor in middle
vim.keymap.set("n", "N", "Nzzzv")

vim.keymap.set("x", "<leader>p", [["_dP]]) -- when pasting, current register stays same

vim.keymap.set({ "n", "v" }, "<leader>y", [["+y]]) -- paste to system clipboard
vim.keymap.set("n", "<leader>Y", [["+Y]]) -- copy line to system clipboard

vim.keymap.set({ "n", "v" }, "<leader>d", [["_d]]) -- delete to void

vim.keymap.set("n", "Q", "<nop>") -- do nothing(dunno why this was set)
vim.keymap.set("n", "<C-f>", "<cmd>silent !tmux neww tmux-sessionizer.sh<CR>")

vim.keymap.set("n", "<C-k>", "<cmd>cnext<CR>zz")
vim.keymap.set("n", "<C-j>", "<cmd>cprev<CR>zz")
vim.keymap.set("n", "<leader>k", "<cmd>lnext<CR>zz")
vim.keymap.set("n", "<leader>j", "<cmd>lprev<CR>zz")

vim.keymap.set("n", "<leader>s", [[:%s/\<<C-r><C-w>\>/<C-r><C-w>/gI<Left><Left><Left>]]) -- replace the word cursor was on

vim.keymap.set("n", "<leader><leader>", function() -- source
	vim.cmd("so")
end)
