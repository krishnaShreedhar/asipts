"""
Sample code to demonstrate logging
"""
import logging
import logger.logging_setup as log

log.setup_logging()
LOGGER = logging.getLogger('core')


def fun(text):
    LOGGER.info(f"Hello There!")
    return text + text


def logs():
    LOGGER.debug('debug message')
    LOGGER.info('info message')
    LOGGER.warning('warn message')
    LOGGER.error('error message')
    LOGGER.critical('critical message')


def main():
    list_tests = [str(x) for x in range(10)]
    for index, text in enumerate(list_tests):
        out = fun(text)
        LOGGER.info(f"input: {text}, output: {out}")

    logs()


if __name__ == '__main__':
    main()
