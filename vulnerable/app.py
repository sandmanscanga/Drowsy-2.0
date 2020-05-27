"""Module used to run the vulnerable server"""
from server.main import create_server


def main(db_size=250, port=5000):
    """Creates an instance of and run the application

    Instantiates a blueprint object from the vulnerable server application
    using the specified number of users, then runs the application listening
    for all connections on port 5000 by default.

    Args:
        db_size (int): the total number of users to load in the database
        port (int): the port number to listen for connections on

    """
    app = create_server(db_size)
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s", "--size", dest="db_size",
        type=int, default=250, required=False,
        help="specify total rows to use in the database"
    )
    args = parser.parse_args()

    main(db_size=args.db_size)
