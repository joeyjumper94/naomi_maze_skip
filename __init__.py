import sys

import renpy
import renpy.sl2.slast as slast
import renpy.parser as parser
import renpy.ast as ast

from modloader import modinfo, modast
from modloader.modgame import sprnt
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod

def connect(node,next):
    """
    Args:
        node (Node): The node to connect from
        next (Node): The node to connect to after node
    """
    hook=modast.hook_opcode(node,None)
    hook.chain(next)
    #thanks 4onen for explaining this
    """
    node_i_want_to_hook=modast.find_say("Ooh, I do hope what I'm saying now is unique across all time, or I might link the wrong spot!")
    my_hook=modast.hook_opcode(node_i_want_to_hook,None) # makes my_hook the next node, but preserves the old next as an old_next on the my_hook object, as well as making my_hook.next equal to the old next.
    my_hook.chain(modast.find_label('my_unique_mod_label')) # replaces my_hook.next, but leaves my_hook.old_next intact
    """
@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("Naomi Maze Skip", "v0.1", "joeyjumper94")

    def mod_load(self):
        if not "A Solitary Mind" in modinfo.get_mods():
            raise Exception("A Solitary Mind not found.\nThis mod is required by %s\nthe workship id for A Solitary Mind is 1597292073." % " ".join(self.mod_info()))
        else:
            eck_naomi_m3_biolab=modast.find_label("eck_naomi_m3_biolab")
            filename=eck_naomi_m3_biolab.filename
            joeyjumper_naomi_maze_reset=modast.find_label("joeyjumper_naomi_maze_reset")
            for node in renpy.game.script.all_stmts:
                if filename==node.filename and isinstance(node,ast.Say):
                    if node.what=="I put my rebreather back on and went to the cave entrance at the seafloor.":
                        connect(modast.find_label("joeyjumper_naomi_maze_skip_no"),node.next)
                        connect(node,modast.find_label("joeyjumper_naomi_maze_skip_choice"))
                        #joeyjumper_naomi_maze_skip_yes is handled in the rpy by jumping to eck_naomi_m3_biolab
                    if node.what=="It was a mostly intact scientific facility.":
                        modast.call_hook(node,joeyjumper_naomi_maze_reset)
                    if node.what=="Soon, we were back on the beach. I quickly changed back to my daily clothes, happy to take off the skin-tight wetsuit.":
                        modast.call_hook(node,joeyjumper_naomi_maze_reset)

    def mod_complete(self):
        pass