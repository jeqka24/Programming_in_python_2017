import functools
import json

def to_json(func):
    @functools.wraps(func)
    def wrapped(*argc, **kwarg):
        res = func(*argc, **kwarg)
        return json.dumps(res, ensure_ascii=False)
    return wrapped

if (__name__ == "__main__"):
    @to_json
    def test():
        return {"meaning":42}
    print(test())