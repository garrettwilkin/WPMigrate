import peewee as pw
import json

access = json.load(open('access.json'))
khon = pw.MySQLDatabase("khon",
    host=access["host"], port=access["port"],
    user=access["user"], password=access["password"])
khon.connect()

def main():
  print sys.argv
  if (sys.argv[1] > 0):
    post_id = int(sys.argv[1])
  else:
    print "must supply post_id."
  khon = pw.MySQLDatabase("khon",
      host="khon.hacktivate.org", port="3306",
      user="khon",password="khon")
  khon.connect()

if __name__ == "__main__":
  main()
