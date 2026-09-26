function Feed(props) {
  const { children, className, events, size } = props
  const classes = cx('ui', size, 'feed', className)
  const rest = getUnhandledProps(Feed, props)
  const ElementType = getElementType(Feed, props)
  if (!childrenUtils.isNil(children)) {
    return (
      <ElementType {...rest} className={classes}>
        {children}
      </ElementType>
    )
  }
  const eventElements = _.map(events, (eventProps) => {
    const { childKey, date, meta, summary, ...eventData } = eventProps
    const finalKey = childKey || [date, meta, summary].join('-')
    return <FeedEvent date={date} key={finalKey} meta={meta} summary={summary} {...eventData} />
  })
  return (
    <ElementType {...rest} className={classes}>
      {eventElements}
    </ElementType>
  )
}