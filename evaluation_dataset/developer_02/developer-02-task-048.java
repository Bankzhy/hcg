protected Paint getPolygonFillPaint(FeatureStyle featureStyle) {
        Paint paint = null;
        boolean hasStyleColor = false;
        if (featureStyle != null) {
            StyleRow style = featureStyle.getStyle();
            if (style != null) {
                if (style.hasFillColor()) {
                    paint = getStylePaint(style, FeatureDrawType.FILL);
                } else {
                    hasStyleColor = style.hasColor();
                }
            }
        }
        if (paint == null && !hasStyleColor && fillPolygon) {
            paint = polygonFillPaint;
        }
        return paint;
    }