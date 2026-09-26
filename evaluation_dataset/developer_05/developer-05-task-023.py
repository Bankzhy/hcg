def check_not_bot(self, user_id):
    self.small_delay()
    user_id = self.convert_to_user_id(user_id)
    if not user_id:
        return False
    if user_id in self.whitelist:
        return True
    if user_id in self.blacklist:
        return False
    user_info = self.get_user_info(user_id)
    if not user_info:
        return True
    skipped = self.skipped_file
    if "following_count" in user_info and user_info["following_count"] > self.max_following_to_block:
        msg = 'following_count > bot.max_following_to_block, skipping!'
        self.console_print(msg, 'red')
        skipped.append(user_id)
        return False
    if search_stop_words_in_user(self, user_info):
        msg = '`bot.search_stop_words_in_user` found in user, skipping!'
        skipped.append(user_id)
        return False
    return True