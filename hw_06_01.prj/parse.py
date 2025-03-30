
def parse_input(user_input):
    if user_input:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    return ""
