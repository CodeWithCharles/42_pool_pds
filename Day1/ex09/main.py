import os
from tqdm import tqdm
import sys


def build(verb: bool):
    """Runs python3 setup.py sdist bdist_wheel

    Args:
        verb (bool): Should it be verbose
    """
    with tqdm(total=100, desc="Build  ") as pbar:
        os.system(f"python3 setup.py sdist bdist_wheel\
                  {" > /dev/null 2>&1" if not verb else ""}")
        pbar.update(100)
    print()


def install(verb: bool):
    """Runs pip3 install ./dist/ft_package-0.0.1.tar.gz

    Args:
        verb (bool): Should it be verbose
    """
    with tqdm(total=100, desc="Install") as pbar:
        os.system(f"pip3 install ./dist/ft_package-0.0.1.tar.gz\
            {"> /dev/null 2>&1" if not verb else ""}")
        pbar.update(100)
    print()


def show(verb: bool):
    """Runs pip3 show -v ft_package

    Args:
        verb (bool): Should the function be ran or not
    """
    if (verb):
        with tqdm(total=100, desc="Display") as pbar:
            pbar.update(100)
        print()
        os.system("pip3 show -v ft_package")
        print()


def test(verb: bool):
    """Runs python3 tester.py

    Args:
        verb (bool): Should it be verbose
    """
    print("-------------- TESTS --------------")
    os.system("python3 tester.py")


def uninstall(verb: bool):
    """Cleans the artifacts generate by build and uninstall package

    Args:
        verb (bool): Should it be verbose
    """
    os.system("rm -rf build")
    os.system("rm -rf dist")
    os.system("rm -rf ft_package.egg-info")
    os.system("rm -rf ft_package/__pycache__")
    os.system("pip3 uninstall ft_package")


def full_install(verb: bool):
    """Build, install and show the package

    Args:
        verb (bool): Should it be verbose
    """
    build(verb)
    install(verb)
    show(verb)


def full_run(verb: bool):
    """Full_install and run tests

    Args:
        verb (bool): Should it be verbose
    """
    full_install(verb)
    test(verb)


def re(verb: bool):
    """Uninstall then full_install

    Args:
        verb (bool): Should it be verbose
    """
    uninstall(verb)
    full_install(verb)


def re_test(verb: bool):
    """Uninstall, full_install then run tests

    Args:
        verb (bool): Should it be verbose
    """
    re(verb)
    test(verb)


def main():
    """Usage: main.py <func> [-v, --verbose]
    Func list :
    build, install, show, test, uninstall, full_install, full_run, re, re_test

    Raises:
        AssertionError: If less than 2 args or arg[1] not in callable
        AssertionError: If 3 args and arg[2] not -v or --verbose
    """
    callable_func = {
        "build": build,
        "install": install,
        "show": show,
        "test": test,
        "uninstall": uninstall,
        "full_install": full_install,
        "full_run": full_run,
        "re": re,
        "re_test": re_test
    }
    try:
        verbose_mode = False
        if (len(sys.argv) < 2 or sys.argv[1] not in callable_func):
            raise AssertionError("Usage: main.py <func> [-v, --verbose]")
        if (len(sys.argv) == 3 and sys.argv[2] not in ["-v", "--verbose"]):
            raise AssertionError("Usage: main.py <func> [-v, --verbose]")
        if (len(sys.argv) == 3 or sys.argv[1] == 'show'):
            verbose_mode = True
        callable_func[sys.argv[1]](verbose_mode)

    except Exception as e:
        print(f"{Exception.__name__}: {e}")


if __name__ == "__main__":
    main()
