def get(self):
        self.set_header('Content-Type', 'application/json')
        ws_href = '{}://{}'.format(
            'wss' if self.request.protocol == 'https' else 'ws',
            self.request.headers.get('Host', '')
        )
        descriptions = []
        for thing in self.things.get_things():
            description = thing.as_thing_description()
            description['links'].append({
                'rel': 'alternate',
                'href': '{}{}'.format(ws_href, thing.get_href()),
            })
            descriptions.append(description)
        self.write(json.dumps(descriptions))