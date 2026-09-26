def join(self, word_blocks, float_part):
        word_list = []
        length = len(word_blocks) - 1
        first_block = word_blocks[0],
        start = 0
        if length == 1 and first_block[0][0] == '1':
            word_list += ['seribu']
            start = 1
        for i in range(start, length + 1, 1):
            word_list += word_blocks[i][1]
            if not word_blocks[i][1]:
                continue
            if i == length:
                break
            word_list += [self.TENS_TO[(length - i) * 3]]
        return ' '.join(word_list) + float_part