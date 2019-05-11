from typing import Dict, List
from PodSixNet.Connection import connection, ConnectionListener
import pickle
from _thread import *
import pickle
from collections import defaultdict, deque


class Client(ConnectionListener):
	def __init__(self, host, port, player_name):
		self.actions = deque()
		self.Connect((host, port))
		self.player_name = player_name
		connection.Send({"action": "player_name", "player_name": player_name})
		# t = start_new_thread(self.InputLoop, ())

	def get_action(self):
		if len(self.actions):
			return pickle.loads(self.actions.pop())


	def Update(self):
		#print("---updating ", self.player_name)
		connection.Pump()
		#print("done connection.Pump()")
		self.Pump()
		#print("done self.Pump()")

	def send_action(self, data):
		#print('sending to ', connection)
		connection.Send({"action": "action", "event": pickle.dumps(data), "player_name": self.player_name})

	#######################################
	### Network event/message callbacks ###
	#######################################

	def Network_players(self, data):
		print("*** players: " + ", ".join([p for p in data['players']]))

	def Network_action(self, data):
		#print('hey')
		#print(data)
		if not data['player_name'] == self.player_name:
			self.actions.append(data["event"])

	# built in stuff

	def Network_connected(self, data):
		print("You are now connected to the server")

	def Network_error(self, data):
		print(data)
		print('error:', data['error'][1])
		connection.Close()

	def Network_disconnected(self, data):
		print('Server disconnected')
		exit()
