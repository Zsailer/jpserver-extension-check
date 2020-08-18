import argparse

from jupyter_server.serverapp import ServerApp


success_msg = lambda name: """\n
Congratulations!

The server extension, {}, was successfully found and linked!
""".format(name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('extension_name')
    args = parser.parse_args()

    extension_name = args.extension_name

    app = ServerApp.instance(
        # Set the log level to debug for testing purposes
        port_retries=0,
        open_browser=False,
    )
    app.initialize(argv=[])
    extensions = app.extension_manager.extensions

    # Verify that the extension was found.
    assert extension_name in extensions

    # Verify that the extension is loaded and linked
    assert extension_name in app.extension_manager.linked_extensions

    # Print the success message.
    print(success_msg(extension_name))