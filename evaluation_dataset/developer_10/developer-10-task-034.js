function setChapterActive($chapter, hash) {
    if (!$chapter && !hash) {
        $chapter = $chapters.first();
    }
    if (!!hash) {
        if ($chapters.length > 1) {
            $chapter = $chapters.filter(function() {
                var titleId = getChapterHash($(this));
                return titleId == hash;
            }).first();
        }
        else {
            $chapter = $chapters.first();
        }
    }
    if ($chapter.is($activeChapter)) {
        return;
    }
    $activeChapter = $chapter;
    $chapters.removeClass('active');
    $chapter.addClass('active');
    hash = getChapterHash($chapter);
    var oldUri = window.location.pathname + window.location.hash,
        uri = window.location.pathname + hash;
    if (uri != oldUri) {
        history.replaceState({ path: uri }, null, uri);
    }
}