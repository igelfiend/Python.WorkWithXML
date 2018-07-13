from main import *
import unittest


# Testing node data getter
class TestingDataGetterCase(unittest.TestCase):
    def testNormalCase(self):
        root = getRoot( "data.xml" )
        self.assertEqual( getTagData( root, "language" ), [ '9', '7', '8' ] )

    def testEmptyCase(self):
        root = getRoot( "data.xml" )
        self.assertEqual( getTagData( root, "languages" ), [ '\n\t\t' ] )

    def testNoTagCase(self):
        root = getRoot( "data.xml" )
        self.assertEqual( getTagData( root, "test" ), [] )


# Testing nodes with attribs counter
class TestingCountOfNodesWithAttrib(unittest.TestCase):
    def testNormalCase(self):
        root = getRoot( "data.xml" )
        self.assertEqual( getCountNodesWithAttrib( root, "name" ), 7 )

    def testEmptyCase(self):
        root = getRoot( "data.xml" )
        self.assertEqual( getCountNodesWithAttrib( root, "age" ), 0 )

    def testOnNullTagNameCase(self):
        root = getRoot( "data.xml" )
        self.assertEqual( getCountNodesWithAttrib( root, "" ), 0 )


if __name__ == '__main__':
    unittest.main()
