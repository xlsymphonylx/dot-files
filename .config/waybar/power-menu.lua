#!/usr/bin/lua

local options = {
	["  Shut down"] = "systemctl poweroff",
	["  Reboot"] = "systemctl reboot",
	["  Hibernate"] = "systemctl hibernate",
}

local options_string = ""
local length = 0
for key, _ in pairs(options) do
	options_string = options_string .. key .. "\n"
	length = length + 1
end
options_string = options_string:sub(1, -2)

local f = assert(
	io.popen(
		"echo -e '"
			.. options_string
			.. "' | wofi --dmenu --insensitive --prompt 'Power menu' --height 175 --width 250 "
			------------------ to change the location of the dropdown, use --location 1 (top left) or --location 3 (top right) (see --location in wofi --help)
			.. length,
		"r"
	)
)
local s = assert(f:read("*a"))
s = string.gsub(s, "^%s+", "")
s = string.gsub(s, "%s+$", "")
s = string.gsub(s, "[\n]+", " ")
f:close()

os.execute(options[s])
