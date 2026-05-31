import ast


def validate_python(code: str):

    try:

        ast.parse(code)

        return True, None

    except SyntaxError as e:

        return False, str(e)