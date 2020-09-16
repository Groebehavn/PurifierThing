import logging

from mozilla_thing.deviceconnector import DeviceConnector
from webthing.server import SingleThing, WebThingServer
from webthing.thing import Thing
from webthing.property import Property
from webthing.value import Value

def make_thing(deviceconnector):
    purifier = Thing(
        'hu:lumiere:things:philips-purifier-AC2889',
        'Philips AC2889',
        ['OnOffSwitch'],
        'Philips AC2889 connected air purifier'
    )
    
    purifier.add_property(
    Property(
        purifier,
        'OnOffSwitch',
        Value(False, DeviceConnector.toggleOnOff()),
        metadata={
            '@type': 'OnOffProperty',
            'title': 'On/Off',
            'type': 'boolean',
            'description': 'Whether the lamp is turned on',
        }))

def run_server():
    conn = DeviceConnector()
    conn.toggleOnOff()
    thing = make_thing(conn)

    # If adding more than one thing, use MultipleThings() with a name.
    # In the single thing case, the thing's name will be broadcast.
    server = WebThingServer(SingleThing(thing), port=8888)
    try:
        logging.info('starting the server')
        server.start()
    except KeyboardInterrupt:
        logging.info('stopping the server')
        server.stop()
        logging.info('done')

if __name__ == '__main__':
    logging.basicConfig(
        level=10,
        format="%(asctime)s %(filename)s:%(lineno)s %(levelname)s %(message)s"
    )
    run_server()
