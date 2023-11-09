import logging
import queue

from logging.handlers import QueueListener
import functools


func_log = logging.getLogger(
    name="func_log",
)

func_log_hend2 = logging.StreamHandler()
func_log_form = logging.Formatter("%(name)s:%(asctime)s:%(levelname)s: %(message)s")

func_log.addHandler(
    func_log_hend2,
)

listener = QueueListener(queue.Queue(-1), *logging.getLogger("func_log").handlers)

listener.start()

func_log.warning("Async logging test")


def func_logging(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        func_log.error(f"Функция {func.__name__} выполнена")
        return result

    return wrapper
