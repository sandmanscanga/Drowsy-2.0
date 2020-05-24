from server.main import create_server


def main(db_size=250):
    app = create_server(db_size)
    app.run(host="0.0.0.0")


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
