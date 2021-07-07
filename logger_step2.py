import logging

# Create a module level logger object, rather than using root
logger = logging.getLogger(__name__)

def add(x, y):
    logger.warning("Running add()")
    return x + y

if __name__ == "__main__":
    print ("Result of add :" + str(add(100,200)) )
