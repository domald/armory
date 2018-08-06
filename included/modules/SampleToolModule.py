#!/usr/bin/python

from included.ModuleTemplate import ToolTemplate

class Module(ToolTemplate):
    
    name = "SampleToolModule"
    binary_name = "sample-tool"
    
    def set_options(self):
        super(Module, self).set_options()

        self.options.add_argument('-p', '--print_message', help="Message to print")
        # Change the default timeout
        self.options.set_defaults(timeout="15")
    
    def get_targets(self, args):
        '''
        This module is used to build out a target list containing dictionaries that will get plugged into
        the commands that are executed.
        '''

        return []

    def build_cmd(self, args):
        '''
        Create the actual command that will be executed. Use {target}, {output}, etc as placeholders. These
        should match up to the dictionaries returned by get_targets()
        '''
        
        return ''

    def process_output(self, cmds):
        '''
        Process the output generated by the earlier commands.
        '''
