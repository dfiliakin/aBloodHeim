import functools


def cached(private_name=None, recalculate_always=False, recalculate_on_none=False):

    def decorator(func):

        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            prop_name = (
                func.__name__
            )  # this is the name of class attribute being decorated

            # nested functions can not modify nested variables.
            _private_name = (
                private_name
                if private_name and private_name != prop_name
                else "_" + prop_name
            )

            # The attribute
            #       - is recalculate always
            #       - or has not been generated before
            #       - or was set to None and requires recalculation
            if (
                recalculate_always
                or not hasattr(self, _private_name)
                or (not getattr(self, _private_name) and recalculate_on_none)
            ):
                computed_result = func(self, *args, **kwargs)
                setattr(self, _private_name, computed_result)
                return computed_result

            return getattr(self, _private_name)

        return wrapper

    return decorator
