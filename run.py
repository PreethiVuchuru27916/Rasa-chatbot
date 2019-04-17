from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/foodnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('', #app verification token
							'', # bot verification token
							'', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5010, '/', input_channel))
