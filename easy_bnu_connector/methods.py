__all__ = ['methods']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['_getbyte', '_ALPHA', '_PADCHAR', 's', '_VERSION', 'xEncode', 'base64_encode', 'l'])
@Js
def PyJsHoisted__getbyte_(s, i, this, arguments, var=var):
    var = Scope({'s':s, 'i':i, 'this':this, 'arguments':arguments}, var)
    var.registers(['x', 's', 'i'])
    var.put('x', var.get('s').callprop('charCodeAt', var.get('i')))
    if (var.get('x')>Js(255.0)):
        PyJsTempException = JsToPyException(Js('INVALID_CHARACTER_ERR: DOM Exception 5'))
        raise PyJsTempException
    return var.get('x')
PyJsHoisted__getbyte_.func_name = '_getbyte'
var.put('_getbyte', PyJsHoisted__getbyte_)
@Js
def PyJsHoisted_base64_encode_(s, this, arguments, var=var):
    var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
    var.registers(['s', 'b10', 'x', 'i', 'imax'])
    if PyJsStrictNeq(var.get('arguments').get('length'),Js(1.0)):
        PyJsTempException = JsToPyException(Js('SyntaxError: exactly one argument required'))
        raise PyJsTempException
    var.put('s', var.get('String')(var.get('s')))
    var.put('x', Js([]))
    var.put('imax', (var.get('s').get('length')-(var.get('s').get('length')%Js(3.0))))
    if PyJsStrictEq(var.get('s').get('length'),Js(0.0)):
        return var.get('s')
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('imax')):
        try:
            var.put('b10', (((var.get('_getbyte')(var.get('s'), var.get('i'))<<Js(16.0))|(var.get('_getbyte')(var.get('s'), (var.get('i')+Js(1.0)))<<Js(8.0)))|var.get('_getbyte')(var.get('s'), (var.get('i')+Js(2.0)))))
            var.get('x').callprop('push', var.get('_ALPHA').callprop('charAt', (var.get('b10')>>Js(18.0))))
            var.get('x').callprop('push', var.get('_ALPHA').callprop('charAt', ((var.get('b10')>>Js(12.0))&Js(63.0))))
            var.get('x').callprop('push', var.get('_ALPHA').callprop('charAt', ((var.get('b10')>>Js(6.0))&Js(63.0))))
            var.get('x').callprop('push', var.get('_ALPHA').callprop('charAt', (var.get('b10')&Js(63.0))))
        finally:
                var.put('i', Js(3.0), '+')
    while 1:
        SWITCHED = False
        CONDITION = ((var.get('s').get('length')-var.get('imax')))
        if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
            SWITCHED = True
            var.put('b10', (var.get('_getbyte')(var.get('s'), var.get('i'))<<Js(16.0)))
            var.get('x').callprop('push', (((var.get('_ALPHA').callprop('charAt', (var.get('b10')>>Js(18.0)))+var.get('_ALPHA').callprop('charAt', ((var.get('b10')>>Js(12.0))&Js(63.0))))+var.get('_PADCHAR'))+var.get('_PADCHAR')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
            SWITCHED = True
            var.put('b10', ((var.get('_getbyte')(var.get('s'), var.get('i'))<<Js(16.0))|(var.get('_getbyte')(var.get('s'), (var.get('i')+Js(1.0)))<<Js(8.0))))
            var.get('x').callprop('push', (((var.get('_ALPHA').callprop('charAt', (var.get('b10')>>Js(18.0)))+var.get('_ALPHA').callprop('charAt', ((var.get('b10')>>Js(12.0))&Js(63.0))))+var.get('_ALPHA').callprop('charAt', ((var.get('b10')>>Js(6.0))&Js(63.0))))+var.get('_PADCHAR')))
            break
        SWITCHED = True
        break
    return var.get('x').callprop('join', Js(''))
PyJsHoisted_base64_encode_.func_name = 'base64_encode'
var.put('base64_encode', PyJsHoisted_base64_encode_)
@Js
def PyJsHoisted_xEncode_(str, key, this, arguments, var=var):
    var = Scope({'str':str, 'key':key, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'str', 'e', 'k', 'p', 'q', 'key', 'y', 'n', 'z', 'v', 'd', 'm'])
    if (var.get('str')==Js('')):
        return Js('')
    var.put('v', var.get('s')(var.get('str'), Js(True)))
    var.put('k', var.get('s')(var.get('key'), Js(False)))
    if (var.get('k').get('length')<Js(4.0)):
        var.get('k').put('length', Js(4.0))
    var.put('n', (var.get('v').get('length')-Js(1.0)))
    var.put('z', var.get('v').get(var.get('n')))
    var.put('y', var.get('v').get('0'))
    var.put('c', (Js(2248228889)|Js(406206880)))
    var.put('q', var.get('Math').callprop('floor', (Js(6.0)+(Js(52.0)/(var.get('n')+Js(1.0))))))
    var.put('d', Js(0.0))
    while (Js(0.0)<(var.put('q',Js(var.get('q').to_number())-Js(1))+Js(1))):
        var.put('d', ((var.get('d')+var.get('c'))&(Js(2363546047)|Js(1931421248))))
        var.put('e', (PyJsBshift(var.get('d'),Js(2.0))&Js(3.0)))
        #for JS loop
        var.put('p', Js(0.0))
        while (var.get('p')<var.get('n')):
            try:
                var.put('y', var.get('v').get((var.get('p')+Js(1.0))))
                var.put('m', (PyJsBshift(var.get('z'),Js(5.0))^(var.get('y')<<Js(2.0))))
                var.put('m', ((PyJsBshift(var.get('y'),Js(3.0))^(var.get('z')<<Js(4.0)))^(var.get('d')^var.get('y'))), '+')
                var.put('m', (var.get('k').get(((var.get('p')&Js(3.0))^var.get('e')))^var.get('z')), '+')
                var.put('z', var.get('v').put(var.get('p'), ((var.get('v').get(var.get('p'))+var.get('m'))&(Js(4021866800)|Js(273100495)))))
            finally:
                    (var.put('p',Js(var.get('p').to_number())+Js(1))-Js(1))
        var.put('y', var.get('v').get('0'))
        var.put('m', (PyJsBshift(var.get('z'),Js(5.0))^(var.get('y')<<Js(2.0))))
        var.put('m', ((PyJsBshift(var.get('y'),Js(3.0))^(var.get('z')<<Js(4.0)))^(var.get('d')^var.get('y'))), '+')
        var.put('m', (var.get('k').get(((var.get('p')&Js(3.0))^var.get('e')))^var.get('z')), '+')
        var.put('z', var.get('v').put(var.get('n'), ((var.get('v').get(var.get('n'))+var.get('m'))&(Js(3141076802)|Js(1153890493)))))
    return var.get('l')(var.get('v'), Js(False))
PyJsHoisted_xEncode_.func_name = 'xEncode'
var.put('xEncode', PyJsHoisted_xEncode_)
@Js
def PyJsHoisted_s_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'c', 'b', 'i', 'v'])
    var.put('c', var.get('a').get('length'))
    var.put('v', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('c')):
        try:
            var.get('v').put((var.get('i')>>Js(2.0)), (((var.get('a').callprop('charCodeAt', var.get('i'))|(var.get('a').callprop('charCodeAt', (var.get('i')+Js(1.0)))<<Js(8.0)))|(var.get('a').callprop('charCodeAt', (var.get('i')+Js(2.0)))<<Js(16.0)))|(var.get('a').callprop('charCodeAt', (var.get('i')+Js(3.0)))<<Js(24.0))))
        finally:
                var.put('i', Js(4.0), '+')
    if var.get('b'):
        var.get('v').put(var.get('v').get('length'), var.get('c'))
    return var.get('v')
PyJsHoisted_s_.func_name = 's'
var.put('s', PyJsHoisted_s_)
@Js
def PyJsHoisted_l_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a', 'b', 'i', 'd', 'm'])
    var.put('d', var.get('a').get('length'))
    var.put('c', ((var.get('d')-Js(1.0))<<Js(2.0)))
    if var.get('b'):
        var.put('m', var.get('a').get((var.get('d')-Js(1.0))))
        if ((var.get('m')<(var.get('c')-Js(3.0))) or (var.get('m')>var.get('c'))):
            return var.get(u"null")
        var.put('c', var.get('m'))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('d')):
        try:
            var.get('a').put(var.get('i'), var.get('String').callprop('fromCharCode', (var.get('a').get(var.get('i'))&Js(255)), (PyJsBshift(var.get('a').get(var.get('i')),Js(8.0))&Js(255)), (PyJsBshift(var.get('a').get(var.get('i')),Js(16.0))&Js(255)), (PyJsBshift(var.get('a').get(var.get('i')),Js(24.0))&Js(255))))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    if var.get('b'):
        return var.get('a').callprop('join', Js('')).callprop('substring', Js(0.0), var.get('c'))
    else:
        return var.get('a').callprop('join', Js(''))
PyJsHoisted_l_.func_name = 'l'
var.put('l', PyJsHoisted_l_)
@Js
def PyJs_anonymous_0_(n, this, arguments, var=var):
    var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['o', 'p', 'h', 'n', 'd', 'l', 'r', 'e', 'g', 'v', 'A', 'f', 'i', 'm', 'c', 'a', 'C', 's', 'u', 't'])
    @Js
    def PyJsHoisted_t_(n, t, this, arguments, var=var):
        var = Scope({'n':n, 't':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'n', 'r'])
        var.put('r', ((Js(65535.0)&var.get('n'))+(Js(65535.0)&var.get('t'))))
        return (((((var.get('n')>>Js(16.0))+(var.get('t')>>Js(16.0)))+(var.get('r')>>Js(16.0)))<<Js(16.0))|(Js(65535.0)&var.get('r')))
    PyJsHoisted_t_.func_name = 't'
    var.put('t', PyJsHoisted_t_)
    @Js
    def PyJsHoisted_r_(n, t, this, arguments, var=var):
        var = Scope({'n':n, 't':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'n'])
        return ((var.get('n')<<var.get('t'))|PyJsBshift(var.get('n'),(Js(32.0)-var.get('t'))))
    PyJsHoisted_r_.func_name = 'r'
    var.put('r', PyJsHoisted_r_)
    @Js
    def PyJsHoisted_e_(n, e, o, u, c, f, this, arguments, var=var):
        var = Scope({'n':n, 'e':e, 'o':o, 'u':u, 'c':c, 'f':f, 'this':this, 'arguments':arguments}, var)
        var.registers(['o', 'c', 'e', 'u', 'f', 'n'])
        return var.get('t')(var.get('r')(var.get('t')(var.get('t')(var.get('e'), var.get('n')), var.get('t')(var.get('u'), var.get('f'))), var.get('c')), var.get('o'))
    PyJsHoisted_e_.func_name = 'e'
    var.put('e', PyJsHoisted_e_)
    @Js
    def PyJsHoisted_o_(n, t, r, o, u, c, f, this, arguments, var=var):
        var = Scope({'n':n, 't':t, 'r':r, 'o':o, 'u':u, 'c':c, 'f':f, 'this':this, 'arguments':arguments}, var)
        var.registers(['o', 'c', 'r', 'u', 'f', 't', 'n'])
        return var.get('e')(((var.get('t')&var.get('r'))|((~var.get('t'))&var.get('o'))), var.get('n'), var.get('t'), var.get('u'), var.get('c'), var.get('f'))
    PyJsHoisted_o_.func_name = 'o'
    var.put('o', PyJsHoisted_o_)
    @Js
    def PyJsHoisted_u_(n, t, r, o, u, c, f, this, arguments, var=var):
        var = Scope({'n':n, 't':t, 'r':r, 'o':o, 'u':u, 'c':c, 'f':f, 'this':this, 'arguments':arguments}, var)
        var.registers(['o', 'c', 'r', 'u', 'f', 't', 'n'])
        return var.get('e')(((var.get('t')&var.get('o'))|(var.get('r')&(~var.get('o')))), var.get('n'), var.get('t'), var.get('u'), var.get('c'), var.get('f'))
    PyJsHoisted_u_.func_name = 'u'
    var.put('u', PyJsHoisted_u_)
    @Js
    def PyJsHoisted_c_(n, t, r, o, u, c, f, this, arguments, var=var):
        var = Scope({'n':n, 't':t, 'r':r, 'o':o, 'u':u, 'c':c, 'f':f, 'this':this, 'arguments':arguments}, var)
        var.registers(['o', 'c', 'r', 'u', 'f', 't', 'n'])
        return var.get('e')(((var.get('t')^var.get('r'))^var.get('o')), var.get('n'), var.get('t'), var.get('u'), var.get('c'), var.get('f'))
    PyJsHoisted_c_.func_name = 'c'
    var.put('c', PyJsHoisted_c_)
    @Js
    def PyJsHoisted_f_(n, t, r, o, u, c, f, this, arguments, var=var):
        var = Scope({'n':n, 't':t, 'r':r, 'o':o, 'u':u, 'c':c, 'f':f, 'this':this, 'arguments':arguments}, var)
        var.registers(['o', 'c', 'r', 'u', 'f', 't', 'n'])
        return var.get('e')((var.get('r')^(var.get('t')|(~var.get('o')))), var.get('n'), var.get('t'), var.get('u'), var.get('c'), var.get('f'))
    PyJsHoisted_f_.func_name = 'f'
    var.put('f', PyJsHoisted_f_)
    @Js
    def PyJsHoisted_i_(n, r, this, arguments, var=var):
        var = Scope({'n':n, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'm', 'r', 'e', 'h', 'g', 'n', 'i', 'v', 'd', 'l'])
        PyJsComma(var.get('n').put((var.get('r')>>Js(5.0)), (Js(128.0)<<(var.get('r')%Js(32.0))), '|'),var.get('n').put((Js(14.0)+(PyJsBshift((var.get('r')+Js(64.0)),Js(9.0))<<Js(4.0))), var.get('r')))
        var.put('l', Js(1732584193.0))
        var.put('g', (-Js(271733879.0)))
        var.put('v', (-Js(1732584194.0)))
        var.put('m', Js(271733878.0))
        #for JS loop
        var.put('e', Js(0.0))
        while (var.get('e')<var.get('n').get('length')):
            try:
                def PyJs_LONG_22_(var=var):
                    def PyJs_LONG_20_(var=var):
                        def PyJs_LONG_16_(var=var):
                            def PyJs_LONG_12_(var=var):
                                def PyJs_LONG_8_(var=var):
                                    def PyJs_LONG_4_(var=var):
                                        def PyJs_LONG_1_(var=var):
                                            return var.get('o')(var.get('v'), var.put('m', var.get('o')(var.get('m'), var.put('l', var.get('o')(var.get('l'), var.get('g'), var.get('v'), var.get('m'), var.get('n').get(var.get('e')), Js(7.0), (-Js(680876936.0)))), var.get('g'), var.get('v'), var.get('n').get((var.get('e')+Js(1.0))), Js(12.0), (-Js(389564586.0)))), var.get('l'), var.get('g'), var.get('n').get((var.get('e')+Js(2.0))), Js(17.0), Js(606105819.0))
                                        def PyJs_LONG_2_(var=var):
                                            return var.get('o')(var.get('v'), var.put('m', var.get('o')(var.get('m'), var.put('l', var.get('o')(var.get('l'), var.get('g'), var.get('v'), var.get('m'), var.get('n').get((var.get('e')+Js(4.0))), Js(7.0), (-Js(176418897.0)))), var.get('g'), var.get('v'), var.get('n').get((var.get('e')+Js(5.0))), Js(12.0), Js(1200080426.0))), var.get('l'), var.get('g'), var.get('n').get((var.get('e')+Js(6.0))), Js(17.0), (-Js(1473231341.0)))
                                        def PyJs_LONG_3_(var=var):
                                            return var.get('o')(var.get('v'), var.put('m', var.get('o')(var.get('m'), var.put('l', var.get('o')(var.get('l'), var.get('g'), var.get('v'), var.get('m'), var.get('n').get((var.get('e')+Js(8.0))), Js(7.0), Js(1770035416.0))), var.get('g'), var.get('v'), var.get('n').get((var.get('e')+Js(9.0))), Js(12.0), (-Js(1958414417.0)))), var.get('l'), var.get('g'), var.get('n').get((var.get('e')+Js(10.0))), Js(17.0), (-Js(42063.0)))
                                        return var.get('o')(var.put('g', var.get('o')(var.put('g', var.get('o')(var.get('g'), var.put('v', PyJs_LONG_1_()), var.get('m'), var.get('l'), var.get('n').get((var.get('e')+Js(3.0))), Js(22.0), (-Js(1044525330.0)))), var.put('v', PyJs_LONG_2_()), var.get('m'), var.get('l'), var.get('n').get((var.get('e')+Js(7.0))), Js(22.0), (-Js(45705983.0)))), var.put('v', PyJs_LONG_3_()), var.get('m'), var.get('l'), var.get('n').get((var.get('e')+Js(11.0))), Js(22.0), (-Js(1990404162.0)))
                                    def PyJs_LONG_5_(var=var):
                                        return var.get('o')(var.get('v'), var.put('m', var.get('o')(var.get('m'), var.put('l', var.get('o')(var.get('l'), var.get('g'), var.get('v'), var.get('m'), var.get('n').get((var.get('e')+Js(12.0))), Js(7.0), Js(1804603682.0))), var.get('g'), var.get('v'), var.get('n').get((var.get('e')+Js(13.0))), Js(12.0), (-Js(40341101.0)))), var.get('l'), var.get('g'), var.get('n').get((var.get('e')+Js(14.0))), Js(17.0), (-Js(1502002290.0)))
                                    def PyJs_LONG_6_(var=var):
                                        return var.get('u')(var.get('v'), var.put('m', var.get('u')(var.get('m'), var.put('l', var.get('u')(var.get('l'), var.get('g'), var.get('v'), var.get('m'), var.get('n').get((var.get('e')+Js(1.0))), Js(5.0), (-Js(165796510.0)))), var.get('g'), var.get('v'), var.get('n').get((var.get('e')+Js(6.0))), Js(9.0), (-Js(1069501632.0)))), var.get('l'), var.get('g'), var.get('n').get((var.get('e')+Js(11.0))), Js(14.0), Js(643717713.0))
                                    def PyJs_LONG_7_(var=var):
                                        return var.get('u')(var.get('v'), var.put('m', var.get('u')(var.get('m'), var.put('l', var.get('u')(var.get('l'), var.get('g'), var.get('v'), var.get('m'), var.get('n').get((var.get('e')+Js(5.0))), Js(5.0), (-Js(701558691.0)))), var.get('g'), var.get('v'), var.get('n').get((var.get('e')+Js(10.0))), Js(9.0), Js(38016083.0))), var.get('l'), var.get('g'), var.get('n').get((var.get('e')+Js(15.0))), Js(14.0), (-Js(660478335.0)))
                                    return var.get('u')(var.put('g', var.get('u')(var.put('g', var.get('o')(var.put('g', PyJs_LONG_4_()), var.put('v', PyJs_LONG_5_()), var.get('m'), var.get('l'), var.get('n').get((var.get('e')+Js(15.0))), Js(22.0), Js(1236535329.0))), var.put('v', PyJs_LONG_6_()), var.get('m'), var.get('l'), var.get('n').get(var.get('e')), Js(20.0), (-Js(373897302.0)))), var.put('v', PyJs_LONG_7_()), var.get('m'), var.get('l'), var.get('n').get((var.get('e')+Js(4.0))), Js(20.0), (-Js(405537848.0)))
                                def PyJs_LONG_9_(var=var):
                                    return var.get('u')(var.get('v'), var.put('m', var.get('u')(var.get('m'), var.put('l', var.get('u')(var.get('l'), var.get('g'), var.get('v'), var.get('m'), var.get('n').get((var.get('e')+Js(9.0))), Js(5.0), Js(568446438.0))), var.get('g'), var.get('v'), var.get('n').get((var.get('e')+Js(14.0))), Js(9.0), (-Js(1019803690.0)))), var.get('l'), var.get('g'), var.get('n').get((var.get('e')+Js(3.0))), Js(14.0), (-Js(187363961.0)))
                                def PyJs_LONG_10_(var=var):
                                    return var.get('u')(var.get('v'), var.put('m', var.get('u')(var.get('m'), var.put('l', var.get('u')(var.get('l'), var.get('g'), var.get('v'), var.get('m'), var.get('n').get((var.get('e')+Js(13.0))), Js(5.0), (-Js(1444681467.0)))), var.get('g'), var.get('v'), var.get('n').get((var.get('e')+Js(2.0))), Js(9.0), (-Js(51403784.0)))), var.get('l'), var.get('g'), var.get('n').get((var.get('e')+Js(7.0))), Js(14.0), Js(1735328473.0))
                                def PyJs_LONG_11_(var=var):
                                    return var.get('c')(var.get('v'), var.put('m', var.get('c')(var.get('m'), var.put('l', var.get('c')(var.get('l'), var.get('g'), var.get('v'), var.get('m'), var.get('n').get((var.get('e')+Js(5.0))), Js(4.0), (-Js(378558.0)))), var.get('g'), var.get('v'), var.get('n').get((var.get('e')+Js(8.0))), Js(11.0), (-Js(2022574463.0)))), var.get('l'), var.get('g'), var.get('n').get((var.get('e')+Js(11.0))), Js(16.0), Js(1839030562.0))
                                return var.get('c')(var.put('g', var.get('u')(var.put('g', var.get('u')(var.put('g', PyJs_LONG_8_()), var.put('v', PyJs_LONG_9_()), var.get('m'), var.get('l'), var.get('n').get((var.get('e')+Js(8.0))), Js(20.0), Js(1163531501.0))), var.put('v', PyJs_LONG_10_()), var.get('m'), var.get('l'), var.get('n').get((var.get('e')+Js(12.0))), Js(20.0), (-Js(1926607734.0)))), var.put('v', PyJs_LONG_11_()), var.get('m'), var.get('l'), var.get('n').get((var.get('e')+Js(14.0))), Js(23.0), (-Js(35309556.0)))
                            def PyJs_LONG_13_(var=var):
                                return var.get('c')(var.get('v'), var.put('m', var.get('c')(var.get('m'), var.put('l', var.get('c')(var.get('l'), var.get('g'), var.get('v'), var.get('m'), var.get('n').get((var.get('e')+Js(1.0))), Js(4.0), (-Js(1530992060.0)))), var.get('g'), var.get('v'), var.get('n').get((var.get('e')+Js(4.0))), Js(11.0), Js(1272893353.0))), var.get('l'), var.get('g'), var.get('n').get((var.get('e')+Js(7.0))), Js(16.0), (-Js(155497632.0)))
                            def PyJs_LONG_14_(var=var):
                                return var.get('c')(var.get('v'), var.put('m', var.get('c')(var.get('m'), var.put('l', var.get('c')(var.get('l'), var.get('g'), var.get('v'), var.get('m'), var.get('n').get((var.get('e')+Js(13.0))), Js(4.0), Js(681279174.0))), var.get('g'), var.get('v'), var.get('n').get(var.get('e')), Js(11.0), (-Js(358537222.0)))), var.get('l'), var.get('g'), var.get('n').get((var.get('e')+Js(3.0))), Js(16.0), (-Js(722521979.0)))
                            def PyJs_LONG_15_(var=var):
                                return var.get('c')(var.get('v'), var.put('m', var.get('c')(var.get('m'), var.put('l', var.get('c')(var.get('l'), var.get('g'), var.get('v'), var.get('m'), var.get('n').get((var.get('e')+Js(9.0))), Js(4.0), (-Js(640364487.0)))), var.get('g'), var.get('v'), var.get('n').get((var.get('e')+Js(12.0))), Js(11.0), (-Js(421815835.0)))), var.get('l'), var.get('g'), var.get('n').get((var.get('e')+Js(15.0))), Js(16.0), Js(530742520.0))
                            return var.get('c')(var.put('g', var.get('c')(var.put('g', var.get('c')(var.put('g', PyJs_LONG_12_()), var.put('v', PyJs_LONG_13_()), var.get('m'), var.get('l'), var.get('n').get((var.get('e')+Js(10.0))), Js(23.0), (-Js(1094730640.0)))), var.put('v', PyJs_LONG_14_()), var.get('m'), var.get('l'), var.get('n').get((var.get('e')+Js(6.0))), Js(23.0), Js(76029189.0))), var.put('v', PyJs_LONG_15_()), var.get('m'), var.get('l'), var.get('n').get((var.get('e')+Js(2.0))), Js(23.0), (-Js(995338651.0)))
                        def PyJs_LONG_17_(var=var):
                            return var.get('f')(var.get('v'), var.put('m', var.get('f')(var.get('m'), var.put('l', var.get('f')(var.get('l'), var.get('g'), var.get('v'), var.get('m'), var.get('n').get(var.get('e')), Js(6.0), (-Js(198630844.0)))), var.get('g'), var.get('v'), var.get('n').get((var.get('e')+Js(7.0))), Js(10.0), Js(1126891415.0))), var.get('l'), var.get('g'), var.get('n').get((var.get('e')+Js(14.0))), Js(15.0), (-Js(1416354905.0)))
                        def PyJs_LONG_18_(var=var):
                            return var.get('f')(var.get('v'), var.put('m', var.get('f')(var.get('m'), var.put('l', var.get('f')(var.get('l'), var.get('g'), var.get('v'), var.get('m'), var.get('n').get((var.get('e')+Js(12.0))), Js(6.0), Js(1700485571.0))), var.get('g'), var.get('v'), var.get('n').get((var.get('e')+Js(3.0))), Js(10.0), (-Js(1894986606.0)))), var.get('l'), var.get('g'), var.get('n').get((var.get('e')+Js(10.0))), Js(15.0), (-Js(1051523.0)))
                        def PyJs_LONG_19_(var=var):
                            return var.get('f')(var.get('v'), var.put('m', var.get('f')(var.get('m'), var.put('l', var.get('f')(var.get('l'), var.get('g'), var.get('v'), var.get('m'), var.get('n').get((var.get('e')+Js(8.0))), Js(6.0), Js(1873313359.0))), var.get('g'), var.get('v'), var.get('n').get((var.get('e')+Js(15.0))), Js(10.0), (-Js(30611744.0)))), var.get('l'), var.get('g'), var.get('n').get((var.get('e')+Js(6.0))), Js(15.0), (-Js(1560198380.0)))
                        return var.get('f')(var.put('g', var.get('f')(var.put('g', var.get('f')(var.put('g', PyJs_LONG_16_()), var.put('v', PyJs_LONG_17_()), var.get('m'), var.get('l'), var.get('n').get((var.get('e')+Js(5.0))), Js(21.0), (-Js(57434055.0)))), var.put('v', PyJs_LONG_18_()), var.get('m'), var.get('l'), var.get('n').get((var.get('e')+Js(1.0))), Js(21.0), (-Js(2054922799.0)))), var.put('v', PyJs_LONG_19_()), var.get('m'), var.get('l'), var.get('n').get((var.get('e')+Js(13.0))), Js(21.0), Js(1309151649.0))
                    def PyJs_LONG_21_(var=var):
                        return var.get('f')(var.get('v'), var.put('m', var.get('f')(var.get('m'), var.put('l', var.get('f')(var.get('l'), var.get('g'), var.get('v'), var.get('m'), var.get('n').get((var.get('e')+Js(4.0))), Js(6.0), (-Js(145523070.0)))), var.get('g'), var.get('v'), var.get('n').get((var.get('e')+Js(11.0))), Js(10.0), (-Js(1120210379.0)))), var.get('l'), var.get('g'), var.get('n').get((var.get('e')+Js(2.0))), Js(15.0), Js(718787259.0))
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('i', var.get('l')),var.put('a', var.get('g'))),var.put('d', var.get('v'))),var.put('h', var.get('m'))),var.put('g', var.get('f')(var.put('g', PyJs_LONG_20_()), var.put('v', PyJs_LONG_21_()), var.get('m'), var.get('l'), var.get('n').get((var.get('e')+Js(9.0))), Js(21.0), (-Js(343485551.0))))),var.put('l', var.get('t')(var.get('l'), var.get('i')))),var.put('g', var.get('t')(var.get('g'), var.get('a')))),var.put('v', var.get('t')(var.get('v'), var.get('d')))),var.put('m', var.get('t')(var.get('m'), var.get('h'))))
                PyJs_LONG_22_()
            finally:
                    var.put('e', Js(16.0), '+')
        return Js([var.get('l'), var.get('g'), var.get('v'), var.get('m')])
    PyJsHoisted_i_.func_name = 'i'
    var.put('i', PyJsHoisted_i_)
    @Js
    def PyJsHoisted_a_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'n', 'r', 'e'])
        var.put('r', Js(''))
        var.put('e', (Js(32.0)*var.get('n').get('length')))
        #for JS loop
        var.put('t', Js(0.0))
        while (var.get('t')<var.get('e')):
            try:
                var.put('r', var.get('String').callprop('fromCharCode', (PyJsBshift(var.get('n').get((var.get('t')>>Js(5.0))),(var.get('t')%Js(32.0)))&Js(255.0))), '+')
            finally:
                    var.put('t', Js(8.0), '+')
        return var.get('r')
    PyJsHoisted_a_.func_name = 'a'
    var.put('a', PyJsHoisted_a_)
    @Js
    def PyJsHoisted_d_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'n', 'r', 'e'])
        var.put('r', Js([]))
        #for JS loop
        PyJsComma(var.get('r').put(((var.get('n').get('length')>>Js(2.0))-Js(1.0)), PyJsComma(Js(0.0), Js(None))),var.put('t', Js(0.0)))
        while (var.get('t')<var.get('r').get('length')):
            try:
                var.get('r').put(var.get('t'), Js(0.0))
            finally:
                    var.put('t', Js(1.0), '+')
        var.put('e', (Js(8.0)*var.get('n').get('length')))
        #for JS loop
        var.put('t', Js(0.0))
        while (var.get('t')<var.get('e')):
            try:
                var.get('r').put((var.get('t')>>Js(5.0)), ((Js(255.0)&var.get('n').callprop('charCodeAt', (var.get('t')/Js(8.0))))<<(var.get('t')%Js(32.0))), '|')
            finally:
                    var.put('t', Js(8.0), '+')
        return var.get('r')
    PyJsHoisted_d_.func_name = 'd'
    var.put('d', PyJsHoisted_d_)
    @Js
    def PyJsHoisted_h_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['n'])
        return var.get('a')(var.get('i')(var.get('d')(var.get('n')), (Js(8.0)*var.get('n').get('length'))))
    PyJsHoisted_h_.func_name = 'h'
    var.put('h', PyJsHoisted_h_)
    @Js
    def PyJsHoisted_l_(n, t, this, arguments, var=var):
        var = Scope({'n':n, 't':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['o', 'c', 'r', 'e', 'u', 't', 'n'])
        var.put('o', var.get('d')(var.get('n')))
        var.put('u', Js([]))
        var.put('c', Js([]))
        #for JS loop
        PyJsComma(PyJsComma(var.get('u').put('15', var.get('c').put('15', PyJsComma(Js(0.0), Js(None)))),((var.get('o').get('length')>Js(16.0)) and var.put('o', var.get('i')(var.get('o'), (Js(8.0)*var.get('n').get('length')))))),var.put('r', Js(0.0)))
        while (var.get('r')<Js(16.0)):
            try:
                PyJsComma(var.get('u').put(var.get('r'), (Js(909522486.0)^var.get('o').get(var.get('r')))),var.get('c').put(var.get('r'), (Js(1549556828.0)^var.get('o').get(var.get('r')))))
            finally:
                    var.put('r', Js(1.0), '+')
        return PyJsComma(var.put('e', var.get('i')(var.get('u').callprop('concat', var.get('d')(var.get('t'))), (Js(512.0)+(Js(8.0)*var.get('t').get('length'))))),var.get('a')(var.get('i')(var.get('c').callprop('concat', var.get('e')), Js(640.0))))
    PyJsHoisted_l_.func_name = 'l'
    var.put('l', PyJsHoisted_l_)
    @Js
    def PyJsHoisted_g_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'n', 'r', 'e'])
        var.put('e', Js(''))
        #for JS loop
        var.put('r', Js(0.0))
        while (var.get('r')<var.get('n').get('length')):
            try:
                PyJsComma(var.put('t', var.get('n').callprop('charCodeAt', var.get('r'))),var.put('e', (Js('0123456789abcdef').callprop('charAt', (PyJsBshift(var.get('t'),Js(4.0))&Js(15.0)))+Js('0123456789abcdef').callprop('charAt', (Js(15.0)&var.get('t')))), '+'))
            finally:
                    var.put('r', Js(1.0), '+')
        return var.get('e')
    PyJsHoisted_g_.func_name = 'g'
    var.put('g', PyJsHoisted_g_)
    @Js
    def PyJsHoisted_v_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['n'])
        return var.get('unescape')(var.get('encodeURIComponent')(var.get('n')))
    PyJsHoisted_v_.func_name = 'v'
    var.put('v', PyJsHoisted_v_)
    @Js
    def PyJsHoisted_m_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['n'])
        return var.get('h')(var.get('v')(var.get('n')))
    PyJsHoisted_m_.func_name = 'm'
    var.put('m', PyJsHoisted_m_)
    @Js
    def PyJsHoisted_p_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['n'])
        return var.get('g')(var.get('m')(var.get('n')))
    PyJsHoisted_p_.func_name = 'p'
    var.put('p', PyJsHoisted_p_)
    @Js
    def PyJsHoisted_s_(n, t, this, arguments, var=var):
        var = Scope({'n':n, 't':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'n'])
        return var.get('l')(var.get('v')(var.get('n')), var.get('v')(var.get('t')))
    PyJsHoisted_s_.func_name = 's'
    var.put('s', PyJsHoisted_s_)
    @Js
    def PyJsHoisted_C_(n, t, this, arguments, var=var):
        var = Scope({'n':n, 't':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'n'])
        return var.get('g')(var.get('s')(var.get('n'), var.get('t')))
    PyJsHoisted_C_.func_name = 'C'
    var.put('C', PyJsHoisted_C_)
    @Js
    def PyJsHoisted_A_(n, t, r, this, arguments, var=var):
        var = Scope({'n':n, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'n', 'r'])
        return ((var.get('s')(var.get('t'), var.get('n')) if var.get('r') else var.get('C')(var.get('t'), var.get('n'))) if var.get('t') else (var.get('m')(var.get('n')) if var.get('r') else var.get('p')(var.get('n'))))
    PyJsHoisted_A_.func_name = 'A'
    var.put('A', PyJsHoisted_A_)
    Js('use strict')
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    @Js
    def PyJs_anonymous_23_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return var.get('A')
    PyJs_anonymous_23_._set_name('anonymous')
    (var.get('define')(PyJs_anonymous_23_) if ((Js('function')==var.get('define',throw=False).typeof()) and var.get('define').get('amd')) else (var.get('module').put('exports', var.get('A')) if ((Js('object')==var.get('module',throw=False).typeof()) and var.get('module').get('exports')) else var.get('n').put('md5', var.get('A'))))
PyJs_anonymous_0_._set_name('anonymous')
PyJs_anonymous_0_(var.get(u"this")).neg()
@Js
def PyJs_anonymous_24_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['o', 'a', 'r', 'c', 'e', 'p', 'h', 's', 'u', 'y', 'f', 't', 'n', 'i'])
    @Js
    def PyJsHoisted_t_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        def PyJs_LONG_26_(var=var):
            def PyJs_LONG_25_(var=var):
                return var.get('f').put('0', var.get('f').put('16', var.get('f').put('1', var.get('f').put('2', var.get('f').put('3', var.get('f').put('4', var.get('f').put('5', var.get('f').put('6', var.get('f').put('7', var.get('f').put('8', var.get('f').put('9', var.get('f').put('10', var.get('f').put('11', var.get('f').put('12', var.get('f').put('13', var.get('f').put('14', var.get('f').put('15', Js(0.0))))))))))))))))))
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma((PyJsComma(PyJs_LONG_25_(),var.get(u"this").put('blocks', var.get('f'))) if var.get('t') else var.get(u"this").put('blocks', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))),var.get(u"this").put('h0', Js(1732584193.0))),var.get(u"this").put('h1', Js(4023233417.0))),var.get(u"this").put('h2', Js(2562383102.0))),var.get(u"this").put('h3', Js(271733878.0))),var.get(u"this").put('h4', Js(3285377520.0))),var.get(u"this").put('block', var.get(u"this").put('start', var.get(u"this").put('bytes', var.get(u"this").put('hBytes', Js(0.0)))))),var.get(u"this").put('finalized', var.get(u"this").put('hashed', Js(1.0).neg()))),var.get(u"this").put('first', Js(0.0).neg()))
        PyJs_LONG_26_()
    PyJsHoisted_t_.func_name = 't'
    var.put('t', PyJsHoisted_t_)
    Js('use strict')
    pass
    var.put('h', (var.get('window') if (Js('object')==var.get('window',throw=False).typeof()) else Js({})))
    var.put('s', (((var.get('h').get('JS_SHA1_NO_NODE_JS').neg() and (Js('object')==var.get('process',throw=False).typeof())) and var.get('process').get('versions')) and var.get('process').get('versions').get('node')))
    (var.get('s') and var.put('h', var.get('global')))
    var.put('i', ((var.get('h').get('JS_SHA1_NO_COMMON_JS').neg() and (Js('object')==var.get('module',throw=False).typeof())) and var.get('module').get('exports')))
    var.put('e', ((Js('function')==var.get('define',throw=False).typeof()) and var.get('define').get('amd')))
    var.put('r', Js('0123456789abcdef').callprop('split', Js('')))
    var.put('o', Js([(-Js(2147483648.0)), Js(8388608.0), Js(32768.0), Js(128.0)]))
    var.put('n', Js([Js(24.0), Js(16.0), Js(8.0), Js(0.0)]))
    var.put('a', Js([Js('hex'), Js('array'), Js('digest'), Js('arrayBuffer')]))
    var.put('f', Js([]))
    @Js
    def PyJs_anonymous_27_(h, this, arguments, var=var):
        var = Scope({'h':h, 'this':this, 'arguments':arguments}, var)
        var.registers(['h'])
        @Js
        def PyJs_anonymous_28_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('t').create(Js(0.0).neg()).callprop('update', var.get('s')).callprop(var.get('h'))
        PyJs_anonymous_28_._set_name('anonymous')
        return PyJs_anonymous_28_
    PyJs_anonymous_27_._set_name('anonymous')
    var.put('u', PyJs_anonymous_27_)
    @Js
    def PyJs_anonymous_29_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['h', 'i', 'e'])
        var.put('h', var.get('u')(Js('hex')))
        @Js
        def PyJs_anonymous_30_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return var.get('t').create()
        PyJs_anonymous_30_._set_name('anonymous')
        @Js
        def PyJs_anonymous_31_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            return var.get('h').callprop('create').callprop('update', var.get('t'))
        PyJs_anonymous_31_._set_name('anonymous')
        PyJsComma(PyJsComma((var.get('s') and var.put('h', var.get('p')(var.get('h')))),var.get('h').put('create', PyJs_anonymous_30_)),var.get('h').put('update', PyJs_anonymous_31_))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('a').get('length')):
            try:
                var.put('e', var.get('a').get(var.get('i')))
                var.get('h').put(var.get('e'), var.get('u')(var.get('e')))
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        return var.get('h')
    PyJs_anonymous_29_._set_name('anonymous')
    var.put('c', PyJs_anonymous_29_)
    @Js
    def PyJs_anonymous_32_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'h', 's', 'i'])
        var.put('h', var.get('eval')(Js("require('crypto')")))
        var.put('s', var.get('eval')(Js("require('buffer').Buffer")))
        @Js
        def PyJs_anonymous_33_(i, this, arguments, var=var):
            var = Scope({'i':i, 'this':this, 'arguments':arguments}, var)
            var.registers(['i'])
            if (Js('string')==var.get('i',throw=False).typeof()):
                return var.get('h').callprop('createHash', Js('sha1')).callprop('update', var.get('i'), Js('utf8')).callprop('digest', Js('hex'))
            if PyJsStrictEq(var.get('i').get('constructor'),var.get('ArrayBuffer')):
                var.put('i', var.get('Uint8Array').create(var.get('i')))
            else:
                if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get('i').get('length')):
                    return var.get('t')(var.get('i'))
            return var.get('h').callprop('createHash', Js('sha1')).callprop('update', var.get('s').create(var.get('i'))).callprop('digest', Js('hex'))
        PyJs_anonymous_33_._set_name('anonymous')
        var.put('i', PyJs_anonymous_33_)
        return var.get('i')
    PyJs_anonymous_32_._set_name('anonymous')
    var.put('p', PyJs_anonymous_32_)
    def PyJs_LONG_66_(var=var):
        @Js
        def PyJs_anonymous_34_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['o', 'a', 'r', 'e', 's', 't', 'i'])
            if var.get(u"this").get('finalized').neg():
                var.put('s', (Js('string')!=var.get('t',throw=False).typeof()))
                ((var.get('s') and PyJsStrictEq(var.get('t').get('constructor'),var.get('h').get('ArrayBuffer'))) and var.put('t', var.get('Uint8Array').create(var.get('t'))))
                #for JS loop
                var.put('r', Js(0.0))
                var.put('o', (var.get('t').get('length') or Js(0.0)))
                var.put('a', var.get(u"this").get('blocks'))
                while (var.get('r')<var.get('o')):
                    def PyJs_LONG_35_(var=var):
                        return PyJsComma(PyJsComma(var.get(u"this").put('hashed', Js(1.0).neg()),var.get('a').put('0', var.get(u"this").get('block'))),var.get('a').put('16', var.get('a').put('1', var.get('a').put('2', var.get('a').put('3', var.get('a').put('4', var.get('a').put('5', var.get('a').put('6', var.get('a').put('7', var.get('a').put('8', var.get('a').put('9', var.get('a').put('10', var.get('a').put('11', var.get('a').put('12', var.get('a').put('13', var.get('a').put('14', var.get('a').put('15', Js(0.0))))))))))))))))))
                    if PyJsComma((var.get(u"this").get('hashed') and PyJs_LONG_35_()),var.get('s')):
                        #for JS loop
                        var.put('e', var.get(u"this").get('start'))
                        while ((var.get('r')<var.get('o')) and (var.get('e')<Js(64.0))):
                            try:
                                var.get('a').put((var.get('e')>>Js(2.0)), (var.get('t').get(var.get('r'))<<var.get('n').get((Js(3.0)&(var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))))), '|')
                            finally:
                                    var.put('r',Js(var.get('r').to_number())+Js(1))
                    else:
                        #for JS loop
                        var.put('e', var.get(u"this").get('start'))
                        while ((var.get('r')<var.get('o')) and (var.get('e')<Js(64.0))):
                            try:
                                def PyJs_LONG_38_(var=var):
                                    def PyJs_LONG_36_(var=var):
                                        return PyJsComma(PyJsComma(var.get('a').put((var.get('e')>>Js(2.0)), ((Js(224.0)|(var.get('i')>>Js(12.0)))<<var.get('n').get((Js(3.0)&(var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))))), '|'),var.get('a').put((var.get('e')>>Js(2.0)), ((Js(128.0)|((var.get('i')>>Js(6.0))&Js(63.0)))<<var.get('n').get((Js(3.0)&(var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))))), '|')),var.get('a').put((var.get('e')>>Js(2.0)), ((Js(128.0)|(Js(63.0)&var.get('i')))<<var.get('n').get((Js(3.0)&(var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))))), '|'))
                                    def PyJs_LONG_37_(var=var):
                                        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('i', (Js(65536.0)+(((Js(1023.0)&var.get('i'))<<Js(10.0))|(Js(1023.0)&var.get('t').callprop('charCodeAt', var.put('r',Js(var.get('r').to_number())+Js(1))))))),var.get('a').put((var.get('e')>>Js(2.0)), ((Js(240.0)|(var.get('i')>>Js(18.0)))<<var.get('n').get((Js(3.0)&(var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))))), '|')),var.get('a').put((var.get('e')>>Js(2.0)), ((Js(128.0)|((var.get('i')>>Js(12.0))&Js(63.0)))<<var.get('n').get((Js(3.0)&(var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))))), '|')),var.get('a').put((var.get('e')>>Js(2.0)), ((Js(128.0)|((var.get('i')>>Js(6.0))&Js(63.0)))<<var.get('n').get((Js(3.0)&(var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))))), '|')),var.get('a').put((var.get('e')>>Js(2.0)), ((Js(128.0)|(Js(63.0)&var.get('i')))<<var.get('n').get((Js(3.0)&(var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))))), '|'))
                                    return (PyJsComma(var.get('a').put((var.get('e')>>Js(2.0)), ((Js(192.0)|(var.get('i')>>Js(6.0)))<<var.get('n').get((Js(3.0)&(var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))))), '|'),var.get('a').put((var.get('e')>>Js(2.0)), ((Js(128.0)|(Js(63.0)&var.get('i')))<<var.get('n').get((Js(3.0)&(var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))))), '|')) if (var.get('i')<Js(2048.0)) else (PyJs_LONG_36_() if ((var.get('i')<Js(55296.0)) or (var.get('i')>=Js(57344.0))) else PyJs_LONG_37_()))
                                (var.get('a').put((var.get('e')>>Js(2.0)), (var.get('i')<<var.get('n').get((Js(3.0)&(var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))))), '|') if (var.put('i', var.get('t').callprop('charCodeAt', var.get('r')))<Js(128.0)) else PyJs_LONG_38_())
                            finally:
                                    var.put('r',Js(var.get('r').to_number())+Js(1))
                    def PyJs_LONG_39_(var=var):
                        return PyJsComma(PyJsComma(var.get(u"this").put('lastByteIndex', var.get('e')),var.get(u"this").put('bytes', (var.get('e')-var.get(u"this").get('start')), '+')),(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('block', var.get('a').get('16')),var.get(u"this").put('start', (var.get('e')-Js(64.0)))),var.get(u"this").callprop('hash')),var.get(u"this").put('hashed', Js(0.0).neg())) if (var.get('e')>=Js(64.0)) else var.get(u"this").put('start', var.get('e'))))
                    PyJs_LONG_39_()
                
                return PyJsComma(((var.get(u"this").get('bytes')>Js(4294967295.0)) and PyJsComma(var.get(u"this").put('hBytes', ((var.get(u"this").get('bytes')/Js(4294967296.0))<<Js(0.0)), '+'),var.get(u"this").put('bytes', (var.get(u"this").get('bytes')%Js(4294967296.0))))),var.get(u"this"))
        PyJs_anonymous_34_._set_name('anonymous')
        @Js
        def PyJs_anonymous_40_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['t', 'h'])
            if var.get(u"this").get('finalized').neg():
                var.get(u"this").put('finalized', Js(0.0).neg())
                var.put('t', var.get(u"this").get('blocks'))
                var.put('h', var.get(u"this").get('lastByteIndex'))
                def PyJs_LONG_42_(var=var):
                    def PyJs_LONG_41_(var=var):
                        return PyJsComma(PyJsComma((var.get(u"this").get('hashed') or var.get(u"this").callprop('hash')),var.get('t').put('0', var.get(u"this").get('block'))),var.get('t').put('16', var.get('t').put('1', var.get('t').put('2', var.get('t').put('3', var.get('t').put('4', var.get('t').put('5', var.get('t').put('6', var.get('t').put('7', var.get('t').put('8', var.get('t').put('9', var.get('t').put('10', var.get('t').put('11', var.get('t').put('12', var.get('t').put('13', var.get('t').put('14', var.get('t').put('15', Js(0.0))))))))))))))))))
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('t').put('16', var.get(u"this").get('block')),var.get('t').put((var.get('h')>>Js(2.0)), var.get('o').get((Js(3.0)&var.get('h'))), '|')),var.get(u"this").put('block', var.get('t').get('16'))),((var.get('h')>=Js(56.0)) and PyJs_LONG_41_())),var.get('t').put('14', ((var.get(u"this").get('hBytes')<<Js(3.0))|PyJsBshift(var.get(u"this").get('bytes'),Js(29.0))))),var.get('t').put('15', (var.get(u"this").get('bytes')<<Js(3.0)))),var.get(u"this").callprop('hash'))
                PyJs_LONG_42_()
        PyJs_anonymous_40_._set_name('anonymous')
        @Js
        def PyJs_anonymous_43_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['o', 'r', 'e', 'h', 's', 't', 'n', 'i'])
            var.put('s', var.get(u"this").get('h0'))
            var.put('i', var.get(u"this").get('h1'))
            var.put('e', var.get(u"this").get('h2'))
            var.put('r', var.get(u"this").get('h3'))
            var.put('o', var.get(u"this").get('h4'))
            var.put('n', var.get(u"this").get('blocks'))
            #for JS loop
            var.put('t', Js(16.0))
            while (var.get('t')<Js(80.0)):
                try:
                    PyJsComma(var.put('h', (((var.get('n').get((var.get('t')-Js(3.0)))^var.get('n').get((var.get('t')-Js(8.0))))^var.get('n').get((var.get('t')-Js(14.0))))^var.get('n').get((var.get('t')-Js(16.0))))),var.get('n').put(var.get('t'), ((var.get('h')<<Js(1.0))|PyJsBshift(var.get('h'),Js(31.0)))))
                finally:
                        var.put('t',Js(var.get('t').to_number())+Js(1))
            #for JS loop
            var.put('t', Js(0.0))
            while (var.get('t')<Js(20.0)):
                try:
                    def PyJs_LONG_46_(var=var):
                        def PyJs_LONG_45_(var=var):
                            def PyJs_LONG_44_(var=var):
                                return (var.put('h', ((var.put('o', (((((var.put('h', ((var.get('s')<<Js(5.0))|PyJsBshift(var.get('s'),Js(27.0))))+((var.get('i')&var.get('e'))|((~var.get('i'))&var.get('r'))))+var.get('o'))+Js(1518500249.0))+var.get('n').get(var.get('t')))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('o'),Js(27.0))))+((var.get('s')&var.put('i', ((var.get('i')<<Js(30.0))|PyJsBshift(var.get('i'),Js(2.0)))))|((~var.get('s'))&var.get('e'))))
                            return var.put('e', (((((var.put('h', ((var.put('r', ((((PyJs_LONG_44_()+var.get('r'))+Js(1518500249.0))+var.get('n').get((var.get('t')+Js(1.0))))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('r'),Js(27.0))))+((var.get('o')&var.put('s', ((var.get('s')<<Js(30.0))|PyJsBshift(var.get('s'),Js(2.0)))))|((~var.get('o'))&var.get('i'))))+var.get('e'))+Js(1518500249.0))+var.get('n').get((var.get('t')+Js(2.0))))<<Js(0.0)))
                        return (var.put('h', ((var.put('i', (((((var.put('h', ((PyJs_LONG_45_()<<Js(5.0))|PyJsBshift(var.get('e'),Js(27.0))))+((var.get('r')&var.put('o', ((var.get('o')<<Js(30.0))|PyJsBshift(var.get('o'),Js(2.0)))))|((~var.get('r'))&var.get('s'))))+var.get('i'))+Js(1518500249.0))+var.get('n').get((var.get('t')+Js(3.0))))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('i'),Js(27.0))))+((var.get('e')&var.put('r', ((var.get('r')<<Js(30.0))|PyJsBshift(var.get('r'),Js(2.0)))))|((~var.get('e'))&var.get('o'))))
                    PyJsComma(var.put('s', ((((PyJs_LONG_46_()+var.get('s'))+Js(1518500249.0))+var.get('n').get((var.get('t')+Js(4.0))))<<Js(0.0))),var.put('e', ((var.get('e')<<Js(30.0))|PyJsBshift(var.get('e'),Js(2.0)))))
                finally:
                        var.put('t', Js(5.0), '+')
            #for JS loop
            
            while (var.get('t')<Js(40.0)):
                try:
                    def PyJs_LONG_49_(var=var):
                        def PyJs_LONG_48_(var=var):
                            def PyJs_LONG_47_(var=var):
                                return (((var.put('h', ((var.put('o', (((((var.put('h', ((var.get('s')<<Js(5.0))|PyJsBshift(var.get('s'),Js(27.0))))+((var.get('i')^var.get('e'))^var.get('r')))+var.get('o'))+Js(1859775393.0))+var.get('n').get(var.get('t')))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('o'),Js(27.0))))+((var.get('s')^var.put('i', ((var.get('i')<<Js(30.0))|PyJsBshift(var.get('i'),Js(2.0)))))^var.get('e')))+var.get('r'))+Js(1859775393.0))
                            return var.put('h', ((var.put('e', (((((var.put('h', ((var.put('r', ((PyJs_LONG_47_()+var.get('n').get((var.get('t')+Js(1.0))))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('r'),Js(27.0))))+((var.get('o')^var.put('s', ((var.get('s')<<Js(30.0))|PyJsBshift(var.get('s'),Js(2.0)))))^var.get('i')))+var.get('e'))+Js(1859775393.0))+var.get('n').get((var.get('t')+Js(2.0))))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('e'),Js(27.0))))
                        return ((var.put('h', ((var.put('i', (((((PyJs_LONG_48_()+((var.get('r')^var.put('o', ((var.get('o')<<Js(30.0))|PyJsBshift(var.get('o'),Js(2.0)))))^var.get('s')))+var.get('i'))+Js(1859775393.0))+var.get('n').get((var.get('t')+Js(3.0))))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('i'),Js(27.0))))+((var.get('e')^var.put('r', ((var.get('r')<<Js(30.0))|PyJsBshift(var.get('r'),Js(2.0)))))^var.get('o')))+var.get('s'))
                    PyJsComma(var.put('s', (((PyJs_LONG_49_()+Js(1859775393.0))+var.get('n').get((var.get('t')+Js(4.0))))<<Js(0.0))),var.put('e', ((var.get('e')<<Js(30.0))|PyJsBshift(var.get('e'),Js(2.0)))))
                finally:
                        var.put('t', Js(5.0), '+')
            #for JS loop
            
            while (var.get('t')<Js(60.0)):
                try:
                    def PyJs_LONG_52_(var=var):
                        def PyJs_LONG_51_(var=var):
                            def PyJs_LONG_50_(var=var):
                                return (var.put('h', ((var.put('o', (((((var.put('h', ((var.get('s')<<Js(5.0))|PyJsBshift(var.get('s'),Js(27.0))))+(((var.get('i')&var.get('e'))|(var.get('i')&var.get('r')))|(var.get('e')&var.get('r'))))+var.get('o'))-Js(1894007588.0))+var.get('n').get(var.get('t')))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('o'),Js(27.0))))+(((var.get('s')&var.put('i', ((var.get('i')<<Js(30.0))|PyJsBshift(var.get('i'),Js(2.0)))))|(var.get('s')&var.get('e')))|(var.get('i')&var.get('e'))))
                            return ((((var.put('h', ((var.put('r', ((((PyJs_LONG_50_()+var.get('r'))-Js(1894007588.0))+var.get('n').get((var.get('t')+Js(1.0))))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('r'),Js(27.0))))+(((var.get('o')&var.put('s', ((var.get('s')<<Js(30.0))|PyJsBshift(var.get('s'),Js(2.0)))))|(var.get('o')&var.get('i')))|(var.get('s')&var.get('i'))))+var.get('e'))-Js(1894007588.0))+var.get('n').get((var.get('t')+Js(2.0))))
                        return ((var.put('i', (((((var.put('h', ((var.put('e', (PyJs_LONG_51_()<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('e'),Js(27.0))))+(((var.get('r')&var.put('o', ((var.get('o')<<Js(30.0))|PyJsBshift(var.get('o'),Js(2.0)))))|(var.get('r')&var.get('s')))|(var.get('o')&var.get('s'))))+var.get('i'))-Js(1894007588.0))+var.get('n').get((var.get('t')+Js(3.0))))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('i'),Js(27.0)))
                    PyJsComma(var.put('s', (((((var.put('h', PyJs_LONG_52_())+(((var.get('e')&var.put('r', ((var.get('r')<<Js(30.0))|PyJsBshift(var.get('r'),Js(2.0)))))|(var.get('e')&var.get('o')))|(var.get('r')&var.get('o'))))+var.get('s'))-Js(1894007588.0))+var.get('n').get((var.get('t')+Js(4.0))))<<Js(0.0))),var.put('e', ((var.get('e')<<Js(30.0))|PyJsBshift(var.get('e'),Js(2.0)))))
                finally:
                        var.put('t', Js(5.0), '+')
            #for JS loop
            
            while (var.get('t')<Js(80.0)):
                try:
                    def PyJs_LONG_55_(var=var):
                        def PyJs_LONG_54_(var=var):
                            def PyJs_LONG_53_(var=var):
                                return (((var.put('h', ((var.put('o', (((((var.put('h', ((var.get('s')<<Js(5.0))|PyJsBshift(var.get('s'),Js(27.0))))+((var.get('i')^var.get('e'))^var.get('r')))+var.get('o'))-Js(899497514.0))+var.get('n').get(var.get('t')))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('o'),Js(27.0))))+((var.get('s')^var.put('i', ((var.get('i')<<Js(30.0))|PyJsBshift(var.get('i'),Js(2.0)))))^var.get('e')))+var.get('r'))-Js(899497514.0))
                            return var.put('h', ((var.put('e', (((((var.put('h', ((var.put('r', ((PyJs_LONG_53_()+var.get('n').get((var.get('t')+Js(1.0))))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('r'),Js(27.0))))+((var.get('o')^var.put('s', ((var.get('s')<<Js(30.0))|PyJsBshift(var.get('s'),Js(2.0)))))^var.get('i')))+var.get('e'))-Js(899497514.0))+var.get('n').get((var.get('t')+Js(2.0))))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('e'),Js(27.0))))
                        return ((var.put('h', ((var.put('i', (((((PyJs_LONG_54_()+((var.get('r')^var.put('o', ((var.get('o')<<Js(30.0))|PyJsBshift(var.get('o'),Js(2.0)))))^var.get('s')))+var.get('i'))-Js(899497514.0))+var.get('n').get((var.get('t')+Js(3.0))))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('i'),Js(27.0))))+((var.get('e')^var.put('r', ((var.get('r')<<Js(30.0))|PyJsBshift(var.get('r'),Js(2.0)))))^var.get('o')))+var.get('s'))
                    PyJsComma(var.put('s', (((PyJs_LONG_55_()-Js(899497514.0))+var.get('n').get((var.get('t')+Js(4.0))))<<Js(0.0))),var.put('e', ((var.get('e')<<Js(30.0))|PyJsBshift(var.get('e'),Js(2.0)))))
                finally:
                        var.put('t', Js(5.0), '+')
            def PyJs_LONG_56_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('h0', ((var.get(u"this").get('h0')+var.get('s'))<<Js(0.0))),var.get(u"this").put('h1', ((var.get(u"this").get('h1')+var.get('i'))<<Js(0.0)))),var.get(u"this").put('h2', ((var.get(u"this").get('h2')+var.get('e'))<<Js(0.0)))),var.get(u"this").put('h3', ((var.get(u"this").get('h3')+var.get('r'))<<Js(0.0)))),var.get(u"this").put('h4', ((var.get(u"this").get('h4')+var.get('o'))<<Js(0.0))))
            PyJs_LONG_56_()
        PyJs_anonymous_43_._set_name('anonymous')
        @Js
        def PyJs_anonymous_57_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'h', 's', 't', 'i'])
            var.get(u"this").callprop('finalize')
            var.put('t', var.get(u"this").get('h0'))
            var.put('h', var.get(u"this").get('h1'))
            var.put('s', var.get(u"this").get('h2'))
            var.put('i', var.get(u"this").get('h3'))
            var.put('e', var.get(u"this").get('h4'))
            def PyJs_LONG_62_(var=var):
                def PyJs_LONG_61_(var=var):
                    def PyJs_LONG_60_(var=var):
                        def PyJs_LONG_59_(var=var):
                            def PyJs_LONG_58_(var=var):
                                return (((((((var.get('r').get(((var.get('t')>>Js(28.0))&Js(15.0)))+var.get('r').get(((var.get('t')>>Js(24.0))&Js(15.0))))+var.get('r').get(((var.get('t')>>Js(20.0))&Js(15.0))))+var.get('r').get(((var.get('t')>>Js(16.0))&Js(15.0))))+var.get('r').get(((var.get('t')>>Js(12.0))&Js(15.0))))+var.get('r').get(((var.get('t')>>Js(8.0))&Js(15.0))))+var.get('r').get(((var.get('t')>>Js(4.0))&Js(15.0))))+var.get('r').get((Js(15.0)&var.get('t'))))
                            return (((((((PyJs_LONG_58_()+var.get('r').get(((var.get('h')>>Js(28.0))&Js(15.0))))+var.get('r').get(((var.get('h')>>Js(24.0))&Js(15.0))))+var.get('r').get(((var.get('h')>>Js(20.0))&Js(15.0))))+var.get('r').get(((var.get('h')>>Js(16.0))&Js(15.0))))+var.get('r').get(((var.get('h')>>Js(12.0))&Js(15.0))))+var.get('r').get(((var.get('h')>>Js(8.0))&Js(15.0))))+var.get('r').get(((var.get('h')>>Js(4.0))&Js(15.0))))
                        return ((((((((PyJs_LONG_59_()+var.get('r').get((Js(15.0)&var.get('h'))))+var.get('r').get(((var.get('s')>>Js(28.0))&Js(15.0))))+var.get('r').get(((var.get('s')>>Js(24.0))&Js(15.0))))+var.get('r').get(((var.get('s')>>Js(20.0))&Js(15.0))))+var.get('r').get(((var.get('s')>>Js(16.0))&Js(15.0))))+var.get('r').get(((var.get('s')>>Js(12.0))&Js(15.0))))+var.get('r').get(((var.get('s')>>Js(8.0))&Js(15.0))))+var.get('r').get(((var.get('s')>>Js(4.0))&Js(15.0))))
                    return ((((((((PyJs_LONG_60_()+var.get('r').get((Js(15.0)&var.get('s'))))+var.get('r').get(((var.get('i')>>Js(28.0))&Js(15.0))))+var.get('r').get(((var.get('i')>>Js(24.0))&Js(15.0))))+var.get('r').get(((var.get('i')>>Js(20.0))&Js(15.0))))+var.get('r').get(((var.get('i')>>Js(16.0))&Js(15.0))))+var.get('r').get(((var.get('i')>>Js(12.0))&Js(15.0))))+var.get('r').get(((var.get('i')>>Js(8.0))&Js(15.0))))+var.get('r').get(((var.get('i')>>Js(4.0))&Js(15.0))))
                return ((((((((PyJs_LONG_61_()+var.get('r').get((Js(15.0)&var.get('i'))))+var.get('r').get(((var.get('e')>>Js(28.0))&Js(15.0))))+var.get('r').get(((var.get('e')>>Js(24.0))&Js(15.0))))+var.get('r').get(((var.get('e')>>Js(20.0))&Js(15.0))))+var.get('r').get(((var.get('e')>>Js(16.0))&Js(15.0))))+var.get('r').get(((var.get('e')>>Js(12.0))&Js(15.0))))+var.get('r').get(((var.get('e')>>Js(8.0))&Js(15.0))))+var.get('r').get(((var.get('e')>>Js(4.0))&Js(15.0))))
            return (PyJs_LONG_62_()+var.get('r').get((Js(15.0)&var.get('e'))))
        PyJs_anonymous_57_._set_name('anonymous')
        @Js
        def PyJs_anonymous_63_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'h', 's', 't', 'i'])
            var.get(u"this").callprop('finalize')
            var.put('t', var.get(u"this").get('h0'))
            var.put('h', var.get(u"this").get('h1'))
            var.put('s', var.get(u"this").get('h2'))
            var.put('i', var.get(u"this").get('h3'))
            var.put('e', var.get(u"this").get('h4'))
            return Js([((var.get('t')>>Js(24.0))&Js(255.0)), ((var.get('t')>>Js(16.0))&Js(255.0)), ((var.get('t')>>Js(8.0))&Js(255.0)), (Js(255.0)&var.get('t')), ((var.get('h')>>Js(24.0))&Js(255.0)), ((var.get('h')>>Js(16.0))&Js(255.0)), ((var.get('h')>>Js(8.0))&Js(255.0)), (Js(255.0)&var.get('h')), ((var.get('s')>>Js(24.0))&Js(255.0)), ((var.get('s')>>Js(16.0))&Js(255.0)), ((var.get('s')>>Js(8.0))&Js(255.0)), (Js(255.0)&var.get('s')), ((var.get('i')>>Js(24.0))&Js(255.0)), ((var.get('i')>>Js(16.0))&Js(255.0)), ((var.get('i')>>Js(8.0))&Js(255.0)), (Js(255.0)&var.get('i')), ((var.get('e')>>Js(24.0))&Js(255.0)), ((var.get('e')>>Js(16.0))&Js(255.0)), ((var.get('e')>>Js(8.0))&Js(255.0)), (Js(255.0)&var.get('e'))])
        PyJs_anonymous_63_._set_name('anonymous')
        @Js
        def PyJs_anonymous_64_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['t', 'h'])
            var.get(u"this").callprop('finalize')
            var.put('t', var.get('ArrayBuffer').create(Js(20.0)))
            var.put('h', var.get('DataView').create(var.get('t')))
            def PyJs_LONG_65_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('h').callprop('setUint32', Js(0.0), var.get(u"this").get('h0')),var.get('h').callprop('setUint32', Js(4.0), var.get(u"this").get('h1'))),var.get('h').callprop('setUint32', Js(8.0), var.get(u"this").get('h2'))),var.get('h').callprop('setUint32', Js(12.0), var.get(u"this").get('h3'))),var.get('h').callprop('setUint32', Js(16.0), var.get(u"this").get('h4'))),var.get('t'))
            return PyJs_LONG_65_()
        PyJs_anonymous_64_._set_name('anonymous')
        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('t').get('prototype').put('update', PyJs_anonymous_34_),var.get('t').get('prototype').put('finalize', PyJs_anonymous_40_)),var.get('t').get('prototype').put('hash', PyJs_anonymous_43_)),var.get('t').get('prototype').put('hex', PyJs_anonymous_57_)),var.get('t').get('prototype').put('toString', var.get('t').get('prototype').get('hex'))),var.get('t').get('prototype').put('digest', PyJs_anonymous_63_)),var.get('t').get('prototype').put('array', var.get('t').get('prototype').get('digest'))),var.get('t').get('prototype').put('arrayBuffer', PyJs_anonymous_64_))
    PyJs_LONG_66_()
    var.put('y', var.get('c')())
    @Js
    def PyJs_anonymous_67_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return var.get('y')
    PyJs_anonymous_67_._set_name('anonymous')
    (var.get('module').put('exports', var.get('y')) if var.get('i') else PyJsComma(var.get('h').put('sha1', var.get('y')),(var.get('e') and var.get('define')(PyJs_anonymous_67_))))
PyJs_anonymous_24_._set_name('anonymous')
PyJs_anonymous_24_().neg()
var.put('_PADCHAR', Js('='))
var.put('_ALPHA', Js('LVoJPiCN2R8G90yg+hmFHuacZ1OWMnrsSTXkYpUq/3dlbfKwv6xztjI7DeBE45QA'))
var.put('_VERSION', Js('1.0'))
pass
pass
pass
pass
pass
pass


# Add lib to the module scope
methods = var.to_python()