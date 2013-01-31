#!/usr/bin/env python2.7

"""
Kathryn Nichols
Stefan Behr
LING 571
Project 1
"""

if __name__ == "__main__":
	import nltk, sys
	from parser import CKYParser, timer
	from print_output import print_parses

	try:
		sentence_path = sys.argv[1]
	except IndexError:
		exit("Please give a path to a file of sentences.")

	try:
		grammar_path = sys.argv[2]
	except IndexError:
		exit("Please give a path to a file with a grammar.")

	with open(sentence_path) as sentence_file:
		sentence_data = sentence_file.read()

	sentences = sentence_data.strip().split("\n")
	sentences = [nltk.wordpunct_tokenize(sentence) for sentence in sentences]

	parser = CKYParser(grammar_path)

	# iterate over tokenized sentences, parse each
	# and output parses
	for sentence in sentences:
		sentence = ["'{0}'".format(token) for token in sentence]	# make sure tokens are single-quoted
		parses = parser.get_parses(sentence)
		sys.stdout.write(print_parses(parses))
		print " ".join([token.strip("'\"") for token in sentence])
		print "{0:f} seconds to parse sentence {1} time(s)".format(parser.parse.delta, timer.n)
		print len(parses)
		print 40 * "-"