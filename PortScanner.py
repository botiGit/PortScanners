#!/usr/bin/python

from socket import *
import optparse
from threading import *

def connScan(targetHost, targetPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((targetHost,targetPort))
        print '[+] &d/TCP Open' % targetPort
    except:
        print '[-] &d/TCP Closed' % targetPort
    finally:
        sock.close()


def portScan(targetHost,targetPorts):
    try:
        targetIP =getHostByName(targetHost)
    except:
        print 'Unknown Host %s '%targetHost
    try:
        targetName = getHostByAddress(targetIP)
        print '[+] Scan Results For: ' + targetName[0]
    except:
        print '[+] Scan Results for: ' + targetIP
    setdefaulttimeout(1)
    for targetPort in targetPorts:
        t = Thread(target=connScan, args=(targetHost,int(targetPort)))
        t.start()

def main():
    parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type= 'string', help='specfy target host')
    parser.add_option('-p', dest='tgtPort', type= 'string', help='specfy target ports separated by commas')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print parser.usage
        exit(0)
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()