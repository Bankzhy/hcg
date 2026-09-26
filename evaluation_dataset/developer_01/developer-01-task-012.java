public BoundingBox expandBoundingBox(BoundingBox boundingBox,
                                         Projection projection) {
        BoundingBox expandedBoundingBox = boundingBox;
        ProjectionTransform toWebMercator = projection
                .getTransformation(ProjectionConstants.EPSG_WEB_MERCATOR);
        if (!toWebMercator.isSameProjection()) {
            expandedBoundingBox = expandedBoundingBox.transform(toWebMercator);
        }
        expandedBoundingBox = expandBoundingBox(expandedBoundingBox);
        if (!toWebMercator.isSameProjection()) {
            ProjectionTransform fromWebMercator = toWebMercator
                    .getInverseTransformation();
            expandedBoundingBox = expandedBoundingBox
                    .transform(fromWebMercator);
        }
        return expandedBoundingBox;
    }