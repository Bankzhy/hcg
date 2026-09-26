def update_panel(self, panel_obj, version=None, date_obj=None):
        LOG.info("Updating panel %s", panel_obj['panel_name'])
        date = panel_obj['date']
        if version:
            LOG.info("Updating version from {0} to version {1}".format(
                panel_obj['version'], version))
            panel_obj['version'] = version
            if date_obj:
                date = date_obj
        else:
            date = date_obj or dt.datetime.now()
        panel_obj['date'] = date
        updated_panel = self.panel_collection.find_one_and_replace(
            {'_id': panel_obj['_id']},
            panel_obj,
            return_document=pymongo.ReturnDocument.AFTER
        )
        return updated_panel