# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520060829.482991
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/flairprefs.html'
_template_uri = '/flairprefs.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        if thing.sr_flair_enabled:
            # SOURCE LINE 24
            __M_writer(u'  <form class="toggle flairtoggle">\n    <input id="flair_enabled" type="checkbox" name="flair_enabled"\n')
            # SOURCE LINE 26
            if thing.user_flair_enabled:
                # SOURCE LINE 27
                __M_writer(u'          checked="checked"\n')
            # SOURCE LINE 29
            __M_writer(u'        >\n    <label for="flair_enabled">\n        ')
            # SOURCE LINE 31
            __M_writer(conditional_websafe(_("Show my flair on this subreddit. It looks like:")))
            __M_writer(u'\n    </label>\n  </form>\n  <div class="tagline">')
            # SOURCE LINE 34
            __M_writer(conditional_websafe(thing.wrapped_user))
            __M_writer(u'</div>\n')
        # SOURCE LINE 36
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()

