# The output is an Undirected Graph
import sys
import numpy as np
import re

def adding_lines(a, dblines):
    cmd_name = '"(.*)"'
    cmd_node = "(\(.*?\))"
    street_name = re.findall(cmd_name, a)
    street_node = re.findall(cmd_node, a)
    street_name = "".join(street_name)
    if street_name not in dblines:
        dblines[street_name] = street_node
    else:
        print 'Error: street currently exists.'
    if a[-1] != ')':
        print 'Error: Incorrect input format'

def change_lines(c, dblines):
    cmd_name = '"(.*)"'
    cmd_node = "(\(.*?\))"
    street_name = re.findall(cmd_name, c)
    street_node = re.findall(cmd_node, c)
    street_name = "".join(street_name)
    if street_name not in dblines:
        print "Error: 'c' or 'r' specified for a street that does not exist"
    else:
        for things in dblines:
            if street_name == things:
                   dblines[things] = street_node

def remove_lines(r, dblines):
    cmd_name = re.compile('"(.*)"')
    street_name = "".join(cmd_name.findall(r))
    street_name = "".join(street_name)
    if street_name not in dblines:
        print "Error: 'c' or 'r' specified for a street that does not exist"
    else:
        for things in dblines:
         if street_name == things:
            del dblines[street_name]
         break

def main():
        Db_street_node = {}
        try :
            while True:
                line = raw_input('')
                if line == '':
                    break
                elif line[0] == 'a' and line[1:] != ' ':
                    adding_lines(line, Db_street_node)
                elif line[0] == 'c' and line[1] == ' ':
                    change_lines(line, Db_street_node)
                elif line[0] == 'r' and line[1] == ' ':
                    remove_lines(line, Db_street_node)
                elif line[0] == 'g':
                    if line[1:] == '':
                        vertex = Db_street_node.values()
                        print "V={"
                        #print vertex
                        print "}"
                        print "E={"
                        #for items in Db_street_node:
                        ##
                    else:
                        print('Error: Incorrect input Format')
                elif line[0] != 'r' or 'a' or 'c' or 'r' or 'g' and line[1] == ' ':
                    print "Error: Incorrect input format"

                elif line == '':
                    break
                else:
                    pass
            sys.exit(0)
        except:
            print '\n'


if __name__ == '__main__':
    main()
