import logging


class LogGen:
    @staticmethod
    def loggen():

        #logging.basicConfig(filename='.\\Logs\\automation.log',
                            #format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m%d%Y%I%M%S%p',
                            #level=logging.INFO)
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',datefmt='%m%d%Y%I%M%S%p')
        #logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler('.\\Logs\\automation.log')
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        return logger