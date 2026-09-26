def pop(self):
        move = self.move_stack.pop()
        self.transpositions.subtract((self.zobrist_hash(), ))
        self.move_number -= 1
        captured_piece_type = self.captured_piece_stack.pop()
        captured_piece_color = self.turn
        if not move:
            self.turn ^= 1
            return move
        piece_type = self.piece_type_at(move.to_square)
        if move.promotion:
            piece_type = PIECE_PROMOTED.index(piece_type)
        if move.from_square is None:
            self.add_piece_into_hand(piece_type, self.turn ^ 1)
        else:
            self.set_piece_at(move.from_square, Piece(piece_type, self.turn ^ 1))
        if captured_piece_type:
            self.remove_piece_from_hand(captured_piece_type, captured_piece_color ^ 1)
            self.set_piece_at(move.to_square, Piece(captured_piece_type, captured_piece_color))
        else:
            self.remove_piece_at(move.to_square)
        self.turn ^= 1
        return move