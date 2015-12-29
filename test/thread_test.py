#!/usr/bin/python
#coding=utf8

import threading
import thread
import time

class couter(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        print('init')
        pass

    def run(self):
        print('run')
        for x in xrange(10):
            time.sleep(1)
            thread.interrupt_main()
            print('in run')

    def __enter__(self):
        print('enter')
        self.setDaemon(True)
        self.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        self.join()
        print('join called')
        return exc_type is not None and issubclass(exc_type, KeyboardInterrupt)


if __name__ == '__main__':
    c = couter()
    try:
        with c:
            print('main')
            while True:
                time.sleep(1)
                print('in main')
        print('after thread1')
    except KeyboardInterrupt as e:
        print(e)
        pass
