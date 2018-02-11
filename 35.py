import sys

def test_is_python_35():
    major = sys.version_info.major
    minor = sys.version_info.minor
    if major == 3:
        pass
    else:
        print("You are running Python {}, but we need Python {}.".format(major, 3))
        print("Download and install the Anaconda distribution for Python 3.")
        print("Stopping here.")
        #
        # Let's stop here
        sys.exit(1)
        return None
        # assert major == 3, "Stopping here - we need Python 3."

    if minor >= 5:
        print("Testing Python version-> py{}.{} OK".format(major, minor))
    else:
        print("Warning: You should be running Python 3.5 or newer, " +
              "you have Python {}.{}.".format(major, minor))

if __name__ == "__main__":

    print("Running using Python {}".format(sys.version))
    test_is_python_35()