#!/usr/bin/env python
#from __future__ import print_function

# -*- coding: utf_8 -*-
colors = {
    'clear': '\033[0m',
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'purple': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m'
}
#for k, v in colors.iteritems():
#    print '%s%s' % (v, k)

# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'

#     def disable(self):
#         self.HEADER = ''
#         self.OKBLUE = ''
#         self.OKGREEN = ''
#         self.WARNING = ''
#         self.FAIL = ''
#         self.ENDC = ''

print colors['red'] + 'aaa' + colors['white']

#print "\033[95m" + 'Warning: No active frommets remain. Continue?' + "\033]"

#print "\033[95m" #+ 'Warning: No active frommets remain. Continue?' 
      #+ "\033[0m"

#print colored('test', 'red')
#print '%s%s' % (v, k)
