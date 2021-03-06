import time
import os
import psutil


def elapsed_since(start):
    elapsed = time.perf_counter() - start
    if elapsed < 1:
        return str(round(elapsed * 1000, 2)) + "ms"
    if elapsed < 60:
        return str(round(elapsed, 2)) + "s"
    if elapsed < 3600:
        return str(round(elapsed / 60, 2)) + "min"
    else:
        return str(round(elapsed / 3600, 2)) + "hrs"


def format_bytes(bytes):
    if abs(bytes) < 1000:
        return str(bytes) + "B"
    elif abs(bytes) < 1e6:
        return str(round(bytes / 1e3, 2)) + "kB"
    elif abs(bytes) < 1e9:
        return str(round(bytes / 1e6, 2)) + "MB"
    else:
        return str(round(bytes / 1e9, 2)) + "GB"


def get_process_memory():
    process = psutil.Process(os.getpid())
    mi = process.memory_info()
    return mi.rss


def time_it(debug=False):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"\n### Entering in {func.__name__}. ###")
            t1 = time.perf_counter()
            rss_before = get_process_memory()
            s = func(*args, **kwargs)
            if debug:
                print(s)
            elapsed_time = elapsed_since(t1)
            rss_after = get_process_memory()
            print(f"### Quitting function {func.__name__}. ###\n")
            print(
                "Profiling: {:>8}  RSS: {:>8} | time: {:>8}".format(
                    "<" + func.__name__ + ">",
                    format_bytes(rss_after - rss_before),
                    elapsed_time,
                )
            )
            print("\n")
            return s

        return wrapper

    return real_decorator

