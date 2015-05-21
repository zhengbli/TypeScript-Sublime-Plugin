import sublime
import sublime_plugin
import plistlib

from ..libs.global_vars import *
from ..libs.view_helpers import active_view
from ..libs import log


class TypescriptAdaptColorThemeCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        theme_name = active_view().settings().get("color_scheme")
        if "(TypeScript Adapted)" not in theme_name:
            self.adapt_color_theme()

    @staticmethod
    def adapt_color_theme():
        theme_name = sublime.active_window().active_view().settings().get('color_scheme')
        cs = plistlib.readPlistFromBytes(sublime.load_binary_resource(theme_name))
        background_color = "#000000"
        cs["name"] += " (TypeScript Adapted)"
        for rule in cs["settings"]:
            # Found the first node, defining the overall background color
            if "scope" not in rule and "name" not in rule:
                background_color = rule["settings"]["background"]
                r = int(background_color[1:3], 16)
                g = int(background_color[3:5], 16)
                b = int(background_color[5:7], 16)
                if r == 0 and g == 0 and b == 0:
                    rule["settings"]["background"] = "#000001"
                else:
                    if b > 0:
                        b -= 1
                    elif g > 0:
                        g -= 1
                    elif r > 0:
                        r -= 1
                    rule["settings"]["background"] = "#%02x%02x%02x" % (r, g, b)
            else:
                rule["settings"]["background"] = background_color

        new_name = cs["name"] + ".tmTheme"
        path = "%s/%s" % (PLUGIN_DIR, new_name)
        print(path)
        plistlib.writePlist(cs, path)
        sublime.load_settings("Preferences.sublime-settings").set("color_scheme",
                                                                  "Packages/TypeScriptLang/%s" % (new_name))
        sublime.save_settings("Preferences.sublime-settings")
