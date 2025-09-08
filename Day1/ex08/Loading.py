import time
import shutil


def format_time(seconds: float) -> str:
    """
    Format time as MM:SS

    Args:
        seconds (float): Time in secs.

    Returns:
        str: Time formatted as MM:SS
    """
    m = seconds // 60
    s = seconds % 60
    return f"{int(m):02d}:{int(s):02d}"


def ft_tqdm(lst: range) -> None:
    """
    A generator that mimics tqdm-like progress bars in the terminal.

    Args:
        lst (range): An iterable (typically a range) to iterate over.

    Yields:
        item: Each item from the input iterable, one at a time.

    Displays:
        A dynamic progress bar showing:
            - Percentage completed
            - Visual progress bar
            - Current iteration / total
            - Elapsed time
            - Estimated time remaining (ETA)
            - Iterations per second (speed)

    The progress bar updates on each iteration and fits within
    the terminal width.
    """
    total = len(lst)
    has_backtracked = False
    start_time = time.time()

    terminal_width = shutil.get_terminal_size().columns

    meta_width = 28 # Fixed, corresponds to the size of static
    max_len = len(f"{total}")
    progress_bar_width = max(10, terminal_width - meta_width - max_len * 2)

    for i, item in enumerate(lst, start=1):
        elapsed_time = time.time() - start_time
        speed = i / elapsed_time if elapsed_time > 0 else 0
        eta = (total - i) / speed if speed > 0 else 0

        elapsed_fmt = format_time(elapsed_time)
        eta_fmt = format_time(eta)

        actual_width = progress_bar_width - len(f"{speed:.2f}")
        progress_ratio = i / total
        progress = int(progress_ratio * actual_width)
        progress_bar = f"|{'█' * progress:<{actual_width}}|"
        percent = f"{int(progress_ratio * 100):03}%"
        iter_info = f"{i:0{max_len}}/{total:0{max_len}}"
        time_info = f"[{elapsed_fmt}<{eta_fmt}, {speed:{int(terminal_width - meta_width - progress_bar_width - max_len * 2) + len(f"{speed:.2f}")}.2f}it/s]"
        line = f"{percent}{progress_bar} {iter_info} {time_info}"
        print(f"\r{line.ljust(terminal_width)}", end="", flush=True)

        yield item

    print()  # for newline after completion
