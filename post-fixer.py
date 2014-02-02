import peewee as pw
from peewee import *
import json
import sys

access = json.load(open('access.json'))

def main():
  print sys.argv
  if (sys.argv[1] > 0):
    post_id = int(sys.argv[1])
  else:
    print "must supply post_id."
  khon = pw.MySQLDatabase("khon", user=access["user"], passwd=access["password"])
  khon.connect()

if __name__ == "__main__":
  main()
