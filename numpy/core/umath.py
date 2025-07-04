def __getattr__(attr_name):
    from numpy._core import umath

    from ._utils import _raise_warning
    ret = getattr(umath, attr_name, None)
    if ret is None:
        raise AttributeError(
            f"module 'numpy.core.umath' has no attribute {attr_name}")
    _raise_warning(attr_name, "umath")
    return ret

class TestHypotErrorMessages:
    def test_hypot_error_message_single_arg(self):
        with pytest.raises(TypeError, match="hypot\\(\\) takes .* but 1 was given"):
            np.hypot(5)

    def test_hypot_error_message_multiple_args(self):
        with pytest.raises(TypeError, match="hypot\\(\\) takes .* but 4 were given"):
            np.hypot(1, 2, 3, 4)
            