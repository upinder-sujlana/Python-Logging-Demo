import logging

def test_loggingDemo():
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("This is a debug level message")
    logging.info("This is a info level message")
    logging.warning("This is a warning level message")
    logging.error("This is a error level message")
    logging.critical("This is a critical level message")

if __name__ == "__main__":
    test_loggingDemo()
