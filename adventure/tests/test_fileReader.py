#!/usr/bin/python

import unittest
import tempfile
import os.path
from   shutil     import rmtree
from   fileReader import ConfigReader

_TEST_JSON = '''
{
    "Player" : [
        {
            "name"        : "bob",
            "skill"       : 12,
            "stamina"     : 15,
            "luck"        : 9,
            "affiliation" : "ChaoticNeutral"
        }
    ]
}
'''
_TEST_YML = '''
Item:
   - {damage: 1, name: Rock}
   - {damage: 4, name: Sword}
'''

_EXPECTED = {
    'items' : {
        'Item' : [
            { 'damage': 1, 'name': 'Rock'  },
            { 'damage': 4, 'name': 'Sword' }
        ]
    },
    'players' : {
        'Player' : [
            {
                'affiliation' : 'ChaoticNeutral',
                'luck'        : 9,
                'name'        : 'bob',
                'skill'       : 12,
                'stamina'     : 15
            }
        ]
    }
}

class TestConfigReader( unittest.TestCase ):

    def setUp( self ):
        self.configDir    = tempfile.mkdtemp()
        self.configReader = ConfigReader( self.configDir )
        # create two test files
        with open( self.configDir + os.path.sep + 'players.json', 'w' ) as players:
            players.write( _TEST_JSON )
        with open( self.configDir + os.path.sep + 'items.yml', 'w' ) as items:
            items.write( _TEST_YML )
        self.maxDiff = 2000

    def tearDown( self ):
        rmtree( self.configDir )

    def test_get( self ):
        config   = self.configReader.get()
        expected = _EXPECTED
        self.assertEqual( config, expected )
    
    def test__findConfigs( self ):
        self.assertEqual( self.configReader._findConfigs(), [ 'players.json', 'items.yml' ] )
    
    def test__get( self ):
        playersConfig = self.configReader._get( 'players.json' )
        expected      = _EXPECTED[ 'players' ]
        self.assertEqual( playersConfig, expected )

        itemsConfig   = self.configReader._get( 'items.yml' )
        expected      = _EXPECTED[ 'items' ]
        self.assertEqual( itemsConfig, expected )        
        
        self.assertRaises( NotImplementedError, self.configReader._get, 'wrong.jpg' )

    def test__getAll( self ):
        self.assertEqual( self.configReader._getAll(), _EXPECTED )

    def test__readJson( self ):
        pass # tested in real calls above

    def test__readYml( self  ):
        pass # tested in real calls above
        
if __name__ == '__main__':
    unittest.main()

