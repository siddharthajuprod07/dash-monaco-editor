# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashMonacoEditor(Component):
    """A DashMonacoEditor component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- height (string; optional):
    Height of the editor.

- language (string; required):
    The language of the editor.

- theme (string; required):
    current theme \"light\",\"vs-dark\".

- value (string; optional):
    current code."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_monaco_editor'
    _type = 'DashMonacoEditor'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, height=Component.UNDEFINED, language=Component.REQUIRED, value=Component.UNDEFINED, theme=Component.REQUIRED, **kwargs):
        self._prop_names = ['id', 'height', 'language', 'theme', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'height', 'language', 'theme', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['language', 'theme']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(DashMonacoEditor, self).__init__(**args)
