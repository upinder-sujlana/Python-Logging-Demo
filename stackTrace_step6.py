import logging

names = ["Upinder","Sujlana"]
try:
  print (names[2])
except Exception as e:
  logging.error("An exception has occured, stacktrace : ", exc_info=True)
