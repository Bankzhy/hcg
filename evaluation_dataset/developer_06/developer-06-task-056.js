function respond () {
  const context = this
  const consumeOpts = context.consumeOpts
  const channel = context.consumerChannel
  let method
  let args
  const methods = ['ack', 'nack', 'ackAll', 'nackAll', 'reject']
  method = methods.find(function (method) {
    if (context[method]) {
      args = context[method]
      return true
    }
  })
  if (method) {
    args = values(pick(args, ['allUpTo', 'requeue']))
    if (method === 'ack' || method === 'nack') {
      args.unshift(context.message)
    }
    channel[method].apply(channel, args)
  } else if (!consumeOpts.noAck) {
    let err = new NoAckError('Message completed middlewares w/out any acknowledgement')
    Context.onerror(context, err)
  }
}