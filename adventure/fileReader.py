import json
import yaml
import os
import os.path

def stripUnicode( pairs ):
    new_pairs = [ ]
    for key, value in pairs:
        if isinstance( value, unicode ):
            value = value.encode( 'utf-8' )
        if isinstance( key, unicode ):
            key = key.encode( 'utf-8' )
        new_pairs.append( ( key, value ) )
    return dict( new_pairs )

class ConfigReader( object ):
	def __init__( self, configDir ):
		self.configDir = configDir

	def get( self, configFile = None ):
		''' get a specific config, or if none passed, everything '''
		if not configFile:
			return self._getAll()
		else:
			return self._get( configFile )

	def _findConfigs( self ):
		''' walk the configDir and return a list of all the configs '''
		supportedTypes = [ 'json', 'yml' ]
		configs = []
		for extension in supportedTypes:
			configs.extend(
				[ x for x in os.listdir( self.configDir ) if x.endswith( '.%s' % extension ) ]
			)
		return configs

	def _get( self, configFile ):
		''' read a config '''
		if configFile.endswith( '.json' ):
			return self._readJson( configFile )
		elif configFile.endswith( '.yml' ):
			return self._readYml( configFile )
		else:
			raise NotImplementedError( 'file: %s not a supported type' )

	def _getAll( self ):
		''' discover and return ALL configs '''
		config = {}
		for configFile in self._findConfigs():
			withoutExtension = configFile.split('.')[0]
			config[ withoutExtension ] = self._get( configFile )
		return config

	def _readJson( self, configFile ):
		with open( self.configDir + os.path.sep + configFile, 'r' ) as handle:
			config = json.loads( handle.read(), object_pairs_hook = stripUnicode )
		return config

	def _readYml( self, configFile ):
		with open( self.configDir + os.path.sep + configFile, 'r' ) as handle:
			config = yaml.load( handle )
		return config