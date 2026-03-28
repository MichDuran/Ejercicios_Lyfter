def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            # The underscore (_) acts as a wildcard/default case
            return "Something's wrong with the Internet"

print(http_error(404))
print(http_error(500))
