def get_t_tag_content(
        t, parent, remove_bold, remove_italics, meta_data):
    if t is None or t.text is None:
        return ''
    text = cgi.escape(t.text)
    el_is_bold = not remove_bold and (
        is_bold(parent) or
        is_underlined(parent)
    )
    el_is_italics = not remove_italics and is_italics(parent)
    if el_is_bold:
        text = '<strong>%s</strong>' % text
    if el_is_italics:
        text = '<em>%s</em>' % text
    return text