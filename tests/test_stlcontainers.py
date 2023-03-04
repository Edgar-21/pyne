"""Tests the part of stlconverters that is accessible from Python."""
###################
###  WARNING!!! ###
###################
# This file has been autogenerated
from __future__ import print_function
from unittest import TestCase
import pytest

from numpy.testing import assert_array_equal, assert_array_almost_equal

import os
import numpy as np

try:
    from collections.abc import Container, Mapping
except ImportError:
    from collections import Container, Mapping

from pyne import stlcontainers


# SetStr
def test_set_str():
    s = stlcontainers.SetStr()
    s.add("Aha")
    assert "Aha" in s
    assert "Me" not in s

    s = stlcontainers.SetStr(["Aha", "Take", "Me"])
    assert "Take" in s
    assert "On" not in s


# SetInt
def test_set_int():
    s = stlcontainers.SetInt()
    s.add(1)
    assert 1 in s
    assert -65 not in s

    s = stlcontainers.SetInt([1, 42, -65])
    assert 42 in s
    assert 18 not in s


# MapStrStr
def test_map_str_str():
    m = stlcontainers.MapStrStr()
    uismap = isinstance("Me", Mapping)
    m["Aha"] = "On"
    m["Take"] = "Me"
    import pprint

    pprint.pprint(m)
    assert len(m) == 2
    if uismap:
        for key, value in m["Take"].items():
            print(key, value, "Me"[key])
            if isinstance(value, np.ndarray):
                assert value == "Me"[key]
            else:
                assert value == "Me"[key]
    else:
        assert m["Take"] == "Me"

    m = stlcontainers.MapStrStr({"Me": "Take", "On": "Aha"})
    assert len(m) == 2
    if uismap:
        for key, value in m["Me"].items():
            if isinstance(value, np.ndarray):
                print(key, value, "Take"[key])
                assert value == "Take"[key]
            else:
                assert value == "Take"[key]
    else:
        assert m["Me"] == "Take"

    n = stlcontainers.MapStrStr(m, False)
    assert len(n) == 2
    if uismap:
        for key, value in m["Me"].items():
            if isinstance(value, np.ndarray):
                assert value == "Take"[key]
            else:
                assert value == "Take"[key]
    else:
        assert m["Me"] == "Take"

    # points to the same underlying map
    n["Take"] = "Me"
    if uismap:
        for key, value in m["Take"].items():
            if isinstance(value, np.ndarray):
                assert value == "Me"[key]
            else:
                assert value == "Me"[key]
    else:
        assert m["Take"] == "Me"


# MapStrInt
def test_map_str_int():
    m = stlcontainers.MapStrInt()
    uismap = isinstance(-65, Mapping)
    m["Aha"] = 18
    m["Take"] = -65
    import pprint

    pprint.pprint(m)
    assert len(m) == 2
    if uismap:
        for key, value in m["Take"].items():
            print(key, value, -65[key])
            if isinstance(value, np.ndarray):
                assert value == pytest.approx(-65[key])
            else:
                assert value == -65[key]
    else:
        assert m["Take"] == pytest.approx(-65)

    m = stlcontainers.MapStrInt({"Me": 42, "On": 1})
    assert len(m) == 2
    if uismap:
        for key, value in m["Me"].items():
            if isinstance(value, np.ndarray):
                print(key, value, 42[key])
                assert value == pytest.approx(42[key])
            else:
                assert value == 42[key]
    else:
        assert m["Me"] == pytest.approx(42)

    n = stlcontainers.MapStrInt(m, False)
    assert len(n) == 2
    if uismap:
        for key, value in m["Me"].items():
            if isinstance(value, np.ndarray):
                assert value  == pytest.approx(42[key])
            else:
                assert value == 42[key]
    else:
        assert m["Me"] == pytest.approx(42)

    # points to the same underlying map
    n["Take"] = -65
    if uismap:
        for key, value in m["Take"].items():
            if isinstance(value, np.ndarray):
                assert value == pytest.approx(-65[key])
            else:
                assert value == -65[key]
    else:
        assert m["Take"] == pytest.approx(-65)


# MapIntStr
def test_map_int_str():
    m = stlcontainers.MapIntStr()
    uismap = isinstance("Me", Mapping)
    m[1] = "On"
    m[42] = "Me"
    import pprint

    pprint.pprint(m)
    assert len(m) == 2
    if uismap:
        for key, value in m[42].items():
            print(key, value, "Me"[key])
            if isinstance(value, np.ndarray):
                assert value == "Me"[key]
            else:
                assert value == "Me"[key]
    else:
        assert m[42] == "Me"

    m = stlcontainers.MapIntStr({-65: "Take", 18: "Aha"})
    assert len(m) == 2
    if uismap:
        for key, value in m[-65].items():
            if isinstance(value, np.ndarray):
                print(key, value, "Take"[key])
                assert value == "Take"[key]
            else:
                assert value == "Take"[key]
    else:
        assert m[-65] == "Take"

    n = stlcontainers.MapIntStr(m, False)
    assert len(n) == 2
    if uismap:
        for key, value in m[-65].items():
            if isinstance(value, np.ndarray):
                assert value == "Take"[key]
            else:
                assert value == "Take"[key]
    else:
        assert m[-65] == "Take"

    # points to the same underlying map
    n[42] = "Me"
    if uismap:
        for key, value in m[42].items():
            if isinstance(value, np.ndarray):
                assert value == "Me"[key]
            else:
                assert value == "Me"[key]
    else:
        assert m[42] == "Me"


# MapStrUInt
def test_map_str_uint():
    m = stlcontainers.MapStrUInt()
    uismap = isinstance(4294967295, Mapping)
    m["Aha"] = 42
    m["Take"] = 4294967295
    import pprint

    pprint.pprint(m)
    assert len(m) == 2
    if uismap:
        for key, value in m["Take"].items():
            print(key, value, 4294967295[key])
            if isinstance(value, np.ndarray):
                assert value == pytest.approx(4294967295[key])
            else:
                assert value == 4294967295[key]
    else:
        assert m["Take"] == pytest.approx(4294967295)

    m = stlcontainers.MapStrUInt({"Me": 65, "On": 1})
    assert len(m) == 2
    if uismap:
        for key, value in m["Me"].items():
            if isinstance(value, np.ndarray):
                print(key, value, 65[key])
                assert value == pytest.approx(65[key])
            else:
                assert value == 65[key]
    else:
        assert m["Me"] == pytest.approx(65)

    n = stlcontainers.MapStrUInt(m, False)
    assert len(n) == 2
    if uismap:
        for key, value in m["Me"].items():
            if isinstance(value, np.ndarray):
                assert value == pytest.approx(65[key])
            else:
                assert value == 65[key]
    else:
        assert m["Me"] == pytest.approx(65)

    # points to the same underlying map
    n["Take"] = 4294967295
    if uismap:
        for key, value in m["Take"].items():
            if isinstance(value, np.ndarray):
                assert value == pytest.approx(4294967295[key])
            else:
                assert value == 4294967295[key]
    else:
        assert m["Take"] == pytest.approx(4294967295)


# MapUIntStr
def test_map_uint_str():
    m = stlcontainers.MapUIntStr()
    uismap = isinstance("Me", Mapping)
    m[1] = "On"
    m[65] = "Me"
    import pprint

    pprint.pprint(m)
    assert len(m) == 2
    if uismap:
        for key, value in m[65].items():
            print(key, value, "Me"[key])
            if isinstance(value, np.ndarray):
                assert value == "Me"[key]
            else:
                assert value == "Me"[key]
    else:
        assert m[65] == "Me"

    m = stlcontainers.MapUIntStr({4294967295: "Take", 42: "Aha"})
    assert len(m) == 2
    if uismap:
        for key, value in m[4294967295].items():
            if isinstance(value, np.ndarray):
                print(key, value, "Take"[key])
                assert value == "Take"[key]
            else:
                assert value == "Take"[key]
    else:
        assert m[4294967295] == "Take"

    n = stlcontainers.MapUIntStr(m, False)
    assert len(n) == 2
    if uismap:
        for key, value in m[4294967295].items():
            if isinstance(value, np.ndarray):
                assert value == "Take"[key]
            else:
                assert value == "Take"[key]
    else:
        assert m[4294967295] == "Take"

    # points to the same underlying map
    n[65] = "Me"
    if uismap:
        for key, value in m[65].items():
            if isinstance(value, np.ndarray):
                assert value == "Me"[key]
            else:
                assert value == "Me"[key]
    else:
        assert m[65] == "Me"


# MapStrDouble
def test_map_str_double():
    m = stlcontainers.MapStrDouble()
    uismap = isinstance(-65.5555, Mapping)
    m["Aha"] = 18
    m["Take"] = -65.5555
    import pprint

    pprint.pprint(m)
    assert len(m) == 2
    if uismap:
        for key, value in m["Take"].items():
            print(key, value, -65.5555[key])
            if isinstance(value, np.ndarray):
                assert value == pytest.approx(-65.5555[key])
            else:
                assert value == -65.5555[key]
    else:
        assert m["Take"] == pytest.approx(-65.5555)

    m = stlcontainers.MapStrDouble({"Me": 42.42, "On": 1.0})
    assert len(m) == 2
    if uismap:
        for key, value in m["Me"].items():
            if isinstance(value, np.ndarray):
                print(key, value, 42.42[key])
                assert value == pytest.approx(42.42[key])
            else:
                assert value == 42.42[key]
    else:
        assert m["Me"] == pytest.approx(42.42)

    n = stlcontainers.MapStrDouble(m, False)
    assert len(n) == 2
    if uismap:
        for key, value in m["Me"].items():
            if isinstance(value, np.ndarray):
                assert value == pytest.approx(42.42[key])
            else:
                assert value == 42.42[key]
    else:
        assert m["Me"] == pytest.approx(42.42)

    # points to the same underlying map
    n["Take"] = -65.5555
    if uismap:
        for key, value in m["Take"].items():
            if isinstance(value, np.ndarray):
                assert value == pytest.approx(-65.5555[key])
            else:
                assert value == -65.5555[key]
    else:
        assert m["Take"] == pytest.approx(-65.5555)


# MapUIntUInt
def test_map_uint_uint():
    m = stlcontainers.MapUIntUInt()
    uismap = isinstance(4294967295, Mapping)
    m[1] = 42
    m[65] = 4294967295
    import pprint

    pprint.pprint(m)
    assert len(m) == 2
    if uismap:
        for key, value in m[65].items():
            print(key, value, 4294967295[key])
            if isinstance(value, np.ndarray):
                assert value == pytest.approx(4294967295[key])
            else:
                assert value == 4294967295[key]
    else:
        assert m[65] == pytest.approx(4294967295)

    m = stlcontainers.MapUIntUInt({4294967295: 65, 42: 1})
    assert len(m) == 2
    if uismap:
        for key, value in m[4294967295].items():
            if isinstance(value, np.ndarray):
                print(key, value, 65[key])
                assert value == pytest.approx(65[key])
            else:
                assert value == 65[key]
    else:
        assert m[4294967295] == pytest.approx(65)

    n = stlcontainers.MapUIntUInt(m, False)
    assert len(n) == 2
    if uismap:
        for key, value in m[4294967295].items():
            if isinstance(value, np.ndarray):
                assert value == pytest.approx(65[key])
            else:
                assert value == 65[key]
    else:
        assert m[4294967295] == pytest.approx(65)

    # points to the same underlying map
    n[65] = 4294967295
    if uismap:
        for key, value in m[65].items():
            if isinstance(value, np.ndarray):
                assert value == pytest.approx(4294967295[key])
            else:
                assert value == 4294967295[key]
    else:
        assert m[65] == pytest.approx(4294967295)


# MapIntInt
def test_map_int_int():
    m = stlcontainers.MapIntInt()
    uismap = isinstance(-65, Mapping)
    m[1] = 18
    m[42] = -65
    import pprint

    pprint.pprint(m)
    assert len(m) == 2
    if uismap:
        for key, value in m[42].items():
            print(key, value, -65[key])
            if isinstance(value, np.ndarray):
                assert value == pytest.approx(-65[key])
            else:
                assert value == -65[key]
    else:
        assert m[42] == pytest.approx(-65)

    m = stlcontainers.MapIntInt({-65: 42, 18: 1})
    assert len(m) == 2
    if uismap:
        for key, value in m[-65].items():
            if isinstance(value, np.ndarray):
                print(key, value, 42[key])
                assert value == pytest.approx(42[key])
            else:
                assert value == 42[key]
    else:
        assert m[-65] == pytest.approx(42)

    n = stlcontainers.MapIntInt(m, False)
    assert len(n) == 2
    if uismap:
        for key, value in m[-65].items():
            if isinstance(value, np.ndarray):
                assert value == pytest.approx(42[key])
            else:
                assert value == 42[key]
    else:
        assert m[-65] == pytest.approx(42)

    # points to the same underlying map
    n[42] = -65
    if uismap:
        for key, value in m[42].items():
            if isinstance(value, np.ndarray):
                assert value == pytest.approx(-65[key])
            else:
                assert value == -65[key]
    else:
        assert m[42] == pytest.approx(-65)


# MapIntDouble
def test_map_int_double():
    m = stlcontainers.MapIntDouble()
    uismap = isinstance(-65.5555, Mapping)
    m[1] = 18
    m[42] = -65.5555
    import pprint

    pprint.pprint(m)
    assert len(m) == 2
    if uismap:
        for key, value in m[42].items():
            print(key, value, -65.5555[key])
            if isinstance(value, np.ndarray):
                assert value == pytest.approx(-65.5555[key])
            else:
                assert value == -65.5555[key]
    else:
        assert m[42] == pytest.approx(-65.5555)

    m = stlcontainers.MapIntDouble({-65: 42.42, 18: 1.0})
    assert len(m) == 2
    if uismap:
        for key, value in m[-65].items():
            if isinstance(value, np.ndarray):
                print(key, value, 42.42[key])
                assert value == pytest.approx(42.42[key])
            else:
                assert value == 42.42[key]
    else:
        assert m[-65] == pytest.approx(42.42)

    n = stlcontainers.MapIntDouble(m, False)
    assert len(n) == 2
    if uismap:
        for key, value in m[-65].items():
            if isinstance(value, np.ndarray):
                assert value == pytest.approx(42.42[key])
            else:
                assert value == 42.42[key]
    else:
        assert m[-65] == pytest.approx(42.42)

    # points to the same underlying map
    n[42] = -65.5555
    if uismap:
        for key, value in m[42].items():
            if isinstance(value, np.ndarray):
                assert value == pytest.approx(-65.5555[key])
            else:
                assert value == -65.5555[key]
    else:
        assert m[42] == pytest.approx(-65.5555)


# MapIntComplex
def test_map_int_complex():
    m = stlcontainers.MapIntComplex()
    uismap = isinstance((-65.55 - 1j), Mapping)
    m[1] = 0.18j
    m[42] = -65.55 - 1j
    import pprint

    pprint.pprint(m)
    assert len(m) == 2
    if uismap:
        for key, value in m[42].items():
            print(key, value, (-65.55 - 1j)[key])
            if isinstance(value, np.ndarray):
                assert value == pytest.approx((-65.55 - 1j)[key])
            else:
                assert value == (-65.55 - 1j)[key]
    else:
        assert m[42] == pytest.approx((-65.55 - 1j))

    m = stlcontainers.MapIntComplex({-65: (42 + 42j), 18: 1.0})
    assert len(m) == 2
    if uismap:
        for key, value in m[-65].items():
            if isinstance(value, np.ndarray):
                print(key, value, (42 + 42j)[key])
                assert value == pytest.approx((42 + 42j)[key])
            else:
                assert value == (42 + 42j)[key]
    else:
        assert m[-65] == pytest.approx((42 + 42j))

    n = stlcontainers.MapIntComplex(m, False)
    assert len(n) == 2
    if uismap:
        for key, value in m[-65].items():
            if isinstance(value, np.ndarray):
                assert value == pytest.approx((42 + 42j)[key])
            else:
                assert value == (42 + 42j)[key]
    else:
        assert m[-65] == pytest.approx((42 + 42j))

    # points to the same underlying map
    n[42] = -65.55 - 1j
    if uismap:
        for key, value in m[42].items():
            if isinstance(value, np.ndarray):
                assert value == pytest.approx((-65.55 - 1j)[key])
            else:
                assert value == (-65.55 - 1j)[key]
    else:
        assert m[42] == pytest.approx((-65.55 - 1j))


# MapUIntDouble
def test_map_uint_double():
    m = stlcontainers.MapUIntDouble()
    uismap = isinstance(-65.5555, Mapping)
    m[1] = 18
    m[65] = -65.5555
    import pprint

    pprint.pprint(m)
    assert len(m) == 2
    if uismap:
        for key, value in m[65].items():
            print(key, value, -65.5555[key])
            if isinstance(value, np.ndarray):
                assert value == pytest.approx(-65.5555[key])
            else:
                assert value == -65.5555[key]
    else:
        assert m[65] == pytest.approx(-65.5555)

    m = stlcontainers.MapUIntDouble({4294967295: 42.42, 42: 1.0})
    assert len(m) == 2
    if uismap:
        for key, value in m[4294967295].items():
            if isinstance(value, np.ndarray):
                print(key, value, 42.42[key])
                assert value == pytest.approx(42.42[key])
            else:
                assert value == 42.42[key]
    else:
        assert m[4294967295] == pytest.approx(42.42)

    n = stlcontainers.MapUIntDouble(m, False)
    assert len(n) == 2
    if uismap:
        for key, value in m[4294967295].items():
            if isinstance(value, np.ndarray):
                assert value == pytest.approx(42.42[key])
            else:
                assert value == 42.42[key]
    else:
        assert m[4294967295] == pytest.approx(42.42)

    # points to the same underlying map
    n[65] = -65.5555
    if uismap:
        for key, value in m[65].items():
            if isinstance(value, np.ndarray):
                assert value == pytest.approx(-65.5555[key])
            else:
                assert value == -65.5555[key]
    else:
        assert m[65] == pytest.approx(-65.5555)


# MapStrVectorDouble
def test_map_str_vector_double():
    m = stlcontainers.MapStrVectorDouble()
    uismap = isinstance([1.0, -65.5555, 1.0, -65.5555], Mapping)
    m["Aha"] = [42.42, 18, 42.42, 18]
    m["Take"] = [1.0, -65.5555, 1.0, -65.5555]
    assert len(m) == 2
    if uismap:
        for key, value in m["Take"].items():
            print(key, value, [1.0, -65.5555, 1.0, -65.5555][key])
            if isinstance(value, np.ndarray):
                assert_array_almost_equal(value, [1.0, -65.5555, 1.0, -65.5555][key])
            else:
                assert value == [1.0, -65.5555, 1.0, -65.5555][key]
    else:
        assert_array_almost_equal(m["Take"], [1.0, -65.5555, 1.0, -65.5555])

    m = stlcontainers.MapStrVectorDouble(
        {"Me": [18, -65.5555, 42.42, 1.0], "On": [1.0, 42.42, -65.5555, 18]}
    )
    assert len(m) == 2
    if uismap:
        for key, value in m["Me"].items():
            if isinstance(value, np.ndarray):
                print(key, value, [18, -65.5555, 42.42, 1.0][key])
                assert_array_almost_equal(value, [18, -65.5555, 42.42, 1.0][key])
            else:
                assert value == [18, -65.5555, 42.42, 1.0][key]
    else:
        assert_array_almost_equal(m["Me"], [18, -65.5555, 42.42, 1.0])

    n = stlcontainers.MapStrVectorDouble(m, False)
    assert len(n) == 2
    if uismap:
        for key, value in m["Me"].items():
            if isinstance(value, np.ndarray):
                assert_array_almost_equal(value, [18, -65.5555, 42.42, 1.0][key])
            else:
                assert value == [18, -65.5555, 42.42, 1.0][key]
    else:
        assert_array_almost_equal(m["Me"], [18, -65.5555, 42.42, 1.0])

    # points to the same underlying map
    n["Take"] = [1.0, -65.5555, 1.0, -65.5555]
    if uismap:
        for key, value in m["Take"].items():
            if isinstance(value, np.ndarray):
                assert_array_almost_equal(value, [1.0, -65.5555, 1.0, -65.5555][key])
            else:
                assert value == [1.0, -65.5555, 1.0, -65.5555][key]
    else:
        assert_array_almost_equal(m["Take"], [1.0, -65.5555, 1.0, -65.5555])


# MapIntVectorDouble
def test_map_int_vector_double():
    m = stlcontainers.MapIntVectorDouble()
    uismap = isinstance([1.0, -65.5555, 1.0, -65.5555], Mapping)
    m[1] = [42.42, 18, 42.42, 18]
    m[42] = [1.0, -65.5555, 1.0, -65.5555]
    assert len(m) == 2
    if uismap:
        for key, value in m[42].items():
            print(key, value, [1.0, -65.5555, 1.0, -65.5555][key])
            if isinstance(value, np.ndarray):
                assert_array_almost_equal(value, [1.0, -65.5555, 1.0, -65.5555][key])
            else:
                assert value == [1.0, -65.5555, 1.0, -65.5555][key]
    else:
        assert_array_almost_equal(m[42], [1.0, -65.5555, 1.0, -65.5555])

    m = stlcontainers.MapIntVectorDouble(
        {-65: [18, -65.5555, 42.42, 1.0], 18: [1.0, 42.42, -65.5555, 18]}
    )
    assert len(m) == 2
    if uismap:
        for key, value in m[-65].items():
            if isinstance(value, np.ndarray):
                print(key, value, [18, -65.5555, 42.42, 1.0][key])
                assert_array_almost_equal(value, [18, -65.5555, 42.42, 1.0][key])
            else:
                assert value == [18, -65.5555, 42.42, 1.0][key]
    else:
        assert_array_almost_equal(m[-65], [18, -65.5555, 42.42, 1.0])

    n = stlcontainers.MapIntVectorDouble(m, False)
    assert len(n) == 2
    if uismap:
        for key, value in m[-65].items():
            if isinstance(value, np.ndarray):
                assert_array_almost_equal(value, [18, -65.5555, 42.42, 1.0][key])
            else:
                assert value == [18, -65.5555, 42.42, 1.0][key]
    else:
        assert_array_almost_equal(m[-65], [18, -65.5555, 42.42, 1.0])

    # points to the same underlying map
    n[42] = [1.0, -65.5555, 1.0, -65.5555]
    if uismap:
        for key, value in m[42].items():
            if isinstance(value, np.ndarray):
                assert_array_almost_equal(value, [1.0, -65.5555, 1.0, -65.5555][key])
            else:
                assert value == [1.0, -65.5555, 1.0, -65.5555][key]
    else:
        assert_array_almost_equal(m[42], [1.0, -65.5555, 1.0, -65.5555])


if __name__ == "__main__":
    nose.run()
