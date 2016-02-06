"""
Simple example of the default args as function behaviour

"""

import datetime
import time


def print_message_with_time(message, time=datetime.datetime.now()):
    print("%s : %s" % (time.isoformat(), message))


def main():
    print_message_with_time("first call")
    # sleep 1 second
    time.sleep(1)
    print_message_with_time("second call")


if __name__ == "__main__":
    main()
