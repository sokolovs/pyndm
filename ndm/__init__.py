# -*- coding: utf-8 -*-
import inspect
import pkgutil

from ndm.transport import AbstractTransport


# Load all transport classes from submodules
__all__ = ['ALL_TRANSPORT', 'ALL_TRANSPORT_CLS']
ALL_TRANSPORT = dict()      # dict of all possible transport
ALL_TRANSPORT_CLS = dict()  # dict of all possible transport classes
for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)
    for name, value in inspect.getmembers(module):
        if name == 'AbstractTransport':
            continue
        if inspect.isclass(value) and issubclass(value, AbstractTransport):
            globals()[name] = value
            __all__.append(name)
            tname = getattr(value, 'name') or name
            ALL_TRANSPORT[name] = tname
            ALL_TRANSPORT_CLS[name] = value
