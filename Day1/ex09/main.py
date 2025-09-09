import os
from tqdm import tqdm
import sys


def build(verb: bool):
    with tqdm(total=100, desc="Build  ") as pbar:
        os.system(f"python3 setup.py sdist bdist_wheel\
                  {" > /dev/null 2>&1" if not verb else ""}")
        pbar.update(100)
    print()


def install(verb: bool):
    with tqdm(total=100, desc="Install") as pbar:
        os.system(f"pip3 install ./dist/ft_package-0.0.1.tar.gz\
            {"> /dev/null 2>&1" if not verb else ""}")
        pbar.update(100)
    print()


def show(verb: bool):
    if (verb):
        with tqdm(total=100, desc="Display") as pbar:
            pbar.update(100)
        print()
        os.system("pip3 show -v ft_package")
        print()


def test(verb: bool):
    print("-------------- TESTS --------------")
    os.system("python3 tester.py")


def uninstall(verb: bool):
    os.system("rm -rf build")
    os.system("rm -rf dist")
    os.system("rm -rf ft_package.egg-info")
    os.system("rm -rf ft_package/__pycache__")
    os.system("pip3 uninstall ft_package")


def full_install(verb: bool):
    build(verb)
    install(verb)
    show(verb)


def full_run(verb: bool):
    full_install(verb)
    test(verb)


def re(verb: bool):
    uninstall(verb)
    full_install(verb)


def re_test(verb: bool):
    re(verb)
    test(verb)


def main():
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
        if (len(sys.argv) == 3):
            verbose_mode = True
        callable_func[sys.argv[1]](verbose_mode)

    except Exception as e:
        print(f"{Exception.__name__}: {e}")


if __name__ == "__main__":
    main()
