import sublime
import sublime_plugin


class HighlightPythonBreakpoints(sublime_plugin.EventListener):
    """ An event listener that finds and highlights Python breakpoints """
    def on_modified(self, view):
        """ EventListener event, fires when the buffer the modified """

        # Erase all existing breakpoint regions
        view.erase_regions("breakpoints")

        # Regex to find breakpoints
        regex = r"^([\t\ ]+(import pdb;|pdb\.set_trace()).*)"

        # Find all regions to highlight using regex
        regions = view.find_all(regex)

        # Colouring to use on the highlight block
        scope = "invalid.illegal.unclosed-string.python"

        # Highlight flags, set to be solid and underlined
        flags = sublime.DRAW_SOLID_UNDERLINE

        # Add regions to the view
        view.add_regions("breakpoints", regions, scope, "dot", flags)
