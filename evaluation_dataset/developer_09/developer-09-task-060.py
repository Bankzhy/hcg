def create_buffer(self, bins, repeats, base_buffer_size, max_buffer_size=0):
        samples = bins * repeats
        buffer_repeats = 1
        buffer_size = math.ceil(samples / base_buffer_size) * base_buffer_size
        if not max_buffer_size:
            max_buffer_size = (100 * 1024**2) / 8
        if max_buffer_size > 0:
            max_buffer_size = math.ceil(max_buffer_size / base_buffer_size) * base_buffer_size
            if buffer_size > max_buffer_size:
                logger.warning('Required buffer size ({}) will be shrinked to max_buffer_size ({})!'.format(
                    buffer_size, max_buffer_size
                ))
                buffer_repeats = math.ceil(buffer_size / max_buffer_size)
                buffer_size = max_buffer_size
        logger.info('repeats: {}'.format(repeats))
        logger.info('samples: {} (time: {:.5f} s)'.format(samples, samples / self.device.sample_rate))
        if max_buffer_size > 0:
            logger.info('max_buffer_size (samples): {} (repeats: {:.2f}, time: {:.5f} s)'.format(
                max_buffer_size, max_buffer_size / bins, max_buffer_size / self.device.sample_rate
            ))
        else:
            logger.info('max_buffer_size (samples): UNLIMITED')
        logger.info('buffer_size (samples): {} (repeats: {:.2f}, time: {:.5f} s)'.format(
            buffer_size, buffer_size / bins, buffer_size / self.device.sample_rate
        ))
        logger.info('buffer_repeats: {}'.format(buffer_repeats))
        return (buffer_repeats, zeros(buffer_size, numpy.complex64))