#!/usr/bin/python

from dice      import roll, D6
from inventory import Inventory

class Player( object ):
  	''' base class for all players '''
  	def __init__( self, playerName, skill = None, stamina = None, luck = None, inventory = None, affiliation = None ):
  		self.playerName  = playerName
  		self.skill       = skill     or roll( [ D6, D6 ] )
  		self.stamina     = stamina   or roll( [ D6, D6 ] ) + 6
  		self.luck        = luck      or roll( [ D6, D6 ] )
  		self.inventory   = inventory or Inventory( 'Backpack', self.playerName )
  		self.affiliation = affiliation

  	def __repr__( self ):
  		return 'Player: %s (Skill: %d, Stamina: %d, Luck: %d, Affiliation: %s)\n\nInventory: %s' % (
  			self.playerName,
  			self.skill,
  			self.stamina,
  			self.luck,
  			self.affiliation,
  			self.inventory
  		)