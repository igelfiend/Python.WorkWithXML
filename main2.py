# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ETree

def init():
    data = ETree.Element( "data" )
    ETree.SubElement( data, "name" ).text =  "Petya"
    ETree.SubElement( data, "age"  ).text = "23"
    ETree.SubElement( data, "sex"  ).text = "true"
    item_langs = ETree.SubElement( data, "languages" )
    item_pc    = ETree.SubElement( data, "pc" )

    item_lang1 = ETree.SubElement( item_langs, "language" )
    item_lang1.set( "name", "Python" )
    item_lang1.text = "9"

    item_lang2 = ETree.SubElement( item_langs, "language" )
    item_lang2.set( "name", "Java" )
    item_lang2.text = "7"

    item_lang3 = ETree.SubElement( item_langs, "language" )
    item_lang3.set( "name", "C#" )
    item_lang3.text = "8"

    item_pc1 = ETree.SubElement( item_pc, "pc_item" )
    item_pc1.set( "name", "os" )
    item_pc1.text = "Linux"

    item_pc2 = ETree.SubElement( item_pc, "pc_item" )
    item_pc2.set( "name", "proc" )
    item_pc2.text = "Intel Core i7-8700"

    item_pc3 = ETree.SubElement( item_pc, "pc_item" )
    item_pc3.set( "name", "ram" )
    item_pc3.text = "64"

    item_pc4 = ETree.SubElement( item_pc, "pc_item" )
    item_pc4.set( "name", "hard" )
    item_pc4.text = "5000"

    return data

def serialize( obj ):
    ser = ETree.tostring( obj, encoding="utf8", method="xml" ).decode()

    with open( "data_new.xml", "w" ) as f:
        f.write( ser )


def listNodes( root ):
    result = []
    for node in root.iter():
        result.append( node.tag )

    return result;

def getParent( root, node ):
    for child in root:
        if child == node:
            return root

    for child in root:
        res = getParent( child, node )
        if res != None:
            return res

    return None

def deleteNode( parent, node ):
    # parent = getParent( root, node )
    node.clear()
    parent.remove( node )

def deleteTagNodes2( root, tagname ):
    # problem version, skip element after delete,
    # so half of elements not deleted
    for node in root:
        if node.tag == tagname:
            deleteNode( root, node )
        else:
            deleteTagNodes2( node, tagname )

def deleteTagNodes3( root, tagname ):
    # problem vesrion, skip element after delete,
    # so half elements not deleted
    for node in root.iter():
        if node.tag == tagname:
            deleteNode( getParent( root, node ), node )

def deleteTagNodes( root, tagname ):
    #print( "find all in", root.tag, " with tagname ", tagname )
    toDelete = root.findall( tagname )

    for node in toDelete:
        #print( "delete: ", node.tag, node.text, node.attrib )
        deleteNode( root, node )

    for node in root:
        #print( "process node", node.tag, node.text )
        deleteTagNodes( node, tagname )


def main():
    data = init()
    print( "list nodes: ", listNodes( data ) )

    # getting language Java, it's parent is languages
    lang = getParent( data, data[ 3 ][ 1 ] )
    print( "\nparent tag: ", lang.tag )

    print( "\nwork version" )
    deleteTagNodes( data, "pc_item" )
    print( "list nodes: ", listNodes( data ) )

    print( "\nfail version" )
    deleteTagNodes2( data, "pc_item" )
    print( "list nodes: ", listNodes( data ) )

    print( "\nfail version2" )
    deleteTagNodes3( data, "pc_item" )
    print( "list nodes: ", listNodes( data ) )


if __name__ == "__main__":
    main()

