import json
import csv

filename = 'message_8'

with open(f'{filename}.json') as messages_file:
    data = json.load(messages_file)

# Get participants

participants = data['participants']

participants = list(map(lambda x: x['name'], participants))

print(f'Number participants: {len(participants)}')

# Get messages

messages = data['messages']

senders = list(map(lambda x: x['sender_name'], messages))

print(f'Number messages: {len(senders)}')

# Get messages per participant and write to CSV

with open(f'{filename}_messagesCount.csv', mode='w', newline='') as results_file:
    messageCountWriter = csv.writer(results_file)

    messageCountWriter.writerow(['Name', 'Messages sent'])

    for participant in participants:
        messageCountWriter.writerow([participant, senders.count(participant)])

# Reactions

# reactionsList = []

# for message in messages:
#     reactions = message.get('reactions')
#     if reactions:
#         reactionsList += reactions

# uniqueReactions = list(set(map(lambda x: x['reaction'], reactions)))

# print(len(reactionsList))
