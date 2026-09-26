def update_pr_main():
    parser = argparse.ArgumentParser(
        description='Build package.',
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--pr-number', '-p',
                        dest='pr_number', type=int, required=True,
                        help='PR number')
    parser.add_argument('--repo', '-r',
                        dest='repo_id', default="Azure/azure-sdk-for-python",
                        help='Repo id. [default: %(default)s]')
    parser.add_argument("-v", "--verbose",
                        dest="verbose", action="store_true",
                        help="Verbosity in INFO mode")
    parser.add_argument("--debug",
                        dest="debug", action="store_true",
                        help="Verbosity in DEBUG mode")
    args = parser.parse_args()
    main_logger = logging.getLogger()
    if args.verbose or args.debug:
        logging.basicConfig()
        main_logger.setLevel(logging.DEBUG if args.debug else logging.INFO)
    update_pr(
        os.environ.get("GH_TOKEN", None),
        args.repo_id,
        int(args.pr_number),
    )