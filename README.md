# optionaldict

[![Build Status](https://travis-ci.org/messense/optionaldict.svg)](https://travis-ci.org/messense/optionaldict)
[![Build status](https://ci.appveyor.com/api/projects/status/qkj8q2cuitihj2dx/branch/master?svg=true)](https://ci.appveyor.com/project/messense/optionaldict/branch/master)
[![Coverage Status](https://coveralls.io/repos/messense/optionaldict/badge.svg)](https://coveralls.io/r/messense/optionaldict)

``optionaldict`` is a dict-like object that ignore NoneType values for Python which is pickable and JSON serializable.

# Installation

You can install ``optionaldict`` simply using ``pip``:
```bash
pip install optionaldict
```

# Usage
``optionaldict``'s usage is very simple, you will import it by:

```python
from optionaldict import optionaldict
```

or if you prefer the CamelCasing style naming, you can import it by:

```python
from optionaldict import OptionalDict
```

> Tips: In fact, ``optionaldict`` is just an alias for ``OptionalDict``.

Then you can use it just like the built-in ``dict``:

```python
d1 = optionaldict(a=1, b=None)
d1['c'] = 2
d1.setdefault('d', None)

d2 = optionaldict()
d2['a'] = 1
d2['b'] = None

d3 = optionaldict({
    'a': 1,
    'b': None
})
```
