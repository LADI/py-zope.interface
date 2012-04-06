##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Basic components support
"""
import sys
import types

if sys.version_info[0] < 3: #pragma NO COVER

    def _u(s):
        return unicode(s, 'unicode_escape')

    def _normalize_name(name):
        if isinstance(name, basestring):
            return unicode(name)
        raise TypeError("name must be a regular or unicode string")

    CLASS_TYPES = (type, types.ClassType)
    STRING_TYPES = (basestring,)

    _FUNC_DEFAULTS = 'func_defaults'
    _FUNC_CODE = 'func_code'
    _IM_SELF = 'im_self'
    _IM_FUNC = 'im_func'
    _BUILTINS = '__builtin__'

    PYTHON3 = False
    PYTHON2 = True

else: #pragma NO COVER

    def _u(s):
        return s

    def _normalize_name(name):
        if isinstance(name, bytes):
            name = str(name, 'ascii')
        if isinstance(name, str):
            return name
        raise TypeError("name must be a string or ASCII-only bytes")

    CLASS_TYPES = (type,)
    STRING_TYPES = (str,)

    _FUNC_DEFAULTS = '__defaults__'
    _FUNC_CODE = '__code__'
    _IM_SELF = '__self__'
    _IM_FUNC = '__func__'
    _BUILTINS = 'builtins'

    PYTHON3 = True
    PYTHON2 = False

def _skip_under_py3k(test_method): #pragma NO COVER
    if sys.version_info[0] < 3:
        return test_method
    def _dummy(*args):
        pass
    return _dummy

def _skip_under_py2(test_method): #pragma NO COVER
    if sys.version_info[0] > 2:
        return test_method
    def _dummy(*args):
        pass
    return _dummy
