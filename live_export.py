from hearthstone.enums import GameTag

from hslog.export import EntityTreeExporter, BaseExporter
from live_entities import LiveCard, LiveGame, LivePlayer
from live_utils import terminal_output

import hearthstone.entities as ent

class LiveEntityTreeExporter(EntityTreeExporter):
	"""
		Inherits EntityTreeExporter to provide Live entities
	"""

	game_class = LiveGame
	player_class = LivePlayer
	card_class = LiveCard

	def __init__(self, packet_tree):
		super(LiveEntityTreeExporter, self).__init__(packet_tree)
	
	def handle_option(self, packet):

		isHero = False

		#id represents the id of the option or the suboption

		if (packet.entity == 66) | (packet.entity == 64) | (packet.entity == 65):
			isHero = True

		#viable options which are not end turn
		if not packet.error:
			current_entity = self.game.find_entity_by_id(packet.entity)

			
			#suboptions don't have a type
			if not packet.type:
				if isHero:
					terminal_output("TARGET LISTED", packet.entity)

				else:
					terminal_output("TARGET LISTED", current_entity, current_entity.tags.get(GameTag.ZONE_POSITION), current_entity.ownerstr)
					

			else:
				if isHero:
					terminal_output("OPTION LISTED", packet.entity)
				else:
					terminal_output("OPTION LISTED", current_entity.zone, current_entity.tags.get(GameTag.ZONE_POSITION),  packet.id)

		#option end turn
		if packet.type == 2:
			terminal_output("END TURN", packet.ts, packet.type, packet.id)

	def handle_send_option(self, packet):
		terminal_output("sendoptions", packet.target, packet.position, packet.suboption)