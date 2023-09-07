from pynotifier import Notification

Notification(
	title='Emergency',
	description='Hola Cristofer',
	duration=5,                                   # Duration in seconds
	urgency='normal'
).send()