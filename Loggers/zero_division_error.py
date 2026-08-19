import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def divide(a, b):
    logger.info("Dividing %s by %s, a, b")

    try:
        return a/b
    except ZeroDivisionError:
        logger.error("Cannot divide b zero")
        return None

divide(10, 0)