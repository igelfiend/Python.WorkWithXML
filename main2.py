# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ETree

def init():
    data = ETree.Element( "data" )
    ETree.SubElement( data, "name" ).text =  "Petya"
    ETree.SubElement( data, "sex"  ).text = "true"
    ETree.SubElement( data, "age"  ).text = "23"
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

    ser = ETree.tostring( data, encoding="utf8", method="xml" ).decode()

    with open( "data_new.xml", "w" ) as f:
        f.write( ser )



def main():
    init()

if __name__ == "__main__":
    main()

