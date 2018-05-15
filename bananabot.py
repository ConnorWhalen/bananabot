import json
import logging
import nltk
from nltk.tokenize import word_tokenize
from random import randint

import tweeter

logging.basicConfig(level='INFO', filename='bananabot.log')
logger = logging.getLogger(__name__)

def bananabot():
	quotes_file = open('quotes.json')
	quotes_str = quotes_file.read()
	quotes_json = json.loads(quotes_str)

	nouns = []
	while len(nouns) == 0:
		quote_index = randint(0, len(quotes_json)-1)
		quote_json = quotes_json[quote_index]
		quote_author = quote_json['quoteAuthor']
		quote_text = quote_json['quoteText']
		logger.info('Candidate quote:')
		logger.info('"' + quote_text + '"')
		logger.info(' - ' + quote_author)

		quote_tokens = word_tokenize(quote_text)
		tagged_words = nltk.pos_tag(quote_tokens)
		for word in tagged_words:
			if word[1] == 'NN':
				nouns.append(word[0])

	noun_index = randint(0, len(nouns)-1)
	noun = nouns[noun_index]

	quote_split = quote_text.split(noun)
	occurences = len(quote_split)-1
	occurence_index = randint(0, occurences-1)

	quote_replaced = quote_split[0]
	for i in range(occurences):
		if i == occurence_index:
			if noun[0].isupper():
				quote_replaced += 'Banana' + quote_split[i+1]
			else:
				quote_replaced += 'banana' + quote_split[i+1]
		else:
			quote_replaced += noun + quote_split[i+1]

	logger.info('Banana-fied quote:')
	logger.info(quote_replaced)

	author = quote_author
	if author == '':
		author = 'Unknown'

	message = '"{0}"\n - {1}'.format(quote_replaced, author)

	logger.info("Full message:")
	logger.info(message)

	# tweeter.post_tweet(quote_replaced)

	# logger.info('')
	# logger.info('Quote tweeted successfully!')
	# logger.info('')

try:
	bananabot()
except Exception as e:
	logger.error(e)
