import logging
import os

logger = logging.getLogger("dadabot")

if "PORT" in os.environ:
    logger.setLevel(logging.INFO)
else:
    logger.setLevel(logging.DEBUG)

logger.addHandler(logging.StreamHandler())
