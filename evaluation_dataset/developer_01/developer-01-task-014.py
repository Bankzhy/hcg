def login(*args, **kwargs):
    if args and args[0].api_key:
        solvebio.login(api_key=args[0].api_key)
    elif kwargs:
        solvebio.login(**kwargs)
    else:
        interactive_login()
    user = client.whoami()
    if user:
        print_user(user)
        save_credentials(user['email'].lower(), solvebio.api_key)
        _print_msg('Updated local credentials.')
        return True
    else:
        _print_msg('Invalid credentials. You may not be logged-in.')
        return False