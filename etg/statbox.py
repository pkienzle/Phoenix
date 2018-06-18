#---------------------------------------------------------------------------
# Name:        etg/statbox.py
# Author:      Robin Dunn
#
# Created:     29-Oct-2011
# Copyright:   (c) 2011-2018 by Total Control Software
# License:     wxWindows License
#---------------------------------------------------------------------------

import etgtools
import etgtools.tweaker_tools as tools

PACKAGE   = "wx"
MODULE    = "_core"
NAME      = "statbox"   # Base name of the file to generate to for this script
DOCSTRING = ""

# The classes and/or the basename of the Doxygen XML files to be processed by
# this script.
ITEMS  = [ "wxStaticBox",
           ]

#---------------------------------------------------------------------------

def run():
    # Parse the XML file(s) building a collection of Extractor objects
    module = etgtools.ModuleDef(PACKAGE, MODULE, NAME, DOCSTRING)
    etgtools.parseDoxyXML(module, ITEMS)

    #-----------------------------------------------------------------
    # Tweak the parsed meta objects in the module object as needed for
    # customizing the generated code and docstrings.

    c = module.find('wxStaticBox')
    assert isinstance(c, etgtools.ClassDef)
    c.find('wxStaticBox.label').default = 'wxEmptyString'
    c.find('Create.label').default = 'wxEmptyString'
    tools.fixWindowClass(c)

    # TODO: The window-label ctor is only available on MSW and GTK so disable
    # for now. Maybe replace it with a factory function that returns None on
    # OSX??
    c.find('wxStaticBox').findOverload('wxWindow *label').ignore()
    c.find('Create').findOverload('wxWindow *label').ignore()

    # "unfix" the 2nd ctor and Create method so the required parameter lists
    # are different enough for them to be overloaded.
    #for name in ['wxStaticBox', 'Create']:
    #    m = c.find(name).findOverload('wxWindow *label')
    #    m.find('id').default = ''




    module.addGlobalStr('wxStaticBoxNameStr', c)

    #-----------------------------------------------------------------
    tools.doCommonTweaks(module)
    tools.runGenerators(module)


#---------------------------------------------------------------------------
if __name__ == '__main__':
    run()

