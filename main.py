from GeminiModule import api_gemini
import argparse

parser = argparse.ArgumentParser(
    prog = 'CLIbot',
    description='allows you to ask get a response from gemini in terminal'
)

parser.add_argument('message', metavar="message", type=str, help='enter your message to chatbot')

args = parser.parse_args()

message = args.message

api_gemini.ai_response(message)