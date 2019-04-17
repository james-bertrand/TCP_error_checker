# client.py
"""
    I'm thinking the client should be ran a single instance at a time, exiting and closing the socket after sending message and receiving validation or not
"""

import socket, random
import sys, argparse


# function sets up the argparser arguments for the program
def setup_argparser(parser):
    # change required to true when socket connection function is project-ready
    parser.add_argument('-p', '--port', type=int, required=False, help='Usage: -p or --port <portNumber>')
    parser.add_argument('-b', '--bits', type=int, required=True, help='Usage: -b or --bits <numberOfBits>')
    parser.add_argument('-t', '--type', type=str, required=False, help='Usage: -t or --type <typeOfErrorCheck>')
    # can delete --function arg if we decide to not let the user specify the crc polynomial
    parser.add_argument('-f', '--function', type=bin, required=False, help='Usage: -f or --polynomialFunction <crcPolynomial>')
    args = parser.parse_args()
    return args


# return a numpy array of length num_bits, containing only 1s and 0s
def generate_message(num_bits):
    return random.getrandbits(num_bits)


# pass the message to the appropriate error checking function
def generate_error_code():

    # call error checking function (i.e. parity_1D) depending on argparser value
    # these functions return the appropriate binary error code, which this function will return
    # return error_code
    pass


# 1D parity check
def parity_1D():
    pass


# 2D parity check
def parity_2D():
    pass


# cyclic redundancy check
def crc():
    # need to figure out a way to pass in the polynomial if the user is going to specify that
    # otherwise we can just use a default one
    pass


# checksum, perhaps summing the message in 8-bit pieces?
def checksum():
    pass


# print the message and error code, separated in 8-bit groupings, as a nice easy to read table
def pretty_print_message(message, error_code):
    # process the message and error_code ints as binary numbers (without the 0b prefix) and convert to a string,
    # spaced by every 8 bits
    message_string = '{0:b}'.format(message)
    message_string = ' '.join([message_string[n:n + 8] for n in range(0, len(message_string), 8)])

    error_code_string = '{0:b}'.format(error_code)
    error_code_string = ' '.join([error_code_string[n:n + 8] for n in range(0, len(error_code_string), 8)])

    # some formatting for a nice print out of the message
    print('\nMessage {0:{1}}| Error Code'.format('', (len(message_string) - len('Message'))))
    print('{0:->{1}}{2:-<{1}}'.format('|', (len(message_string) + 2), ''))
    print('{0} | {1}'.format(message_string, error_code_string))


# implement functions for connecting to, sending data, and receiving data from the server here


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    args = setup_argparser(parser)


    message = generate_message(args.bits)
    pretty_print_message(message, 12)
