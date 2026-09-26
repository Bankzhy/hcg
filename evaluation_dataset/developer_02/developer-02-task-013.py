def save_checkpoint(model, filename, optimizer=None, meta=None):
    if meta is None:
        meta = {}
    elif not isinstance(meta, dict):
        raise TypeError('meta must be a dict or None, but got {}'.format(
            type(meta)))
    meta.update(mmcv_version=mmcv.__version__, time=time.asctime())
    mmcv.mkdir_or_exist(osp.dirname(filename))
    if hasattr(model, 'module'):
        model = model.module
    checkpoint = {
        'meta': meta,
        'state_dict': weights_to_cpu(model.state_dict())
    }
    if optimizer is not None:
        checkpoint['optimizer'] = optimizer.state_dict()
    torch.save(checkpoint, filename)