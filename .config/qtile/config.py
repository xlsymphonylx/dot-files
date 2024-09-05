from libqtile import bar, layout, qtile
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration, RectDecoration
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal, send_notification
from libqtile import hook
from spotify import Spotify
import subprocess
import os

# here it will be, my empire, my custom functions


@hook.subscribe.startup_once
def autostart():
    subprocess.Popen([os.path.expanduser("~/.config/qtile/bash-scripts/autostart.sh")])


# polybar height variable
polybar_height = 35
mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # custom keybinds for qlite
    Key([mod], "q", lazy.spawn("kitty"), desc="Launch kitty"),
    Key([mod], "d", lazy.spawn("rofi -show drun"), desc="Launch rofi"),
    Key([mod], "e", lazy.spawn("thunar")),
    Key(
        [mod, "shift"],
        "q",
        lazy.spawn("firefox"),
        desc="Launch firefox",
    ),
    # Launch Flameshot GUI for screenshots
    Key([mod], "g", lazy.spawn("flameshot gui")),
    # Toggle between different layouts as defined below
    Key([mod], "tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [
    Group("1", label="  Web"),  # Browser/Globe icon for Web
    Group("2", label=" Programming"),  # Code icon for Programming
    Group("3", label="  Bash"),  # Terminal icon for Bash
    Group("4", label="  Work"),  # Rocket icon for Work
    Group("5", label="  Media"),  # Music note icon for Media
    Group("6", label="  Steam"),  # Steam icon for Steam
    Group("7", label="  Files"),  # Folder icon for Files
    Group("8", label="  Chats"),  # Chat icon for Chats
    Group("9", label="  Extra"),  # Miscellaneous icon for Extra
]
for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Spiral(
        border_normal="#01012b",
        border_focus="#05d9e8",
        border_width=4,
        margin=12,  # [Top, Right, Bottom, Left],
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Mononoki Nerd Font",
    fontsize=17,
    padding=1,
)
extension_defaults = widget_defaults.copy()


right_direction_powerline = {
    "decorations": [
        PowerLineDecoration(path="forward_slash", padding_y=0),
    ]
}

left_direction_powerline = {
    "decorations": [
        PowerLineDecoration(path="forward_slash", padding_y=0),
    ]
}

screens = [
    Screen(
        bottom=bar.Bar(
            # Dark Greenish-Blue for
            [
                widget.GroupBox(
                    font="Mononoki Nerd Font",
                    highlight_method="line",
                    fmt="<span weight='bold'>{}</span>",
                    padding=8,
                    margin=5,
                    rounded=True,  # Rounded border
                    disable_drag=True,
                    center_aligned=True,
                    markup=True,
                    fontsize=16,
                    highlight_color="#000",
                    background="#000",
                    this_current_screen_border="#28EAD0",
                    active="#28EAD0",  # Active group text color
                    inactive="#FFF",  # Inactive group text color
                    **right_direction_powerline,
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#05d9e8", "#d1f7ff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Spacer(
                    length=bar.STRETCH,
                    **left_direction_powerline,
                ),
                widget.TextBox(
                    "  Symphony ",
                    foreground="#000",
                    background="#28EAD0",
                    **left_direction_powerline,
                ),
                widget.StatusNotifier(
                    background="#000",
                    padding=5,
                    margin=5,
                    icon_size=21,
                    **left_direction_powerline,
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                # widget.Systray(),
                widget.Clock(
                    background="#28EAD0",
                    foreground="#000",
                    **left_direction_powerline,
                    format="  %I:%M %p  ",
                ),
                widget.QuickExit(
                    default_text="Shutdown",  # Custom text with a power icon
                    countdown_format="[{} Secs]",  # Format for countdown text
                    timer_interval=1,  # Countdown interval in seconds
                    exit_command="poweroff",  # Command to execute on click
                    fontsize=18,  # Font size
                    foreground="#28ead0",  # text color (white)
                    background="#000",  # background color (red)
                    font="Mononoki Nerd Font",
                ),
            ],
            27,  # height of bar
            background="#00000000",
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        top=bar.Bar(
            [
                widget.CPU(
                    background="#000",
                    foreground="#28EAD0",
                    format="   CPU {load_percent}%",
                    **right_direction_powerline,
                ),
                widget.Memory(
                    background="#28EAD0",
                    foreground="#000",
                    format=" 󰘚 RAM {MemPercent}%",
                    **right_direction_powerline,
                ),
                widget.Net(
                    background="#000",
                    foreground="#28EAD0",
                    format=" 󰌘 NET {down:.0f}{down_suffix}  {up:.0f}{up_suffix}  ",
                    **right_direction_powerline,
                ),
                widget.Spacer(length=bar.STRETCH),
                widget.WindowName(
                    background="#00000000",
                    foreground="#FFF",
                    padding=10,
                    **right_direction_powerline,
                ),
                widget.Spacer(
                    length=bar.STRETCH,
                    **left_direction_powerline,
                ),
                widget.Clock(
                    foreground="#28ead0",  # text color (white)
                    background="#000",  # background color (red)
                    **left_direction_powerline,
                    format="  %d/%m/%y ",
                ),
                widget.PulseVolume(
                    background="#28EAD0",
                    foreground="#000",
                    mute_command="pactl set-sink-mute @DEFAULT_SINK@ toggle",
                    unmute_format="   {volume}% ",
                    mute_format="  Muted ",
                    volume_app="pavucontrol",
                    get_volume_command="pactl get-sink-volume @DEFAULT_SINK@ | grep -oP '\\d{1,3}%' | head -1",
                    **left_direction_powerline,
                ),
                Spotify(
                    foreground="#28ead0",  # text color (white)
                    background="#000",  # background color (red)
                    **left_direction_powerline,
                ),
            ],
            27,  # height of bar
            background="#00000000",
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_width=4,
    border_focus="#05d9e8",
    border_normal="#01012b",
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="polybar-main-bar_DP-2"),
        Match(title="Save"),
        Match(title="Sign in to Steam"),
    ],
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
