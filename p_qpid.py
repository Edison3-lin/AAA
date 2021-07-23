import sys
from qpid.messaging import *

if len(sys.argv)<2:
  broker =  "localhost:5672" 
else:
  broker = sys.argv[1]

if len(sys.argv)<3: 
  address = "amq.topic" 
else:
  address = sys.argv[2]

connection = Connection(broker)

try:
  connection.open()
  session = connection.session()

  sender = session.sender(address)
  receiver = session.receiver(address)

  sender.send(Message("Hello world!"));

  message = receiver.fetch()
  print(message.content)
  session.acknowledge()

except:
  print('m')

connection.close()