#---------------------------------------------------------------------------
# Name:        etg/richtextbuffer.py
# Author:      Robin Dunn
#
# Created:     23-Mar-2013
# Copyright:   (c) 2013 by Total Control Software
# License:     wxWindows License
#---------------------------------------------------------------------------

import etgtools
import etgtools.tweaker_tools as tools

PACKAGE   = "wx"   
MODULE    = "_richtext"
NAME      = "richtextbuffer"   # Base name of the file to generate to for this script
DOCSTRING = ""

# The classes and/or the basename of the Doxygen XML files to be processed by
# this script. 
ITEMS  = [ "wxTextAttrDimension",
           "wxTextAttrDimensions",
           "wxTextAttrSize",
           "wxTextAttrDimensionConverter",
           "wxTextAttrBorder",
           "wxTextAttrBorders",
           "wxTextBoxAttr",
           "wxRichTextAttr",
           "wxRichTextProperties",
           "wxRichTextFontTable",
           "wxRichTextRange",
           "wxRichTextSelection",
           "wxRichTextDrawingContext",
           "wxRichTextObject",
           "wxRichTextCompositeObject",
           "wxRichTextParagraphLayoutBox",
           "wxRichTextBox",
           "wxRichTextField",
           "wxRichTextFieldType",
           "wxRichTextFieldTypeStandard",
           "wxRichTextLine",
           "wxRichTextParagraph",
           "wxRichTextPlainText",
           "wxRichTextImageBlock",
           "wxRichTextImage",
           "wxRichTextBuffer",
           "wxRichTextCell",
           "wxRichTextTable",
           "wxRichTextObjectAddress",
           "wxRichTextCommand",
           "wxRichTextAction",
           "wxRichTextFileHandler",
           "wxRichTextPlainTextHandler",
           "wxRichTextDrawingHandler",
           "wxRichTextBufferDataObject",
           "wxRichTextRenderer",
           "wxRichTextStdRenderer",
        
           ]    
    
#---------------------------------------------------------------------------

def run():
    # Parse the XML file(s) building a collection of Extractor objects
    module = etgtools.ModuleDef(PACKAGE, MODULE, NAME, DOCSTRING)
    etgtools.parseDoxyXML(module, ITEMS)
    
    #-----------------------------------------------------------------
    # Tweak the parsed meta objects in the module object as needed for
    # customizing the generated code and docstrings.
    
    module.addHeaderCode('#include <wx/richtext/richtextbuffer.h>')
    
    module.addItem(
        tools.wxArrayWrapperTemplate('wxRichTextRangeArray', 'wxRichTextRange', module))
    module.addItem(
        tools.wxArrayWrapperTemplate('wxRichTextAttrArray', 'wxRichTextAttr', module))
    module.addItem(
        tools.wxArrayWrapperTemplate('wxRichTextVariantArray', 'wxVariant', module))     
    module.addItem(
        tools.wxListWrapperTemplate('wxRichTextObjectList', 'wxRichTextObject', module))
    module.addItem(
        tools.wxListWrapperTemplate('wxRichTextLineList', 'wxRichTextLine', module))
    
    # Can this even work?
    module.addItem(
        tools.wxArrayWrapperTemplate('wxRichTextObjectPtrArray', 'wxRichTextObject', module))     
    module.addItem(
        tools.wxArrayWrapperTemplate('wxRichTextObjectPtrArrayArray', 'wxRichTextObjectPtrArray', module))     
    
        
    
    module.find('wxRICHTEXT_ALL').ignore()
    module.find('wxRICHTEXT_NONE').ignore()
    module.find('wxRICHTEXT_NO_SELECTION').ignore()
    module.addPyCode("""\
        RICHTEXT_ALL = RichTextRange(-2, -2)
        RICHTEXT_NONE = RichTextRange(-1, -1)
        RICHTEXT_NO_SELECTION = RichTextRange(-2, -2)
        """)
    
    module.insertItem(0, etgtools.WigCode("""\
        // forward declarations
        class wxRichTextStyleDefinition;
        class wxRichTextListStyleDefinition;
        class wxRichTextXMLHandler;
        class wxRichTextCtrl;
        class wxRichTextStyleSheet;
        class wxRichTextFloatCollector;
        """))
    
    
    #-------------------------------------------------------
    c = module.find('wxTextAttrDimension')
    assert isinstance(c, etgtools.ClassDef)
    c.find('SetValue').findOverload('units').ignore()
    
    #-------------------------------------------------------
    c = module.find('wxTextAttrDimensions')
    # There are const and non-const versions of each of these, get rid of one
    # of each pair.
    c.find('GetLeft').ignore()
    c.find('GetRight').ignore()
    c.find('GetTop').ignore()
    c.find('GetBottom').ignore()

    
    #-------------------------------------------------------
    c = module.find('wxTextAttrSize')
    c.find('GetWidth').ignore()
    c.find('GetHeight').ignore()
    c.find('SetWidth').findOverload('units').ignore()
    c.find('SetHeight').findOverload('units').ignore()
    
    #-------------------------------------------------------
    c = module.find('wxTextAttrBorder')
    c.find('GetWidth').ignore()


    #-------------------------------------------------------
    c = module.find('wxTextAttrBorders')
    c.find('GetLeft').ignore()
    c.find('GetRight').ignore()
    c.find('GetTop').ignore()
    c.find('GetBottom').ignore()


    #-------------------------------------------------------
    c = module.find('wxTextBoxAttr')
    c.find('GetMargins').ignore()
    c.find('GetLeftMargin').ignore()
    c.find('GetRightMargin').ignore()
    c.find('GetTopMargin').ignore()
    c.find('GetBottomMargin').ignore()
    
    c.find('GetPosition').ignore()
    
    c.find('GetLeft').ignore()
    c.find('GetRight').ignore()
    c.find('GetTop').ignore()
    c.find('GetBottom').ignore()

    c.find('GetPadding').ignore()
    c.find('GetLeftPadding').ignore()
    c.find('GetRightPadding').ignore()
    c.find('GetTopPadding').ignore()
    c.find('GetBottomPadding').ignore()
    
    c.find('GetBorder').ignore()
    c.find('GetLeftBorder').ignore()
    c.find('GetRightBorder').ignore()
    c.find('GetTopBorder').ignore()
    c.find('GetBottomBorder').ignore()

    c.find('GetOutline').ignore()
    c.find('GetLeftOutline').ignore()
    c.find('GetRightOutline').ignore()
    c.find('GetTopOutline').ignore()
    c.find('GetBottomOutline').ignore()

    c.find('GetSize').ignore()
    c.find('GetMinSize').ignore()
    c.find('GetMaxSize').ignore()
    c.find('GetWidth').ignore()
    c.find('GetHeight').ignore()


    #-------------------------------------------------------
    c = module.find('wxRichTextAttr')
    c.find('GetTextBoxAttr').ignore()
    

    #-------------------------------------------------------
    c = module.find('wxRichTextProperties')
    c.find('operator[]').ignore()
    c.find('GetProperties').ignore()

    c.find('SetProperty').findOverload('bool').ignore()
    
    
    #-------------------------------------------------------
    c = module.find('wxRichTextSelection')
    c.find('GetRanges').ignore()


    #-------------------------------------------------------
    c = module.find('wxRichTextObject')
    #c.find('ImportFromXML').ignore()
    c.find('GetRange').ignore()
    c.find('GetOwnRange').ignore()
    c.find('GetAttributes').ignore()
    c.find('GetProperties').ignore()


    #-------------------------------------------------------
    c = module.find('wxRichTextCompositeObject')
    c.find('GetChildren').ignore()


    #-------------------------------------------------------
    c = module.find('wxRichTextLine')
    c.find('GetRange').ignore()


    #-------------------------------------------------------
    c = module.find('wxRichTextParagraph')
    
    # These methods use an untyped wxList, but since we know what is in it
    # we'll make a fake typed list for wxPython so we can know what kinds of
    # values to get from it.
    module.addItem(
        tools.wxListWrapperTemplate('wxList', 'wxRichTextObject', module, 
                                    fakeListClassName='wxRichTextObjectList_'))
    c.find('MoveToList.list').type = 'wxRichTextObjectList_&'
    c.find('MoveFromList.list').type = 'wxRichTextObjectList_&'
    
    
    #-------------------------------------------------------
    c = module.find('wxRichTextBuffer')
    c.find('GetFontTable').ignore()

    # More untyped wxLists
    module.addItem(
        tools.wxListWrapperTemplate('wxList', 'wxRichTextFileHandler', module, 
                                    fakeListClassName='wxRichTextFileHandlerList'))
    c.find('GetHandlers').type = 'wxRichTextFileHandlerList&'
    c.find('GetHandlers').noCopy = True
    
    module.addItem(
        tools.wxListWrapperTemplate('wxList', 'wxRichTextDrawingHandler', module, 
                                    fakeListClassName='wxRichTextDrawingHandlerList'))
    c.find('GetDrawingHandlers').type = 'wxRichTextDrawingHandlerList&'
    c.find('GetDrawingHandlers').noCopy = True

    # TODO: Need a template to wrap STRING_HASH_MAP
    c.find('GetFieldTypes').ignore()
    

    #-------------------------------------------------------
    c = module.find('wxRichTextTable')
    c.find('GetCells').ignore()
    
    
    #-------------------------------------------------------
    c = module.find('wxRichTextObjectAddress')
    c.find('GetAddress').ignore()


    #-------------------------------------------------------
    c = module.find('wxRichTextCommand')
    
    module.addItem(
        tools.wxListWrapperTemplate('wxList', 'wxRichTextAction', module, 
                                    fakeListClassName='wxRichTextActionList'))
    c.find('GetActions').type = 'wxRichTextActionList&'
    c.find('GetActions').noCopy = True
       
    
    #-------------------------------------------------------
    c = module.find('wxRichTextAction')
    c.find('GetContainerAddress').ignore()

    
    #-------------------------------------------------------
    c = module.find('wxRichTextFileHandler')
    c.find('DoLoadFile').ignore(False)
    c.find('DoSaveFile').ignore(False)
    
    c = module.find('wxRichTextPlainTextHandler')
    c.find('DoLoadFile').ignore(False)
    c.find('DoSaveFile').ignore(False)

    
    #-------------------------------------------------------
    #-------------------------------------------------------
    #-------------------------------------------------------
    #-------------------------------------------------------


    
    
    #-------------------------------------------------------
    # Ignore all Dump() methods since we don't wrap wxTextOutputStream.
    
    # TODO: try swithcing the parameter type to wxOutputStream and then in
    # the wrapper code create a wxTextOutputStream from that to pass on to
    # Dump.
    
    for m in module.findAll('Dump'):
        if m.findItem('stream'):
            m.ignore()
    

    
    #-----------------------------------------------------------------
    tools.doCommonTweaks(module)
    tools.runGenerators(module)
    
    
#---------------------------------------------------------------------------
if __name__ == '__main__':
    run()
