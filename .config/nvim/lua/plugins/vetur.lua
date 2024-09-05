-- plugins/vetur.lua

return {
  {
    "neovim/nvim-lspconfig",
    config = function()
      local lspconfig = require("lspconfig")

      -- Configure Vetur (vuels) for Vue 2 support
      lspconfig.vuels.setup({
        settings = {
          vetur = {
            completion = {
              autoImport = true,
              tagCasing = "kebab",
              useScaffoldSnippets = true,
            },
            format = {
              enable = true,
              defaultFormatter = {
                js = "prettier",
                ts = "prettier",
              },
              scriptInitialIndent = false,
              styleInitialIndent = false,
            },
            validation = {
              script = true,
              style = true,
              template = true,
            },
          },
        },
      })
    end,
  },
}
