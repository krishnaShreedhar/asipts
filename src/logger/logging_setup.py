import logging.config
import os
import yaml
import datetime as dtime

DEFAULT_CONFIG_FILE = 'logger/config_log.yaml'
DIR_LOGS = "../logs"


def setup_logging(config_file=DEFAULT_CONFIG_FILE):
    """

    :param config_file:
    :return:
    """
    if not os.path.exists(DIR_LOGS):
        os.makedirs(DIR_LOGS)

    with open(config_file, 'r') as file:
        config_logger = yaml.load(file, Loader=yaml.FullLoader)
        # print(config_logger)

    prefix = config_logger["extra"]["prefix"]
    if config_logger["extra"]["use_timestamp"]:
        str_ts_fmt = config_logger["extra"]["str_ts_fmt"]
        str_ts = dtime.datetime.now().strftime(str_ts_fmt)
        filename = f"{prefix}{str_ts}.txt"
    else:
        filename = f"{prefix}.txt"
    config_logger["handlers"]["out_file"]["filename"] = filename

    logging.config.dictConfig(config_logger)


setup_logging()
LOGGER = logging.getLogger('utils')


def main():
    # 'application' code
    LOGGER.debug('debug message')
    LOGGER.info('info message')
    LOGGER.warning('warn message')
    LOGGER.error('error message')
    LOGGER.critical('critical message')


if __name__ == '__main__':
    main()
