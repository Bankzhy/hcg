def google_cloud_to_local(self, file_name):
        if not file_name.startswith('gs://'):
            return file_name
        path_components = file_name[self.GCS_PREFIX_LENGTH:].split('/')
        if len(path_components) < 2:
            raise Exception(
                'Invalid Google Cloud Storage (GCS) object path: {}'
                .format(file_name))
        bucket_id = path_components[0]
        object_id = '/'.join(path_components[1:])
        local_file = '/tmp/dataflow{}-{}'.format(str(uuid.uuid4())[:8],
                                                 path_components[-1])
        self._gcs_hook.download(bucket_id, object_id, local_file)
        if os.stat(local_file).st_size > 0:
            return local_file
        raise Exception(
            'Failed to download Google Cloud Storage (GCS) object: {}'
            .format(file_name))