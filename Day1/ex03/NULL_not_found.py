def NULL_not_found(object: any) -> int:
    try:
        desc = f"{object} {type(object)}"
        if object is None:
            print(f"Nothing: {desc}")
        elif (isinstance(object, float) and object != object):
            print(f"Cheese: {desc}")
        elif (object == 0 and isinstance(object, int)):
            print(f"Zero: {desc}")
        elif (object == '' and isinstance(object, str)):
            print(f"Empty: {desc}")
        elif (object is False and isinstance(object, bool)):
            print(f"Fake: {desc}")
        else:
            raise Exception("Type not Found")
        return 0
    except Exception as e:
        print(e)
        return 1
