# AUTO GENERATED FILE - DO NOT EDIT

export ''_dashmonacoeditor

"""
    ''_dashmonacoeditor(;kwargs...)

A DashMonacoEditor component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `height` (String; optional): Height of the editor
- `language` (String; required): The language of the editor
- `theme` (String; required): current theme "light","vs-dark"
- `value` (String; optional): current code
"""
function ''_dashmonacoeditor(; kwargs...)
        available_props = Symbol[:id, :height, :language, :theme, :value]
        wild_props = Symbol[]
        return Component("''_dashmonacoeditor", "DashMonacoEditor", "dash_monaco_editor", available_props, wild_props; kwargs...)
end

