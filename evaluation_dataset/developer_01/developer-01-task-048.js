function(val) {
    if (typeof val === "string") {
      if (val.indexOf("0x") === 0) {
        return val.trim();
      } else {
        val = new utils.BN(val);
      }
    }
    if (typeof val === "boolean") {
      val = val ? 1 : 0;
    }
    if (typeof val === "number") {
      val = utils.intToHex(val);
    } else if (val == null) {
      return "0x";
    } else if (typeof val === "object") {
      val = val.toString("hex");
    }
    return utils.addHexPrefix(val);
  }