#! python3
# superCountdown.py - takes args for seconds/minutes/hours for a countdown

import time
import sys
import getopt
import subprocess


def main():
    timeLeft = 0
    hours = 0
    minutes = 0
    seconds = 0
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hHms', [
                                   'help', 'hours=', 'minutes=', 'seconds='])
    except getopt.GetoptError:
        print('superCountdown.py -H <hours> -m <minutes> -s <seconds>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('superCountdown.py -H <hours> -m <minutes> -s <seconds>')
            sys.exit()
        elif opt in ('-H', '--hours'):
            hours = int(arg)
        elif opt in ('-m', '--minutes'):
            minutes = int(arg)
        elif opt in ('-s', '--seconds'):
            seconds = int(arg)
    timeLeft = (hours * 3600 + minutes * 60 + seconds)
    while timeLeft > 0:
        m, s = divmod(timeLeft, 60)
        h, m = divmod(m, 60)
        print("%d:%02d:%02d remaining" % (h, m, s))
        # http://stackoverflow.com/questions/775049/python-time-seconds-to-hms
        timeLeft -= 1
        time.sleep(1)
    # subprocess.Popen(['start', 'alarm.wav'], shell=True)


if __name__ == "__main__":
    main()
