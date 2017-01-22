#! python3
# superCountdown.py - takes args for seconds/minutes/hours for a countdown

import time
import sys
import getopt
# import subprocess
import pyaudio
import wave


def main():
    timeLeft = 0
    hours = 0
    minutes = 0
    seconds = 0
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hH:m:s:', [
                                   'help', 'hours=', 'minutes=', 'seconds='])
    except getopt.GetoptError:
        printHelp()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            printHelp()
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
        print("\r%d:%02d:%02d remaining" % (h, m, s), end='')
        # http://stackoverflow.com/questions/775049/python-time-seconds-to-hms
        timeLeft -= 1
        time.sleep(1)
    print("\r%d:%02d:%02d remaining" % (h, m, 0), end='')  # to appease the OCD
    print('\nDone!')
    timeOver = 0
    try:
        while True:
            m, s = divmod(timeOver, 60)
            h, m = divmod(m, 60)
            if m % 2 == 0 and s == 0:
                start = time.time()
                playSound()
                # to roughly sync the time over
                timeOver += int(time.time() - start)
            print("\r%d:%02d:%02d over!" % (h, m, s), end='', flush=True)
            timeOver += 1
            time.sleep(1)
    except KeyboardInterrupt:
        print('\nIt\'s about time!')


def printHelp():
    print('OPTIONS:\n\nhelp\t-h, --help\nhours\t-H, --hours\n' +
          'minutes\t-m, --minutes\nseconds\t-s, --seconds')


def playSound():
    chunk = 1411
    # subprocess.Popen(['start', 'alarm.wav'], shell=True)
    w = wave.open('alarm.wav', 'r')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(w.getsampwidth()),
                    channels=w.getnchannels(),
                    rate=w.getframerate(),
                    output=True)
    data = w.readframes(chunk)

    while data:
        stream.write(data)
        data = w.readframes(chunk)

    # stop stream
    stream.stop_stream()
    stream.close()

    # close PyAudio
    p.terminate()


if __name__ == "__main__":
    main()
