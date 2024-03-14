# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashMonacoEditor <- function(id=NULL, height=NULL, language=NULL, theme=NULL, value=NULL) {
    
    props <- list(id=id, height=height, language=language, theme=theme, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashMonacoEditor',
        namespace = 'dash_monaco_editor',
        propNames = c('id', 'height', 'language', 'theme', 'value'),
        package = 'dashMonacoEditor'
        )

    structure(component, class = c('dash_component', 'list'))
}
