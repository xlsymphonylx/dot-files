-- Read the docs: https://www.lunarvim.org/docs/configuration
-- Example configs: https://github.com/LunarVim/starter.lvim
-- Video Tutorials: https://www.youtube.com/watch?v=sFA9kX-Ud_c&list=PLhoH5vyxr6QqGu0i7tt_XoVK9v-KvZ3m6
-- Forum: https://www.reddit.com/r/lunarvim/
-- Discord: https://discord.com/invite/Xb9B4Ny:
--
lvim.builtin.which_key.setup.plugins.presets.z = true
lvim.format_on_save.enabled = true
local lspconfig = require('lspconfig')
local formatters = require "lvim.lsp.null-ls.formatters"
local linters = require "lvim.lsp.null-ls.linters"
formatters.setup {
  {
    name = "prettier",
    ---@usage arguments to pass to the formatter
    -- these cannot contain whitespace
    -- options such as `--line-width 80` become either `{"--line-width", "80"}` or `{"--line-width=80"}`
    args = { "--print-width", "100" },
  },
}


-- ESLint
linters.setup {
  { name = "eslint_d" },
}

lspconfig.vuels.setup({
  filetypes = { 'vue' }, -- Ensure Vetur handles Vue files

})

lspconfig.volar.setup({
  filetypes = { 'typescript', 'javascript', 'javascriptreact', 'typescriptreact' }, -- Exclude 'vue'
})
