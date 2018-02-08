import sys
import json
import predict

import utility as u
import sma_experiment as sma

def decide():
    return sma.decide()

def read_in():
    lines = sys.stdin.readlines()
    return json.loads(lines[0])

def main():
    # Demonstrate how we can receive data from JS using this method
    #lines = read_in()

    # Simple print data to send back for JS
    print(decide())

if __name__ == '__main__':
    main()
