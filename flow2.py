from flow import Flow
flow=Flow('Folks')
def print_message(notif_type,notif_data):
	regular_messages=notif_data["regularMessages"]
	for message in regular_messages:
		print("Got message '%s' from ChannelID='%s'" %(message["text"],message["ChannelID"]))

flow.process_notifications()
