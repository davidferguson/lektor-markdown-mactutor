# -*- coding: utf-8 -*-

from lektor.pluginsystem import Plugin
import mistune
import re

import commands.m_link
import commands.gl_link
import commands.math_inline
import commands.text_inline

# list of plugins here. to add new ones, import them and add them to this list
plugins = [
    commands.m_link,
    commands.gl_link,
    commands.math_inline,
    commands.text_inline
]


class MarkdownMactutorPlugin(Plugin):
    name = 'Markdown MacTutor'
    description = u'Lektor plugin that adds custom markdown syntax used for MacTutor.'

    def on_markdown_config(self, config, **extra):
        # create inline and block lexers
        inline_lexer = mistune.InlineLexer(mistune.Renderer())
        block_lexer = mistune.BlockLexer()

        # does an lexer already exist? if so, use that
        if 'inline' in config.options:
            inline_lexer = config.options['inline']
        if 'block' in config.options:
            block_lexer = config.options['inline']

        # loop through all enabled plugins
        for plugin in plugins:
            # select the correct lexer
            lexer = inline_lexer
            if plugin.type == 'block':
                lexer = block_lexer

            # add the plugin in
            setattr(lexer.rules, plugin.name, plugin.regex)

            # if there is a position and renderer, add that in too
            if hasattr(plugin, 'position') and hasattr(plugin, 'render'):
                lexer.default_rules.insert(plugin.position, plugin.name)
                setattr(lexer, 'output_%s' % plugin.name, plugin.render)

        # set the config to use these custom lexers
        config.options['inline'] = inline_lexer
        config.options['block'] = block_lexer
