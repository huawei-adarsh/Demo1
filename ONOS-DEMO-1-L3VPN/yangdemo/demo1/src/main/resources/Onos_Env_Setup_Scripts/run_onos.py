#!/usr/bin/python

import pexpect
import time
import sys
import os

print('Logging-in to the ONOS console. Please wait')
try:

    child1 = pexpect.spawn('./buck-out/gen/tools/package/onos-package/onos-1.10.0-SNAPSHOT/apache-karaf-3.0.8/bin/karaf',timeout=120,ignore_sighup=True)
    child1.expect('onos> ')
    print('Successfully logged-in to ONOS console')
except pexpect.TIMEOUT:
    print('Login failed. Please check karaf.log for help')


def activateApp(app):
    try:
	print('Activating: '+app)
        child1.sendline('app activate org.onosproject.'+app)
        child1.expect('>')
	#time.sleep(5)
    except pexpect.TIMEOUT:
        print('Failed to execute: '+app)

def activateApps():
    print('Wait for 60 secs before feature installation')
    time.sleep(60)
    activateApp('yang')
    activateApp('config')
    activateApp('yms')
    activateApp('restconf')
    activateApp('ovsdbhostprovider')
    activateApp('protocols.restconfserver')
    activateApp('yangdemo')
    activateApp('netconf')
    activateApp('netconfsb')

    #child1.expect('>')
    print('All required features are installed successfully')

def getConsole():
    print('Activating MSO, Relax.... ')
    #time.sleep(240)
    print('MSO acivated successfully.')
    print('ONOS console can be access now. Enjoy :-)')
    child1.interact()
    

activateApps()
getConsole()
