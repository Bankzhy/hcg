public static String generateSeed() {
        byte[] bytes = new byte[21];
        new SecureRandom().nextBytes(bytes);
        byte[] rhash = hash(bytes, 0, 20, SHA256);
        bytes[20] = rhash[0];
        BigInteger rand = new BigInteger(bytes);
        BigInteger mask = new BigInteger(new byte[]{0, 0, 7, -1});
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 15; i++) {
            sb.append(i > 0 ? ' ' : "")
                    .append(SEED_WORDS[rand.and(mask).intValue()]);
            rand = rand.shiftRight(11);
        }
        return sb.toString();
    }