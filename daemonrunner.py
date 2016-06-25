'''
https://opensource.org/licenses/MIT

License: The MIT License (MIT)

Copyright (c) 2016 Ariel Kalingking akalingking@gmail.com

Permission is hereby granted, free of charge, to any person 
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, 
merge, publish, distribute, sublicense, and/or sell copies of 
the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be 
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
'''
from daemon import runner
import getopt, sys

class DaemonRunner(runner.DaemonRunner):
    def __init__(self, app):
        # store app here, so we can access it in parse args.
        self.app_save = app
        self.detach_process = True
        runner.DaemonRunner.__init__(self, app)

    def parse_args(self, argv=None):
        try:
            opts, args = getopt.getopt(sys.argv[1:],
                    'skrl:p:fvh',
                   ['start', 'kill', 'log_file=',
                    'pid_file=', 'foreground'])
        except getopt.GetoptError:
            print sys.exc_info()
            print 'getopt error...'
            sys.exit(2)

        self.action = ''
        for opt, arg in opts:
            #print 'opt / arg :', opt, arg
            if opt in ('-s'):
                self.action = 'start'
            elif opt in ('-k'):
                self.action = 'stop'
            elif opt in ('-r'):
                self.action = 'restart'
            elif opt in ('-l', '--log_file'):
                self.app_save.application.logfile_ = arg
            elif opt in ('-p', '--pidfile'):
                self.app_save.pidfile_path = arg
                #print 'arg is :', arg
            elif opt in ('-f', '--foreground'):
                self.detach_process = False
                self.app_save.stdout_path = '/dev/tty'
                self.app_save.stderr_path = '/dev/tty'
                self.app_save.foreground = True
            elif opt in ('-v'):
                self.verbose = True
            elif opt in ('-h', '--help'):
                print 'show usage...'
                sys.exit(2)
            else:
                print 'show usage'
                sys.exit(2)

        if not self.action:
            print sys.argv[0] + ' (-s|-k|-r) [options]'
            sys.exit(1)
