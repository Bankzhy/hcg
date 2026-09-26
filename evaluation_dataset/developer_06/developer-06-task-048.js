function localizeChapterTitle(language_slug, chapter_number) {
    var translations = {
        'ar': 'الفصل %',
        'en': 'Chapter %',
        'ru': 'Глава %',
        'hu': '%. fejezet',
        'sr-Latin': 'Поглавље %',
        'default': 'Chapter %'
    };
    var title = translations[language_slug];
    if(!title) title = translations['default'];
    var num = parseInt(chapter_number);
    if (isNaN(num)) num = chapter_number;
    return title.replace('%', num);
}