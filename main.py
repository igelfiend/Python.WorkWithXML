# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ETree

def getRoot( path ):
    xml1 = ETree.parse( path )
    return xml1.getroot()

def printNode( node, level=None ):
    # Recursive printing XML nodes with indent
    if level == None:
        level = 0

    tab = "    " * level
    print( tab, "tag:     ", node.tag )
    print( tab, "attribs: ", ",".join( list( node.attrib.keys() ) ) )
    print( tab, "text:    ", node.text )

    level += 1

    if len( node ) == 0:
        print()

    for subnode in node:
        printNode( subnode, level )

def getTagData( node, tagname ):
    # Receive recursive data from node and it's child with tag named "tagname"
    result = []
    if node.tag == tagname:
        result.append( node.text )

    for subnode in node:
        result += getTagData( subnode, tagname )

    return result

def main():
    root = getRoot( "data.xml" )
    #printNode( root )
    print( getTagData( root, "pc_item" ) )

if __name__ == "__main__":
    main()