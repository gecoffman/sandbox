#!/usr/bin/python

class Item( object ):
  def __init__( self, name ):
    self.name = name

  def __repr__( self ):
    return self.name

class Inventory( object ):
  def __init__( self, name, owner, capacity = 10, items = None ):
    self.name     = name
    self.owner    = owner
    self.capacity = capacity
    self.items    = items or [ ]
    if len( self.items ) > self.capacity:
      raise ValueError( 'Inventory %s initialized with item list greater than capacity %d' % ( self.name, self.capacity ) )

  def __repr__( self ):
    return "Contents of %s's %s ( capacity: %d )\n%s" % (
      self.name,
      self.owner,
      self.capacity,
      '\n'.join( str(x) for x in self.items )
    )
